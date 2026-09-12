import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Define Palette (exact SAMVEDNA AI design language)
C_NAVY       = RGBColor(15, 23, 42)     # #0F172A (Dark Navy background & primary header)
C_CARD_NAVY  = RGBColor(30, 41, 59)     # #1E293B (Card Dark Navy)
C_AMBER      = RGBColor(245, 158, 11)   # #F59E0B (Amber / Gold accent)
C_DEEP_AMBER = RGBColor(180, 83, 9)     # #B45309 (Deep Amber accent)
C_GREEN      = RGBColor(16, 185, 129)   # #10B981 (Emerald Green accent)
C_BLUE       = RGBColor(2, 132, 199)    # #0284C7 (Ocean / Tech Cyan accent)
C_RED        = RGBColor(220, 38, 38)    # #DC2626 (Crimson risk accent)
C_PURPLE     = RGBColor(124, 58, 237)   # #7C3AED (Purple accent)
C_WHITE      = RGBColor(255, 255, 255)  # #FFFFFF
C_LIGHT_BG   = RGBColor(248, 250, 252)  # #F8FAFC (Card canvas fill)
C_BORDER     = RGBColor(226, 232, 240)  # #E2E8F0 (Neutral card border)
C_SLATE_DARK = RGBColor(30, 41, 59)     # #1E293B
C_SLATE_TEXT = RGBColor(51, 65, 85)     # #334155 (High readability body text)
C_MUTED_GRAY = RGBColor(100, 116, 139)  # #64748B (Muted secondary text)

FONT_HEADING = "Segoe UI"
FONT_BODY    = "Segoe UI"

ASSETS_DIR = r"d:\SAMVEDNA\extracted_assets"

