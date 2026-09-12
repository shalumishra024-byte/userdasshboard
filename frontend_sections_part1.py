# -*- coding: utf-8 -*-
import os
import sys
import math
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class SIHFrontendNotesPDF(FPDF):
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
        self.set_text_color(14, 116, 144) # teal/cyan accent
        self.cell(100, 6, 'SAMVEDNA AI (NHAA 14566) | Frontend Architecture & UI/UX Notes', align='L')
        self.set_font(self.font_family_name, 'I', 8)
        self.set_text_color(120, 130, 140)
        self.cell(90, 6, 'Smart India Hackathon Technical Reference', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(200, 230, 235)
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
        self.cell(95, 8, 'SAMVEDNA AI Team | Frontend Technical Reference', align='L')
        self.cell(95, 8, f'Page {self.page_no()}', align='R')

    def chapter_title(self, number, title):
        if self.get_y() > 230:
            self.add_page()
        else:
            self.ln(5)
        self.set_fill_color(240, 253, 250) # light teal
        self.set_draw_color(14, 165, 233) # sky blue
        self.set_line_width(1.0)
        self.rect(10, self.get_y(), 3.5, 10, 'F')
        self.set_x(16)
        self.set_font(self.font_family_name, 'B', 12)
        self.set_text_color(12, 74, 110) # deep sky
        self.cell(184, 10, f'{number}. {title}', align='L', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def section_heading(self, title):
        if self.get_y() > 245:
            self.add_page()
        else:
            self.ln(2.5)
        self.set_font(self.font_family_name, 'B', 10.5)
        self.set_text_color(2, 132, 199)
        self.cell(0, 6.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(210, 235, 245)
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
            'info': ((240, 249, 255), (14, 165, 233), (3, 105, 161)),
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
    pdf.set_fill_color(224, 242, 254)
    pdf.set_draw_color(14, 165, 233)
    pdf.set_line_width(0.4)
    pdf.set_font(pdf.font_family_name, 'B', 8.5)
    pdf.set_text_color(2, 132, 199)
    pdf.cell(190, 7, '  SMART INDIA HACKATHON (SIH) | PROBLEM STATEMENT: NHAA 14566  ', align='C', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(8)
    
    # Title
    pdf.set_font(pdf.font_family_name, 'B', 26)
    pdf.set_text_color(12, 74, 110)
    pdf.cell(190, 12, 'SAMVEDNA AI', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font(pdf.font_family_name, 'I', 13)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(190, 8, 'Trauma-Informed Frontend Architecture & UI/UX Technical Guide', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(190, 6, 'Omnichannel Web Portal, Web Audio Prosody, Real-Time Analytics & i18n', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(6)
    
    # Decorative line
    pdf.set_draw_color(14, 165, 233)
    pdf.set_line_width(0.8)
    pdf.line(50, pdf.get_y(), 160, pdf.get_y())
    pdf.ln(6)
    
    # Subtitle Badge
    pdf.set_font(pdf.font_family_name, 'B', 12)
    pdf.set_text_color(3, 105, 161)
    pdf.cell(190, 7, 'COMPLETE FRONTEND TECHNICAL DOCUMENTATION & VIVA NOTES', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(pdf.font_family_name, '', 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(190, 5, 'Comprehensive Reference for SIH Team Members, Technical Viva & UI/UX Evaluations', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
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
        ('Frontend Architecture', 'Zero-Build SPA (Single-Page Application) | HTML5, Tailwind CSS, Vanilla JS'),
        ('Audio Ingestion Engine', 'Web Audio API (16kHz AudioContext, Linear 16-bit PCM Blob Encoder)'),
        ('Real-Time Visualizer', 'HTML5 Canvas AnalyserNode Waveform Renderer (#0284c7 dynamic stroke)'),
        ('Speech Interfaces', 'Web Speech API SpeechRecognition (STT) + SpeechSynthesis (TTS)'),
        ('Multilingual System', 'Dynamic DOM i18n Engine (Hindi, English, Bengali, Tamil, Telugu)'),
        ('Dual User Experience', 'Victim Omnichannel Portal vs. Official Caseworker & Nodal Console'),
        ('Data Visualizations', 'Chart.js Longitudinal Trajectory, Legal Stage Doughnut & Impact Radar'),
        ('Client Privacy/Security', 'Zero Local Storage of Audio, PII Masking, No App Store Footprint'),
        ('Accessibility Standard', 'WCAG 2.1 AA Compliant, Dark Calm Theme (#020617) for Trauma Reduction')
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
    pdf.set_fill_color(240, 253, 250)
    pdf.set_draw_color(153, 246, 228)
    pdf.rect(15, pdf.get_y(), 180, 22, 'DF')
    box_y = pdf.get_y() + 3
    pdf.set_y(box_y)
    pdf.set_x(20)
    pdf.set_font(pdf.font_family_name, 'B', 8.5)
    pdf.set_text_color(15, 118, 110)
    pdf.cell(170, 4.5, 'Smart India Hackathon Frontend Mastery Document', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(pdf.font_family_name, '', 8)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(190, 4.5, 'Details in-browser audio capture, live waveform math, client i18n, and trauma-informed UX.', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(190, 4.5, 'Designed for SIH jury questions regarding client performance, privacy, and accessibility.', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

def add_toc(pdf):
    pdf.add_page()
    pdf.chapter_title('TOC', 'Table of Contents')
    pdf.body_p('This document serves as the master frontend reference manual for the SAMVEDNA AI system. Review each section to master the client-side audio signal processing, state transitions, and trauma-informed design choices.')
    pdf.ln(2)
    
    toc_items = [
        ('1', 'Frontend Design Philosophy & Trauma-Informed UI/UX Principles'),
        ('2', 'Single-Page Application (SPA) Layout & Zero-Build Architecture'),
        ('3', 'In-Browser Audio Capture & Web Audio API Pipeline (app.js)'),
        ('4', 'Speech-to-Text (STT) & Text-to-Speech (TTS) Speech Integration'),
        ('5', 'Centralized Multilingual i18n Localization Engine (translations.js)'),
        ('6', 'Victim Omnichannel Portal: Components, State & Interactions'),
        ('7', 'Official Caseworker & Counsellor Dashboard UI Architecture'),
        ('8', 'Chart.js Longitudinal Trajectory & Regional Triage Visualizations'),
        ('9', 'Real-Time Alert Hub, Polling & Emergency Escalation UI'),
        ('10', 'Client-Side Security, Privacy & Survivor Safety Protections'),
        ('11', 'Network Resilience, Low-Bandwidth Optimization & 2G/3G Support'),
        ('12', 'SIH Grand Finale Viva & Jury Q&A Master Cheat Sheet for Frontend')
    ]
    
    for num, title in toc_items:
        pdf.set_font(pdf.font_family_name, 'B', 8.8)
        pdf.set_text_color(2, 132, 199)
        pdf.cell(10, 6.2, f'Sec {num}', align='L')
        pdf.set_font(pdf.font_family_name, '', 8.8)
        pdf.set_text_color(30, 41, 59)
        pdf.cell(165, 6.2, title, align='L')
        pdf.set_text_color(148, 163, 184)
        pdf.cell(15, 6.2, '..', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
    pdf.ln(4)
    pdf.callout_box(
        'Quick Tip for Frontend SIH Defense',
        'When evaluating judges ask why we used Vanilla JS instead of React or Vue, emphasize: (1) Zero-build, sub-100ms First Contentful Paint (FCP) on low-end smartphones; (2) Minimal memory footprint in volatile RAM; (3) Elimination of heavy bundle overhead on rural 2G/3G mobile networks; and (4) Complete zero-installation privacy for survivors facing domestic or caste surveillance.',
        'info'
    )
