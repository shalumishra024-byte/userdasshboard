# -*- coding: utf-8 -*-
from fpdf.enums import XPos, YPos

def add_section_5(pdf):
    pdf.chapter_title('5', 'Dynamic Distress Scoring (DDS) Multi-Modal Engine (distress_scoring.py)')
    
    pdf.section_heading('5.1 Multi-Modal Fusion Mathematics & Weight Calibration')
    pdf.body_p('Single-modality analysis (e.g. text sentiment only) fails in high-stress atrocity contexts because victims often under-report distress due to shame, shock, or fear. The Dynamic Distress Scoring (DDS) Engine fuses physical acoustic biomarkers, semantic linguistic cues, longitudinal clinical baselines, and legal risk factors into a unified composite score (0.0 to 100.0):')
    
    pdf.code_block(
        'DDS_base = ( 0.28 * S_voice ) + ( 0.28 * S_nlp ) + ( 0.20 * S_clinical ) + \n'
        '           ( 0.16 * S_legal ) + ( 0.08 * S_engagement )'
    )
    
    pdf.bullet('w_voice = 0.28 (28%)', 'Objective physiological biomarkers (F0 pitch volatility, jitter%, shimmer%, tremor) reflecting sympathetic autonomic arousal.')
    pdf.bullet('w_nlp = 0.28 (28%)', 'Semantic markers (intimidating threats, social ostracism, hopeless ideation, linguistic sentiment).')
    pdf.bullet('w_trauma_clinical = 0.20 (20%)', 'Clinical intake baseline (PHQ-9 depression index, PTSD severity, history of panic episodes).')
    pdf.bullet('w_legal_threat = 0.16 (16%)', 'Vulnerability index of current trial milestone (e.g. accused out on bail, trial deposition scheduled within 7 days, compensation delayed).')
    pdf.bullet('w_engagement = 0.08 (8%)', 'Behavioral volatility (sudden check-in dropouts, nocturnal activity shifts, speech latency delays).')

    pdf.section_heading('5.2 Non-Linear Safety Overrides (Life-Safety Rules)')
    pdf.body_p('Linear weighting alone can dilute acute emergencies. If a victim speaks calmly but describes a death threat, a linear weighted average could yield a false low score. To prevent catastrophic false negatives, non-linear overrides are hardcoded into the pipeline:')
    pdf.bullet('Threat Intimidation Override', 'If threat_detected == True: base_score = max(base_score, 72.0) + 12.0 (guarantees immediate HIGH or CRITICAL alert).')
    pdf.bullet('Self-Harm / Suicide Override', 'If self_harm_detected == True: base_score = max(base_score, 85.0) + 10.0 (instantly forces CRITICAL tier: 95.0 - 100.0).')

    pdf.section_heading('5.3 Risk Tiers & Color Codes')
    pdf.bullet('CRITICAL (80.0 - 100.0) | Red (#EF4444)', 'Immediate physical peril or acute psychiatric crisis. Dispatches real-time alerts to SP / District Nodal Officer.')
    pdf.bullet('HIGH (60.0 - 79.9) | Orange (#F97316)', 'Severe pressure, impending trial distress, or accused out on bail. Requires priority caseworker contact within 24 hours.')
    pdf.bullet('MODERATE (35.0 - 59.9) | Yellow (#EAB308)', 'Persistent trauma, economic hardship, or legal procedural fatigue. Scheduled bi-weekly supportive counselling.')
    pdf.bullet('LOW (0.0 - 34.9) | Green (#10B981)', 'Stable baseline, adaptive coping mechanisms, and safe environment. Routine monitoring.')

    pdf.section_heading('5.4 Velocity Metric & Trajectory Tracking (Delta DDS)')
    pdf.body_p('Static scores miss momentum. A victim moving from 40 to 65 in 48 hours is at much higher risk than one stable at 65. The engine calculates velocity: Delta DDS = DDS_current - DDS_previous:')
    pdf.bullet('Delta >= +18.0 pts', 'Acute Crisis Spike: Triggers immediate emergency intervention regardless of absolute score.')
    pdf.bullet('Delta >= +10.0 pts', 'Rapid Escalation: Flags dangerous deteriorating trajectory.')
    pdf.bullet('Delta <= -10.0 pts', 'Significant Recovery / Stabilization: Validates positive treatment efficacy.')

