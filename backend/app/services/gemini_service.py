import os
import time
import json
import logging
from typing import Dict, Any, List, Optional
from app.config import settings

logger = logging.getLogger("samvedna.gemini")

# Try importing google-genai
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


class GeminiConversationalService:
    """
    Production-Grade Gemini Conversational AI Service for SAMVEDNA AI.
    Connects to the official Google Gemini API (gemini-3.5-flash / gemini-3.6-flash) with:
      - Deep Multimodal Audio Prosody & Vocal Emotion Perception Engine
      - Multi-turn conversational session memory (sliding context window)
      - Multimodal emotional context injection (Voice Prosody + Text NLP + Mood Layer)
      - Trauma-informed, empathetic, non-diagnostic behavioral instructions
      - Multilingual fluency across Hindi, English, Bengali, Tamil, Telugu, and natural Hinglish
      - Resilient multi-model failover & offline fallback generation.
    """

    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
        self.model_name = settings.GEMINI_MODEL or "gemini-flash-lite-latest"
        self.client = None
        self._session_memory: Dict[str, List[Dict[str, str]]] = {}

        if GENAI_AVAILABLE and self.api_key:
            try:
                self.client = genai.Client(api_key=self.api_key)
                logger.info(f"[GEMINI] Client initialized successfully with model {self.model_name}")
            except Exception as e:
                logger.warning(f"[GEMINI] Could not initialize Gemini Client: {e}")
                self.client = None

    def refresh_client_if_needed(self):
        """Re-checks environment variable in case GEMINI_API_KEY or model was updated at runtime."""
        current_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
        current_model = settings.GEMINI_MODEL or os.getenv("GEMINI_MODEL", "gemini-flash-lite-latest")
        if current_key and (current_key != self.api_key or current_model != self.model_name or self.client is None) and GENAI_AVAILABLE:
            self.api_key = current_key
            self.model_name = current_model
            try:
                self.client = genai.Client(api_key=self.api_key)
                logger.info(f"[GEMINI] Client refreshed with model {self.model_name}.")
            except Exception as e:
                logger.warning(f"[GEMINI] Failed to refresh Gemini Client: {e}")

    def get_conversation_history(self, session_id: str) -> List[Dict[str, str]]:
        """Retrieves recent dialogue turns for the given session."""
        return self._session_memory.get(session_id, [])

    def record_turn(self, session_id: str, user_text: str, assistant_text: str):
        """Records a completed turn in session memory (unlimited conversation length)."""
        if session_id not in self._session_memory:
            self._session_memory[session_id] = []
        
        self._session_memory[session_id].append({"role": "user", "content": user_text})
        self._session_memory[session_id].append({"role": "assistant", "content": assistant_text})

    def clear_session(self, session_id: str):
        """Clears conversation history and session memory for the given session ID."""
        if session_id in self._session_memory:
            self._session_memory[session_id] = []
        logger.info(f"[GEMINI] Conversation session cleared for {session_id}")

    def analyze_audio_deep_prosody(
        self,
        audio_bytes: bytes,
        mime_type: str = "audio/wav",
        language: str = "hi"
    ) -> Dict[str, Any]:
        """
        Deep Multimodal Audio & Speech Emotion Perception Engine.
        Uses Google Gemini to perform high-resolution acoustic, prosodic, and vocal emotion analysis
        directly from raw audio bytes.
        Returns:
          - transcription (verbatim in original script)
          - primary_vocal_emotion & secondary_vocal_emotion
          - emotion_confidence (0.0 to 1.0)
          - vocal_stress_score (0.0 to 100.0)
          - acoustic_observations (vocal_stability, breathing_pattern, speech_tempo, vocal_energy, paralinguistic_cues)
          - vocal_text_concordance
          - clinical_voice_summary
        """
        self.refresh_client_if_needed()

        if not self.client or not GENAI_AVAILABLE or len(audio_bytes) < 100:
            logger.warning("[VOICE-DEEP] Gemini client unavailable or audio buffer too small. Using fallback profile.")
            return self._build_default_voice_analysis("Insufficient audio data for deep analysis")

        lang_name = "Hindi (हिन्दी)" if language == "hi" else ("English" if language == "en" else language)

        system_instruction = (
            "You are an expert clinical forensic audio analyst and speech prosody specialist for a National Crime/Atrocity Victim Support System. "
            "Your role is to deeply analyze the acoustic qualities, vocal biomarkers, emotional prosody, and verbatim speech from the user's recorded audio. "
            "Listen directly to the physical sound: vocal tremors, pitch stability, respiratory patterns, speech velocity, sobbing or sighs, and vocal tension. "
            "Output your analysis strictly in valid JSON matching the exact requested schema."
        )

        instructions_prompt = (
            f"Analyze the provided voice recording carefully. The speaker may be speaking in {lang_name} or an Indian dialect.\n"
            "Perform a deep acoustic, emotional, and speech analysis. Return a JSON object with EXACTLY this structure:\n"
            "{\n"
            '  "transcription": "Verbatim transcription of what was spoken in its original script and language. If inaudible or pure crying/sighing, describe in brackets like [heavy breathing and weeping]",\n'
            '  "detected_language": "Hindi / English / Hinglish / Bengali / Tamil / Telugu / etc.",\n'
            '  "primary_vocal_emotion": "One of: Fear / Terror, Acute Distress, Suppressed Grief, Anxious Hesitation, Agitation / Anger, Despair / Hopelessness, Calm / Relief, Neutral / Steady",\n'
            '  "secondary_vocal_emotion": "Secondary emotional nuance (e.g. Nervous Trembling, Exhaustion)",\n'
            '  "emotion_confidence": 0.88,\n'
            '  "vocal_stress_score": 75.0,\n'
            '  "acoustic_observations": {\n'
            '    "vocal_stability": "One of: steady, trembling, choked_up, cracking, strained, unsteady",\n'
            '    "breathing_pattern": "One of: normal, shallow_hyperventilation, heavy_sighs, audible_sobbing, gasping",\n'
            '    "speech_tempo": "One of: steady, rapid_agitated, hesitant_with_long_pauses, slow_depressive",\n'
            '    "vocal_energy": "One of: normal, whispering, strained_volume, suppressed_tears, loud_agitated",\n'
            '    "paralinguistic_cues": ["crying", "stifled sobs", "gasping for air", "voice cracking", "frequent pauses"]\n'
            '  },\n'
            '  "vocal_text_concordance": "One of: concordant, voice_distress_masked_by_text, mixed_signals",\n'
            '  "clinical_voice_summary": "A 1-2 sentence non-diagnostic summary describing how the speaker sounds physically and emotionally."\n'
            "}\n"
            "Ensure all float scores are numeric and not strings."
        )

        candidate_models = [self.model_name]
        for m in ["gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.6-flash"]:
            if m not in candidate_models:
                candidate_models.append(m)

        for cand_model in candidate_models:
            try:
                fast_http_options = types.HttpOptions(
                    timeout=30000,
                    retry_options=types.HttpRetryOptions(attempts=1)
                ) if GENAI_AVAILABLE else None

                response = self.client.models.generate_content(
                    model=cand_model,
                    contents=[audio_part, instructions_prompt],
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.2, # Low temperature for accurate clinical extraction
                        max_output_tokens=700,
                        response_mime_type="application/json",
                        http_options=fast_http_options
                    )
                )

                if response and response.text:
                    parsed = json.loads(response.text.strip())
                    logger.info(
                        f"[VOICE-DEEP] Extracted via {cand_model} | "
                        f"Emotion: {parsed.get('primary_vocal_emotion')} | "
                        f"Conf: {parsed.get('emotion_confidence')} | "
                        f"Stress: {parsed.get('vocal_stress_score')}/100 | "
                        f"Stability: {parsed.get('acoustic_observations', {}).get('vocal_stability')}"
                    )
                    return parsed
            except Exception as e:
                logger.warning(f"[VOICE-DEEP] Model {cand_model} deep audio call failed ({e}), trying next candidate...")

        return self._build_default_voice_analysis("Gemini deep audio analysis offline fallback")

    def _build_default_voice_analysis(self, reason: str = "") -> Dict[str, Any]:
        """Provides a safe, non-hallucinatory default voice analysis profile."""
        return {
            "transcription": "[Voice check-in audio recorded]",
            "detected_language": "Unknown",
            "primary_vocal_emotion": "Neutral / Steady",
            "secondary_vocal_emotion": "Uncertain",
            "emotion_confidence": 0.50,
            "vocal_stress_score": 30.0,
            "acoustic_observations": {
                "vocal_stability": "steady",
                "breathing_pattern": "normal",
                "speech_tempo": "steady",
                "vocal_energy": "normal",
                "paralinguistic_cues": []
            },
            "vocal_text_concordance": "concordant",
            "clinical_voice_summary": f"Vocal audio observed. {reason}".strip()
        }

    def generate_contextual_response(
        self,
        session_id: str,
        user_message: str,
        emotional_state: Dict[str, Any],
        voice_analysis: Dict[str, Any],
        legal_context: Optional[Dict[str, Any]] = None,
        language: str = "hi",
        response_length: str = "normal"
    ) -> str:
        """
        Generates a dynamic, empathetic, context-aware conversational response.
        Deeply conditioned on vocal acoustic cues (tremors, breathing, volume, emotion).
        """
        self.refresh_client_if_needed()

        history = self.get_conversation_history(session_id)
        has_voice = voice_analysis and (
            "AUTHENTIC" in voice_analysis.get("feature_status", "") 
            or voice_analysis.get("has_audio", False)
            or voice_analysis.get("primary_vocal_emotion") is not None
        )
        
        logger.info(f"[GEMINI] Request sent | session={session_id} | lang={language} | length={response_length} | history={len(history)} turns | has_voice={has_voice}")

        system_instruction = self._build_system_instruction(language)
        prompt_payload = self._build_context_prompt(
            user_message=user_message,
            history=history,
            emotional_state=emotional_state,
            voice_analysis=voice_analysis,
            legal_context=legal_context,
            language=language,
            response_length=response_length
        )

        # 1. Try Live Gemini API Generation with Multi-Model Failover
        t_gemini_start = time.time()
        if self.client:
            fast_http_options = types.HttpOptions(
                timeout=30000,
                retry_options=types.HttpRetryOptions(attempts=1)
            )

            # Fast responsive candidate sequence: primary model then 1 fast backup
            candidate_models = ["gemini-flash-lite-latest", "gemini-2.5-flash"]
            if self.model_name and self.model_name not in candidate_models:
                candidate_models.insert(0, self.model_name)
            candidate_models = candidate_models[:2]

            for cand_model in candidate_models:
                try:
                    response = self.client.models.generate_content(
                        model=cand_model,
                        contents=prompt_payload,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.7,
                            max_output_tokens=2048,
                            http_options=fast_http_options
                        )
                    )
                    if response and response.text:
                        clean_response = response.text.strip()
                        elapsed = time.time() - t_gemini_start
                        logger.info(f"[GEMINI] Request: {elapsed:.2f}s | Model: {cand_model} | Output: {len(clean_response)} chars")
                        self.record_turn(session_id, user_message, clean_response)
                        return clean_response
                except Exception as err:
                    err_msg = str(err)
                    if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
                        logger.warning(f"[GEMINI] Rate limit (429 RESOURCE_EXHAUSTED) on {cand_model}. Trying failover...")
                        time.sleep(0.3)
                    else:
                        logger.warning(f"[GEMINI] Model {cand_model} non-quota error ({err_msg}). Trying failover...")

        # 2. Resilient Trauma-Informed Local Dynamic Synthesizer
        logger.info("[GEMINI] Live API unavailable or rate-limited; deploying empathetic fallback synthesizer.")
        fallback_text = self._generate_dynamic_fallback(
            user_message=user_message,
            history=history,
            emotional_state=emotional_state,
            voice_analysis=voice_analysis,
            legal_context=legal_context,
            language=language,
            response_length=response_length
        )
        self.record_turn(session_id, user_message, fallback_text)
        return fallback_text

    def _build_system_instruction(self, language: str) -> str:
        """
        Constructs the multimodal, trauma-informed, versatility-aware system instruction.
        """
        return (
            "You are SAMVEDNA AI (संवेदना), an empathetic, culturally grounded conversational AI assistant "
            "designed to provide supportive, conversational, and victim-centric care in coordination with "
            "the National Helpline Against Atrocities (NHAA 14566), Tele-MANAS (14416), and the District Legal Services Authority (DLSA).\n\n"
            "CRITICAL ARCHITECTURE PRINCIPLES:\n"
            "0. MULTIMODAL FUSION & FINAL USER STATE:\n"
            "   - You receive a comprehensive FINAL USER STATE containing `intent`, `valence`, `emotion`, `arousal`, `distress_level`, and `response_mode`.\n"
            "   - This state was synthesized by the application's multimodal fusion layer combining text semantics (primary) and voice prosody (secondary).\n"
            "   - You MUST adapt your conversational tone directly to `response_mode`:\n"
            "     * 'casual': User is greeting, chatting, or checking in. Respond like a warm, natural, friendly chatbot. DO NOT mention trauma, distress, or helplines.\n"
            "     * 'positive': User is sharing positive news, joy, or excitement. Celebrate with them warmly and ask an engaging, joyful question. DO NOT inject crisis warnings.\n"
            "     * 'neutral': User is asking for information or making neutral remarks. Answer plainly, clearly, and helpfully. DO NOT give unsolicited emotional therapy or crisis disclaimers.\n"
            "     * 'supportive': User is expressing everyday worries, exam anxiety, fatigue, or sadness. Respond with calm emotional grounding, encouragement, and active listening.\n"
            "     * 'distress_support': User is experiencing acute distress, fear, threats, or severe overwhelm. Prioritize safety, validate feelings gently, and mention NHAA 14566, Police 112, or Tele-MANAS 14416.\n"
            "     * 'clarification': Signals are ambiguous or uncertain. Ask a gentle, open-ended question without assuming a negative mental state.\n"
            "1. NO MANUFACTURED DISTRESS:\n"
            "   - High arousal (e.g. exclamation marks, rapid tempo, loud volume) DOES NOT mean distress: it can represent excitement, joy, or enthusiasm.\n"
            "   - Never treat greetings ('Hi', 'Hello') or positive updates ('I am so happy!') as emotional distress.\n"
            "2. CONVERSATIONAL MEMORY & CONTEXT:\n"
            "   - Maintain session memory across dialogue turns. Connect current replies to earlier user remarks.\n"
            "3. STRICTLY NON-DIAGNOSTIC:\n"
            "   - NEVER give medical or psychiatric diagnoses. Do not claim the user has PTSD, depression, or an illness.\n"
            "4. NATURAL CONVERSATION:\n"
            "   - Respond naturally like a normal conversational LLM. Do not forcefully or repetitively mention 'I can hear the trembling in your voice'.\n"
            "   - Only acknowledge their vocal state if it heavily contrasts with their text or if they are in severe crisis.\n"
            "   - If no audio was recorded (text check-in), DO NOT make claims about vocal sound, tone, or breathing.\n"
            "5. LANGUAGE & TONE:\n"
            "   - Respond in the requested language (Hindi if 'hi', English if 'en', Bengali if 'bn', Tamil if 'ta', Telugu if 'te', or natural Hinglish).\n"
            "   - Provide comprehensive, detailed, and highly empathetic responses. Ensure you fully address all aspects of the user's concerns.\n"
            "6. STRICT MEDICAL SAFETY CONSTRAINT:\n"
            "   - NEVER provide medical advice, do not prescribe or mention specific medicines, and do not diagnose any diseases. Assure the user everything is fine where appropriate, but remain strictly non-medical."
        )

    def _build_context_prompt(
        self,
        user_message: str,
        history: List[Dict[str, str]],
        emotional_state: Dict[str, Any],
        voice_analysis: Dict[str, Any],
        legal_context: Optional[Dict[str, Any]],
        language: str,
        response_length: str
    ) -> str:
        """
        Structures the multimodal context package for Gemini.
        Passes the FINAL FUSED USER STATE, acoustic observations, and legal context.
        """
        has_voice = voice_analysis and (
            "AUTHENTIC" in str(voice_analysis.get("feature_status", ""))
            or bool(voice_analysis.get("has_audio"))
            or voice_analysis.get("primary_vocal_emotion") is not None
            or float(voice_analysis.get("duration_sec", 0.0)) > 0.1
        )
        calc_voice = voice_analysis.get("calculated_features", {}) or voice_analysis

        if has_voice:
            obs = voice_analysis.get("acoustic_observations", {})
            voice_summary = {
                "voice_recorded": True,
                "primary_vocal_emotion": voice_analysis.get("primary_vocal_emotion", "Acoustic observations recorded"),
                "arousal": voice_analysis.get("arousal", "medium"),
                "voice_valence": voice_analysis.get("voice_valence", voice_analysis.get("valence", "uncertain")),
                "vocal_tension_score": voice_analysis.get("vocal_tension", voice_analysis.get("acoustic_stress_score", 25.0)),
                "vocal_stability": voice_analysis.get("vocal_stability", obs.get("vocal_stability", "Stable")),
                "breathing_pattern": obs.get("breathing_pattern", "normal"),
                "speech_tempo": obs.get("speech_tempo", "steady"),
                "paralinguistic_cues": voice_analysis.get("supporting_evidence", voice_analysis.get("indicators", [])),
                "clinical_voice_summary": voice_analysis.get("clinical_voice_summary", "")
            }
        else:
            voice_summary = {
                "voice_recorded": False,
                "note": "Text-only check-in. No audio submitted. Do NOT invent vocal observations."
            }

        tone_guidance = self._emotion_tone_guidance(emotional_state, voice_analysis)
        context_dict = {
            "target_language": "Hindi (हिन्दी)" if language == "hi" else ("English" if language == "en" else language),
            "response_length_preference": response_length,
            "final_fused_user_state": {
                "intent": emotional_state.get("intent", "other"),
                "valence": emotional_state.get("valence", "neutral"),
                "emotion": emotional_state.get("emotion", "neutral"),
                "arousal": emotional_state.get("arousal", "low"),
                "distress_level": emotional_state.get("distress_level", "none"),
                "confidence": emotional_state.get("confidence", 0.85),
                "reason": emotional_state.get("reason", ""),
                "response_mode": emotional_state.get("response_mode", "casual"),
                "inferred_mood": emotional_state.get("mood", "Neutral"),
                "concordance": emotional_state.get("concordance_state", "text_only"),
                "voice_evidence": voice_summary
            },
            "recent_conversation_history": history[-6:] if history else [],
            "legal_and_protection_context": {
                "legal_stage": legal_context.get("legal_stage", "Special Court Trial") if legal_context else "Special Court Trial",
                "accused_on_bail": legal_context.get("accused_on_bail", False) if legal_context else False,
                "district": legal_context.get("district", "Protected District") if legal_context else "Protected District"
            },
            "current_user_message": user_message
        }

        return (
            f"CONTEXT & MULTI-MODAL EVIDENCE:\n```json\n{json.dumps(context_dict, ensure_ascii=False, indent=2)}\n```\n\n"
            f"INSTRUCTIONS FOR RESPONSE LENGTH:\n"
            f"- If response_length_preference is 'brief': Provide a very short, concise, and direct response (1-2 sentences maximum).\n"
            f"- If response_length_preference is 'descriptive': Provide a very long, highly detailed, comprehensive response (2+ paragraphs).\n"
            f"- If response_length_preference is 'normal': Provide a standard conversational response.\n"
            f"The current preference is: '{response_length}'. Strictly obey this.\n\n"
            f"TONE & STRATEGY GUIDANCE:\n{tone_guidance}\n\n"
            "TASK: Speak directly to the user in a detailed, empathetic, and comprehensive manner. Provide actionable and comforting advice in the target language. "
            "Never output meta-instructions, outlines, or JSON. Output ONLY the response you speak to the user."
        )

    def _emotion_tone_guidance(self, emotional_state: Dict[str, Any], voice_analysis: Dict[str, Any]) -> str:
        """Determines tone guidance matching the fused user state."""
        response_mode = str(emotional_state.get("response_mode", "casual")).lower()
        level = str(emotional_state.get("distress_level", "none")).lower()
        intent = str(emotional_state.get("intent", "other")).lower()

        if response_mode == "casual":
            return "Respond as a warm, friendly, helpful assistant. Do NOT provide crisis disclaimers or helplines."
        if response_mode == "positive":
            return "Celebrate the user's positive experience or excitement warmly. Ask an encouraging follow-up."
        if response_mode == "neutral" or intent == "information_seeking":
            return "Provide a clear, accurate, helpful explanation or answer directly without emotional over-empathy."
        if response_mode == "clarification":
            return "Ask a gentle, non-judgmental clarifying question to understand how best to assist them."
        if response_mode == "supportive":
            return "Use calm, validating, grounding language to help with worries, exam pressure, or sadness."
        if response_mode == "distress_support" or level == "high":
            return "Prioritize physical safety and reassurance. Speak calmly and reference NHAA 14566 or Emergency 112."
        return "Speak warmly, respectfully, and attentively."

    def _generate_dynamic_fallback(
        self,
        user_message: str,
        history: List[Dict[str, str]],
        emotional_state: Dict[str, Any],
        voice_analysis: Dict[str, Any],
        legal_context: Optional[Dict[str, Any]],
        language: str
    ) -> str:
        """
        Fallback response when the Gemini API is unreachable or rate-limited.
        Per architectural requirements: DO NOT use keyword matching or fake intelligence.
        """
        is_hi = (language == "hi")
        if is_hi:
            return "नमस्ते, मैं संवेदना एआई हूँ। अभी नेटवर्क कनेक्टिविटी के कारण मैं आपकी बात का पूरा अर्थ समझने में असमर्थ हूँ। कृपया प्रतीक्षा करें या बाद में पुनः प्रयास करें। आपात स्थिति में 112 डायल करें।"
        return "Hello, I am SAMVEDNA AI. Due to network connectivity issues, I am currently unable to fully process your message contextually. Please try again in a moment. In an emergency, dial 112."


gemini_engine = GeminiConversationalService()

