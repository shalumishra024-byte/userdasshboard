import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Colors (SIH Reference Color Palette)
C_NAVY         = RGBColor(15, 23, 42)      # #0F172A
C_HEADER_NAVY  = RGBColor(30, 58, 138)     # #1E3A8A (Header Pill)
C_BANNER_GREEN = RGBColor(22, 78, 58)      # #164E3A (Banner Pill)
C_TEAL_HEADER  = RGBColor(13, 148, 136)    # #0D9488 (Card Sub-headers)
C_AMBER        = RGBColor(245, 158, 11)    # #F59E0B
C_BLUE_BORDER  = RGBColor(59, 130, 246)    # #3B82F6
C_LIGHT_BG     = RGBColor(248, 250, 252)   # #F8FAFC
C_WHITE        = RGBColor(255, 255, 255)   # #FFFFFF
C_SLATE_DARK   = RGBColor(15, 23, 42)      # #0F172A
C_SLATE_TEXT   = RGBColor(51, 65, 85)      # #334155
C_MUTED_GRAY   = RGBColor(100, 116, 139)   # #64748B
C_CARD_BORDER  = RGBColor(203, 213, 225)   # #CBD5E1
C_ARROW_BLUE   = RGBColor(37, 99, 235)     # #2563EB

FONT_NAME = "Segoe UI"
ASSETS_DIR = r"d:\SAMVEDNA\extracted_assets"
SIH_LOGO = os.path.join(ASSETS_DIR, "p1_img1_17_181x92.jpeg")
SIH_BULB_CLEAN = os.path.join(ASSETS_DIR, "s1_bulb_clean.png")
SIH_BULB_HEX = os.path.join(ASSETS_DIR, "s1_bulb_with_hexagons.png")

