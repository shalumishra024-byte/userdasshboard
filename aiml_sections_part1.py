# -*- coding: utf-8 -*-
import os
import sys
import math
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class SIHAIMLNotesPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=16)
        
        if os.path.exists('C:/Windows/Fonts/arial.ttf'):
            self.add_font('MainFont', '', 'C:/Windows/Fonts/arial.ttf')
            self.add_font('MainFont', 'B', 'C:/Windows/Fonts/arialbd.ttf')
            self.add_font('MainFont', 'I', 'C:/Windows/Fonts/ariali.ttf')
            self.font_family_name = 'MainFont'
        else:
            self.font_family_name = 'Helvetica'

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font(self.font_family_name, 'B', 8)
        self.set_text_color(109, 40, 217) # deep purple accent for AI/ML
        self.cell(100, 6, 'SAMVEDNA AI (NHAA 14566) | AI / ML Technical Architecture & Formulations', align='L')
        self.set_font(self.font_family_name, 'I', 8)
        self.set_text_color(120, 130, 140)
        self.cell(90, 6, 'Smart India Hackathon AI/ML Reference', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(220, 210, 245)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_draw_color(220, 225, 230)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(1)
        self.set_font(self.font_family_name, '', 8)
        self.set_text_color(130, 140, 150)
        self.cell(95, 8, 'SAMVEDNA AI Team | AI / ML Technical Reference', align='L')
        self.cell(95, 8, f'Page {self.page_no()}', align='R')

    def chapter_title(self, number, title):
        if self.get_y() > 230:
            self.add_page()
        else:
            self.ln(5)
        self.set_fill_color(245, 243, 255) # light purple
        self.set_draw_color(139, 92, 246) # violet
        self.set_line_width(1.0)
        self.rect(10, self.get_y(), 3.5, 10, 'F')
        self.set_x(16)
        self.set_font(self.font_family_name, 'B', 12)
        self.set_text_color(76, 29, 149) # deep violet
        self.cell(184, 10, f'{number}. {title}', align='L', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def section_heading(self, title):
        if self.get_y() > 245:
            self.add_page()
        else:
            self.ln(2.5)
        self.set_font(self.font_family_name, 'B', 10.5)
        self.set_text_color(109, 40, 217)
        self.cell(0, 6.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(225, 215, 250)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)

    def sub_section(self, title):
        if self.get_y() > 255:
            self.add_page()
        else:
            self.ln(1.5)
        self.set_font(self.font_family_name, 'B', 9.2)
        self.set_text_color(30, 41, 59)
        self.cell(0, 5.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def body_p(self, text):
        self.set_font(self.font_family_name, '', 8.8)
        self.set_text_color(45, 55, 65)
        self.multi_cell(190, 4.6, text)
        self.ln(1.5)

    def bullet(self, title, desc):
        if self.get_y() > 260:
            self.add_page()
        self.set_font(self.font_family_name, 'B', 8.6)
        self.set_text_color(15, 23, 42)
        self.cell(5, 4.4, '-', align='C')
        t_w = self.get_string_width(title + ': ') + 1
        self.cell(t_w, 4.4, title + ': ')
        self.set_font(self.font_family_name, '', 8.6)
        self.set_text_color(51, 65, 85)
        rem_w = 190 - self.get_x()
        self.multi_cell(rem_w, 4.4, desc)
        self.ln(1)

    def code_block(self, code_text):
        lines = code_text.strip().split('\n')
        h = len(lines) * 4.0 + 5
        if self.get_y() + h > 265:
            self.add_page()
            
        start_y = self.get_y()
        self.set_fill_color(248, 250, 252)
        self.set_draw_color(226, 232, 240)
        self.set_line_width(0.3)
        self.rect(10, start_y, 190, h, 'DF')
        
        self.set_y(start_y + 2.5)
        self.set_font('Courier', '', 7.8)
        self.set_text_color(15, 23, 42)
        for line in lines:
            self.set_x(13)
            self.cell(184, 4.0, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2.5)

    def callout_box(self, title, text, box_type='info'):
        colors = {
            'info': ((245, 243, 255), (139, 92, 246), (109, 40, 217)),
            'warning': ((255, 251, 235), (245, 158, 11), (180, 83, 9)),
            'success': ((240, 253, 244), (34, 197, 94), (21, 128, 61)),
            'danger': ((254, 242, 242), (239, 68, 68), (185, 28, 28))
        }
        bg, border, text_c = colors.get(box_type, colors['info'])
        
        approx_h = 7 + math.ceil(len(text) / 95) * 4.4 + 4
        if self.get_y() + approx_h > 265:
            self.add_page()
            
        start_y = self.get_y()
        self.set_fill_color(*bg)
        self.set_draw_color(*border)
        self.set_line_width(0.4)
        
        self.set_y(start_y + 2.5)
        self.set_font(self.font_family_name, 'B', 8.8)
        self.set_text_color(*text_c)
        self.set_x(15)
        self.cell(180, 5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_font(self.font_family_name, '', 8.5)
        self.set_text_color(51, 65, 85)
        self.set_x(15)
        self.multi_cell(180, 4.2, text)
        
        end_y = self.get_y()
        box_h = end_y - start_y + 3
        self.rect(10, start_y, 190, box_h, 'D')
        self.set_fill_color(*border)
        self.rect(10, start_y, 3, box_h, 'F')
        self.ln(3)

def add_cover_page(pdf):
    pdf.add_page()
    pdf.ln(12)
    
    # Category Tag
    pdf.set_fill_color(237, 233, 254)
    pdf.set_draw_color(139, 92, 246)
    pdf.set_line_width(0.4)
    pdf.set_font(pdf.font_family_name, 'B', 8.5)
    pdf.set_text_color(109, 40, 217)
    pdf.cell(190, 7, '  SMART INDIA HACKATHON (SIH) | PROBLEM STATEMENT: NHAA 14566  ', align='C', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(8)
    
    # Title
    pdf.set_font(pdf.font_family_name, 'B', 26)
    pdf.set_text_color(76, 29, 149)
    pdf.cell(190, 12, 'SAMVEDNA AI', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font(pdf.font_family_name, 'I', 13)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(190, 8, 'Artificial Intelligence, Machine Learning & Signal Processing Architecture', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(190, 6, 'Mathematical Formulations, Multi-Modal Fusion, SHAP XAI & LLM Integration', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(6)
    
    # Decorative line
    pdf.set_draw_color(139, 92, 246)
    pdf.set_line_width(0.8)
    pdf.line(50, pdf.get_y(), 160, pdf.get_y())
    pdf.ln(6)
    
    # Subtitle Badge
    pdf.set_font(pdf.font_family_name, 'B', 12)
    pdf.set_text_color(91, 33, 182)
    pdf.cell(190, 7, 'COMPLETE AI / ML TECHNICAL STUDY MANUAL & VIVA NOTES', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(pdf.font_family_name, '', 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(190, 5, 'Specialized Handbook for the AI/ML Team Member, Technical Jury Defense & Code Review', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(8)
    
    # Metadata Overview Box
    start_y = pdf.get_y()
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(226, 232, 240)
    pdf.set_line_width(0.4)
    pdf.rect(15, start_y, 180, 72, 'DF')
    pdf.rect(15, start_y, 3, 72, 'F')
    
    pdf.set_y(start_y + 4)
    meta_rows = [
        ('Core Machine Learning Domain', 'Affective Computing, Multimodal Fusion, Speech Biomarkers & NLP'),
        ('Audio Signal Processing (DSP)', 'Autocorrelation F0 Pitch, Jitter%, Shimmer%, HNR dB, 13 MFCCs, Micro-Tremor'),
        ('Natural Language Processing', 'Multilingual 5 Indic Languages (HI, EN, BN, TA, TE) + Transliteration Regex Mining'),
        ('Distress Prediction Paradigm', 'Dynamic Distress Scoring (DDS): Non-Linear Multi-Modal Fusion Engine'),
        ('Affect Modeling Theory', 'Russell Circumplex Model of Affect (2D Valence-Arousal Trajectory Mapping)'),
        ('Explainable AI (XAI)', 'SHAP-Inspired Cooperative Game Theory Feature Attribution for Judicial Evidentiary Audit'),
        ('Generative AI / LLM', 'Google Gemini Flash-Lite Sub-Second Cascade + Offline Dynamic Rule Synthesizer'),
        ('Optimization & Latency', 'Vectorized NumPy/SciPy Execution (<80ms DSP, <1.1s End-to-End LLM Turnaround)'),
        ('Clinical Decision Support', 'Deterministic Statutory Mapping (Sec 15A PoA Act, Rule 5(1)(e), Tele-MANAS)')
    ]
    
    for label, val in meta_rows:
        pdf.set_x(22)
        pdf.set_font(pdf.font_family_name, 'B', 8.2)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(48, 6.8, label + ':', align='L')
        pdf.set_font(pdf.font_family_name, '', 8.2)
        pdf.set_text_color(51, 65, 85)
        pdf.cell(120, 6.8, val, align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
    pdf.ln(8)
    
    # Team & Submission Details
    pdf.set_fill_color(245, 243, 255)
    pdf.set_draw_color(196, 181, 253)
    pdf.rect(15, pdf.get_y(), 180, 22, 'DF')
    box_y = pdf.get_y() + 3
    pdf.set_y(box_y)
    pdf.set_x(20)
    pdf.set_font(pdf.font_family_name, 'B', 8.5)
    pdf.set_text_color(91, 33, 182)
    pdf.cell(170, 4.5, 'Smart India Hackathon AI / ML Lead Reference Manual', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(pdf.font_family_name, '', 8)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(190, 4.5, 'Covers mathematical equations, signal processing derivations, fusion weights, and 20 jury cheat-sheet answers.', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(190, 4.5, 'Arming the AI/ML presenter with deep theoretical knowledge and verifiable algorithmic defense.', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

def add_toc(pdf):
    pdf.add_page()
    pdf.chapter_title('TOC', 'Table of Contents')
    pdf.body_p('This document serves as the master mathematical and algorithmic reference for the AI/ML Lead of the SAMVEDNA AI project. Review each section to understand both signal physics and high-level predictive models.')
    pdf.ln(2)
    
    toc_items = [
        ('1', 'AI/ML Problem Formulation & Multi-Modal Framework'),
        ('2', 'Digital Signal Processing & Acoustic Prosody Engine (voice_analytics.py)'),
        ('3', 'Multilingual NLP & Threat Intimidation Mining Engine (nlp_engine.py)'),
        ('4', 'Russell Circumplex Affect Model & Longitudinal Trajectory (mood_estimator.py)'),
        ('5', 'Dynamic Distress Scoring (DDS) Multi-Modal Fusion Engine (distress_scoring.py)'),
        ('6', 'Explainable AI (XAI) & SHAP-Inspired Attribution Matrix (xai_explainer.py)'),
        ('7', 'LLM Conversational Empathy & Google Gemini Optimization (gemini_service.py)'),
        ('8', 'Feature Normalization, In-Memory Signal Vectors & Preprocessing'),
        ('9', 'Evaluation Metrics, Calibration & Zero-False-Negative Safety Strategy'),
        ('10', 'Computational Efficiency, Vectorization & Sub-Second Latency Benchmarks'),
        ('11', 'AI Ethics, Algorithmic Fairness across Castes/Dialects & Anti-Hallucination'),
        ('12', 'SIH Grand Finale Viva & Jury Q&A Master Cheat Sheet for AI/ML Lead')
    ]
    
    for num, title in toc_items:
        pdf.set_font(pdf.font_family_name, 'B', 8.8)
        pdf.set_text_color(109, 40, 217)
        pdf.cell(10, 6.2, f'Sec {num}', align='L')
        pdf.set_font(pdf.font_family_name, '', 8.8)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(165, 6.2, title, align='L')
        pdf.set_text_color(148, 163, 184)
        pdf.cell(15, 6.2, '..', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
    pdf.ln(4)
    pdf.callout_box(
        'Crucial Advice for the AI/ML Presenter',
        'When speaking to AI judges at SIH, never say "we just used an LLM API". Emphasize: (1) We built a proprietary signal processing pipeline extracting physical biomarkers (F0, Jitter%, Shimmer%, HNR, MFCCs, Tremor); (2) We designed a domain-calibrated multi-modal fusion formula with non-linear safety overrides; (3) We implemented SHAP-inspired XAI for court admissibility; and (4) We built an offline-first dynamic synthesizer for network dropouts.',
        'info'
    )

def add_section_1(pdf):
    pdf.chapter_title('1', 'AI/ML Problem Formulation & Multi-Modal Framework')
    
    pdf.section_heading('1.1 Mathematical Formulation of Atrocity Distress Prediction')
    pdf.body_p('We formulate distress prediction as a continuous multi-modal regression and risk-stratification classification problem. Given a multi-modal check-in tuple at time t:')
    pdf.code_block('X_t = { A_t, T_t, C_i, L_i, H_{t-1} }')
    pdf.body_p('Where A_t is the raw audio waveform, T_t is the textual transcription or typed input, C_i is the clinical trauma baseline (PHQ-9 index), L_i is the legal case vulnerability vector (accused bail status, trial countdown), and H_{t-1} is the historical distress time-series. The goal is to estimate the true latent psychological distress DDS_t in [0.0, 100.0] and map it to an actionable risk tier R_t in {LOW, MODERATE, HIGH, CRITICAL}.')

    pdf.section_heading('1.2 The Failure of Single-Modality Sentiment Analysis')
    pdf.body_p('Standard NLP models (e.g. BERT, VADER, RoBERTa) evaluate semantic valence alone. In atrocity victim surveillance, single-modality NLP catastrophically fails due to:')
    pdf.bullet('1. Psychological Numbing & Shock', 'Survivors under severe trauma experience emotional detachment, entering flat, polite statements like "Sab theek hai" (Everything is fine) while living under acute terror.')
    pdf.bullet('2. Eavesdropping Constraint', 'Perpetrators or hostile village informants nearby prevent victims from speaking explicit complaints aloud.')
    pdf.bullet('3. Linguistic Code-Mixing', 'Complex multilingual switching between regional dialects and Hindi idioms confuses standard pre-trained language models.')

    pdf.section_heading('1.3 Multi-Modal Fusion Taxonomy: Hybrid Fusion Architecture')
    pdf.body_p('SAMVEDNA AI adopts a Hybrid Multi-Modal Fusion architecture:')
    pdf.bullet('Early Feature Extraction', 'Acoustic prosody biomarkers and NLP semantic vectors are extracted independently in specialized parallel pipelines.')
    pdf.bullet('Domain-Specific Calibration', 'Extracted sub-scores are weighted according to psychometric and legal vulnerability parameters.')
    pdf.bullet('Late Non-Linear Decision Fusion', 'Hard life-safety override thresholds prevent linear dilution, guaranteeing high recall for acute threats.')

def add_section_2(pdf):
    pdf.chapter_title('2', 'Digital Signal Processing & Acoustic Prosody Engine (voice_analytics.py)')
    
    pdf.section_heading('2.1 Speech Signal Pre-Processing & Framing')
    pdf.body_p('The input speech waveform x[n] sampled at 16,000 Hz undergoes pre-emphasis filtering to amplify high-frequency vocal tract resonance:')
    pdf.code_block('y[n] = x[n] - alpha * x[n-1]   (where alpha = 0.97)')
    pdf.body_p('The signal is framed into 25ms Hamming-windowed segments with a 10ms frame stride (hop length), yielding 100 analysis frames per second with 60% inter-frame overlap.')

    pdf.section_heading('2.2 Fundamental Frequency (F0 Pitch) via Normalized Autocorrelation')
    pdf.body_p('F0 represents the physical frequency of vocal fold vibration. For each voiced frame, we compute the Short-Time Autocorrelation Function (ACF):')
    pdf.code_block('R_xx(tau) = sum_{n=0}^{N - tau - 1} y[n] * y[n + tau]')
    pdf.body_p('We search for the maximum peak lag tau_peak within the physiological human vocal pitch range (75 Hz to 500 Hz, corresponding to lags 32 <= tau <= 213 at 16kHz). The fundamental frequency is calculated as F0 = F_s / tau_peak. Pitch Volatility is quantified as the standard deviation sigma(F0) across voiced frames.')

    pdf.section_heading('2.3 Vocal Jitter % (Cycle-to-Cycle Period Perturbation)')
    pdf.body_p('Jitter measures the short-term instability in fundamental pitch periods T_i. Under acute trauma, involuntary autonomic micro-spasms in the thyroarytenoid muscles prevent stable pitch maintenance:')
    pdf.code_block('Jitter_pct = ( (1 / (N - 1)) * sum_{i=1}^{N-1} |T_i - T_{i+1}| ) / ( (1 / N) * sum_{i=1}^N T_i ) * 100')
    pdf.body_p('Clinical Threshold: Normal voices exhibit jitter < 1.04%. Jitter > 2.0% signifies acute autonomic laryngeal stress.')

    pdf.section_heading('2.4 Vocal Shimmer % (Cycle-to-Cycle Amplitude Perturbation)')
    pdf.body_p('Shimmer measures the short-term instability in peak amplitude A_i between consecutive pitch cycles, reflecting subglottal respiratory pressure control:')
    pdf.code_block('Shimmer_pct = ( (1 / (N - 1)) * sum_{i=1}^{N-1} |A_i - A_{i+1}| ) / ( (1 / N) * sum_{i=1}^N A_i ) * 100')
    pdf.body_p('Clinical Threshold: Normal voices exhibit shimmer < 3.81%. Shimmer > 5.0% correlates strongly with weeping, trembling voice, or vocal exhaustion.')

    pdf.section_heading('2.5 Harmonics-to-Noise Ratio (HNR in dB)')
    pdf.body_p('HNR quantifies the ratio of periodic energy generated by vocal fold oscillation against aperiodic noise produced by turbulent glottal leakage:')
    pdf.code_block('HNR_dB = 10 * log10( E_periodic / E_noise )')
    pdf.body_p('Clinical Threshold: Normal speech exhibits HNR > 15 dB. Severe breathiness and trauma-induced mutism drop HNR below 10 dB.')

    pdf.section_heading('2.6 Mel-Frequency Cepstral Coefficients (MFCCs)')
    pdf.body_p('13 MFCCs are computed to capture vocal tract spectral envelope:')
    pdf.bullet('1. Short-Time Fourier Transform (STFT)', 'Computes power spectrum |X(k)|^2 via 512-point FFT.')
    pdf.bullet('2. Mel Filterbank Weighting', 'Passes spectrum through 26 triangular bandpass filters spaced linearly below 1kHz and logarithmically above 1kHz, simulating human cochlear frequency resolution: m = 2595 * log10(1 + f / 700).')
    pdf.bullet('3. Log Energy & DCT-II', 'Applies Discrete Cosine Transform to decorrelate filterbank energies into 13 orthogonal cepstral coefficients.')

    pdf.section_heading('2.7 Physiological Vocal Micro-Tremor (4-10 Hz)')
    pdf.body_p('Involuntary physiological tremor manifests as low-frequency modulation (4-10 Hz) in the amplitude and frequency envelopes, reflecting autonomic motor neuron oscillation during terror or panic.')
