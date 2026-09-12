# -*- coding: utf-8 -*-
import os
import sys
import shutil
from frontend_sections_part1 import SIHFrontendNotesPDF, add_cover_page, add_toc
import frontend_sections_part2
import frontend_sections_part3
import frontend_sections_part4

PDF_OUTPUT_PATH = r"C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\SAMVEDNA_AI_Frontend_Complete_Notes.pdf"
DESKTOP_PATH = r"C:\Users\ACER\Desktop\SAMVEDNA_AI_Frontend_Complete_Notes.pdf"
ARTIFACT_PATH = r"C:\Users\ACER\.gemini\antigravity\brain\21444267-dfec-404f-98a2-848b85893200\SAMVEDNA_AI_Frontend_Complete_Notes.pdf"
STATIC_PATH = r"C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\backend\static\SAMVEDNA_AI_Frontend_Complete_Notes.pdf"

def build_pdf():
    print("Initializing Frontend Notes PDF...")
    pdf = SIHFrontendNotesPDF()
    
    print("Generating Cover Page...")
    add_cover_page(pdf)
    
    print("Generating Table of Contents...")
    add_toc(pdf)
    
    print("Generating Sections 1 & 2...")
    frontend_sections_part2.add_section_1(pdf)
    frontend_sections_part2.add_section_2(pdf)
    
    print("Generating Sections 3 & 4...")
    frontend_sections_part2.add_section_3(pdf)
    frontend_sections_part2.add_section_4(pdf)
    
    print("Generating Sections 5, 6, 7 & 8...")
    frontend_sections_part3.add_section_5(pdf)
    frontend_sections_part3.add_section_6(pdf)
    frontend_sections_part3.add_section_7(pdf)
    frontend_sections_part3.add_section_8(pdf)
    
    print("Generating Sections 9, 10, 11 & 12...")
    frontend_sections_part4.add_section_9(pdf)
    frontend_sections_part4.add_section_10(pdf)
    frontend_sections_part4.add_section_11(pdf)
    frontend_sections_part4.add_section_12(pdf)
    
    print(f"Writing PDF output... Total Pages: {pdf.page_no()}")
    pdf.output(PDF_OUTPUT_PATH)
    print(f" [OK] Saved to project: {PDF_OUTPUT_PATH}")
    
    shutil.copy(PDF_OUTPUT_PATH, DESKTOP_PATH)
    print(f" [OK] Saved to Desktop: {DESKTOP_PATH}")
    
    shutil.copy(PDF_OUTPUT_PATH, ARTIFACT_PATH)
    print(f" [OK] Saved to Artifacts: {ARTIFACT_PATH}")
    
    shutil.copy(PDF_OUTPUT_PATH, STATIC_PATH)
    print(f" [OK] Saved to static directory: {STATIC_PATH}")
    
    print("Frontend PDF Generation Complete!")

if __name__ == '__main__':
    build_pdf()