def create_presentation():
    prs = pptx.Presentation()
    # 16:9 Widescreen dimensions: 13.333 x 7.5 inches (960 x 540 pt)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Helper: Set Header and Footer
    def add_header_and_footer(slide, slide_title, ps_tag="MISCELLANEOUS"):
        # Top Header Bar (Height ~0.944 in / 68 pt)
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.944))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_NAVY
        top_bar.line.fill.background()
        
        # Category Tag Box
        tag_box = slide.shapes.add_textbox(Inches(0.486), Inches(0.11), Inches(9.8), Inches(0.28))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = f"SMART INDIA HACKATHON 2025 | PROBLEM STATEMENT ID: SIH25042 | {ps_tag}"
        p_tag.font.name = FONT_HEADING
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_AMBER
        
        # Slide Title Box
        title_box = slide.shapes.add_textbox(Inches(0.486), Inches(0.38), Inches(9.8), Inches(0.50))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = slide_title
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(17)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE
        
        # Right Watermark / Team Badge
        badge_box = slide.shapes.add_textbox(Inches(10.5), Inches(0.19), Inches(2.35), Inches(0.55))
        tf_badge = badge_box.text_frame
        tf_badge.word_wrap = True
        tf_badge.margin_left = tf_badge.margin_top = tf_badge.margin_right = tf_badge.margin_bottom = 0
        p_b1 = tf_badge.paragraphs[0]
        p_b1.text = "DEEPSEQ"
        p_b1.font.name = FONT_HEADING
        p_b1.font.size = Pt(10)
        p_b1.font.bold = True
        p_b1.font.color.rgb = C_AMBER
        p_b1.alignment = PP_ALIGN.RIGHT
        
        p_b2 = tf_badge.add_paragraph()
        p_b2.text = "Team STORM SURGE (77056)"
        p_b2.font.name = FONT_HEADING
        p_b2.font.size = Pt(8.5)
        p_b2.font.color.rgb = C_MUTED_GRAY
        p_b2.alignment = PP_ALIGN.RIGHT
        
        # Bottom Footer Bar (Height ~0.28 in / 20 pt)
        bot_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.22), Inches(13.333), Inches(0.28))
        bot_bar.fill.solid()
        bot_bar.fill.fore_color.rgb = C_NAVY
        bot_bar.line.fill.background()
        
        # Footer Text
        foot_box = slide.shapes.add_textbox(Inches(0.486), Inches(7.25), Inches(12.35), Inches(0.22))
        tf_foot = foot_box.text_frame
        tf_foot.word_wrap = True
        tf_foot.margin_left = tf_foot.margin_top = tf_foot.margin_right = tf_foot.margin_bottom = 0
        p_foot = tf_foot.paragraphs[0]
        p_foot.text = "SIH 2025 Idea Submission Template | PS ID: SIH25042 | Identifying Taxonomy & Assessing Biodiversity from eDNA Datasets"
        p_foot.font.name = FONT_BODY
        p_foot.font.size = Pt(8)
        p_foot.font.color.rgb = C_MUTED_GRAY
        
    # Helper: Create Styled Card with border accent and structured items
    def add_card(slide, left, top, width, height, title, items, border_color, fill_color=C_LIGHT_BG):
        # Card Background Shape
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        # Title Box
        t_box = slide.shapes.add_textbox(left + Inches(0.14), top + Inches(0.11), width - Inches(0.28), Inches(0.36))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        pt = tf_t.paragraphs[0]
        pt.text = title
        pt.font.name = FONT_HEADING
        pt.font.size = Pt(11.5)
        pt.font.bold = True
        pt.font.color.rgb = border_color
        
        # Body Content Box
        b_box = slide.shapes.add_textbox(left + Inches(0.14), top + Inches(0.47), width - Inches(0.28), height - Inches(0.55))
        tf_b = b_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
        
        for i, item in enumerate(items):
            p = tf_b.paragraphs[0] if i == 0 else tf_b.add_paragraph()
            p.space_after = Pt(4)
            p.space_before = Pt(2)
            
            if isinstance(item, tuple):
                lead, rest = item
                r1 = p.add_run()
                r1.text = "• " + lead + (" " if lead.endswith(":") else ": ")
                r1.font.name = FONT_BODY
                r1.font.size = Pt(9.2)
                r1.font.bold = True
                r1.font.color.rgb = C_SLATE_DARK
                
                r2 = p.add_run()
                r2.text = rest
                r2.font.name = FONT_BODY
                r2.font.size = Pt(9.2)
                r2.font.color.rgb = C_SLATE_TEXT
            else:
                r = p.add_run()
                r.text = item
                r.font.name = FONT_BODY
                r.font.size = Pt(9.2)
                r.font.color.rgb = C_SLATE_TEXT
                if item.startswith("•"):
                    r.font.bold = False
        return card

    print("[*] Generating Slide 1: Title Page...")
    # ==========================================
    # SLIDE 1: TITLE PAGE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.fill.background()
    
    # Header SIH Text
    t_sih = slide1.shapes.add_textbox(Inches(0.69), Inches(0.38), Inches(11.95), Inches(0.48))
    tf1 = t_sih.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "SMART INDIA HACKATHON 2025"
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = C_AMBER
    p1.alignment = PP_ALIGN.CENTER
    
    # Subtitle Text
    sub_sih = slide1.shapes.add_textbox(Inches(0.69), Inches(0.88), Inches(11.95), Inches(0.32))
    tf_sub = sub_sih.text_frame
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "IDEA SUBMISSION — OFFICIAL TITLE PAGE"
    p_sub.font.name = FONT_HEADING
    p_sub.font.size = Pt(12)
    p_sub.font.bold = True
    p_sub.font.color.rgb = C_WHITE
    p_sub.alignment = PP_ALIGN.CENTER
    
    # Main Project Card (Dark Navy container with Amber border)
    p_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.69), Inches(1.36), Inches(11.95), Inches(1.36))
    p_card.fill.solid()
    p_card.fill.fore_color.rgb = C_CARD_NAVY
    p_card.line.color.rgb = C_AMBER
    p_card.line.width = Pt(2)
    
    # Main Title
    pt_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.48), Inches(11.73), Inches(0.60))
    tf_pt = pt_box.text_frame
    p_pt = tf_pt.paragraphs[0]
    p_pt.text = "DEEPSEQ"
    p_pt.font.name = FONT_HEADING
    p_pt.font.size = Pt(28)
    p_pt.font.bold = True
    p_pt.font.color.rgb = C_AMBER
    p_pt.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    ps_box = slide1.shapes.add_textbox(Inches(0.8), Inches(2.10), Inches(11.73), Inches(0.48))
    tf_ps = ps_box.text_frame
    p_ps = tf_ps.paragraphs[0]
    p_ps.text = "AI-Powered Marine eDNA Taxonomy Identification & Biodiversity Assessment System"
    p_ps.font.name = FONT_HEADING
    p_ps.font.size = Pt(12)
    p_ps.font.bold = False
    p_ps.font.color.rgb = C_WHITE
    p_ps.alignment = PP_ALIGN.CENTER
    
    # Details White Card
    w_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.69), Inches(2.89), Inches(11.95), Inches(3.82))
    w_card.fill.solid()
    w_card.fill.fore_color.rgb = C_WHITE
    w_card.line.color.rgb = C_BORDER
    w_card.line.width = Pt(1)
    
    # Structured Details inside White Card
    d_box = slide1.shapes.add_textbox(Inches(1.05), Inches(3.05), Inches(11.23), Inches(3.45))
    tf_d = d_box.text_frame
    tf_d.word_wrap = True
    tf_d.margin_left = tf_d.margin_top = tf_d.margin_right = tf_d.margin_bottom = 0
    
    details = [
        ("Problem Statement ID", "SIH25042"),
        ("Problem Statement Title", "Identifying Taxonomy and Assessing Biodiversity from eDNA Datasets"),
        ("Target Ecosystem", "Marine Biodiversity, Deep-Sea Research & Global Taxonomic Repositories (CMLRE, SILVA, NCBI)"),
        ("Theme", "Miscellaneous / Marine Biotechnology & Ecological Surveillance"),
        ("PS Category", "Software"),
        ("Team ID", "77056"),
        ("Team Name", "STORM SURGE"),
        ("Core Innovation", "Alignment-Free Nucleotide Transformers (DNABERT-2) + Unsupervised Novel Taxa Discovery (HDBSCAN)"),
        ("Target Beneficiaries", "Marine Biologists, Oceanographic Researchers, Environmental Agencies & Biodiversity Policy Makers")
    ]
    
    for i, (lead, val) in enumerate(details):
        p = tf_d.paragraphs[0] if i == 0 else tf_d.add_paragraph()
        p.space_after = Pt(4)
        p.space_before = Pt(2)
        r1 = p.add_run()
        r1.text = "• " + lead + " :  "
        r1.font.name = FONT_HEADING
        r1.font.size = Pt(11)
        r1.font.bold = True
        r1.font.color.rgb = C_NAVY
        
        r2 = p.add_run()
        r2.text = val
        r2.font.name = FONT_BODY
        r2.font.size = Pt(11)
        r2.font.color.rgb = C_SLATE_TEXT
        
    # Bottom Footer Note
    f_box = slide1.shapes.add_textbox(Inches(0.69), Inches(6.86), Inches(11.95), Inches(0.30))
    tf_f = f_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "Smart India Hackathon 2025 | Official Idea Submission Template | Team STORM SURGE (77056)"
    p_f.font.name = FONT_BODY
    p_f.font.size = Pt(8.5)
    p_f.font.color.rgb = C_MUTED_GRAY
    p_f.alignment = PP_ALIGN.CENTER

    print("[*] Generating Slide 2: Proposed Solution...")
    # ==========================================
    # SLIDE 2: PROPOSED SOLUTION
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide2, "Proposed Solution (Describe your Idea / Solution / Prototype)")
    
    c1_items = [
        ("Incomplete Reference Databases", "Widespread misclassification and complete failure when identifying undocumented deep-sea marine taxa."),
        ("Slow, Manual Pipelines", "Traditional sequence alignment and bioinformatics workflows require weeks of manual curation to process eDNA datasets."),
        ("Prohibitive Compute Costs", "Pairwise sequence alignment against terabyte-scale databases demands costly, high-performance computing clusters."),
        ("Fragmented Workflows", "Disconnected command-line tools for read quality control, alignment, clustering, and biodiversity reporting."),
        ("Limited Accessibility", "High technical complexity excludes field marine biologists, conservation workers, and non-expert research teams.")
    ]
    add_card(slide2, Inches(0.486), Inches(1.10), Inches(3.96), Inches(5.90), "1. Currently Faced Problems", c1_items, C_NAVY)
    
    c2_items = [
        ("AI-Based Sequence Classification", "Autonomous deep-learning inference independent of incomplete and brittle reference databases."),
        ("Drastic Speed Acceleration", "Reduces end-to-end eDNA processing time from weeks to hours via GPU-accelerated embedding models."),
        ("Unsupervised Novel Species Discovery", "Uncovers uncataloged marine species through high-dimensional latent space density clustering (HDBSCAN)."),
        ("Real-Time Biodiversity Metrics", "Instantaneous computation of species richness, Shannon diversity index, and relative abundance distributions."),
        ("Unified End-to-End Platform", "Seamless one-click system for FASTQ file upload, quality trimming, AI inference, and rich visual dashboards."),
        ("Democratized Accessibility", "Intuitive cloud interface empowering field researchers, students, and conservation bodies to analyze eDNA effortlessly.")
    ]
    add_card(slide2, Inches(4.686), Inches(1.10), Inches(3.96), Inches(5.90), "2. Detailed Proposed Solution (DEEPSEQ)", c2_items, C_DEEP_AMBER)
    
    c3_items = [
        ("Core System Capabilities", "Integrated modular ecosystem:"),
        ("• AI Classification", "DNABERT-2 transformer embeddings capture deep sequence grammar."),
        ("• Real-Time Analysis", "Rapid batch inference delivers metrics in minutes."),
        ("• Cloud Platform", "Serverless autoscaling architecture eliminates idle costs."),
        ("• Biodiversity Metrics", "Automated species richness, evenness & abundance."),
        ("• Novelty Discovery", "Unsupervised clustering flags candidate new species."),
        ("• One-Click Pipeline", "Single unified workflow replacing multi-tool pipelines."),
        ("End-to-End Workflow Flow", "Sample → Sequencing → AI Pipeline → Embedding → Clustering → Classification → Result"),
        ("Interactive Deliverables", "Hosted Website (Live Prototype) | Video Demo | Source Code Repository | Figma Interactive UI Design")
    ]
    add_card(slide2, Inches(8.886), Inches(1.10), Inches(3.96), Inches(5.90), "3. Innovation & Key Deliverables", c3_items, C_GREEN)

    print("[*] Generating Slide 3: Technical Approach...")
    # ==========================================
    # SLIDE 3: TECHNICAL APPROACH
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide3, "Technologies to be Used and Implementation Methodology")
    
    s3_c1_items = [
        ("Raw Sequence Ingestion & QC", "Ingests raw eDNA FASTQ reads. Executes automated quality trimming and filtering via fastp (Q > 30) to eliminate low-quality reads and adapter noise."),
        ("Marker Gene Extraction", "Isolates hypervariable taxonomic regions (18S rRNA / COI marker genes) critical for eukaryotic and marine biodiversity profiling."),
        ("Nucleotide Foundation Transformers", "Pre-trained DNABERT-2 / Nucleotide Transformer encodes 6-mer DNA tokens into 768-dimensional dense vector embeddings without sequence alignment."),
        ("Dual-Track Classification & Discovery", "Two parallel inference engines:"),
        ("  • Supervised Track (Known Taxa)", "Contrastive representation learning (SupCon) cross-referenced with SILVA and NCBI databases for accurate species classification."),
        ("  • Unsupervised Track (Novel Taxa)", "HDBSCAN density clustering groups uncharacterized sequences, isolating candidate novel marine species."),
        ("Hierarchical Taxonomy Assignment", "Systematic top-down mapping: Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species."),
        ("Biotechnological Downstream Impact", "Novel taxa sequences routed for gene extraction, CRISPR exploration, and trait discovery across marine pharmacology, industry & ecology.")
    ]
    add_card(slide3, Inches(0.486), Inches(1.10), Inches(6.0), Inches(5.90), "1. Core Architecture & Biological Pipeline", s3_c1_items, C_NAVY)
    
    # Right Card: Flow of Project & Visual Hierarchy
    card_s3_right = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(1.10), Inches(6.10), Inches(5.90))
    card_s3_right.fill.solid()
    card_s3_right.fill.fore_color.rgb = C_LIGHT_BG
    card_s3_right.line.color.rgb = C_DEEP_AMBER
    card_s3_right.line.width = Pt(1.5)
    
    t_box_s3r = slide3.shapes.add_textbox(Inches(6.89), Inches(1.21), Inches(5.82), Inches(0.35))
    tf_s3r = t_box_s3r.text_frame
    p_s3r = tf_s3r.paragraphs[0]
    p_s3r.text = "2. Project Flow & Taxonomic Methodology"
    p_s3r.font.name = FONT_HEADING
    p_s3r.font.size = Pt(11.5)
    p_s3r.font.bold = True
    p_s3r.font.color.rgb = C_DEEP_AMBER
    
    # Insert Project Flow Image & Hierarchy Diagram
    flow_img_path = os.path.join(ASSETS_DIR, "p3_img5_110_1024x1536.jpeg")
    cone_img_path = os.path.join(ASSETS_DIR, "p3_img3_108_273x574.jpeg")
    dna_img_path  = os.path.join(ASSETS_DIR, "p3_img1_106_477x280.jpeg")
    
    if os.path.exists(flow_img_path):
        slide3.shapes.add_picture(flow_img_path, Inches(6.90), Inches(1.60), width=Inches(3.75))
    if os.path.exists(cone_img_path):
        slide3.shapes.add_picture(cone_img_path, Inches(10.85), Inches(1.60), width=Inches(1.85))
    if os.path.exists(dna_img_path):
        slide3.shapes.add_picture(dna_img_path, Inches(6.90), Inches(5.85), width=Inches(3.75))

    print("[*] Generating Slide 4: Feasibility Analysis...")
    # ==========================================
    # SLIDE 4: FEASIBILITY AND VIABILITY
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide4, "Feasibility Analysis, Potential Challenges and Mitigation Strategies")
    
    s4_c1_items = [
        ("Technical Feasibility", "High viability established:"),
        ("• Proven Genomic AI", "Transformer architectures (DNABERT-2, Nucleotide Transformer) demonstrate state-of-the-art accuracy on biological sequence representations."),
        ("• Abundant Open Datasets", "Tens of thousands of verified marine eDNA sequencing runs available on NCBI SRA, SILVA, and CMLRE for training and validation."),
        ("• Mature Bioinformatics Stack", "Built upon rock-solid foundations: BioPython, fastp, PyTorch, FAISS, and HDBSCAN."),
        ("Economic Feasibility", "Exceptional cost efficiency:"),
        ("• Extreme Cost Reduction", "Reduces per-sample bioinformatics analysis cost by 90%+ compared to manual outsourced laboratory pipelines."),
        ("• Scalable Cloud Architecture", "Serverless GPU inference (Modal / AWS) spins down when idle, eliminating ongoing server cluster expenses."),
        ("Operational Feasibility", "Accessible web & mobile interfaces enable on-vessel and field laboratory analysis without specialized bioinformaticians.")
    ]
    add_card(slide4, Inches(0.486), Inches(1.10), Inches(3.96), Inches(5.90), "1. Feasibility Analysis", s4_c1_items, C_NAVY)
    
    s4_c2_items = [
        ("Machine Learning Accuracy", "Environmental DNA samples frequently contain degraded fragments, chimeric sequences, and variable read lengths that challenge standard classifiers."),
        ("Reference Database Gaps", "More than 80% of deep-sea marine microorganisms lack cataloged reference genomes in SILVA or NCBI GenBank, leading to misclassification."),
        ("Data Quality & Primer Bias", "PCR amplification artifacts, primer-dimer contamination, and sequencing noise in marine field samples can introduce false positives."),
        ("Scalability & Computational Overhead", "High-throughput metagenomic runs generate millions of reads per water sample, risking latency bottlenecks and memory overflow.")
    ]
    add_card(slide4, Inches(4.686), Inches(1.10), Inches(3.96), Inches(5.90), "2. Potential Challenges & Risks", s4_c2_items, C_RED)
    
    s4_c3_items = [
        ("Contrastive DNA Pattern Learning", "Learns fundamental biological grammar and k-mer syntax via SupCon rather than relying on brittle exact string matching, ensuring high accuracy on degraded reads."),
        ("Unsupervised Novel Taxa Discovery", "HDBSCAN density clustering isolates uncataloged deep-sea species into distinct clusters without requiring prior database entries."),
        ("Automated Quality Harmonization", "Integrated fastp preprocessing pipeline trims low-quality reads (Q<30), removes adapter contamination, and isolates 18S/COI marker regions."),
        ("Alignment-Free Vector Indexing", "Replaces slow O(N*M) sequence alignments with O(1) FAISS embedding lookups, delivering sub-second inference even for massive datasets."),
        ("Multi-Database Cross-Validation", "Synthesizes taxonomic consensus across SILVA, NCBI, and CMLRE records to eliminate false-positive assignments.")
    ]
    add_card(slide4, Inches(8.886), Inches(1.10), Inches(3.96), Inches(5.90), "3. Mitigation Strategies", s4_c3_items, C_GREEN)

    print("[*] Generating Slide 5: Impact and Benefits...")
    # ==========================================
    # SLIDE 5: IMPACT AND BENEFITS
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide5, "Potential Impact on Target Audience and Multi-Dimensional Benefits")
    
    s5_c1_items = [
        ("Marine Biologists & Oceanographers", "Accelerates species identification 100x directly from seawater samples, bypassing time-consuming manual morphological sorting and destructive bottom-trawling."),
        ("Ecological & Conservation Agencies", "Provides automated early-warning monitoring for endangered species, invasive marine organisms, and ecosystem collapse signals."),
        ("Universities & Academic Labs", "Lowers the financial barrier of bioinformatics research, enabling smaller collegiate institutions without supercomputers to analyze eDNA."),
        ("Policy Makers & Marine Authorities", "Supplies quantifiable, verifiable biodiversity indices to support Marine Protected Area (MPA) designations and maritime policy compliance.")
    ]
    add_card(slide5, Inches(0.486), Inches(1.10), Inches(3.96), Inches(5.90), "1. Target Audience Impact", s5_c1_items, C_NAVY)
    
    s5_c2_items = [
        ("Analysis Compression (Weeks to Hours)", "Reduces analysis turnaround from weeks down to hours, enabling real-time ecological decision-making on research vessels."),
        ("Unprecedented Novel Species Discovery", "First-of-its-kind unsupervised discovery pipeline uncovering previously invisible, unculturable deep-sea marine biodiversity."),
        ("Database-Independent Resilience", "Maintains high classification performance even in unexplored oceanic trenches where reference genomes do not exist."),
        ("Unified Metagenomic Platform", "Single end-to-end web portal replacing 5+ fragmented CLI tools for QC, embedding, clustering, and biodiversity dashboarding."),
        ("Economic Cost Elimination", "Dramatically cuts sequencing interpretation costs, freeing budgetary funds for field conservation expeditions.")
    ]
    add_card(slide5, Inches(4.686), Inches(1.10), Inches(3.96), Inches(5.90), "2. Solution Benefits & Advantages", s5_c2_items, C_DEEP_AMBER)
    
    s5_c3_items = [
        ("UN SDG 14: Life Below Water", "Direct statutory alignment:"),
        ("• Target 14.2", "Sustainably manage and protect marine and coastal ecosystems to avoid significant adverse impacts."),
        ("• Target 14.a", "Increase scientific knowledge, research capacity, and marine technology transfer."),
        ("UN SDG 13: Climate Action", "Continuous biomonitoring detects climate-driven marine migrations, coral bleaching impacts, and ocean acidification stresses."),
        ("UN SDG 15: Terrestrial & Aquatic Life", "Versatile architecture easily extends to freshwater rivers, lakes, and endangered wetland biomes."),
        ("Global Scientific Collaboration", "Exports standardized Darwin Core biodiversity formats to accelerate global data exchange across oceanographic networks.")
    ]
    add_card(slide5, Inches(8.886), Inches(1.10), Inches(3.96), Inches(5.90), "3. UN SDGs & Global Alignment", s5_c3_items, C_GREEN)

    print("[*] Generating Slide 6: Technical Pipeline...")
    # ==========================================
    # SLIDE 6: TECHNICAL PIPELINE
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide6, "Technical Pipeline and Deep Learning Architecture")
    
    # Left Card: High-Dimensional eDNA Embeddings Cluster Analysis
    card_s6_left = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.486), Inches(1.10), Inches(5.20), Inches(5.90))
    card_s6_left.fill.solid()
    card_s6_left.fill.fore_color.rgb = C_LIGHT_BG
    card_s6_left.line.color.rgb = C_NAVY
    card_s6_left.line.width = Pt(1.5)
    
    t_box_s6l = slide6.shapes.add_textbox(Inches(0.62), Inches(1.21), Inches(4.90), Inches(0.35))
    tf_s6l = t_box_s6l.text_frame
    p_s6l = tf_s6l.paragraphs[0]
    p_s6l.text = "High-Dimensional eDNA Embeddings Cluster Analysis"
    p_s6l.font.name = FONT_HEADING
    p_s6l.font.size = Pt(11.5)
    p_s6l.font.bold = True
    p_s6l.font.color.rgb = C_NAVY
    
    # Embed 3D/2D cluster scatter plot
    scatter_img_path = os.path.join(ASSETS_DIR, "p6_img3_2048x1430.jpeg")
    if os.path.exists(scatter_img_path):
        slide6.shapes.add_picture(scatter_img_path, Inches(0.62), Inches(1.60), width=Inches(4.90))
        
    cap_box = slide6.shapes.add_textbox(Inches(0.62), Inches(5.35), Inches(4.90), Inches(1.50))
    tf_cap = cap_box.text_frame
    tf_cap.word_wrap = True
    tf_cap.margin_left = tf_cap.margin_top = tf_cap.margin_right = tf_cap.margin_bottom = 0
    p_c1 = tf_cap.paragraphs[0]
    p_c1.text = "• Latent Space Clustering: Nucleotide transformer encodes DNA sequences into 768-dim embeddings projected via UMAP/PCA."
    p_c1.font.name = FONT_BODY
    p_c1.font.size = Pt(8.5)
    p_c1.font.color.rgb = C_SLATE_TEXT
    p_c2 = tf_cap.add_paragraph()
    p_c2.text = "• Novelty Isolation: Distinct outlier clusters with high biological cohesion but low database similarity are flagged as putative novel marine taxa."
    p_c2.font.name = FONT_BODY
    p_c2.font.size = Pt(8.5)
    p_c2.font.color.rgb = C_SLATE_TEXT
    
    # Right Card: 6-Stage End-to-End Processing Pipeline
    s6_c2_items = [
        ("1. Objectives", "Accurate taxonomic identification, autonomous detection of novel species, high-speed GPU inference, and national-scale metagenomic scalability."),
        ("2. Data Preparation", "Obtain raw eDNA FASTQ files; perform quality filtering via fastp (Q>30); remove chimeric reads; extract target 18S rRNA / COI marker genes; prepare normalized model input tensors."),
        ("3. Model Processing", "Generate DNA embeddings using DNABERT-2; apply HDBSCAN density clustering; group sequences by biological homology; execute anomaly scoring for unknown taxa; cross-check against SILVA / NCBI."),
        ("4. Analysis & Interpretation", "Assign hierarchical taxonomy (Domain → Species); model community composition; quantify Shannon diversity and relative abundance; generate PCA / UMAP visualization plots."),
        ("5. Dashboard & Insights", "Interactive UI for marine researchers; display depth-wise heatmaps, taxonomic trees, and species abundance curves; provide novel taxa alert logs; export auditable CSV/JSON datasets."),
        ("6. Cloud Deployment", "Containerized Docker microservices deployed on AWS / GCP; serverless GPU inference endpoints (Modal / SageMaker); role-based authentication; secure API architecture for national ocean portals.")
    ]
    add_card(slide6, Inches(5.886), Inches(1.10), Inches(6.96), Inches(5.90), "6-Stage Technical Pipeline & Implementation", s6_c2_items, C_DEEP_AMBER)

    print("[*] Generating Slide 7: Research & References...")
    # ==========================================
    # SLIDE 7: RESEARCH AND REFERENCES
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide7, "Details / Links of Reference Literature, Datasets and Survey Work")
    
    s7_c1_items = [
        ("Nucleotide Transformer Foundation Models", "Dalla-Torre, H., et al. (2024). 'Nucleotide Transformer: Building and evaluating foundation models for genomics', Nature Methods, 21(2), 246–256. [doi:10.1038/s41592-024-02523-z]"),
        ("Hierarchical Density-Based Clustering (HDBSCAN)", "McInnes, L., Healy, J., & Astels, S. (2017). 'hdbscan: Hierarchical density based clustering for data science', Journal of Open Source Software, 2(11), 205. [https://hdbscan.readthedocs.io]"),
        ("Contrastive Learning in Genomics", "Zheng et al. (2025). 'Self-supervised contrastive learning on foundation genomic models for alignment-free metagenomics', arXiv:2509.25274.")
    ]
    add_card(slide7, Inches(0.486), Inches(1.10), Inches(6.0), Inches(2.75), "1. Genomic AI & Literature References", s7_c1_items, C_NAVY)
    
    s7_c2_items = [
        ("Centre for Marine Living Resources & Ecology (CMLRE)", "Ministry of Earth Sciences, Govt. of India — Ongoing Indian Ocean deep-sea biodiversity and marine eDNA sampling cruises."),
        ("SILVA Ribosomal RNA Database Project", "Curated, high-quality ribosomal RNA sequence database (18S / 16S / 28S) for taxonomic validation and tree calibration. [https://www.arb-silva.de]"),
        ("NCBI GenBank Taxonomy Database", "National Center for Biotechnology Information comprehensive genetic sequence repository and global taxonomic backbone. [https://www.ncbi.nlm.nih.gov]")
    ]
    add_card(slide7, Inches(6.75), Inches(1.10), Inches(6.10), Inches(2.75), "2. Reference Databases & Institutional Framework", s7_c2_items, C_DEEP_AMBER)
    
    # Bottom Card: Stakeholder Validation & Community Survey Statistics
    card_s7_bot = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.486), Inches(4.00), Inches(12.36), Inches(3.00))
    card_s7_bot.fill.solid()
    card_s7_bot.fill.fore_color.rgb = C_LIGHT_BG
    card_s7_bot.line.color.rgb = C_GREEN
    card_s7_bot.line.width = Pt(1.5)
    
    t_box_s7b = slide7.shapes.add_textbox(Inches(0.62), Inches(4.11), Inches(12.0), Inches(0.35))
    tf_s7b = t_box_s7b.text_frame
    p_s7b = tf_s7b.paragraphs[0]
    p_s7b.text = "3. Stakeholder Validation & Community Survey Statistics"
    p_s7b.font.name = FONT_HEADING
    p_s7b.font.size = Pt(11.5)
    p_s7b.font.bold = True
    p_s7b.font.color.rgb = C_GREEN
    
    # Survey 1 Info & Image
    s1_text_box = slide7.shapes.add_textbox(Inches(0.62), Inches(4.50), Inches(3.40), Inches(1.30))
    tf_s1 = s1_text_box.text_frame
    tf_s1.word_wrap = True
    p_s1_1 = tf_s1.paragraphs[0]
    p_s1_1.text = "Survey Question 1:"
    p_s1_1.font.name = FONT_HEADING
    p_s1_1.font.size = Pt(10)
    p_s1_1.font.bold = True
    p_s1_1.font.color.rgb = C_NAVY
    p_s1_2 = tf_s1.add_paragraph()
    p_s1_2.text = "Do you think monitoring biodiversity is important for protecting ecosystems?"
    p_s1_2.font.name = FONT_BODY
    p_s1_2.font.size = Pt(9)
    p_s1_2.font.color.rgb = C_SLATE_TEXT
    p_s1_3 = tf_s1.add_paragraph()
    p_s1_3.text = "Result: 95.6% YES  |  4.4% NO"
    p_s1_3.font.name = FONT_HEADING
    p_s1_3.font.size = Pt(9.5)
    p_s1_3.font.bold = True
    p_s1_3.font.color.rgb = C_GREEN
    
    pie1_path = os.path.join(ASSETS_DIR, "p7_img3_185_1200x742.jpeg")
    if os.path.exists(pie1_path):
        slide7.shapes.add_picture(pie1_path, Inches(4.10), Inches(4.50), width=Inches(2.35))
        
    # Survey 2 Info & Image
    s2_text_box = slide7.shapes.add_textbox(Inches(6.85), Inches(4.50), Inches(3.40), Inches(1.30))
    tf_s2 = s2_text_box.text_frame
    tf_s2.word_wrap = True
    p_s2_1 = tf_s2.paragraphs[0]
    p_s2_1.text = "Survey Question 2:"
    p_s2_1.font.name = FONT_HEADING
    p_s2_1.font.size = Pt(10)
    p_s2_1.font.bold = True
    p_s2_1.font.color.rgb = C_NAVY
    p_s2_2 = tf_s2.add_paragraph()
    p_s2_2.text = "Do you think eDNA can help detect endangered or invasive species early?"
    p_s2_2.font.name = FONT_BODY
    p_s2_2.font.size = Pt(9)
    p_s2_2.font.color.rgb = C_SLATE_TEXT
    p_s2_3 = tf_s2.add_paragraph()
    p_s2_3.text = "Result: 96.0% YES  |  4.0% NO"
    p_s2_3.font.name = FONT_HEADING
    p_s2_3.font.size = Pt(9.5)
    p_s2_3.font.bold = True
    p_s2_3.font.color.rgb = C_GREEN
    
    pie2_path = os.path.join(ASSETS_DIR, "p7_img4_186_1200x742.jpeg")
    if os.path.exists(pie2_path):
        slide7.shapes.add_picture(pie2_path, Inches(10.35), Inches(4.50), width=Inches(2.35))
        
    sum_box = slide7.shapes.add_textbox(Inches(0.62), Inches(6.30), Inches(12.0), Inches(0.55))
    tf_sum = sum_box.text_frame
    p_sum = tf_sum.paragraphs[0]
    p_sum.text = "Validation Insight: Overwhelming scientific consensus (>95%) confirms the critical necessity of automated, non-invasive eDNA biodiversity surveillance systems for conservation management."
    p_sum.font.name = FONT_BODY
    p_sum.font.size = Pt(9)
    p_sum.font.color.rgb = C_MUTED_GRAY

    print("[*] Generating Slide 8: UI Screens...")
    # ==========================================
    # SLIDE 8: UI SCREENS & PROTOTYPE
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide8, "Prototype UI & Application Showcase (Web & Mobile)")
    
    # Left Card: Web Platform
    card_s8_web = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.486), Inches(1.10), Inches(7.50), Inches(5.90))
    card_s8_web.fill.solid()
    card_s8_web.fill.fore_color.rgb = C_LIGHT_BG
    card_s8_web.line.color.rgb = C_NAVY
    card_s8_web.line.width = Pt(1.5)
    
    t_box_s8w = slide8.shapes.add_textbox(Inches(0.62), Inches(1.21), Inches(7.20), Inches(0.35))
    tf_s8w = t_box_s8w.text_frame
    p_s8w = tf_s8w.paragraphs[0]
    p_s8w.text = "Web Platform (Researcher Portal & Bioinformatics Dashboard)"
    p_s8w.font.name = FONT_HEADING
    p_s8w.font.size = Pt(11.5)
    p_s8w.font.bold = True
    p_s8w.font.color.rgb = C_NAVY
    
    # Add 4 representative web UI screenshots
    w_img1 = os.path.join(ASSETS_DIR, "p8_img4_203_1600x793.jpeg")
    w_img2 = os.path.join(ASSETS_DIR, "p8_img5_204_1600x783.jpeg")
    w_img3 = os.path.join(ASSETS_DIR, "p8_img7_206_1600x777.jpeg")
    w_img4 = os.path.join(ASSETS_DIR, "p8_img8_207_1600x771.jpeg")
    
    if os.path.exists(w_img1):
        slide8.shapes.add_picture(w_img1, Inches(0.65), Inches(1.60), width=Inches(3.45))
    if os.path.exists(w_img2):
        slide8.shapes.add_picture(w_img2, Inches(4.30), Inches(1.60), width=Inches(3.45))
    if os.path.exists(w_img3):
        slide8.shapes.add_picture(w_img3, Inches(0.65), Inches(3.60), width=Inches(3.45))
    if os.path.exists(w_img4):
        slide8.shapes.add_picture(w_img4, Inches(4.30), Inches(3.60), width=Inches(3.45))
        
    web_desc_box = slide8.shapes.add_textbox(Inches(0.65), Inches(5.60), Inches(7.10), Inches(1.25))
    tf_wd = web_desc_box.text_frame
    tf_wd.word_wrap = True
    p_wd1 = tf_wd.paragraphs[0]
    p_wd1.text = "• Web Capabilities: Drag-and-drop FASTQ upload | 3D UMAP embedding scatter visualizer | Rank-Abundance curves | Novelty Inspector bar charts | Hierarchical taxonomy tree browser | Geospatial biodiversity heatmaps."
    p_wd1.font.name = FONT_BODY
    p_wd1.font.size = Pt(8.5)
    p_wd1.font.color.rgb = C_SLATE_TEXT
    
    # Right Card: Mobile App
    card_s8_app = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.186), Inches(1.10), Inches(4.66), Inches(5.90))
    card_s8_app.fill.solid()
    card_s8_app.fill.fore_color.rgb = C_LIGHT_BG
    card_s8_app.line.color.rgb = C_BLUE
    card_s8_app.line.width = Pt(1.5)
    
    t_box_s8a = slide8.shapes.add_textbox(Inches(8.32), Inches(1.21), Inches(4.35), Inches(0.35))
    tf_s8a = t_box_s8a.text_frame
    p_s8a = tf_s8a.paragraphs[0]
    p_s8a.text = "Mobile App (Field Observer & Marine Station App)"
    p_s8a.font.name = FONT_HEADING
    p_s8a.font.size = Pt(11.5)
    p_s8a.font.bold = True
    p_s8a.font.color.rgb = C_BLUE
    
    # Add mobile UI screenshots
    m_img1 = os.path.join(ASSETS_DIR, "p8_img1_200_922x2048.jpeg")
    m_img2 = os.path.join(ASSETS_DIR, "p8_img2_201_922x2048.jpeg")
    m_img3 = os.path.join(ASSETS_DIR, "p8_img3_202_720x1600.jpeg")
    
    if os.path.exists(m_img1):
        slide8.shapes.add_picture(m_img1, Inches(8.32), Inches(1.60), width=Inches(1.38))
    if os.path.exists(m_img2):
        slide8.shapes.add_picture(m_img2, Inches(9.80), Inches(1.60), width=Inches(1.38))
    if os.path.exists(m_img3):
        slide8.shapes.add_picture(m_img3, Inches(11.28), Inches(1.60), width=Inches(1.38))
        
    mob_desc_box = slide8.shapes.add_textbox(Inches(8.32), Inches(5.60), Inches(4.35), Inches(1.25))
    tf_md = mob_desc_box.text_frame
    tf_md.word_wrap = True
    p_md1 = tf_md.paragraphs[0]
    p_md1.text = "• Mobile Capabilities: Portable analysis dashboard | Real-time sequence viewer with base-level ATCG highlights | Taxa confidence indicators | On-device GPS biodiversity mapping for field marine surveys."
    p_md1.font.name = FONT_BODY
    p_md1.font.size = Pt(8.5)
    p_md1.font.color.rgb = C_SLATE_TEXT

    print("[*] Generating Slide 9: Tech Stack & Team...")
    # ==========================================
    # SLIDE 9: TECH STACK & TEAM DETAILS
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header_and_footer(slide9, "Technology Stack & Team Credentials")
    
    # Top Card: Tech Stack Architecture
    card_s9_top = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.486), Inches(1.10), Inches(12.36), Inches(3.10))
    card_s9_top.fill.solid()
    card_s9_top.fill.fore_color.rgb = C_LIGHT_BG
    card_s9_top.line.color.rgb = C_DEEP_AMBER
    card_s9_top.line.width = Pt(1.5)
    
    t_box_s9t = slide9.shapes.add_textbox(Inches(0.62), Inches(1.21), Inches(12.0), Inches(0.35))
    tf_s9t = t_box_s9t.text_frame
    p_s9t = tf_s9t.paragraphs[0]
    p_s9t.text = "Full-Stack Architecture & Technology Stack"
    p_s9t.font.name = FONT_HEADING
    p_s9t.font.size = Pt(11.5)
    p_s9t.font.bold = True
    p_s9t.font.color.rgb = C_DEEP_AMBER
    
    # 4 Columns of Tech Stack
    tech_categories = [
        ("Backend & APIs", [
            "• FastAPI (Asynchronous REST)",
            "• Alembic (Database Migrations)",
            "• Redis Cache (In-Memory Latency)",
            "• Apache Kafka (Event Streaming)",
            "• Pub-Sub Architecture",
            "• Amazon S3 (FASTQ Storage)"
        ], C_NAVY),
        ("Machine Learning Core", [
            "• DNABERT-2 Nucleotide Transformer",
            "• HDBSCAN (Density-Based Clustering)",
            "• SupCon (Contrastive Learning)",
            "• PyTorch Deep Learning Framework",
            "• HuggingFace Transformers",
            "• FAISS Vector Similarity Engine"
        ], C_DEEP_AMBER),
        ("Frontend & Mobile", [
            "• Next.js 14 (React Framework)",
            "• TypeScript (Strict Typing)",
            "• Tailwind CSS (Modern Styling)",
            "• ShadCN UI Component Library",
            "• React Native (Cross-Platform Mobile)",
            "• Lucide Icons & Responsive Design"
        ], C_BLUE),
        ("DevOps & Cloud Infrastructure", [
            "• AWS Serverless Architecture",
            "• Modal (Serverless GPU Inference)",
            "• AWS SageMaker Model Pipelines",
            "• Docker Containerization",
            "• Kubernetes (K8s Orchestration)",
            "• Automated CI/CD Pipelines"
        ], C_GREEN)
    ]
    
    col_w = Inches(2.95)
    for idx, (cat_title, techs, cat_color) in enumerate(tech_categories):
        cx = Inches(0.65) + idx * Inches(3.05)
        cy = Inches(1.60)
        
        # Sub-card header
        sch_box = slide9.shapes.add_textbox(cx, cy, col_w, Inches(0.30))
        tf_sch = sch_box.text_frame
        p_sch = tf_sch.paragraphs[0]
        p_sch.text = cat_title
        p_sch.font.name = FONT_HEADING
        p_sch.font.size = Pt(10)
        p_sch.font.bold = True
        p_sch.font.color.rgb = cat_color
        
        # Tech items
        sct_box = slide9.shapes.add_textbox(cx, cy + Inches(0.32), col_w, Inches(2.15))
        tf_sct = sct_box.text_frame
        tf_sct.word_wrap = True
        tf_sct.margin_left = tf_sct.margin_top = tf_sct.margin_right = tf_sct.margin_bottom = 0
        for ti, tech in enumerate(techs):
            pt = tf_sct.paragraphs[0] if ti == 0 else tf_sct.add_paragraph()
            pt.space_after = Pt(2)
            pt.text = tech
            pt.font.name = FONT_BODY
            pt.font.size = Pt(8.5)
            pt.font.color.rgb = C_SLATE_TEXT
            
    # Bottom Card: Team STORM SURGE Credentials
    card_s9_bot = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.486), Inches(4.35), Inches(12.36), Inches(2.65))
    card_s9_bot.fill.solid()
    card_s9_bot.fill.fore_color.rgb = C_LIGHT_BG
    card_s9_bot.line.color.rgb = C_NAVY
    card_s9_bot.line.width = Pt(1.5)
    
    t_box_s9b = slide9.shapes.add_textbox(Inches(0.62), Inches(4.45), Inches(12.0), Inches(0.35))
    tf_s9b = t_box_s9b.text_frame
    p_s9b = tf_s9b.paragraphs[0]
    p_s9b.text = "Team STORM SURGE (Team ID: 77056) — Multi-Disciplinary Credentials"
    p_s9b.font.name = FONT_HEADING
    p_s9b.font.size = Pt(11.5)
    p_s9b.font.bold = True
    p_s9b.font.color.rgb = C_NAVY
    
    team_members = [
        ("ANISH SINGH CHAUHAN", "Team Leader", "B.Tech CSE (Data Science)", "3rd Year", "Backend Developer", C_NAVY),
        ("TRIPTI SHARMA", "Team Member", "B.Tech CSIT", "3rd Year", "UI/UX Designer", C_DEEP_AMBER),
        ("KARTIKAY SINGH", "Team Member", "B.Tech CSE (AIML)", "3rd Year", "Frontend Developer", C_BLUE),
        ("APURVI KANAUJIA", "Team Member", "B.Tech IT", "3rd Year", "UX Designer", C_GREEN),
        ("NAVYA GUPTA", "Team Member", "B.Tech CSE", "3rd Year", "Frontend Developer", C_PURPLE),
        ("DIVYANSH VERMA", "Team Member", "B.Tech CSE", "3rd Year", "Backend Developer", C_RED)
    ]
    
    mem_w = Inches(1.95)
    for idx, (name, role, degree, year, domain, badge_color) in enumerate(team_members):
        mx = Inches(0.65) + idx * Inches(2.03)
        my = Inches(4.85)
        
        # Member Card Box
        m_card = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, my, mem_w, Inches(1.95))
        m_card.fill.solid()
        m_card.fill.fore_color.rgb = C_WHITE
        m_card.line.color.rgb = badge_color
        m_card.line.width = Pt(1.2)
        
        mt_box = slide9.shapes.add_textbox(mx + Inches(0.06), my + Inches(0.08), mem_w - Inches(0.12), Inches(1.80))
        tf_mt = mt_box.text_frame
        tf_mt.word_wrap = True
        tf_mt.margin_left = tf_mt.margin_top = tf_mt.margin_right = tf_mt.margin_bottom = 0
        
        # Role Badge
        p_r = tf_mt.paragraphs[0]
        p_r.text = role.upper()
        p_r.font.name = FONT_HEADING
        p_r.font.size = Pt(7.5)
        p_r.font.bold = True
        p_r.font.color.rgb = badge_color
        p_r.alignment = PP_ALIGN.CENTER
        
        # Name
        p_n = tf_mt.add_paragraph()
        p_n.text = name
        p_n.font.name = FONT_HEADING
        p_n.font.size = Pt(8.5)
        p_n.font.bold = True
        p_n.font.color.rgb = C_NAVY
        p_n.alignment = PP_ALIGN.CENTER
        p_n.space_before = Pt(2)
        
        # Degree & Year
        p_d = tf_mt.add_paragraph()
        p_d.text = f"{degree}\n{year}"
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(8)
        p_d.font.color.rgb = C_SLATE_TEXT
        p_d.alignment = PP_ALIGN.CENTER
        p_d.space_before = Pt(2)
        
        # Domain
        p_dom = tf_mt.add_paragraph()
        p_dom.text = f"Domain: {domain}"
        p_dom.font.name = FONT_HEADING
        p_dom.font.size = Pt(7.8)
        p_dom.font.bold = True
        p_dom.font.color.rgb = C_MUTED_GRAY
        p_dom.alignment = PP_ALIGN.CENTER
        p_dom.space_before = Pt(4)

    # Output paths
    pptx_path = r"d:\SAMVEDNA\Storm_Surge_DEEPSEQ_SIH_Presentation.pptx"
    prs.save(pptx_path)
    print(f"[+] Successfully generated PowerPoint presentation: {pptx_path}")

if __name__ == "__main__":
    create_presentation()
