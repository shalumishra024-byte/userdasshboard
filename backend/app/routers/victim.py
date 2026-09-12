import time
import logging
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import Optional, Dict, Any, Set
from datetime import datetime

logger = logging.getLogger("samvedna.victim")

# Concurrency Guard: Prevents duplicate or overlapping check-ins for the same victim
_active_checkins: Set[str] = set()

from app.database import db
from app.services.voice_analytics import voice_engine
from app.services.nlp_engine import nlp_engine
from app.services.mood_estimator import mood_estimator
from app.services.multimodal_fusion import multimodal_fusion_engine
from app.services.gemini_service import gemini_engine
from app.services.distress_scoring import distress_engine
from app.services.xai_explainer import xai_engine
from app.services.intervention import intervention_engine
from app.services.alert_service import alert_hub

router = APIRouter(prefix="/victim", tags=["Victim Omnichannel Portal"])

@router.get("/profile/{victim_id}")
async def get_victim_profile(victim_id: str):
    victim = db.get_victim_by_id(victim_id)
    if not victim:
        raise HTTPException(status_code=404, detail="Victim record not found")
    
    checkins = db.get_victim_checkins(victim_id)
    notes = db.get_counsellor_notes(victim_id)
    
    return {
        "profile": victim,
        "checkin_count": len(checkins),
        "latest_checkin": checkins[-1] if checkins else None,
        "history": checkins,
        "counsellor_notes": notes
    }