def add_section_6(pdf):
    pdf.chapter_title('6', 'Explainable AI (XAI) & Attribution Engine (xai_explainer.py)')
    
    pdf.section_heading('6.1 The Black-Box Challenge in Legal & Clinical Decision-Making')
    pdf.body_p('Judges, Special Public Prosecutors, and clinical psychologists cannot act on an opaque AI probability score. If an AI flags an atrocity case as CRITICAL, the authorities require transparent, auditable legal and physiological evidence before dispatching armed police pickets or relocating families.')
    
    pdf.section_heading('6.2 SHAP-Inspired Feature Attribution Matrix')
    pdf.body_p('The ExplainableAIEngine decomposes the composite DDS into human-interpretable evidence cards with exact point contributions and empirical quotes:')
    pdf.bullet('Acoustic Factor Card', 'e.g., Severe Vocal Instability (+22.4 pts): Jitter 2.8%, Tremor 68/100, 42% speech pause hesitation indicating physiological trauma freeze.')
    pdf.bullet('Threat Factor Card', 'e.g., Direct Perpetrator Threat (+32.5 pts): Extracted cues: dhamki, maar denge, case wapas, evidencing violation of Section 15A.')
    pdf.bullet('Social Boycott Card', 'e.g., Community Ostracism (+22.0 pts): Reported denial of drinking water and village expulsion (Section 3(1)(za)).')
    pdf.bullet('Legal Milestone Card', 'e.g., Accused Bail Vulnerability (+18.0 pts): Primary perpetrator released on High Court bail within 2km of victim residence.')
    pdf.bullet('Economic Delay Card', 'e.g., Pending Compensation Relief (+12.0 pts): 50% statutory interim relief delayed by 4 months, causing acute economic distress.')

def add_section_7(pdf):
    pdf.chapter_title('7', 'LLM Conversational Empathy & Google Gemini (gemini_service.py)')
    
    pdf.section_heading('7.1 High-Speed Sub-Second Multi-Model Cascade')
    pdf.body_p('Conversational empathy must be fast. If a distressed victim waits 10 seconds for a reply, anxiety surges. SAMVEDNA AI implements an intelligent failover cascade using Google GenAI SDK:')
    pdf.bullet('Primary: gemini-flash-lite-latest', 'Benchmarked at 0.75s - 1.1s response latency. Optimal balance of sub-second speed, empathy, and Hindi fluency.')
    pdf.bullet('Failover 1: gemini-3.5-flash-lite', 'Engaged automatically if primary encounters transient network latency.')
    pdf.bullet('Failover 2: gemini-3.7-flash', 'Engaged for complex legal/rehabilitation contextual synthesis (~1.5s).')
    pdf.bullet('Failover 3: gemini-3.6-flash', 'Tertiary backup ensuring 99.99% uptime.')

    pdf.section_heading('7.2 Trauma-Informed Clinical System Prompt Engineering')
    pdf.body_p('The system instruction enforces strict psychiatric guidelines:')
    pdf.bullet('Deep Grounding & Empathy', 'Validates survivor emotions, offers 5-4-3-2-1 sensory grounding techniques, and de-escalates panic.')
    pdf.bullet('Strict Non-Prescriptive Boundaries', 'Explicitly prohibited from prescribing pharmacological medication, diagnosing psychiatric illness, or predicting court trial outcomes.')
    pdf.bullet('Statutory Integration', 'Subtly reminds victims that NHAA 14566 and the District Legal Services Authority (DLSA) are available 24x7.')

    pdf.section_heading('7.3 Zero-Connectivity Local Dynamic Fallback Synthesizer')
    pdf.body_p('Atrocity incidents frequently occur in remote tribal areas with poor mobile networks, or during server outages. SAMVEDNA AI includes a zero-dependency local rule-based dynamic synthesizer that operates 100% offline. It parses the victim language, detected emotion, and legal stage, synthesizing grammatically correct, highly empathetic responses without making any external API calls.')

def add_section_8(pdf):
    pdf.chapter_title('8', 'Clinical Intervention & Decision Support Engine (intervention.py)')
    
    pdf.section_heading('8.1 Statutory Alignment with SC/ST PoA Act & Rules')
    pdf.body_p('SAMVEDNA AI does not merely monitor distress; it generates legally enforceable intervention directives for law enforcement and welfare authorities:')
    pdf.bullet('INT-PROT-01: Armed Police Picket (Within 2 Hours)', 'Mandated under Section 15A(6)(b) of the PoA Act. Triggered when threats or CRITICAL distress are detected. Targets Superintendent of Police (SP) for immediate armed residence security.')
    pdf.bullet('INT-RELOC-02: Safe House Relocation (Within 24 Hours)', 'Mandated under Section 15A(6)(c). Targets District Magistrate (DM) and Social Welfare Officer to authorize emergency transit to a secure facility.')
    pdf.bullet('INT-PSYC-03: Urgent Tele-MANAS Emergency Visit (Within 4 Hours)', 'Mandated under Rule 5(1)(e) PoA Rules. Directs District Mental Health Programme (DMHP) trauma psychologist to initiate video/in-person de-escalation.')
    pdf.bullet('INT-COMP-05: Fast-Track Interim Relief DBT (3 Business Days)', 'Mandated under Annexure I (Schedule) of the PoA Rules. Fast-tracks statutory interim compensation release directly into survivor bank accounts.')
    pdf.bullet('INT-LEGAL-06: Senior Legal Aid Counsel & In-Camera Trial Requisition', 'Mandated under Section 15A(10) PoA Act & NALSA. Requisitions Special Public Prosecutor coordination and video-link deposition for witness protection.')
