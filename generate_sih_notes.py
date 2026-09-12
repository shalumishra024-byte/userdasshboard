# -*- coding: utf-8 -*-
import os
import sys
import math
from fpdf import FPDF
from fpdf.enums import XPos, YPos

PDF_OUTPUT_PATH = r'C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\SAMVEDNA_AI_Backend_Complete_Notes.pdf'
DESKTOP_PATH = r'C:\Users\ACER\Desktop\SAMVEDNA_AI_Backend_Complete_Notes.pdf'
ARTIFACT_PATH = r'C:\Users\ACER\.gemini\antigravity\brain\21444267-dfec-404f-98a2-848b85893200\SAMVEDNA_AI_Backend_Complete_Notes.pdf'

class SIHBackendNotesPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=15)
        
        # Load fonts
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
        self.set_text_color(70, 90, 120)
        self.cell(0, 6, 'SAMVEDNA AI (NHAA 14566) | Complete Backend Technical Documentation & SIH Notes', align='L')
        self.set_font(self.font_family_name, 'I', 8)
        self.set_text_color(120, 130, 140)
        self.cell(0, 6, 'Smart India Hackathon Technical Reference', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(200, 215, 230)
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
        self.cell(95, 8, 'Confidential & Proprietary - SAMVEDNA AI Team', align='L')
        self.cell(95, 8, f'Page {self.page_no()}', align='R')

    def chapter_title(self, number, title):
        self.ln(4)
        self.set_fill_color(240, 245, 255)
        self.set_draw_color(60, 120, 216)
        self.set_line_width(0.8)
        
        # Left accent bar
        self.rect(10, self.get_y(), 3, 11, 'F')
        self.set_x(15)
        self.set_font(self.font_family_name, 'B', 13)
        self.set_text_color(25, 55, 110)
        self.cell(0, 11, f'{number}. {title}', align='L', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def section_heading(self, title):
        self.ln(2)
        self.set_font(self.font_family_name, 'B', 10.5)
        self.set_text_color(40, 75, 135)
        self.cell(0, 7, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(210, 225, 245)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)

    def sub_section(self, title):
        self.ln(1)
        self.set_font(self.font_family_name, 'B', 9.5)
        self.set_text_color(50, 60, 75)
        self.cell(0, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def body_p(self, text):
        self.set_font(self.font_family_name, '', 9)
        self.set_text_color(45, 55, 65)
        self.multi_cell(0, 4.8, text)
        self.ln(1.5)

    def bullet(self, title, desc):
        self.set_font(self.font_family_name, 'B', 8.8)
        self.set_text_color(30, 40, 50)
        self.cell(6, 4.5, chr(149), align='C')
        self.cell(self.get_string_width(title + ': ') + 1, 4.5, title + ': ')
        self.set_font(self.font_family_name, '', 8.8)
        self.set_text_color(55, 65, 75)
        # multi_cell remaining
        rem_w = 190 - self.get_x()
        self.multi_cell(rem_w, 4.5, desc)
        self.ln(1)

    def code_block(self, code_text):
        self.set_fill_color(244, 246, 249)
        self.set_draw_color(215, 222, 232)
        self.set_line_width(0.3)
        self.set_font('Courier', '', 8)
        self.set_text_color(35, 45, 55)
        
        lines = code_text.strip().split('\n')
        # Calculate height
        h = len(lines) * 4.2 + 4
        if self.get_y() + h > 275:
            self.add_page()
            
        start_y = self.get_y()
        self.rect(10, start_y, 190, h, 'DF')
        self.set_y(start_y + 2)
        for line in lines:
            self.set_x(13)
            self.cell(184, 4.2, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def callout_box(self, title, text, box_type='info'):
        colors = {
            'info': ((235, 243, 255), (66, 133, 244), (20, 60, 140)),
            'warning': ((255, 247, 230), (245, 158, 11), (140, 80, 10)),
            'success': ((235, 252, 240), (16, 185, 129), (10, 100, 60)),
            'danger': ((254, 242, 242), (239, 68, 68), (150, 20, 20))
        }
        bg, border, text_c = colors.get(box_type, colors['info'])
        
        self.ln(2)
        self.set_fill_color(*bg)
        self.set_draw_color(*border)
        self.set_line_width(0.5)
        
        start_y = self.get_y()
        # Estimate height
        # Title height = 5, text lines approx = ceil(len(text)/100)*4.5 + 6
        approx_h = 6 + math.ceil(len(text) / 95) * 4.5 + 4
        if start_y + approx_h > 275:
            self.add_page()
            start_y = self.get_y()
            
        self.set_font(self.font_family_name, 'B', 8.8)
        self.set_text_color(*text_c)
        self.set_x(14)
        self.cell(182, 5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_font(self.font_family_name, '', 8.5)
        self.set_text_color(50, 60, 70)
        self.set_x(14)
        self.multi_cell(182, 4.3, text)
        
        end_y = self.get_y()
        box_h = end_y - start_y + 2
        # draw rect behind
        self.rect(10, start_y, 190, box_h, 'D')
        self.set_fill_color(*border)
        self.rect(10, start_y, 2.5, box_h, 'F')
        self.ln(3)

print('Base class defined successfully.')
