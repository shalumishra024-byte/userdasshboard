# -*- coding: utf-8 -*-
from fpdf.enums import XPos, YPos

def add_section_3(pdf):
    pdf.chapter_title('3', 'Multilingual NLP & Threat Intimidation Mining (nlp_engine.py)')
    
    pdf.section_heading('3.1 Multilingual Normalization & Transliteration')
    pdf.body_p('Victims in rural India frequently write or dictate in localized vernaculars or code-mixed Romanized transliterations (Hinglish, Banglish, Tanglish). Standard lemmatizers fail on colloquial slang. Our MultilingualNLPEmotionEngine utilizes phonetic n-gram regex matching across five language dictionaries (Hindi, English, Bengali, Tamil, Telugu), normalizing Unicode characters and stripping diacritics while preserving colloquial idioms.')

    pdf.section_heading('3.2 Statutory Threat & Witness Intimidation Mining')
    pdf.body_p('Witness tampering carries strict penal consequences under Section 15A of the PoA Act. The engine screens text for high-confidence coercive patterns:')
    pdf.bullet('Direct Physical Threats', 'Keywords: maar denge, jaan se, goli, badla, humki, mere phelbo, kolai, champesthamu, kill, murder, retaliation.')
    pdf.bullet('Procedural Coercion', 'Keywords: case wapas, court mat jao, complaint wapas le, jamin (bail), compromise karlo, drop complaint, withdraw case.')
    pdf.bullet('Surveillance & Stalking', 'Keywords: pichha karna, ghar ke bahar ghoomte hain, follow me, watching my house, accused out on bail.')

    pdf.section_heading('3.3 Caste Boycott & Social Ostracism Detection')
    pdf.body_p('Dominant-caste village councils often enforce non-physical sanctions to force FIR retractions, penalized under Section 3(1)(za) and 3(1)(zb) of the PoA Act. The NLP engine scans for historical idioms of ostracism: hookah pani band, paani band, gao se nikal, ration band, samajik bahishkar, oor vilakkam, and samajika bahishkarana.')

    pdf.section_heading('3.4 Crisis & Suicide Ideation Pattern Matching')
    pdf.body_p('Extracts acute hopelessness indicators: mar jana, jaan de dunga, kuch nahi bacha, insaf nahi milega, no hope, end my life, give up, cannot take this anymore. Triggering any suicide pattern immediately elevates the check-in to CRITICAL priority.')

def add_section_4(pdf):
    pdf.chapter_title('4', 'Russell Circumplex Affect Model & Longitudinal Trajectory')
    
    pdf.section_heading('4.1 2D Valence-Arousal Coordinate Space')
    pdf.body_p('Rather than restricting emotion to arbitrary discrete buckets, SAMVEDNA AI grounds its affect modeling in James Russell Circumplex Model of Affect (1980). Emotions are mapped on a continuous two-dimensional Cartesian plane:')
    pdf.bullet('Horizontal Axis: Valence (-1.0 to +1.0)', 'Represents pleasure vs. displeasure. Positive valence signifies relief and safety; negative valence reflects pain, terror, and despair.')
    pdf.bullet('Vertical Axis: Arousal (-1.0 to +1.0)', 'Represents physiological sympathetic activation. High arousal reflects sympathetic nervous excitation (tachycardia, vocal tremor); low arousal reflects parasympathetic freezing or depression.')

    pdf.section_heading('4.2 Quadrant Mapping in Atrocity Trauma')
    pdf.code_block(
        '+-------------------------------------------------------------------------+\\n'
        '| High Arousal, Negative Valence       | High Arousal, Positive Valence   |\\n'
        '| QUADRANT 1: Acute Panic / Terror     | QUADRANT 4: Empowered / Relieved |\\n'
        '| (High F0 volatility, High Jitter%)   | (Restored agency, Case progress) |\\n'
        '+--------------------------------------+----------------------------------+\\n'
        '| Low Arousal, Negative Valence        | Low Arousal, Positive Valence    |\\n'
        '| QUADRANT 2: Trauma Freeze / Numbing  | QUADRANT 3: Calm / Stable Coping |\\n'
        '| (Flat affect, Low HNR, Breathy mutism| (Baseline F0, Low Jitter <1.04%) |\\n'
        '+-------------------------------------------------------------------------+'
    )
    pdf.body_p('Clinical Significance: Detecting Quadrant 2 (Low Arousal, Negative Valence) is vital. Standard sentiment models misinterpret flat, quiet speech as "calm", but our acoustic prosody identifies it as trauma paralysis (depressive freeze).')

    pdf.section_heading('4.3 Longitudinal Trajectory Vector (dV/dt, dA/dt)')
    pdf.body_p('The engine tracks the temporal derivative vector across check-in sessions. A sudden negative shift in Valence combined with a sharp positive spike in Arousal indicates acute panic escalation, prompting proactive counsellor dispatch.')

