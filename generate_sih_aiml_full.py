import os
import shutil
import sys
from aiml_sections_part1 import SIHAIMLNotesPDF, add_cover_page, add_toc, add_section_1, add_section_2
from aiml_sections_part2 import add_section_3, add_section_4, add_section_5, add_section_6
from aiml_sections_part3 import add_section_7, add_section_8, add_section_9, add_section_10
from aiml_sections_part4 import add_section_11, add_section_12

def build_pdf():
    print("[*] Initializing PDF document...")
    pdf = SIHAIMLNotesPDF()

    print("[*] Adding Cover Page...")
    add_cover_page(pdf)

    print("[*] Adding Table of Contents...")
    add_toc(pdf)

    print("[*] Adding Section 1: AI/ML Problem Formulation...")
    add_section_1(pdf)

    print("[*] Adding Section 2: DSP & Acoustic Prosody Engine...")
    add_section_2(pdf)

    print("[*] Adding Section 3: Multilingual NLP Threat Mining...")
    add_section_3(pdf)

    print("[*] Adding Section 4: Russell Circumplex Affect Model...")
    add_section_4(pdf)

    print("[*] Adding Section 5: Multi-Modal Fusion Engine...")
    add_section_5(pdf)

    print("[*] Adding Section 6: Explainable AI & SHAP...")
    add_section_6(pdf)

    print("[*] Adding Section 7: Conversational Empathy & Gemini...")
    add_section_7(pdf)

    print("[*] Adding Section 8: In-Memory Pipeline...")
    add_section_8(pdf)

    print("[*] Adding Section 9: Evaluation Metrics...")
    add_section_9(pdf)

    print("[*] Adding Section 10: Latency Optimization...")
    add_section_10(pdf)

    print("[*] Adding Section 11: AI Safety & Bias Mitigation...")
    add_section_11(pdf)

    print("[*] Adding Section 12: SIH Viva & Defense Cheat Sheet...")
    add_section_12(pdf)

    filename = "SAMVEDNA_AI_AIML_Complete_Notes.pdf"
    pdf.output(filename)
    print(f"[+] Successfully built {filename} with {pdf.page_no()} pages!")

    # Destinations
    destinations = [
        r"C:\Users\ACER\Desktop\SAMVEDNA_AI_AIML_Complete_Notes.pdf",
        os.path.join(r"backend", "static", filename),
        os.path.join(r"C:\Users\ACER\.gemini\antigravity\brain\21444267-dfec-404f-98a2-848b85893200", filename)
    ]

    for dest in destinations:
        dest_dir = os.path.dirname(dest)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)
        shutil.copy2(filename, dest)
        print(f"[+] Copied to: {dest}")

if __name__ == "__main__":
    build_pdf()