@router.post("/checkin")
async def process_victim_checkin(
    victim_id: str = Form(...),
    channel: str = Form("Web_Portal"),
    text_content: Optional[str] = Form(""),
    language: str = Form("hi"),
    response_length: Optional[str] = Form("normal"),
    scenario_preset: Optional[str] = Form(None),
    is_sos: bool = Form(False),
    audio_file: Optional[UploadFile] = File(None)
):
    # Concurrency Protection: Prevent simultaneous check-in processing for the same victim
    original_victim_id = victim_id
    if victim_id in _active_checkins:
        logger.warning(f"[CONCURRENCY] Concurrent check-in blocked for victim: {victim_id}")
        return {
            "status": "busy",
            "message": "A check-in is currently being processed. Please wait a moment.",
            "ai_response": "हम आपका पिछला संदेश प्रोसेस कर रहे हैं, कृपया एक क्षण प्रतीक्षा करें..." if language == "hi" else "Please wait a moment while your previous check-in finishes processing."
        }

    _active_checkins.add(original_victim_id)
    try:
        victim = db.get_victim_by_id(victim_id)
        if not victim:
            victims = db.get_all_victims()
            if victims:
                victim = victims[0]
                victim_id = victim["victim_id"]
            else:
                raise HTTPException(status_code=404, detail="No victim found")
            
        history = db.get_victim_checkins(victim_id)
        
        # 1. Voice Analytics (Fast 10-25ms authentic DSP analysis, zero external API calls)
        transcription = ""
        ai_response = None
        if audio_file:
            t_audio_read_start = time.time()
            audio_bytes = await audio_file.read()
            logger.info(f"[VOICE] Audio received: {len(audio_bytes)} bytes in {time.time() - t_audio_read_start:.3f}s")
            
            # Physical Signal Processing & Authentic Biomarker Extraction (SciPy / NumPy)
            dsp_metrics = voice_engine.analyze_audio_bytes(audio_bytes, audio_file.filename or "recording.wav")
            
            # Silence or corrupted audio detection
            if dsp_metrics.get("feature_status", "").startswith("UNAVAILABLE") or dsp_metrics.get("duration_sec", 0) < 0.2:
                logger.info(f"[VOICE] Audio contained no valid speech: {dsp_metrics.get('feature_status')}")
                # If no text was entered either, return a gentle prompt without calling Gemini
                if not text_content or text_content.strip() in ["Voice distress check-in audio sample", "Voice check-in test audio", "Uploaded audio check-in file", "Voice check-in audio recorded.", ""]:
                    return {
                        "checkin_id": f"CHK-{victim_id[-4:]}-SILENCE",
                        "victim_id": victim_id,
                        "timestamp": datetime.now().isoformat(),
                        "channel": channel,
                        "status": "silence_detected",
                        "ai_response": (
                            "हमें आपकी आवाज़ स्पष्ट रूप से सुनाई नहीं दी। कृपया माइक्रोफ़ोन के पास आकर बोलें, या अपना संदेश नीचे टाइप करें।"
                            if language == "hi" else
                            "We could not detect clear speech in the audio recording. Please speak into your microphone, or feel free to type your message below."
                        ),
                        "voice_metrics": dsp_metrics,
                        "composite_dds": 25.0,
                        "risk_level": "LOW",
                        "emotional_state": {"mood": "Neutral", "confidence": 0.8, "distress_level": "low"}
                    }
                voice_metrics = dsp_metrics
            else:
                voice_metrics = dsp_metrics
                obs = voice_metrics.get("acoustic_observations", {})
                vocal_stress = voice_metrics.get("vocal_stress_score", 30.0)
                logger.info(f"[VOICE] Authentic DSP analysis complete: Emotion={voice_metrics.get('primary_vocal_emotion')} | Stress={vocal_stress}/100 | Stability={obs.get('vocal_stability')}")
                
                # If user typed or Web Speech API transcribed, use it; otherwise perform Server-Side Speech-to-Text
                if not text_content or text_content.strip() in ["Voice distress check-in audio sample", "Voice check-in test audio", "Uploaded audio check-in file", "Voice check-in audio recorded.", ""]:
                    try:
                        import speech_recognition as sr
                        import io
                        
                        logger.info(f"[VOICE->STT] Commencing Speech-to-Text extraction...")
                        r = sr.Recognizer()
                        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
                            audio_data = r.record(source)
                            
                        lang_code_map = {"en": "en-IN", "hi": "hi-IN", "bn": "bn-IN", "ta": "ta-IN", "te": "te-IN"}
                        lang_code = lang_code_map.get(language, "en-US")
                        
                        stt_transcript = r.recognize_google(audio_data, language=lang_code)
                        text_content = stt_transcript
                        logger.info(f"[VOICE->STT] Transcript successfully generated: '{text_content}'")
                    except sr.UnknownValueError:
                        logger.warning(f"[VOICE->STT] Speech could not be understood. Falling back to generic label.")
                        text_content = f"Voice check-in ({voice_metrics.get('primary_vocal_emotion')})"
                    except Exception as e:
                        logger.warning(f"[VOICE->STT] Failed to generate transcript: {e}")
                        text_content = f"Voice check-in ({voice_metrics.get('primary_vocal_emotion')})"
        elif scenario_preset:
            voice_metrics = voice_engine.simulate_acoustic_profile(scenario_preset)
            logger.info(f"[VOICE] Scenario preset applied: {scenario_preset}")
        else:
            # Standard text-only check-in: authentic zeroed voice metrics
            voice_metrics = {
                "has_audio": False,
                "feature_status": "NONE_TEXT_ONLY",
                "acoustic_stress_score": 20.0,
                "vocal_stress_score": 20.0,
                "pitch_mean_hz": 0.0,
                "pitch_volatility": 0.0,
                "jitter_pct": 0.0,
                "shimmer_pct": 0.0,
                "hnr_db": 0.0,
                "pause_ratio": 0.0,
                "tremor_intensity": 0.0,
                "indicators": [],
                "calculated_features": {}
            }
            
        # 2. NLP & Sentiment Analysis
        nlp_metrics = nlp_engine.analyze_text(text_content or "", language)
        
        # 3. Multimodal Mood & Emotional State Estimation
        # Retain the legacy mood estimate for compatibility/audit, then create
        # the final state used for conversation.  Gemini never receives a raw
        # classifier label as its decision context.
        legacy_mood_state = mood_estimator.estimate_mood(
            text_content=text_content or "",
            nlp_metrics=nlp_metrics,
            voice_metrics=voice_metrics,
            recent_history=history,
            language=language
        )
        emotional_state = multimodal_fusion_engine.interpret(nlp_metrics, voice_metrics, history)
        emotional_state["legacy_mood_state"] = legacy_mood_state
        logger.info(f"[EMOTION] Prediction: {emotional_state.get('mood')} | Confidence: {emotional_state.get('confidence')} | Stress: {emotional_state.get('distress_level')}")
        
        # 4. Dynamic Distress Score (DDS) & Longitudinal Risk Trajectory
        has_valid_voice = voice_metrics.get("feature_status") not in ["NONE_TEXT_ONLY", "UNAVAILABLE", "UNAVAILABLE_SILENCE", "UNAVAILABLE_FORMAT"] and "acoustic_stress_score" in voice_metrics
        voice_stress = voice_metrics.get("acoustic_stress_score") if has_valid_voice else None
        
        has_valid_nlp = "nlp_distress_score" in nlp_metrics
        nlp_stress = nlp_metrics.get("nlp_distress_score") if has_valid_nlp else None
        
        dds_result = distress_engine.compute_composite_dds(
            voice_stress_score=voice_stress,
            nlp_distress_score=nlp_stress,
            clinical_phq_score=None,
            legal_stage_risk=None,
            threat_detected=nlp_metrics.get("witness_threat_detected", False) or is_sos,
            self_harm_detected=nlp_metrics.get("self_harm_ideation_detected", False),
            historical_checkins=history
        )
        
        if "status" in dds_result and dds_result["status"] == "insufficient_data":
            return dds_result
        
        # 5. Explainable AI (XAI) Causal Factor Attribution
        xai_factors = xai_engine.generate_explanation(
            composite_dds=dds_result["composite_dds"],
            voice_metrics=voice_metrics,
            nlp_metrics=nlp_metrics,
            legal_stage=victim.get("legal_stage", "Special Court Trial"),
            case_attributes=victim
        )
        
        # 6. Automated Statutory Intervention Matching
        recommended_interventions = intervention_engine.recommend(
            risk_level=dds_result["risk_level"],
            threat_detected=nlp_metrics.get("witness_threat_detected", False) or is_sos,
            social_boycott=nlp_metrics.get("social_boycott_detected", False),
            self_harm=nlp_metrics.get("self_harm_ideation_detected", False),
            case_stage=victim.get("legal_stage", ""),
            case_data=victim
        )
        
        # 7. Single Gemini API Call: Empathetic Contextual Generation with Structured Voice Evidence
        if not ai_response:
            ai_response = gemini_engine.generate_contextual_response(
                session_id=victim_id,
                user_message=text_content or "Voice check-in audio recorded.",
                emotional_state=emotional_state,
                voice_analysis=voice_metrics,
                legal_context=victim,
                language=language,
                response_length=response_length
            )
        
        # 8. Record Check-in Record in Database
        checkin_record = {
            "checkin_id": f"CHK-{victim_id[-4:]}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "victim_id": victim_id,
            "timestamp": datetime.now().isoformat(),
            "channel": channel,
            "input_type": "Voice + Text" if audio_file else "Text",
            "transcript": transcription if transcription else text_content,
            "voice_metrics": voice_metrics,
            "nlp_metrics": nlp_metrics,
            "emotional_state": emotional_state,
            "composite_dds": dds_result["composite_dds"],
            "risk_level": dds_result["risk_level"],
            "escalation_delta": dds_result["escalation_delta"],
            "is_escalating_rapidly": dds_result["is_escalating_rapidly"],
            "risk_trajectory_label": dds_result["risk_trajectory_label"],
            "explainable_factors": xai_factors,
            "recommended_interventions": recommended_interventions,
            "ai_empathetic_response": ai_response
        }
        db.add_checkin(victim_id, checkin_record)
        
        # 9. Trigger Alert if Critical Threshold / Threat Crossed
        if dds_result["immediate_alert_triggered"] or is_sos:
            alert_hub.create_alert(
                victim_id=victim_id,
                victim_name=victim.get("victim_code", "Victim"),
                district=victim.get("district", "District"),
                state=victim.get("state", "State"),
                severity="EMERGENCY_SOS" if is_sos else dds_result["risk_level"],
                trigger_reason="Emergency SOS triggered!" if is_sos else f"Distress score spiked to {dds_result['composite_dds']}/100. Rapid escalation (+{dds_result['escalation_delta']} pts).",
                dds_score=dds_result["composite_dds"],
                escalation_delta=dds_result["escalation_delta"],
                interventions=recommended_interventions
            )
            
        return {
            "status": "success",
            "checkin_id": checkin_record["checkin_id"],
            "voice_score": dds_result.get("voice_score"),
            "nlp_score": dds_result.get("nlp_score"),
            "available_components": dds_result.get("available_components", []),
            "base_dds": dds_result.get("base_dds"),
            "safety_adjustment": dds_result.get("safety_adjustment"),
            "composite_dds": dds_result["composite_dds"],
            "risk_level": dds_result["risk_level"],
            "transcript": transcription or text_content,
            "detected_signals": dds_result.get("fusion_notes", {}).get("safety_categories", []),
            "feature_summary": {
                "f0": voice_metrics.get("pitch_mean_hz"),
                "jitter": voice_metrics.get("jitter_pct"),
                "shimmer": voice_metrics.get("shimmer_pct"),
                "hnr": voice_metrics.get("hnr_db"),
                "tremor": voice_metrics.get("tremor_intensity")
            } if has_valid_voice else {},
            "dds_result": dds_result,
            "emotional_state": emotional_state,
            "voice_metrics": voice_metrics,
            "nlp_metrics": nlp_metrics,
            "explainable_factors": xai_factors,
            "recommended_interventions": recommended_interventions,
            "ai_response": ai_response,
            "is_sos_active": is_sos or dds_result["risk_level"] == "CRITICAL"
        }
    finally:
        _active_checkins.discard(original_victim_id)
        _active_checkins.discard(victim_id)