def build_presentation():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.500)
    blank_layout = prs.slide_layouts[6]

    def add_sih_header(slide, title_text, is_dual_banner=False):
        # Outer Frame
        outer = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.25), Inches(0.15), Inches(12.833), Inches(7.2))
        outer.fill.solid()
        outer.fill.fore_color.rgb = RGBColor(250, 250, 249)
        outer.line.color.rgb = RGBColor(226, 232, 240)
        outer.line.width = Pt(1.5)

        # Left Pill: SAMVEDNA AI
        left_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(0.28), Inches(2.2), Inches(0.55))
        left_pill.fill.solid()
        left_pill.fill.fore_color.rgb = C_HEADER_NAVY
        left_pill.line.fill.background()
        tf_lp = left_pill.text_frame
        tf_lp.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_lp = tf_lp.paragraphs[0]
        p_lp.text = "SAMVEDNA AI"
        p_lp.font.name = FONT_NAME
        p_lp.font.size = Pt(14)
        p_lp.font.bold = True
        p_lp.font.color.rgb = C_WHITE
        p_lp.alignment = PP_ALIGN.CENTER

        # Center Banner Pill(s)
        if not is_dual_banner:
            banner = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.8), Inches(0.28), Inches(5.6), Inches(0.55))
            banner.fill.solid()
            banner.fill.fore_color.rgb = C_BANNER_GREEN
            banner.line.fill.background()
            tf_b = banner.text_frame
            tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
            p_b = tf_b.paragraphs[0]
            p_b.text = title_text
            p_b.font.name = FONT_NAME
            p_b.font.size = Pt(17)
            p_b.font.bold = True
            p_b.font.color.rgb = C_WHITE
            p_b.alignment = PP_ALIGN.CENTER
        else:
            b1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.8), Inches(0.28), Inches(3.8), Inches(0.55))
            b1.fill.solid()
            b1.fill.fore_color.rgb = C_BANNER_GREEN
            b1.line.fill.background()
            tf_b1 = b1.text_frame
            tf_b1.vertical_anchor = MSO_ANCHOR.MIDDLE
            p1 = tf_b1.paragraphs[0]
            p1.text = "Solution Benefits"
            p1.font.name = FONT_NAME
            p1.font.size = Pt(16)
            p1.font.bold = True
            p1.font.color.rgb = C_WHITE
            p1.alignment = PP_ALIGN.CENTER

            b2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(0.28), Inches(4.3), Inches(0.55))
            b2.fill.solid()
            b2.fill.fore_color.rgb = C_BANNER_GREEN
            b2.line.fill.background()
            tf_b2 = b2.text_frame
            tf_b2.vertical_anchor = MSO_ANCHOR.MIDDLE
            p2 = tf_b2.paragraphs[0]
            p2.text = "Target Audience Impacts"
            p2.font.name = FONT_NAME
            p2.font.size = Pt(16)
            p2.font.bold = True
            p2.font.color.rgb = C_WHITE
            p2.alignment = PP_ALIGN.CENTER

        # Right Logo
        if os.path.exists(SIH_LOGO):
            slide.shapes.add_picture(SIH_LOGO, Inches(11.85), Inches(0.22), width=Inches(1.05), height=Inches(0.62))

    # =============================================================
    # SLIDE 1: Title / Official Idea Submission
    # =============================================================
    s1 = prs.slides.add_slide(blank_layout)
    outer1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.500))
    outer1.fill.solid()
    outer1.fill.fore_color.rgb = RGBColor(250, 247, 242)
    outer1.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(9.0), Inches(0.6))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "SMART INDIA HACKATHON 2025"
    p1.font.name = FONT_NAME
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(30, 63, 120)

    if os.path.exists(SIH_LOGO):
        s1.shapes.add_picture(SIH_LOGO, Inches(11.5), Inches(0.55), width=Inches(1.2), height=Inches(0.7))

    details = [
        ("Problem Statement ID :", " SIH25094 (PS ID: 94)"),
        ("Problem Statement Title :", " Identifying Trauma & Dynamic Distress Prediction System for Atrocity Victims (NHAA 14566)"),
        ("Theme :", " Smart Automation / Security and Surveillance (Vulnerable Community Protection)"),
        ("PS Category :", " Software"),
        ("Team ID :", " [Your Team ID / SIH-2025]"),
        ("Team Name :", " SAMVEDNA"),
        ("Target Ecosystem :", " National Helpline Against Atrocities (14566), Integrated Portal & SC/ST (PoA) Act 1989"),
        ("Core Innovation :", " In-Memory Voice Stress Analytics (Jitter/Shimmer DSP) + Multilingual Indic Emotion AI"),
        ("Beneficiaries :", " Atrocity complainants, rape survivors, threatened witnesses and vulnerable SC/ST families")
    ]

    dt_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.55), Inches(8.0), Inches(5.4))
    tf_dt = dt_box.text_frame
    tf_dt.word_wrap = True
    
    for idx, (label, val) in enumerate(details):
        p = tf_dt.add_paragraph() if idx > 0 else tf_dt.paragraphs[0]
        p.space_after = Pt(9)
        run_lbl = p.add_run()
        run_lbl.text = label
        run_lbl.font.name = FONT_NAME
        run_lbl.font.size = Pt(13.5)
        run_lbl.font.bold = True
        run_lbl.font.color.rgb = RGBColor(0, 51, 204)  # Royal Blue matching reference

        run_val = p.add_run()
        run_val.text = val
        run_val.font.name = FONT_NAME
        run_val.font.size = Pt(13.5)
        run_val.font.bold = True
        run_val.font.color.rgb = RGBColor(17, 24, 39)  # Dark Charcoal Black

    if os.path.exists(SIH_BULB_HEX):
        s1.shapes.add_picture(SIH_BULB_HEX, Inches(8.8), Inches(1.35), width=Inches(3.9), height=Inches(5.4))
    elif os.path.exists(SIH_BULB_CLEAN):
        s1.shapes.add_picture(SIH_BULB_CLEAN, Inches(9.2), Inches(1.6), width=Inches(3.4), height=Inches(4.9))

    # =============================================================
    # SLIDE 2: IDEA Title (Problem & Proposed Solution)
    # =============================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_sih_header(s2, "IDEA Title")

    wheel_path = os.path.join(ASSETS_DIR, "s2_capability_wheel.png")
    if os.path.exists(wheel_path):
        s2.shapes.add_picture(wheel_path, Inches(0.45), Inches(1.05), width=Inches(5.6), height=Inches(5.8))

    # Card 1: Problems
    prob_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.15), Inches(1.05), Inches(6.75), Inches(2.45))
    prob_box.fill.solid()
    prob_box.fill.fore_color.rgb = C_WHITE
    prob_box.line.color.rgb = C_CARD_BORDER
    prob_box.line.width = Pt(1.5)

    tf_pb = prob_box.text_frame
    tf_pb.word_wrap = True
    tf_pb.margin_left = tf_pb.margin_right = tf_pb.margin_top = Inches(0.2)
    p_head1 = tf_pb.paragraphs[0]
    p_head1.text = "Currently Faced Problems :"
    p_head1.font.name = FONT_NAME
    p_head1.font.size = Pt(13)
    p_head1.font.bold = True
    p_head1.font.color.rgb = C_HEADER_NAVY
    p_head1.alignment = PP_ALIGN.LEFT
    p_head1.space_after = Pt(6)

    probs = [
        ("No Continuous Psychological Monitoring: ", "Victims left unmonitored for months between trial dates"),
        ("Unchecked Perpetrator Intimidation: ", "Accused on bail threaten witnesses, causing hostile retractions"),
        ("Social & Economic Ostracism: ", "Caste boycotts, wage denial, and water cutoffs drive acute despair"),
        ("Delayed Reactive Interventions: ", "Welfare agencies act only after tragic mental crises or suicides occur"),
        ("Underreporting & Stigma: ", "Retaliation fear and lack of confidential channels silence vulnerable complainants")
    ]
    for p_lead, p_rest in probs:
        p = tf_pb.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(3)
        r_box = p.add_run()
        r_box.text = "☑  "
        r_box.font.name = FONT_NAME
        r_box.font.size = Pt(11)
        r_box.font.bold = True
        r_box.font.color.rgb = RGBColor(2, 132, 199)

        r_lead = p.add_run()
        r_lead.text = p_lead
        r_lead.font.name = FONT_NAME
        r_lead.font.size = Pt(9.5)
        r_lead.font.bold = True
        r_lead.font.color.rgb = C_SLATE_DARK

        r_txt = p.add_run()
        r_txt.text = p_rest
        r_txt.font.name = FONT_NAME
        r_txt.font.size = Pt(9.5)
        r_txt.font.bold = False
        r_txt.font.color.rgb = C_SLATE_TEXT

    # Card 2: Our Idea
    idea_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.15), Inches(3.62), Inches(6.75), Inches(2.80))
    idea_box.fill.solid()
    idea_box.fill.fore_color.rgb = C_WHITE
    idea_box.line.color.rgb = C_CARD_BORDER
    idea_box.line.width = Pt(1.5)

    tf_ib = idea_box.text_frame
    tf_ib.word_wrap = True
    tf_ib.margin_left = tf_ib.margin_right = tf_ib.margin_top = Inches(0.2)
    p_head2 = tf_ib.paragraphs[0]
    p_head2.text = "Our Idea :"
    p_head2.font.name = FONT_NAME
    p_head2.font.size = Pt(13)
    p_head2.font.bold = True
    p_head2.font.color.rgb = C_HEADER_NAVY
    p_head2.alignment = PP_ALIGN.LEFT
    p_head2.space_after = Pt(6)

    ideas = [
        ("Proactive Voice & Text Check-Ins: ", "Empathetic check-ins via Web, Mobile App, and automated IVRS 14566"),
        ("Dual-Engine In-Memory DSP & NLP: ", "Non-intrusive voice stress (<25ms) and threat NLP (<5ms) without GPU"),
        ("Dynamic Distress Score (DDS 0-100): ", "Multi-modal fusion tracking longitudinal trauma trajectory"),
        ("48-72h Crisis Pre-Alarm: ", "Early warning alerts before acute psychological breakdown occurs"),
        ("Automated Statutory Protection: ", "Directly requisitions Section 15A police pickets and Tele-MANAS"),
        ("100% DPDP Act 2023 Compliant: ", "Zero raw-audio storage; audio wiped in volatile RAM in <25ms")
    ]
    for i_lead, i_rest in ideas:
        p = tf_ib.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(3)
        r_box = p.add_run()
        r_box.text = "☑  "
        r_box.font.name = FONT_NAME
        r_box.font.size = Pt(11)
        r_box.font.bold = True
        r_box.font.color.rgb = RGBColor(2, 132, 199)

        r_lead = p.add_run()
        r_lead.text = i_lead
        r_lead.font.name = FONT_NAME
        r_lead.font.size = Pt(9.5)
        r_lead.font.bold = True
        r_lead.font.color.rgb = C_SLATE_DARK

        r_txt = p.add_run()
        r_txt.text = i_rest
        r_txt.font.name = FONT_NAME
        r_txt.font.size = Pt(9.5)
        r_txt.font.bold = False
        r_txt.font.color.rgb = C_SLATE_TEXT

    # Bottom Links Bar (Single Cohesive Pill with link icon matching reference)
    links_cont = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.10), Inches(6.52), Inches(6.80), Inches(0.48))
    links_cont.fill.solid()
    links_cont.fill.fore_color.rgb = C_WHITE
    links_cont.line.color.rgb = RGBColor(51, 65, 85)
    links_cont.line.width = Pt(1.5)

    tf_links = links_cont.text_frame
    tf_links.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_links.word_wrap = False
    tf_links.margin_left = Inches(0.12)
    tf_links.margin_right = Inches(0.12)
    p_link = tf_links.paragraphs[0]
    p_link.alignment = PP_ALIGN.LEFT

    r_icon = p_link.add_run()
    r_icon.text = "🔗  "
    r_icon.font.size = Pt(11)

    link_items = [
        ("Hosted Website", "(click here)"),
        ("Swagger API Docs", "(click here)"),
        ("Source Code", "(click here)"),
        ("System Specs", "(click here)")
    ]
    for idx, (title, action) in enumerate(link_items):
        if idx > 0:
            r_sep = p_link.add_run()
            r_sep.text = "    "
        r_t = p_link.add_run()
        r_t.text = title + " "
        r_t.font.name = FONT_NAME
        r_t.font.size = Pt(8.8)
        r_t.font.bold = True
        r_t.font.underline = True
        r_t.font.color.rgb = RGBColor(0, 51, 204)

        r_a = p_link.add_run()
        r_a.text = action
        r_a.font.name = FONT_NAME
        r_a.font.size = Pt(8.0)
        r_a.font.underline = True
        r_a.font.color.rgb = RGBColor(0, 51, 204)

    # =============================================================
    # SLIDE 3: TECHNICAL APPROACH
    # =============================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_sih_header(s3, "TECHNICAL APPROACH")

    fc_path = os.path.join(ASSETS_DIR, "s3_flowchart.png")
    if os.path.exists(fc_path):
        s3.shapes.add_picture(fc_path, Inches(0.45), Inches(1.05), width=Inches(3.4), height=Inches(5.9))

    fn_path = os.path.join(ASSETS_DIR, "s3_distress_funnel.png")
    if os.path.exists(fn_path):
        s3.shapes.add_picture(fn_path, Inches(4.0), Inches(1.05), width=Inches(3.2), height=Inches(5.9))

    c1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.35), Inches(1.05), Inches(5.5), Inches(2.85))
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_WHITE
    c1.line.color.rgb = C_CARD_BORDER
    c1.line.width = Pt(1.5)

    bh1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.35), Inches(1.05), Inches(5.5), Inches(0.45))
    bh1.fill.solid()
    bh1.fill.fore_color.rgb = C_TEAL_HEADER
    bh1.line.fill.background()
    p = bh1.text_frame.paragraphs[0]
    p.text = "Flow of Project / Dual-Engine Processing Core"
    p.font.name = FONT_NAME
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    tf_c1 = c1.text_frame
    tf_c1.margin_top = Inches(0.55)
    tf_c1.margin_left = tf_c1.margin_right = Inches(0.2)
    tf_c1.word_wrap = True
    
    c1_bullets = [
        "Acoustic Voice Stress DSP (<25ms CPU): Evaluates normalized autocorrelation F0 pitch, Jitter % (vocal fold instability), Shimmer % (amplitude perturbation), and HNR (dB).",
        "Vocal Tremor & Pause Ratio: Quantifies 4-8Hz micro-tremor and cognitive hesitation pauses indicative of suppressed panic or terror.",
        "Multilingual NLP & Threat Intelligence (<5ms): Regex threat vectorization across 6 Indic languages (Hi, En, Mr, Ta, Te, Bn) detecting boycott and intimidation.",
        "Russell 2D Circumplex Model: Maps emotional valence against arousal to isolate cathartic crying from acute crisis danger."
    ]
    for idx, b in enumerate(c1_bullets):
        p = tf_c1.add_paragraph() if idx > 0 else tf_c1.paragraphs[0]
        p.space_after = Pt(4)
        p.text = "• " + b
        p.font.name = FONT_NAME
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_SLATE_TEXT

    c2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.35), Inches(4.05), Inches(5.5), Inches(2.90))
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_WHITE
    c2.line.color.rgb = C_CARD_BORDER
    c2.line.width = Pt(1.5)

    bh2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.35), Inches(4.05), Inches(5.5), Inches(0.45))
    bh2.fill.solid()
    bh2.fill.fore_color.rgb = C_TEAL_HEADER
    bh2.line.fill.background()
    p = bh2.text_frame.paragraphs[0]
    p.text = "Foundation of Distress Scoring & Mathematical Model"
    p.font.name = FONT_NAME
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    tf_c2 = c2.text_frame
    tf_c2.margin_top = Inches(0.55)
    tf_c2.margin_left = tf_c2.margin_right = Inches(0.2)
    tf_c2.word_wrap = True

    c2_bullets = [
        "Composite Dynamic Distress Score: DDS = 0.28·Voice + 0.28·NLP + 0.20·Clinical + 0.16·Legal + 0.08·Engagement.",
        "Non-Linear Critical Safety Triggers: Immediate score elevation: Max(DDS, 72)+12 for perpetrator threats; Max(DDS, 85)+10 for acute suicidal despair.",
        "Velocity Spike Detection (Delta-DDS): A jump of >= 18 points between check-ins flags an Acute Crisis Spike 48-72h in advance.",
        "Explainable AI (XAI) Attribution: Produces court-admissible SHAP factor attribution breakdown adhering to Section 61 BNSS standards."
    ]
    for idx, b in enumerate(c2_bullets):
        p = tf_c2.add_paragraph() if idx > 0 else tf_c2.paragraphs[0]
        p.space_after = Pt(4)
        p.text = "• " + b
        p.font.name = FONT_NAME
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_SLATE_TEXT

    # =============================================================
    # SLIDE 4: Feasibility And Viability
    # =============================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_sih_header(s4, "Feasibility And Viability")

    tree_path = os.path.join(ASSETS_DIR, "s4_feasibility_tree.png")
    if os.path.exists(tree_path):
        s4.shapes.add_picture(tree_path, Inches(0.45), Inches(1.05), width=Inches(6.0), height=Inches(2.7))

    ch_path = os.path.join(ASSETS_DIR, "s4_challenges_flow.png")
    if os.path.exists(ch_path):
        s4.shapes.add_picture(ch_path, Inches(0.45), Inches(3.90), width=Inches(6.0), height=Inches(3.0))

    strat_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.65), Inches(1.05), Inches(6.25), Inches(5.85))
    strat_box.fill.solid()
    strat_box.fill.fore_color.rgb = C_WHITE
    strat_box.line.color.rgb = C_CARD_BORDER
    strat_box.line.width = Pt(1.5)

    sb_h = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.65), Inches(1.05), Inches(6.25), Inches(0.55))
    sb_h.fill.solid()
    sb_h.fill.fore_color.rgb = C_TEAL_HEADER
    sb_h.line.fill.background()
    p = sb_h.text_frame.paragraphs[0]
    p.text = "Our Strategic Approach"
    p.font.name = FONT_NAME
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    strat_items = [
        ("Zero Hardware Footprint", "Operates seamlessly on existing smartphones, web portals & low-cost IVRS telephony."),
        ("Real-Time <35ms Execution", "Lightweight DSP runs on basic CPUs with zero GPU hardware overhead."),
        ("Multilingual Indic Coverage", "Dedicated emotion lexicons across Hindi, Marathi, Tamil, Telugu, Bengali & English."),
        ("Court-Admissible XAI", "Decomposes risk scores into evidentiary SHAP factor cards for Section 61 BNSS."),
        ("Statutory Protection Hook", "Automated direct requisitions for Section 15A armed police pickets."),
        ("Rapid Alert Protocol", "Common Alerting Protocol (CAP JSON-LD) dispatches emergency alerts in <2 seconds.")
    ]

    cw = Inches(2.85)
    ch = Inches(1.55)
    for idx, (stitle, sdesc) in enumerate(strat_items):
        col = idx % 2
        row = idx // 2
        cx = Inches(6.85) + col * Inches(3.05)
        cy = Inches(1.80) + row * Inches(1.68)

        scard = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, cw, ch)
        scard.fill.solid()
        scard.fill.fore_color.rgb = RGBColor(241, 245, 249)
        scard.line.color.rgb = RGBColor(147, 197, 253)
        scard.line.width = Pt(1.2)

        tf_sc = scard.text_frame
        tf_sc.margin_left = tf_sc.margin_right = tf_sc.margin_top = Inches(0.12)
        tf_sc.word_wrap = True
        
        p = tf_sc.paragraphs[0]
        p.text = stitle
        p.font.name = FONT_NAME
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_HEADER_NAVY
        p.space_after = Pt(4)

        p2 = tf_sc.add_paragraph()
        p2.text = sdesc
        p2.font.name = FONT_NAME
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = C_SLATE_TEXT

    # =============================================================
    # SLIDE 5: Solution Benefits & Target Audience Impacts
    # =============================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_sih_header(s5, "", is_dual_banner=True)

    sb_flow = os.path.join(ASSETS_DIR, "s5_benefits_flow.png")
    if os.path.exists(sb_flow):
        s5.shapes.add_picture(sb_flow, Inches(0.45), Inches(1.05), width=Inches(6.0), height=Inches(3.85))

    sb_summary = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(5.05), Inches(6.0), Inches(1.85))
    sb_summary.fill.solid()
    sb_summary.fill.fore_color.rgb = C_WHITE
    sb_summary.line.color.rgb = C_CARD_BORDER
    sb_summary.line.width = Pt(1.5)
    tf_sbs = sb_summary.text_frame
    tf_sbs.margin_left = tf_sbs.margin_right = tf_sbs.margin_top = Inches(0.2)
    tf_sbs.word_wrap = True

    p = tf_sbs.paragraphs[0]
    p.space_after = Pt(8)
    r_arr = p.add_run()
    r_arr.text = "➔  "
    r_arr.font.bold = True
    r_arr.font.size = Pt(12)
    r_arr.font.color.rgb = C_HEADER_NAVY
    r_txt = p.add_run()
    r_txt.text = "Ensures continuous, proactive, and objective trauma monitoring using in-memory AI, replacing months of unmonitored post-complaint neglect."
    r_txt.font.name = FONT_NAME
    r_txt.font.size = Pt(11)
    r_txt.font.bold = True
    r_txt.font.color.rgb = C_SLATE_DARK

    p2 = tf_sbs.add_paragraph()
    r_arr2 = p2.add_run()
    r_arr2.text = "➔  "
    r_arr2.font.bold = True
    r_arr2.font.size = Pt(12)
    r_arr2.font.color.rgb = C_HEADER_NAVY
    r_txt2 = p2.add_run()
    r_txt2.text = "Predicts acute distress spikes 48-72h in advance and delivers legally-enforceable evidence to prevent witness retractions and suicides."
    r_txt2.font.name = FONT_NAME
    r_txt2.font.size = Pt(11)
    r_txt2.font.bold = True
    r_txt2.font.color.rgb = C_SLATE_DARK

    ta_flow = os.path.join(ASSETS_DIR, "s5_impacts_flow.png")
    if os.path.exists(ta_flow):
        s5.shapes.add_picture(ta_flow, Inches(6.65), Inches(1.05), width=Inches(6.25), height=Inches(3.85))

    ta_summary = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.65), Inches(5.05), Inches(6.25), Inches(1.85))
    ta_summary.fill.solid()
    ta_summary.fill.fore_color.rgb = C_WHITE
    ta_summary.line.color.rgb = C_CARD_BORDER
    ta_summary.line.width = Pt(1.5)
    tf_tas = ta_summary.text_frame
    tf_tas.margin_left = tf_tas.margin_right = tf_tas.margin_top = Inches(0.2)
    tf_tas.word_wrap = True

    p = tf_tas.paragraphs[0]
    p.space_after = Pt(8)
    r_arr = p.add_run()
    r_arr.text = "➔  "
    r_arr.font.bold = True
    r_arr.font.size = Pt(12)
    r_arr.font.color.rgb = C_HEADER_NAVY
    r_txt = p.add_run()
    r_txt.text = "Directly supports vulnerable atrocity victims with statutory police protection, emergency psychiatric visits, and fast-track relief DBT."
    r_txt.font.name = FONT_NAME
    r_txt.font.size = Pt(11)
    r_txt.font.bold = True
    r_txt.font.color.rgb = C_SLATE_DARK

    p2 = tf_tas.add_paragraph()
    r_arr2 = p2.add_run()
    r_arr2.text = "➔  "
    r_arr2.font.bold = True
    r_arr2.font.size = Pt(12)
    r_arr2.font.color.rgb = C_HEADER_NAVY
    r_txt2 = p2.add_run()
    r_txt2.text = "Drives systemic justice delivery aligned with UN SDGs: SDG 3 (Mental Health), SDG 5 (Gender Equality), SDG 10 (Inequalities), and SDG 16 (Peace & Justice)."
    r_txt2.font.name = FONT_NAME
    r_txt2.font.size = Pt(11)
    r_txt2.font.bold = True
    r_txt2.font.color.rgb = C_SLATE_DARK

    # =============================================================
    # SLIDE 6: TECHNICAL PIPELINE
    # =============================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_sih_header(s6, "TECHNICAL PIPELINE")

    scat_path = os.path.join(ASSETS_DIR, "s6_left_visuals.png")
    if not os.path.exists(scat_path):
        scat_path = os.path.join(ASSETS_DIR, "s6_scatter_clusters.png")
    if os.path.exists(scat_path):
        s6.shapes.add_picture(scat_path, Inches(0.45), Inches(1.05), width=Inches(5.4), height=Inches(5.85))

    pipe_steps = [
        ("Objectives", [
            "Continuous non-intrusive voice tracking",
            "Detection of perpetrator intimidation",
            "Real-time AI-based triage and scoring",
            "High-trust court-admissible evidence",
            "Scalable architecture for national scale"
        ], Inches(6.15), Inches(1.10)),
        ("Data Preparation", [
            "Obtain raw audio from Web, App, IVRS",
            "Perform in-memory PCM conversion (16kHz)",
            "Filter low-frequency background noise",
            "Extract voiced glottal frames (30ms)",
            "Sanitize input text across 6 Indic tongues"
        ], Inches(8.40), Inches(1.10)),
        ("Model Processing", [
            "Calculate F0, Jitter %, Shimmer % via DSP",
            "Evaluate 4-8Hz vocal cord tremor index",
            "Score intimidation & threat lexicons",
            "Fuse modalities via weighted DDS model",
            "Evaluate non-linear critical override triggers"
        ], Inches(10.65), Inches(1.10)),
        ("Analysis & Interpretation", [
            "Assign Risk Tiers (Stable to Critical)",
            "Track longitudinal velocity (Delta-DDS)",
            "Quantify distress escalation trajectory",
            "Generate SHAP evidentiary factor cards",
            "Validate compliance under Section 61 BNSS"
        ], Inches(10.65), Inches(4.15)),
        ("Dashboard & Insights", [
            "Interactive UI for District Magistrates / SP",
            "Display GIS heatmaps, triage list & alerts",
            "Counsellor longitudinal trajectory curves",
            "Provide one-click Section 15A requisitions",
            "Allow encrypted JSON/PDF export for court"
        ], Inches(8.40), Inches(4.15)),
        ("Deployment & Dispatch", [
            "CAP v1.2 JSON-LD push to Police CAD 112",
            "Automate Tele-MANAS (14416) crisis dispatch",
            "Alert SP & District Nodal Officer in <2s",
            "Secure ephemeral processing in RAM buffer",
            "Zero raw-audio storage (DPDP 2023 compliant)"
        ], Inches(6.15), Inches(4.15))
    ]

    pw = Inches(2.15)
    ph = Inches(2.80)
    for (stitle, sbullets, px, py) in pipe_steps:
        pcard = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, py, pw, ph)
        pcard.fill.solid()
        pcard.fill.fore_color.rgb = RGBColor(238, 242, 255)
        pcard.line.color.rgb = RGBColor(147, 197, 253)
        pcard.line.width = Pt(1.2)

        tf_p = pcard.text_frame
        tf_p.margin_left = tf_p.margin_right = tf_p.margin_top = Inches(0.12)
        tf_p.word_wrap = True

        p = tf_p.paragraphs[0]
        p.text = stitle
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_HEADER_NAVY
        p.space_after = Pt(4)

        for b in sbullets:
            p = tf_p.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_NAME
            p.font.size = Pt(8.5)
            p.font.color.rgb = C_SLATE_TEXT

    # Add 5 connecting flow arrows matching Storm Surge pipeline
    # 1. Objectives -> Data Prep (right)
    arr1 = s6.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(8.30), Inches(2.35), Inches(0.12), Inches(0.25))
    arr1.fill.solid()
    arr1.fill.fore_color.rgb = C_ARROW_BLUE
    arr1.line.fill.background()

    # 2. Data Prep -> Model Processing (right)
    arr2 = s6.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(10.55), Inches(2.35), Inches(0.12), Inches(0.25))
    arr2.fill.solid()
    arr2.fill.fore_color.rgb = C_ARROW_BLUE
    arr2.line.fill.background()

    # 3. Model Processing -> Analysis (down)
    arr3 = s6.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(11.60), Inches(3.90), Inches(0.25), Inches(0.22))
    arr3.fill.solid()
    arr3.fill.fore_color.rgb = C_ARROW_BLUE
    arr3.line.fill.background()

    # 4. Analysis -> Dashboard (left)
    arr4 = s6.shapes.add_shape(MSO_SHAPE.LEFT_ARROW, Inches(10.55), Inches(5.45), Inches(0.12), Inches(0.25))
    arr4.fill.solid()
    arr4.fill.fore_color.rgb = C_ARROW_BLUE
    arr4.line.fill.background()

    # 5. Dashboard -> Deployment (left)
    arr5 = s6.shapes.add_shape(MSO_SHAPE.LEFT_ARROW, Inches(8.30), Inches(5.45), Inches(0.12), Inches(0.25))
    arr5.fill.solid()
    arr5.fill.fore_color.rgb = C_ARROW_BLUE
    arr5.line.fill.background()

    # =============================================================
    # SLIDE 7: RESEARCH AND REFERENCES
    # =============================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_sih_header(s7, "RESEARCH AND REFERENCES")

    top_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(1.05), Inches(12.45), Inches(2.85))
    top_card.fill.solid()
    top_card.fill.fore_color.rgb = C_WHITE
    top_card.line.color.rgb = C_CARD_BORDER
    top_card.line.width = Pt(1.5)

    tf_tc = top_card.text_frame
    tf_tc.margin_left = tf_tc.margin_right = tf_tc.margin_top = Inches(0.25)
    tf_tc.word_wrap = True

    refs_data = [
        ("Acoustic Voice Stress & Emotion AI Datasets", [
            "RAVDESS & CREMA-D: Validated multi-actor databases (14,700+ clips) calibrating acoustic distress and vocal tremor thresholds.",
            "Reference: https://zenodo.org/record/1188976",
            "EMO-DB Database: Technical Univ. of Berlin benchmark for frequency perturbation (Jitter/Shimmer) under psychological duress.",
            "Reference: http://emodb.bilderbar.info/",
            "IndicNLP Library: Parallel corpora and lexical threat models across Hindi, Bengali, Tamil, Telugu, and English distress expressions.",
            "Reference: https://github.com/anoopkunchukuttan/indic_nlp_library"
        ]),
        ("Institutional Frameworks & Statutory Compliance", [
            "Polyvagal Theory & Russell Circumplex Model: Porges (2011) vocal cord tension & Russell (1980) 2D Valence-Arousal mapping.",
            "Reference: Journal of Personality & Social Psychology",
            "Explainable AI (SHAP): Lundberg & Lee (NeurIPS 2017) game-theoretic attribution for court-admissible evidence cards.",
            "Reference: https://arxiv.org/abs/1705.07874",
            "Statutory Standards: NHAA 14566 (MoSJE), SC/ST (PoA) Act Sec 15A, DPDP Act 2023, Bharatiya Nagarik Suraksha Sanhita (BNSS 2023 Sec 61).",
            "Reference: https://socialjustice.gov.in"
        ])
    ]

    p_idx = 0
    for header, blist in refs_data:
        p = tf_tc.add_paragraph() if p_idx > 0 else tf_tc.paragraphs[0]
        p_idx += 1
        p.alignment = PP_ALIGN.LEFT
        p.text = "■  " + header
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_HEADER_NAVY
        p.space_after = Pt(2)

        for b in blist:
            p = tf_tc.add_paragraph()
            p_idx += 1
            p.alignment = PP_ALIGN.LEFT
            if b.startswith("Reference:"):
                p.text = "     ■  " + b
                p.font.name = FONT_NAME
                p.font.size = Pt(8.5)
                p.font.color.rgb = RGBColor(2, 132, 199)
                p.font.underline = True
            else:
                p.text = "  • " + b
                p.font.name = FONT_NAME
                p.font.size = Pt(9.5)
                p.font.color.rgb = C_SLATE_TEXT
            p.space_after = Pt(2)

    sq_box = s7.shapes.add_textbox(Inches(0.65), Inches(3.92), Inches(3.5), Inches(0.35))
    tf_sq = sq_box.text_frame
    tf_sq.margin_left = tf_sq.margin_top = 0
    p_sq = tf_sq.paragraphs[0]
    p_sq.text = "Survey Questions"
    p_sq.font.name = FONT_NAME
    p_sq.font.size = Pt(14)
    p_sq.font.bold = True
    p_sq.font.color.rgb = C_SLATE_DARK

    surv_path = os.path.join(ASSETS_DIR, "s7_survey_charts.png")
    if os.path.exists(surv_path):
        s7.shapes.add_picture(surv_path, Inches(0.45), Inches(4.25), width=Inches(12.45), height=Inches(2.65))

    # =============================================================
    # SLIDE 8: UI SCREENS
    # =============================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_sih_header(s8, "UI SCREENS")

    web_b = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(1.05), Inches(7.3), Inches(0.48))
    web_b.fill.solid()
    web_b.fill.fore_color.rgb = C_TEAL_HEADER
    web_b.line.fill.background()
    p = web_b.text_frame.paragraphs[0]
    p.text = "Website"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    web_grid_path = os.path.join(ASSETS_DIR, "s8_website_grid.png")
    if os.path.exists(web_grid_path):
        s8.shapes.add_picture(web_grid_path, Inches(0.45), Inches(1.60), width=Inches(7.3), height=Inches(5.30))

    app_b = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.95), Inches(1.05), Inches(4.95), Inches(0.48))
    app_b.fill.solid()
    app_b.fill.fore_color.rgb = C_TEAL_HEADER
    app_b.line.fill.background()
    p = app_b.text_frame.paragraphs[0]
    p.text = "APP"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    mobile_grid_path = os.path.join(ASSETS_DIR, "s8_mobile_grid.png")
    if os.path.exists(mobile_grid_path):
        s8.shapes.add_picture(mobile_grid_path, Inches(7.95), Inches(1.60), width=Inches(4.95), height=Inches(5.30))

    # =============================================================
    # SLIDE 9: TECH STACK & TEAM
    # =============================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_sih_header(s9, "TECH STACK")

    # Top: Exact Serpentine Metro Ribbon Image
    ribbon_path = os.path.join(ASSETS_DIR, "s9_metro_ribbon_final.png")
    if os.path.exists(ribbon_path):
        s9.shapes.add_picture(ribbon_path, Inches(0.45), Inches(1.05), width=Inches(12.45), height=Inches(3.60))

    # Bottom: 6 Team Member Cards in a Row
    members = [
        ("[Team Leader]", "Team Leader", "B.Tech - CSE / IT", "3rd / 4th Year", "Domain: Lead Architect & Full Stack", C_HEADER_NAVY),
        ("[Team Member 2]", "Team Member", "B.Tech - AI / DS", "3rd / 4th Year", "Domain: Speech DSP & Acoustic Models", C_AMBER),
        ("[Team Member 3]", "Team Member", "B.Tech - CSE(AIML)", "3rd / 4th Year", "Domain: Indic NLP & Threat Modeling", C_BLUE_BORDER),
        ("[Team Member 4]", "Team Member", "B.Tech - IT / CSE", "3rd / 4th Year", "Domain: Backend & Statutory Triage API", RGBColor(16, 185, 129)),
        ("[Team Member 5]", "Team Member", "B.Tech - CSE / IT", "3rd / 4th Year", "Domain: Frontend & Interactive PWA", RGBColor(124, 58, 237)),
        ("[Team Member 6]", "Team Member", "B.Tech - CSE / IT", "3rd / 4th Year", "Domain: DevOps & Security Lead", RGBColor(220, 38, 38))
    ]

    card_w = Inches(1.95)
    card_h = Inches(2.15)
    start_x = Inches(0.45)
    gap_x = Inches(0.15)
    card_y = Inches(4.80)

    for idx, (m_name, m_role, m_deg, m_yr, m_dom, m_color) in enumerate(members):
        cx = start_x + idx * (card_w + gap_x)
        
        mc = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, card_h)
        mc.fill.solid()
        mc.fill.fore_color.rgb = C_WHITE
        mc.line.color.rgb = m_color
        mc.line.width = Pt(1.2)

        rpill = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.15), card_y + Inches(0.12), card_w - Inches(0.30), Inches(0.35))
        rpill.fill.solid()
        rpill.fill.fore_color.rgb = m_color
        rpill.line.fill.background()
        p = rpill.text_frame.paragraphs[0]
        p.text = m_role
        p.font.name = FONT_NAME
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

        tbox = s9.shapes.add_textbox(cx + Inches(0.08), card_y + Inches(0.55), card_w - Inches(0.16), card_h - Inches(0.60))
        tf_m = tbox.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_right = 0
        
        p_name = tf_m.paragraphs[0]
        p_name.text = m_name
        p_name.font.name = FONT_NAME
        p_name.font.size = Pt(10)
        p_name.font.bold = True
        p_name.font.color.rgb = C_SLATE_DARK
        p_name.alignment = PP_ALIGN.CENTER
        p_name.space_after = Pt(4)

        p_deg = tf_m.add_paragraph()
        p_deg.text = f"{m_deg}\n{m_yr}"
        p_deg.font.name = FONT_NAME
        p_deg.font.size = Pt(9)
        p_deg.font.color.rgb = C_MUTED_GRAY
        p_deg.alignment = PP_ALIGN.CENTER
        p_deg.space_after = Pt(4)

        p_dom = tf_m.add_paragraph()
        p_dom.text = m_dom
        p_dom.font.name = FONT_NAME
        p_dom.font.size = Pt(8.5)
        p_dom.font.bold = True
        p_dom.font.color.rgb = C_SLATE_TEXT
        p_dom.alignment = PP_ALIGN.CENTER

    pptx_path = r"d:\SAMVEDNA\SAMVEDNA_AI_SIH_Final_Presentation.pptx"
    prs.save(pptx_path)
    print(f"[+] PPTX saved successfully: {pptx_path}")
    return pptx_path

if __name__ == "__main__":
    build_presentation()
