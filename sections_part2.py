# -*- coding: utf-8 -*-
from fpdf.enums import XPos, YPos

def add_section_1(pdf):
    pdf.chapter_title('1', 'SIH Problem Statement & Legal Architecture')
    
    pdf.section_heading('1.1 Context: National Helpline Against Atrocities (NHAA 14566)')
    pdf.body_p('The National Helpline Against Atrocities (NHAA 14566) was instituted under the aegis of the Ministry of Social Justice and Empowerment (MoSJE), Government of India, to ensure prompt reporting, legal aid, and protection for victims belonging to Scheduled Castes (SC) and Scheduled Tribes (ST) facing offenses under the Scheduled Castes and the Scheduled Tribes (Prevention of Atrocities) Act, 1989 (PoA Act).')
    
    pdf.body_p('Despite statutory safeguards, National Crime Records Bureau (NCRB) data reflects an alarmingly high acquittal rate (surpassing 65% in several jurisdictions) in SC/ST atrocity trials. Comprehensive field studies indicate that the overwhelming driver of acquittals is not frivolous complaints, but victim and witness hostility induced by systemic post-incident intimidation, protracted trial trauma, social boycott, and psychological exhaustion.')
    
    pdf.section_heading('1.2 Statutory Legal Provisions Addressed by SAMVEDNA AI')
    pdf.bullet('Section 15A SC/ST (PoA) Act', 'Statutory duty of the State to afford witness and victim protection, including protection from intimidation, provision of armed pickets, safe house transit, and in-camera trial depositions.')
    pdf.bullet('Section 3(1)(za) & (zb) PoA Act', 'Criminalizes social boycotts, economic boycotts, and denial of customary rights to public paths, wells, and communal resources (traditionally known as hookah-paani band).')
    pdf.bullet('Rule 5(1)(e) PoA Rules 1995/2016', 'Mandates prompt psychiatric, medical, and psychological care for atrocity survivors and dependents through district healthcare machinery and Tele-MANAS.')
    pdf.bullet('Annexure I (Schedule) PoA Rules', 'Establishes a mandatory Direct Benefit Transfer (DBT) schedule (25%, 50%, 100%) for economic rehabilitation and interim relief.')
    
    pdf.section_heading('1.3 Why Traditional Helplines Fail (The Need for SAMVEDNA AI)')
    pdf.bullet('Reactive vs. Proactive', 'Existing helplines rely exclusively on the victim initiating a distress call during an emergency. Traumatized victims frequently experience psychological freeze, mutism, or acute fear of perpetrator eavesdropping.')
    pdf.bullet('Subjective Call Logs', 'Call-center operators lack clinical diagnostic tools to quantify invisible psychological distress, leading to under-reported risk and delayed escalation.')
    pdf.bullet('Retraumatization Cycle', 'Requiring victims to repetitively recount traumatic assault details to rotating operators compounds secondary victimization.')
    
    pdf.callout_box(
        'The SAMVEDNA AI Paradigm Shift',
        'SAMVEDNA AI converts NHAA 14566 into an active, continuous, multi-modal distress monitoring sentinel. By fusing non-invasive voice prosody biomarkers with trauma-informed multilingual NLP and legal stage attributes, the system objectively detects escalating distress before tragic self-harm or witness compromise occurs.',
        'success'
    )

