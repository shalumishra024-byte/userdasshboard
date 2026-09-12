# SAMVEDNA AI (संवेदना)
## AI-Based Dynamic Mental Health Monitoring & Distress Prediction System
### National Helpline Against Atrocities (NHAA 14566) & SC/ST (PoA) Act Care System

---

## 📌 Overview & Problem Statement
Victims of atrocities (under the **Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989** and related protection frameworks) frequently experience prolonged, unmonitored psychological distress following complaint registration. This is driven by:
- Perpetrator threats & witness intimidation
- Repeated court depositions & judicial delays
- Release of accused on bail in proximity to victim residences
- Social ostracism / caste-based economic boycotts
- Severe delays in interim relief / rehabilitation compensation

**SAMVEDNA AI** bridges this critical institutional gap by continuously tracking psychological distress, analyzing voice and sentiment biomarkers, predicting crises 48–72 hours in advance, and directly connecting victims to District Authorities, Police Nodal Officers, and Psychological Counsellors in real time.

---

## 🌟 Key Innovations & Architecture

### 1. Voice Stress & Acoustic Prosody Analytics
- **Acoustic Biomarkers Extracted**: Fundamental Frequency ($F_0$ pitch volatility), Jitter (frequency instability), Shimmer (amplitude perturbation), Harmonics-to-Noise Ratio (HNR in dB), silence/pause ratio, and vocal tremor intensity (4–8 Hz modulation).
- **Clinical Prosody Classification**: Detects *Acute Panic*, *Elevated Threat Response*, *Apathy / Flat Affect (Depressive Numbness)*, and *Controlled Baseline*.

### 2. Multilingual NLP, Emotion & Trauma AI
- **Languages Supported**: Native support for **Hindi, English, Marathi, Tamil, Telugu, and Bengali**.
- **Trauma & Safety Lexicons**: Real-time detection of witness intimidation cues, court hearing dread, community ostracism/boycott, and acute despair / self-harm signals.
- **Empathetic AI Conversational Agent**: Delivers culturally grounded, trauma-informed responses without re-traumatizing victims.

### 3. Dynamic Distress Score (DDS) & Longitudinal Risk Modeling
- **Composite Dynamic Distress Score (0–100)**:
  $$\text{DDS}_t = w_1 \cdot \text{VoiceStress}_t + w_2 \cdot \text{NLPSentiment}_t + w_3 \cdot \text{ClinicalTrauma}_t + w_4 \cdot \text{LegalCaseRisk}_t + w_5 \cdot \text{EngagementDrop}_t$$
- **Velocity Spike Detection**: Flags rapid escalation when $\Delta\text{DDS} \ge 18\text{ points}$ within 7 days.
- **Explainable AI (XAI)**: Generates human-readable causal factor breakdowns for District Magistrates and Judges.

### 4. Government & Counsellor Portals
- **Victim Voice & Chat Portal**: Live Web Audio recording, real-time waveform visualizer, empathetic conversational agent, and 1-Touch Emergency SOS.
- **District Magistrate & Police Nodal Triage**: Automated priority queue, filter by PoA Act section, and 1-click armed police protection orders under Section 15A.
- **Counsellor Tele-Workbench**: 4-week longitudinal time-series trajectory chart, voice spectrogram biomarkers, and statutory intervention requisitioning.
- **National & State Analytics**: Stage-of-justice vulnerability analysis and policy impact briefs.

---

## 🚀 Quick Start Guide

### 1. Requirements
- Python 3.10+
- Dependencies: `fastapi`, `uvicorn`, `pydantic`, `numpy`, `python-multipart`, `requests`, `httpx`

### 2. Running the Server
```bash
python run_server.py
```
Open your browser and navigate to:
- **Interactive Web App**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3. Running Automated Verification
```bash
python test_system.py
python test_api.py
```

---

## ⚖️ Statutory & Legal Alignment
- **Section 15A SC/ST (PoA) Act, 1989**: Rights of Victims and Witnesses (Armed police escort, secure transit, residence picketing, safe house relocation).
- **Rule 5(1)(e) SC/ST (PoA) Rules**: Immediate psychological counselling and psychiatric trauma care.
- **Central Sector Scheme**: Mandatory 50% interim relief grant upon chargesheet filing.
- **Helpline Integrations**: NHAA 14566, Police 112, Tele-MANAS 14416, NALSA Legal Aid 15100.
