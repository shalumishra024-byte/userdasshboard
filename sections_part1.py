# -*- coding: utf-8 -*-
from fpdf.enums import XPos, YPos

def add_cover_page(pdf):
    pdf.add_page()
    pdf.ln(12)
    
    # Category Tag
    pdf.set_fill_color(230, 240, 255)
    pdf.set_draw_color(66, 133, 244)
    pdf.set_line_width(0.4)
    pdf.set_font(pdf.font_family_name, 'B', 8.5)
    pdf.set_text_color(30, 90, 200)
    pdf.cell(190, 7, '  SMART INDIA HACKATHON (SIH) | PROBLEM STATEMENT: NHAA 14566  ', align='C', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(8)
    
    # Title
    pdf.set_font(pdf.font_family_name, 'B', 26)
    pdf.set_text_color(20, 45, 95)
    pdf.cell(190, 12, 'SAMVEDNA AI', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font(pdf.font_family_name, 'I', 13)
    pdf.set_text_color(70, 90, 120)
    pdf.cell(190, 8, 'AI-Based Dynamic Mental Health Monitoring & Distress Prediction System', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(190, 6, 'for Atrocity Victims (National Helpline Against Atrocities - NHAA 14566)', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(6)
    
    # Decorative line
    pdf.set_draw_color(66, 133, 244)
    pdf.set_line_width(0.8)
    pdf.line(50, pdf.get_y(), 160, pdf.get_y())
    pdf.ln(6)
    
    # Subtitle Badge
    pdf.set_font(pdf.font_family_name, 'B', 12)
    pdf.set_text_color(35, 60, 110)
    pdf.cell(190, 7, 'COMPLETE BACKEND TECHNICAL DOCUMENTATION & VIVA NOTES', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(pdf.font_family_name, '', 9)
    pdf.set_text_color(100, 110, 125)
    pdf.cell(190, 5, 'Comprehensive Reference for SIH Team Members, Technical Viva & Jury Evaluations', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(8)
    
    # Metadata Overview Box
    start_y = pdf.get_y()
    pdf.set_fill_color(248, 250, 253)
    pdf.set_draw_color(210, 222, 238)
    pdf.set_line_width(0.4)
    pdf.rect(15, start_y, 180, 72, 'DF')
    pdf.rect(15, start_y, 3, 72, 'F')
    
    pdf.set_y(start_y + 4)
    meta_rows = [
        ('Project Code', 'SAMVEDNA-NHAA-14566 (Samvedna)'),
        ('Target Beneficiaries', 'Scheduled Castes & Scheduled Tribes (SC/ST) Atrocity Survivors'),
        ('Nodal Legislation', 'SC/ST (Prevention of Atrocities) Act 1989 & Amendment Rules 2016'),
        ('Backend Technology', 'FastAPI ASGI Framework + Uvicorn (Python 3.11+)'),
        ('Acoustic AI Engine', 'Zero-Disk Signal Prosody (F0, Jitter%, Shimmer%, HNR, MFCCs, Tremor)'),
        ('NLP & Threat AI', 'Multilingual 5 Indic Languages (HI, EN, BN, TA, TE) + Hinglish Transliteration'),
        ('Core Innovation', 'Dynamic Distress Scoring (DDS) + Explainable AI (SHAP XAI) + Gemini Flash-Lite'),
        ('Failover Architecture', 'Sub-second Multi-Model LLM Cascade with Local Offline Fallback Synthesizer'),
        ('Security & Privacy', 'Differential Privacy, Zero-Disk Audio Buffers, Field Masking (HIPAA/DPDP)')
    ]
    
    for label, val in meta_rows:
        pdf.set_x(22)
        pdf.set_font(pdf.font_family_name, 'B', 8.2)
        pdf.set_text_color(40, 60, 90)
        pdf.cell(48, 6.8, label + ':', align='L')
        pdf.set_font(pdf.font_family_name, '', 8.2)
        pdf.set_text_color(30, 40, 50)
        pdf.cell(120, 6.8, val, align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
    pdf.ln(8)
    
    # Team & Submission Details
    pdf.set_fill_color(240, 248, 255)
    pdf.set_draw_color(180, 210, 245)
    pdf.rect(15, pdf.get_y(), 180, 22, 'DF')
    box_y = pdf.get_y() + 3
    pdf.set_y(box_y)
    pdf.set_x(20)
    pdf.set_font(pdf.font_family_name, 'B', 8.5)
    pdf.set_text_color(30, 70, 140)
    pdf.cell(170, 4.5, 'Smart India Hackathon Team Reference Document', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(pdf.font_family_name, '', 8)
    pdf.set_text_color(60, 70, 85)
    pdf.cell(190, 4.5, 'Designed for deep technical defense, architectural transparency, and live viva presentation.', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(190, 4.5, 'Contains mathematical equations, code snippets, execution traces, and 20 jury cheat-sheet answers.', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

def add_toc(pdf):
    pdf.add_page()
    pdf.chapter_title('TOC', 'Table of Contents')
    pdf.body_p('This document serves as the master technical blueprint of the SAMVEDNA AI backend system. Review each section to understand both high-level system flows and deep algorithmic implementations.')
    pdf.ln(2)
    
    toc_items = [
        ('1', 'SIH Problem Statement & Legal Context (NHAA 14566, SC/ST PoA Act)'),
        ('2', 'High-Level System Architecture & End-to-End Check-in Pipeline'),
        ('3', 'Voice Prosody & Acoustic Stress Analytics Engine (voice_analytics.py)'),
        ('4', 'Multilingual NLP, Threat Mining & Intimidation Engine (nlp_engine.py)'),
        ('5', 'Dynamic Distress Scoring (DDS) Multi-Modal Engine (distress_scoring.py)'),
        ('6', 'Explainable AI (XAI) & Algorithmic Attribution Engine (xai_explainer.py)'),
        ('7', 'LLM Conversational Empathy & Google Gemini Integration (gemini_service.py)'),
        ('8', 'Clinical Decision Support & Automated Intervention Engine (intervention.py)'),
        ('9', 'Data Layer, In-Memory Repository & Schema Models (database.py, schemas.py)'),
        ('10', 'ASGI Web Framework & REST API Route Gateway (main.py, routers/*.py)'),
        ('11', 'Security, Data Privacy & Ethical AI Safeguards (DPDP Act & Trauma Ethics)'),
        ('12', 'SIH Grand Finale Viva & Jury Q&A Master Cheat Sheet (20 Key Questions)')
    ]
    
    for num, title in toc_items:
        pdf.set_font(pdf.font_family_name, 'B', 8.8)
        pdf.set_text_color(35, 75, 140)
        pdf.cell(10, 6.2, f'Sec {num}', align='L')
        pdf.set_font(pdf.font_family_name, '', 8.8)
        pdf.set_text_color(40, 50, 65)
        pdf.cell(165, 6.2, title, align='L')
        pdf.set_text_color(120, 130, 140)
        pdf.cell(15, 6.2, '..', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
    pdf.ln(4)
    pdf.callout_box(
        'Quick Tip for SIH Presenters',
        'When answering judges, always emphasize: (1) True multi-modal fusion combining acoustic physics with NLP semantics; (2) Strict legal alignment with Section 15A of the SC/ST PoA Act; (3) Explainable AI (XAI) that provides transparent evidence for counsellors; and (4) Complete offline fallback resilience if Internet drops.',
        'info'
    )

print('Cover and TOC module defined successfully.')