def add_section_5(pdf):
    pdf.chapter_title('5', 'Dynamic Distress Scoring (DDS) Multi-Modal Fusion Engine')
    
    pdf.section_heading('5.1 Mathematical Multi-Modal Formulation')
    pdf.body_p('The composite Dynamic Distress Score (DDS) fuses five heterogeneous feature modalities into an authoritative index from 0.0 to 100.0:')
    pdf.code_block(
        'DDS_base = ( w_voice * S_voice ) + ( w_nlp * S_nlp ) + ( w_clinical * S_clinical ) + \\n'
        '           ( w_legal * S_legal ) + ( w_engagement * S_engagement )\\n'
        '\\n'
        'Where:\\n'
        '  w_voice      = 0.28   (28% Acoustic Prosody Physics)\\n'
        '  w_nlp        = 0.28   (28% Semantic NLP Threats & Sentiment)\\n'
        '  w_clinical   = 0.20   (20% Baseline PHQ-9 & Trauma History)\\n'
        '  w_legal      = 0.16   (16% Legal Vulnerability & Trial Milestones)\\n'
        '  w_engagement = 0.08   (8% Longitudinal Check-in Volatility)'
    )

    pdf.section_heading('5.2 Theoretical Justification of Weight Distribution')
    pdf.bullet('Equal Acoustic & NLP Weight (28% each)', 'Balances physical involuntary biomarkers (vocal tremor) with semantic linguistic intent (threat cues), preventing single-modality deception.')
    pdf.bullet('Clinical Trauma Baseline (20%)', 'Anchors the score to validated psychometric scales (PHQ-9 / PCL-5), preventing over-reaction to temporary situational mood swings.')
    pdf.bullet('Legal Milestone Vulnerability (16%)', 'Empirically incorporates procedural risks: cases where the accused was granted bail or where witness depositions are scheduled within 7 days carry elevated risk.')
    pdf.bullet('Engagement Volatility (8%)', 'Tracks behavioral anomalies such as sudden dropouts in communication, reflecting perpetrator confiscation of victim phones.')

    pdf.section_heading('5.3 Non-Linear Safety Overrides (Zero-False-Negative Safeguards)')
    pdf.body_p('Linear weighted averages can dangerously dilute emergency crises. We implement hard deterministic boundary overrides:')
    pdf.code_block(
        'if threat_detected:\\n'
        '    base_score = max(base_score, 72.0) + 12.0  # Guarantees >= 84.0 (CRITICAL)\\n'
        'if self_harm_detected:\\n'
        '    base_score = max(base_score, 85.0) + 10.0  # Guarantees >= 95.0 (CRITICAL)'
    )

    pdf.section_heading('5.4 Risk Stratification & Velocity Metric (Delta DDS)')
    pdf.bullet('Risk Stratification', 'CRITICAL (80.0-100.0 | Red), HIGH (60.0-79.9 | Orange), MODERATE (35.0-59.9 | Yellow), LOW (0.0-34.9 | Green).')
    pdf.bullet('Velocity Metric (Delta DDS)', 'Delta = DDS_t - DDS_{t-1}. Delta >= +18.0 flags an Acute Crisis Spike requiring immediate armed protection.')

def add_section_6(pdf):
    pdf.chapter_title('6', 'Explainable AI (XAI) & SHAP-Style Attribution Matrix')
    
    pdf.section_heading('6.1 Cooperative Game Theory & Shapley Value Formulation')
    pdf.body_p('In criminal justice and mental health, black-box neural networks cannot be admitted as legal evidence. Under cooperative game theory, Shapley values distribute the total payout among contributing feature players:')
    pdf.code_block(
        'phi_i(v) = sum_{S subseteq F \\ {i}} [ |S|! * (|F| - |S| - 1)! / |F|! ] * [ v(S cup {i}) - v(S) ]'
    )
    pdf.body_p('Where F is the set of all modalities, S is a coalition of features, and v(S) is the marginal distress prediction.')

    pdf.section_heading('6.2 Generating Evidentiary Judicial Attribution Cards')
    pdf.body_p('The ExplainableAIEngine translates Shapley contributions into court-admissible evidence cards:')
    pdf.bullet('Card 1: Acoustic Laryngeal Stress (+22.4 pts)', 'Evidence: Jitter 2.8%, Tremor 68/100, 42% speech hesitation indicative of acute autonomic trauma.')
    pdf.bullet('Card 2: Direct Perpetrator Intimidation (+32.5 pts)', 'Evidence: Extracted cues: dhamki, case wapas, evidencing violation of Section 15A PoA Act.')
    pdf.bullet('Card 3: Accused Bail Vulnerability (+18.0 pts)', 'Evidence: Primary perpetrator released on bail within 2km of survivor dwelling.')
