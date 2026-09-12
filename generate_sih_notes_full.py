# -*- coding: utf-8 -*-
import os
import sys
import math
import shutil
from fpdf import FPDF
from fpdf.enums import XPos, YPos

PDF_OUTPUT_PATH = r'C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\SAMVEDNA_AI_Backend_Complete_Notes.pdf'
DESKTOP_PATH = r'C:\Users\ACER\Desktop\SAMVEDNA_AI_Backend_Complete_Notes.pdf'
ARTIFACT_PATH = r'C:\Users\ACER\.gemini\antigravity\brain\21444267-dfec-404f-98a2-848b85893200\SAMVEDNA_AI_Backend_Complete_Notes.pdf'

class SIHBackendNotesPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=16)
        
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
        self.set_text_color(50, 80, 140)
        self.cell(100, 6, 'SAMVEDNA AI (NHAA 14566) | Backend Architecture & SIH Notes', align='L')
        self.set_font(self.font_family_name, 'I', 8)
        self.set_text_color(120, 130, 140)
        self.cell(90, 6, 'Smart India Hackathon Technical Reference', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(210, 225, 240)
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
        self.cell(95, 8, 'SAMVEDNA AI Team | Confidential & Technical Reference', align='L')
        self.cell(95, 8, f'Page {self.page_no()}', align='R')

    def chapter_title(self, number, title):
        if self.get_y() > 230:
            self.add_page()
        else:
            self.ln(5)
        self.set_fill_color(238, 244, 255)
        self.set_draw_color(40, 110, 220)
        self.set_line_width(1.0)
        self.rect(10, self.get_y(), 3.5, 10, 'F')
        self.set_x(16)
        self.set_font(self.font_family_name, 'B', 12)
        self.set_text_color(20, 50, 110)
        self.cell(184, 10, f'{number}. {title}', align='L', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def section_heading(self, title):
        if self.get_y() > 245:
            self.add_page()
        else:
            self.ln(2.5)
        self.set_font(self.font_family_name, 'B', 10.5)
        self.set_text_color(30, 70, 135)
        self.cell(0, 6.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(210, 225, 245)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)

    def sub_section(self, title):
        if self.get_y() > 255:
            self.add_page()
        else:
            self.ln(1.5)
        self.set_font(self.font_family_name, 'B', 9.2)
        self.set_text_color(45, 55, 75)
        self.cell(0, 5.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def body_p(self, text):
        self.set_font(self.font_family_name, '', 8.8)
        self.set_text_color(40, 50, 60)
        self.multi_cell(190, 4.6, text)
        self.ln(1.5)

    def bullet(self, title, desc):
        if self.get_y() > 260:
            self.add_page()
        self.set_font(self.font_family_name, 'B', 8.6)
        self.set_text_color(25, 35, 45)
        self.cell(5, 4.4, '-', align='C')
        t_w = self.get_string_width(title + ': ') + 1
        self.cell(t_w, 4.4, title + ': ')
        self.set_font(self.font_family_name, '', 8.6)
        self.set_text_color(55, 65, 75)
        rem_w = 190 - self.get_x()
        self.multi_cell(rem_w, 4.4, desc)
        self.ln(1)

    def code_block(self, code_text):
        lines = code_text.strip().split('\n')
        h = len(lines) * 4.0 + 5
        if self.get_y() + h > 265:
            self.add_page()
            
        start_y = self.get_y()
        self.set_fill_color(245, 247, 250)
        self.set_draw_color(215, 222, 230)
        self.set_line_width(0.3)
        self.rect(10, start_y, 190, h, 'DF')
        
        self.set_y(start_y + 2.5)
        self.set_font('Courier', '', 7.8)
        self.set_text_color(30, 40, 50)
        for line in lines:
            self.set_x(13)
            self.cell(184, 4.0, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2.5)

    def callout_box(self, title, text, box_type='info'):
        colors = {
            'info': ((238, 245, 255), (66, 133, 244), (20, 60, 140)),
            'warning': ((255, 248, 235), (245, 158, 11), (140, 80, 10)),
            'success': ((236, 253, 243), (16, 185, 129), (10, 100, 60)),
            'danger': ((254, 242, 242), (239, 68, 68), (150, 20, 20))
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
        self.set_text_color(50, 60, 70)
        self.set_x(15)
        self.multi_cell(180, 4.2, text)
        
        end_y = self.get_y()
        box_h = end_y - start_y + 3
        self.rect(10, start_y, 190, box_h, 'D')
        self.set_fill_color(*border)
        self.rect(10, start_y, 3, box_h, 'F')
        self.ln(3)

print('Part 1 of generator defined.')

# Import sections
import sections_part1
import sections_part2
import sections_part3
import sections_part4
import sections_part5

def build_pdf():
    print('Initializing PDF...')
    pdf = SIHBackendNotesPDF()
    
    # 1. Cover
    print('Generating Cover Page...')
    sections_part1.add_cover_page(pdf)
    
    # 2. TOC
    print('Generating Table of Contents...')
    sections_part1.add_toc(pdf)
    
    # 3. Sections 1 & 2
    print('Generating Sections 1 & 2...')
    sections_part2.add_section_1(pdf)
    sections_part2.add_section_2(pdf)
    
    # 4. Sections 3 & 4
    print('Generating Sections 3 & 4...')
    sections_part3.add_section_3(pdf)
    sections_part3.add_section_4(pdf)
    
    # 5. Sections 5, 6, 7 & 8
    print('Generating Sections 5, 6, 7 & 8...')
    sections_part4.add_section_5(pdf)
    sections_part4.add_section_6(pdf)
    sections_part4.add_section_7(pdf)
    sections_part4.add_section_8(pdf)
    
    # 6. Sections 9, 10, 11 & 12
    print('Generating Sections 9, 10, 11 & 12...')
    sections_part5.add_section_9(pdf)
    sections_part5.add_section_10(pdf)
    sections_part5.add_section_11(pdf)
    sections_part5.add_section_12(pdf)
    
    print(f'Writing PDF output... Total Pages: {pdf.page_no()}')
    pdf.output(PDF_OUTPUT_PATH)
    print(f' [OK] Saved to project: {PDF_OUTPUT_PATH}')
    
    shutil.copy(PDF_OUTPUT_PATH, DESKTOP_PATH)
    print(f' [OK] Saved to Desktop: {DESKTOP_PATH}')
    
    shutil.copy(PDF_OUTPUT_PATH, ARTIFACT_PATH)
    print(f' [OK] Saved to Artifacts: {ARTIFACT_PATH}')
    print('PDF Generation Complete!')

if __name__ == '__main__':
    build_pdf()