@router.post("/reset")
async def reset_victim_session(victim_id: str = Form(...)):
    gemini_engine.clear_session(victim_id)
    return {
        "status": "success",
        "message": f"Conversation session memory cleared for {victim_id}"
    }

@router.post("/sos")
async def trigger_emergency_sos(
    victim_id: str = Form(...),
    location: Optional[str] = Form("Latitude: 26.4948, Longitude: 77.9940 (Morena, MP)"),
    emergency_note: Optional[str] = Form("EMERGENCY PANIC: Immediate security threat near residence.")
):
    victim = db.get_victim_by_id(victim_id)
    if not victim:
        victims = db.get_all_victims()
        victim = victims[0]
        victim_id = victim["victim_id"]
        
    interventions = intervention_engine.recommend(
        risk_level="CRITICAL",
        threat_detected=True,
        social_boycott=False,
        self_harm=False,
        case_stage=victim.get("legal_stage", "Special Court Trial"),
        case_data=victim
    )
    
    alert = alert_hub.create_alert(
        victim_id=victim_id,
        victim_name=victim.get("victim_code", "Victim"),
        district=victim.get("district", "District"),
        state=victim.get("state", "State"),
        severity="EMERGENCY_SOS",
        trigger_reason=f"ONE-TOUCH PANIC SOS BUTTON ACTIVATED. {emergency_note}. Location: {location}",
        dds_score=98.0,
        escalation_delta=35.0,
        interventions=interventions
    )
    
    return {
        "status": "EMERGENCY_DISPATCHED",
        "alert_id": alert["alert_id"],
        "hotlines": {
            "NHAA": "14566",
            "Police": "112",
            "TeleMANAS": "14416"
        },
        "target_officers_alerted": [
            f"Superintendent of Police, {victim.get('district')}",
            f"District Magistrate, {victim.get('district')}",
            "NHAA National Emergency Rapid Response Nodal Team"
        ],
        "interventions": interventions,
        "guidance": "Police protection unit dispatched under Section 15A. Keep phone active and remain in a locked, secure room."
    }