def add_section_2(pdf):
    pdf.chapter_title('2', 'High-Level System Architecture & Request Lifecycle')
    
    pdf.section_heading('2.1 Multi-Tier Layered Architecture')
    pdf.body_p('SAMVEDNA AI is built on a high-throughput, microservices-ready layered ASGI architecture engineered for sub-second latency, zero-disk forensics, and multi-tenant operational security.')
    
    arch_code = (
        '+-------------------------------------------------------------------------+\n'
        '| 1. CLIENT LAYER: Omnichannel Victim Portal & Counsellor Dashboard      |\n'
        '|    - Web Audio API (16kHz PCM recording) | Multilingual UI (5 Languages)|\n'
        '+-------------------------------------------------------------------------+\n'
        '                                     | (HTTPS / REST & WebSockets)\n'
        '+-------------------------------------------------------------------------+\n'
        '| 2. ASGI GATEWAY LAYER: FastAPI 0.115+ & Uvicorn Async Runtime            |\n'
        '|    - Request Validation (Pydantic v2) | CORS Security | Zero-Disk Memory|\n'
        '+-------------------------------------------------------------------------+\n'
        '             |                                             |\n'
        '             v                                             v\n'
        '+----------------------------+               +----------------------------+\n'
        '| 3A. VOICE PROSODY ENGINE   |               | 3B. MULTILINGUAL NLP ENGINE|\n'
        '| - SciPy / NumPy Pipeline   |               | - Threat & Retaliation Lex |\n'
        '| - F0 Pitch & Jitter% / Shim|               | - Social Boycott Detection |\n'
        '| - HNR dB, MFCCs & Tremor   |               | - Hopelessness / Ideation  |\n'
        '+----------------------------+               +----------------------------+\n'
        '             |                                             |\n'
        '             +----------------------+----------------------+\n'
        '                                    |\n'
        '                                    v\n'
        '+-------------------------------------------------------------------------+\n'
        '| 4. DYNAMIC DISTRESS SCORING (DDS) ENGINE: Multi-Modal Fusion            |\n'
        '|    DDS = 0.28*Voice + 0.28*NLP + 0.20*Clinical + 0.16*Legal + 0.08*Eng  |\n'
        '|    Safety Overrides: Threat (+12 / min 72) | Self-Harm (+10 / min 85)   |\n'
        '+-------------------------------------------------------------------------+\n'
        '         |                         |                         |\n'
        '         v                         v                         v\n'
        '+-----------------+       +-----------------+       +---------------------+\n'
        '| 5. EXPLAINABLE  |       | 6. INTERVENTION |       | 7. LLM EMPATHY      |\n'
        '|    AI (XAI)     |       |    RECOMMENDER  |       |    GEMINI FLASH-LITE|\n'
        '| SHAP-style Cues |       | Sec 15A / NALSA |       | <1.5s Dynamic Synthe|\n'
        '+-----------------+       +-----------------+       +---------------------+\n'
        '                                   |\n'
        '                                   v\n'
        '+-------------------------------------------------------------------------+\n'
        '| 8. REAL-TIME ALERTING HUB: WebSockets, Push Alerts to SP/DM & Database  |\n'
        '+-------------------------------------------------------------------------+'
    )
    pdf.code_block(arch_code)
    
    pdf.section_heading('2.2 Step-by-Step Lifecycle of a Check-in Request')
    steps = [
        ('Step 1: Ingestion', 'Client records speech via Web Audio API or enters text; sends multipart/form-data to POST /api/v1/victim/checkin.'),
        ('Step 2: Buffer Parsing', 'FastAPI receives audio in-memory as bytes. Zero bytes are written to hard disk, preserving forensic integrity.'),
        ('Step 3: Acoustic Prosody', 'VoiceStressAnalyticsEngine reads raw 16-bit PCM arrays and extracts F0 pitch, Jitter%, Shimmer%, HNR, MFCCs, and tremor.'),
        ('Step 4: NLP Threat Mining', 'MultilingualNLPEmotionEngine cleans text, runs regex pattern matching against 5 Indic language lexicons for threats and caste boycotts.'),
        ('Step 5: Case Lookup', 'Database loads victim baseline: past DDS history, clinical PHQ score, legal milestone, and accused bail status.'),
        ('Step 6: DDS Calculation', 'DynamicDistressScoringEngine computes composite score, evaluates non-linear critical overrides, and calculates velocity (Delta DDS).'),
        ('Step 7: XAI Attribution', 'ExplainableAIEngine breaks down distress score into explainable points for legal and clinical transparency.'),
        ('Step 8: Interventions', 'AutomatedInterventionRecommender generates statutory action items based on SC/ST PoA Act and Tele-MANAS protocols.'),
        ('Step 9: LLM Empathy', 'GeminiService sends context to Gemini Flash-Lite with sub-second failover sequence or activates offline dynamic synthesizer.'),
        ('Step 10: Alert Hub', 'If DDS >= 80 or Threat detected, alert_hub immediately dispatches high-priority notifications to SP and District Nodal Officer.'),
        ('Step 11: Persistence', 'The check-in record is committed to the longitudinal database for time-series trend tracking.'),
        ('Step 12: Client Return', 'Unified JSON payload containing DDS score, XAI factors, interventions, and empathetic response is returned to the user.')
    ]
    for st_num, desc in steps:
        pdf.bullet(st_num, desc)

print('Section 1 and 2 defined successfully.')
