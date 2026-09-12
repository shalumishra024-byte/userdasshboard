import os
import shutil
import sys
from research_sections_part1 import SIHResearchNotesPDF, add_cover_page, add_toc, add_chapter_1, add_chapter_2
from research_sections_part2 import add_chapter_3, add_chapter_4
from research_sections_part3 import add_chapter_5, add_chapter_6, add_chapter_7

def build_pdf():
    print("[*] Initializing Research & Validation PDF document...")
    pdf = SIHResearchNotesPDF()

    print("[*] Adding Cover Page...")
    add_cover_page(pdf)

    print("[*] Adding Table of Contents & Evaluation Matrix...")
    add_toc(pdf)

    print("[*] Adding Chapter 1: Crime-Victim Problem Landscape...")
    add_chapter_1(pdf)

    print("[*] Adding Chapter 2: Limitations of Existing Solutions...")
    add_chapter_2(pdf)

    print("[*] Adding Chapter 3: Datasets & Multilingual Corpus...")
    add_chapter_3(pdf)

    print("[*] Adding Chapter 4: Empirical Testing & Benchmarks...")
    add_chapter_4(pdf)

    print("[*] Adding Chapter 5: Social Impact & UN SDGs...")
    add_chapter_5(pdf)

    print("[*] Adding Chapter 6: Scalability & Future Scope...")
    add_chapter_6(pdf)

    print("[*] Adding Chapter 7: SIH Viva Defense Cheat Sheet...")
    add_chapter_7(pdf)

    filename = "SAMVEDNA_AI_Research_Impact_Validation_Notes.pdf"
    pdf.output(filename)
    print(f"[+] Successfully built {filename} with {pdf.page_no()} pages!")

    # Destinations
    destinations = [
        r"C:\Users\ACER\Desktop\SAMVEDNA_AI_Research_Impact_Validation_Notes.pdf",
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
