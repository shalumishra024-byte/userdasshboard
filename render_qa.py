import os
import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

qa_dir = r"d:\SAMVEDNA\qa_renders"
os.makedirs(qa_dir, exist_ok=True)

# 1. Render SAMVEDNA Reference PDF
ref_pdf = r"d:\SAMVEDNA\backend\static\SAMVEDNA_AI_SIH_Presentation.pdf"
doc_ref = pymupdf.open(ref_pdf)
print(f"SAMVEDNA reference pages: {len(doc_ref)}")
for i, page in enumerate(doc_ref):
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(qa_dir, f"samvedna_slide_{i+1}.png")
    pix.save(out_path)
    print(f"  Saved SAMVEDNA slide {i+1} -> {out_path}")

# 2. Render DEEPSEQ Target PDF
deep_pdf = r"d:\SAMVEDNA\Storm_Surge_DEEPSEQ_SIH_Presentation.pdf"
doc_deep = pymupdf.open(deep_pdf)
print(f"DEEPSEQ generated pages: {len(doc_deep)}")
for i, page in enumerate(doc_deep):
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(qa_dir, f"deepseq_slide_{i+1}.png")
    pix.save(out_path)
    print(f"  Saved DEEPSEQ slide {i+1} -> {out_path}")

print("Rendering complete!")
