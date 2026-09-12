import os
import math
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"d:\SAMVEDNA\extracted_assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

FONT_PATH_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_PATH_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_PATH_SEMIBOLD = r"C:\Windows\Fonts\seguisb.ttf"

def get_font(size, bold=False):
    path = FONT_PATH_BOLD if bold else FONT_PATH_REG
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

# -------------------------------------------------------------
# 1. Slide 2: Capability Wheel & Mini Pipeline
# -------------------------------------------------------------
def generate_s2_wheel():
    w, h = 1000, 1000
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = 500, 430
    radius = 310

    # Draw subtle circular track
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], outline=(186, 215, 245, 180), width=3)
    draw.ellipse([cx - radius + 40, cy - radius + 40, cx + radius - 40, cy + radius - 40], outline=(226, 232, 240, 140), width=2)

    # Center box: SAMVEDNA AI
    cw, ch = 250, 110
    draw.rounded_rectangle([cx - cw//2, cy - ch//2, cx + cw//2, cy + ch//2], radius=18, fill=(15, 23, 42, 255), outline=(37, 99, 235, 255), width=3)
    f_center = get_font(26, bold=True)
    f_center_sub = get_font(14, bold=False)
    
    draw.text((cx, cy - 14), "SAMVEDNA AI", fill=(255, 255, 255), font=f_center, anchor="mm")
    draw.text((cx, cy + 18), "DYNAMIC DISTRESS AI", fill=(147, 197, 253), font=f_center_sub, anchor="mm")

    # 8 Satellite Nodes
    nodes = [
        "Voice Stress\nDSP (<25ms)",
        "Real-Time\nAnalysis",
        "Cloud & Edge\nPlatform",
        "Dynamic\nDistress Score",
        "Crisis\nForecasting",
        "In-Memory\nComputing",
        "Privacy-First\n(DPDP 2023)",
        "Section 15A\nPolice Pickets"
    ]

    nw, nh = 160, 68
    f_node = get_font(16, bold=True)

    for i, label in enumerate(nodes):
        angle = i * (2 * math.pi / 8) - math.pi / 2
        nx = int(cx + radius * math.cos(angle))
        ny = int(cy + radius * math.sin(angle))

        # Radial connector line
        draw.line([(cx + int(120 * math.cos(angle)), cy + int(60 * math.sin(angle))), (nx, ny)], fill=(147, 197, 253, 160), width=2)

        # Node pill
        draw.rounded_rectangle([nx - nw//2, ny - nh//2, nx + nw//2, ny + nh//2], radius=14, fill=(59, 130, 246, 255), outline=(29, 78, 216, 255), width=2)
        
        # Text
        lines = label.split("\n")
        if len(lines) == 1:
            draw.text((nx, ny), lines[0], fill=(255, 255, 255), font=f_node, anchor="mm")
        else:
            draw.text((nx, ny - 10), lines[0], fill=(255, 255, 255), font=f_node, anchor="mm")
            draw.text((nx, ny + 12), lines[1], fill=(238, 242, 255), font=get_font(13, bold=False), anchor="mm")

    # Bottom Mini-Flow (7 Steps)
    flow_steps = ["Check-in", "Audio Buffer", "Voice DSP", "Emotion NLP", "DDS Fusion", "Triage Queue", "Relief Action"]
    step_w = 110
    gap = 22
    start_x = 35
    fy = 870
    f_step = get_font(13, bold=True)

    for idx, st in enumerate(flow_steps):
        sx = start_x + idx * (step_w + gap)
        draw.rounded_rectangle([sx, fy, sx + step_w, fy + 48], radius=8, fill=(241, 245, 249, 255), outline=(148, 163, 184, 255), width=1)
        draw.text((sx + step_w//2, fy + 24), st, fill=(15, 23, 42), font=f_step, anchor="mm")
        if idx < len(flow_steps) - 1:
            # Arrow
            ax = sx + step_w + 3
            draw.line([(ax, fy + 24), (ax + 14, fy + 24)], fill=(37, 99, 235), width=2)
            draw.polygon([(ax + 14, fy + 20), (ax + 20, fy + 24), (ax + 14, fy + 28)], fill=(37, 99, 235))

    out_path = os.path.join(ASSETS_DIR, "s2_capability_wheel.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 2 wheel: {out_path}")

# -------------------------------------------------------------
# 2. Slide 3: Technical Approach Flowchart & Funnel
# -------------------------------------------------------------
def generate_s3_flowchart():
    w, h = 550, 950
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    steps = [
        ("Multi-Channel Check-in Ingestion", "Web, Mobile App, IVRS 14566, WhatsApp, SOS", (239, 246, 255), (37, 99, 235)),
        ("In-Memory Signal Capture (<30ms)", "16kHz PCM audio & raw UTF-8 text buffer", (240, 253, 250), (13, 148, 136)),
        ("Dual In-Memory Processing Core", "Acoustic Voice Stress DSP + Multilingual NLP", (245, 243, 255), (124, 58, 237)),
        ("Dynamic Distress Scoring (DDS)", "Multi-modal weighted fusion (0-100 index)", (255, 251, 235), (217, 119, 6)),
        ("Longitudinal Time-Series Velocity", "Delta-DDS / Delta-t 48-72h crisis escalation", (254, 242, 242), (220, 38, 38)),
        ("Explainable AI (XAI) Attribution", "Court-admissible SHAP evidence cards", (248, 250, 252), (71, 85, 105)),
        ("Statutory Triage & Real-World Relief", "Sec 15A police pickets, Tele-MANAS, DBT", (236, 253, 245), (16, 185, 129))
    ]

    bx = 35
    bw = 480
    bh = 85
    f_title = get_font(18, bold=True)
    f_sub = get_font(14, bold=False)

    for idx, (title, sub, bg, border) in enumerate(steps):
        by = 25 + idx * 130
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=12, fill=bg, outline=border, width=2)
        draw.text((bx + 20, by + 22), title, fill=(15, 23, 42), font=f_title)
        draw.text((bx + 20, by + 50), sub, fill=(71, 85, 105), font=f_sub)

        if idx < len(steps) - 1:
            ay = by + bh
            draw.line([(bx + bw//2, ay), (bx + bw//2, ay + 42)], fill=(37, 99, 235), width=3)
            draw.polygon([(bx + bw//2 - 6, ay + 38), (bx + bw//2 + 6, ay + 38), (bx + bw//2, ay + 45)], fill=(37, 99, 235))

    out_path = os.path.join(ASSETS_DIR, "s3_flowchart.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 3 flowchart: {out_path}")

def generate_s3_funnel():
    w, h = 520, 1020
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    tiers = [
        ("CRITICAL CRISIS", "DDS 81 - 100", "Armed Police Picket (Sec 15A) + Tele-MANAS", (220, 38, 38)),
        ("HIGH RISK", "DDS 61 - 80", "DLSA Legal Aid + Urgent Psychiatric Visit", (234, 88, 12)),
        ("MODERATE WATCH", "DDS 36 - 60", "Supportive Tele-Counselling + Relief Tracking", (217, 119, 6)),
        ("MILD / STABLE", "DDS 0 - 35", "Routine Bi-Weekly Empathetic Follow-ups", (16, 185, 129)),
        ("PRIVACY SANDBOX", "IN-MEMORY RAM", "Zero Raw Audio Stored (DPDP 2023 Compliant)", (37, 99, 235))
    ]

    f_tier = get_font(18, bold=True)
    f_range = get_font(14, bold=True)
    f_desc = get_font(12, bold=False)

    total_tiers = len(tiers)
    for idx, (name, rng, desc, color) in enumerate(tiers):
        inset = idx * 26
        bx1 = 30 + inset
        bx2 = w - 30 - inset
        by = 25 + idx * 195
        bh = 145

        draw.rounded_rectangle([bx1, by, bx2, by + bh], radius=16, fill=color, outline=(255, 255, 255), width=2)
        cx = (bx1 + bx2) // 2
        draw.text((cx, by + 32), name, fill=(255, 255, 255), font=f_tier, anchor="mm")
        draw.text((cx, by + 68), rng, fill=(254, 240, 138), font=f_range, anchor="mm")
        draw.text((cx, by + 106), desc, fill=(255, 255, 255), font=f_desc, anchor="mm")

        if idx < total_tiers - 1:
            ay = by + bh
            draw.line([(cx, ay), (cx, ay + 48)], fill=color, width=3)
            draw.polygon([(cx - 5, ay + 44), (cx + 5, ay + 44), (cx, ay + 50)], fill=color)

    out_path = os.path.join(ASSETS_DIR, "s3_distress_funnel.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 3 funnel: {out_path}")

# -------------------------------------------------------------
# 3. Slide 4: Feasibility Tree & Challenges Flow
# -------------------------------------------------------------
def generate_s4_feasibility_tree():
    w, h = 800, 360
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    f_head = get_font(20, bold=True)
    f_sub = get_font(15, bold=True)
    f_body = get_font(13, bold=False)

    # Root
    rx, ry, rw, rh = 300, 15, 200, 48
    draw.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=10, fill=(15, 23, 42), outline=(37, 99, 235), width=2)
    draw.text((rx + rw//2, ry + rh//2), "Feasibility", fill=(255, 255, 255), font=f_head, anchor="mm")

    # Branches: Left (Technical), Right (Economic)
    lx, ly, lw, lh = 20, 110, 360, 60
    rx2, ry2, rw2, rh2 = 420, 110, 360, 60

    # Connector lines
    draw.line([(400, ry + rh), (400, 85)], fill=(100, 116, 139), width=2)
    draw.line([(200, 85), (600, 85)], fill=(100, 116, 139), width=2)
    draw.line([(200, 85), (200, ly)], fill=(100, 116, 139), width=2)
    draw.line([(600, 85), (600, ry2)], fill=(100, 116, 139), width=2)

    draw.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=8, fill=(239, 246, 255), outline=(37, 99, 235), width=2)
    draw.text((lx + lw//2, ly + lh//2), "Technical Feasibility", fill=(15, 23, 42), font=f_sub, anchor="mm")

    draw.rounded_rectangle([rx2, ry2, rx2 + rw2, ry2 + rh2], radius=8, fill=(236, 253, 245), outline=(16, 185, 129), width=2)
    draw.text((rx2 + rw2//2, ry2 + rh2//2), "Economic Feasibility", fill=(15, 23, 42), font=f_sub, anchor="mm")

    # Leaves under Technical
    tech_items = [
        "Lightweight DSP: Runs <35ms on basic CPU",
        "Zero GPU dependency: Highly cost effective",
        "Low bandwidth 16kHz mono audio stream"
    ]
    for i, it in enumerate(tech_items):
        tx = lx + 10
        ty = ly + lh + 18 + i * 45
        draw.rounded_rectangle([tx, ty, tx + lw - 20, ty + 36], radius=6, fill=(248, 250, 252), outline=(203, 213, 225), width=1)
        draw.text((tx + 12, ty + 18), "• " + it, fill=(51, 65, 85), font=f_body, anchor="lm")

    # Leaves under Economic
    econ_items = [
        "Zero hardware cost: Web, Mobile & IVRS",
        "National scale: NHAA 14566 integration",
        "Cost reduction: Automated triage vs manual"
    ]
    for i, it in enumerate(econ_items):
        tx = rx2 + 10
        ty = ry2 + rh2 + 18 + i * 45
        draw.rounded_rectangle([tx, ty, tx + rw2 - 20, ty + 36], radius=6, fill=(248, 250, 252), outline=(203, 213, 225), width=1)
        draw.text((tx + 12, ty + 18), "• " + it, fill=(51, 65, 85), font=f_body, anchor="lm")

    out_path = os.path.join(ASSETS_DIR, "s4_feasibility_tree.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 4 tree: {out_path}")

def generate_s4_challenges_flow():
    w, h = 850, 420
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    f_c = get_font(15, bold=True)
    f_m = get_font(14, bold=False)

    pairs = [
        ("Ambient Rural Noise\n(Livestock, traffic, distortion)", "Glottal Harmonic Filtering (HNR separates voice;\nambient noise impact capped at <=8% of score)", (239, 68, 68), (16, 185, 129)),
        ("Victim Fear & Retaliation\n(Hesitation to speak openly)", "DPDP Act 2023 In-Memory Sandboxing\n(Zero audio saved; ephemeral RAM wipe in <25ms)", (249, 115, 22), (37, 99, 235)),
        ("Dialect & Linguistic Diversity\n(Slang, code-switching, Hinglish)", "Multilingual Indic Lexicons & Transliteration\n(6 regional languages with colloquial threat models)", (234, 179, 8), (124, 58, 237)),
        ("False Alarm Fatigue\n(Emotional venting vs. acute threat)", "Russell 2D Circumplex Model (Arousal-Valence)\n(Disambiguates cathartic crying from true danger)", (168, 85, 247), (13, 148, 136))
    ]

    cw = 310
    mw = 420
    ch = 72

    for idx, (c_text, m_text, c_col, m_col) in enumerate(pairs):
        cy = 15 + idx * 98
        draw.rounded_rectangle([20, cy, 20 + cw, cy + ch], radius=8, fill=(254, 242, 242), outline=c_col, width=2)
        lines = c_text.split("\n")
        draw.text((32, cy + 18), lines[0], fill=(185, 28, 28), font=f_c)
        draw.text((32, cy + 42), lines[1], fill=(100, 116, 139), font=get_font(12, bold=False))

        ax1 = 20 + cw + 5
        ax2 = ax1 + 65
        for dot_x in range(ax1, ax2, 8):
            draw.line([(dot_x, cy + ch//2), (dot_x + 4, cy + ch//2)], fill=(100, 116, 139), width=2)
        draw.polygon([(ax2, cy + ch//2 - 5), (ax2 + 8, cy + ch//2), (ax2, cy + ch//2 + 5)], fill=(100, 116, 139))

        mx = ax2 + 15
        draw.rounded_rectangle([mx, cy, mx + mw, cy + ch], radius=8, fill=(240, 253, 250), outline=m_col, width=2)
        mlines = m_text.split("\n")
        draw.text((mx + 16, cy + 18), mlines[0], fill=(15, 23, 42), font=get_font(14, bold=True))
        draw.text((mx + 16, cy + 42), mlines[1], fill=(71, 85, 105), font=f_m)

    out_path = os.path.join(ASSETS_DIR, "s4_challenges_flow.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 4 challenges: {out_path}")

# -------------------------------------------------------------
# 4. Slide 5: Solution Benefits & Target Audience Impacts
# -------------------------------------------------------------
def generate_s5_benefits_flow():
    w, h = 880, 520
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    f_bold = get_font(16, bold=True)
    f_sub = get_font(13, bold=False)

    draw.rounded_rectangle([20, 200, 220, 310], radius=12, fill=(15, 23, 42), outline=(37, 99, 235), width=2)
    draw.text((120, 235), "SAMVEDNA AI", fill=(255, 255, 255), font=f_bold, anchor="mm")
    draw.text((120, 268), "Dual-Engine Pipeline", fill=(147, 197, 253), font=f_sub, anchor="mm")

    benefits = [
        "Continuous Care (24/7)",
        "Pre-Crisis Warning (48-72h)",
        "Objective Vocal Biomarkers",
        "Court-Admissible XAI Cards"
    ]
    bw, bh = 270, 58
    mid_x = 290
    for idx, b in enumerate(benefits):
        by = 50 + idx * 110
        draw.rounded_rectangle([mid_x, by, mid_x + bw, by + bh], radius=8, fill=(239, 246, 255), outline=(37, 99, 235), width=1)
        draw.text((mid_x + bw//2, by + bh//2), b, fill=(15, 23, 42), font=f_bold, anchor="mm")

        draw.line([(220, 255), (mid_x, by + bh//2)], fill=(147, 197, 253), width=2)
        draw.line([(mid_x + bw, by + bh//2), (630, 255)], fill=(147, 197, 253), width=2)

    draw.rounded_rectangle([630, 185, 860, 325], radius=12, fill=(236, 253, 245), outline=(16, 185, 129), width=3)
    draw.text((745, 225), "Key Strategic Benefit:", fill=(5, 150, 105), font=get_font(15, bold=True), anchor="mm")
    draw.text((745, 258), "Proactive, Legally-Enforceable", fill=(15, 23, 42), font=get_font(15, bold=True), anchor="mm")
    draw.text((745, 288), "Victim Safety & Protection", fill=(15, 23, 42), font=get_font(15, bold=True), anchor="mm")

    out_path = os.path.join(ASSETS_DIR, "s5_benefits_flow.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 5 benefits: {out_path}")

def generate_s5_impacts_flow():
    w, h = 880, 520
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    f_bold = get_font(15, bold=True)
    f_sub = get_font(13, bold=False)

    draw.rounded_rectangle([20, 200, 220, 310], radius=12, fill=(15, 23, 42), outline=(16, 185, 129), width=2)
    draw.text((120, 235), "SAMVEDNA AI", fill=(255, 255, 255), font=f_bold, anchor="mm")
    draw.text((120, 268), "Victim Protection Core", fill=(167, 243, 208), font=f_sub, anchor="mm")

    groups = [
        "Rape & Atrocity Survivors",
        "Threatened Witnesses & Kin",
        "SC/ST Complainants",
        "District Magistrate / SP Nodal",
        "Special Courts & Prosecutors"
    ]
    gw, gh = 260, 50
    mid_x = 290
    for idx, g in enumerate(groups):
        gy = 40 + idx * 88
        draw.rounded_rectangle([mid_x, gy, mid_x + gw, gy + gh], radius=8, fill=(240, 253, 250), outline=(20, 184, 166), width=1)
        draw.text((mid_x + gw//2, gy + gh//2), g, fill=(15, 23, 42), font=f_bold, anchor="mm")

        draw.line([(220, 255), (mid_x, gy + gh//2)], fill=(153, 246, 228), width=2)
        draw.line([(mid_x + gw, gy + gh//2), (630, 255)], fill=(153, 246, 228), width=2)

    draw.rounded_rectangle([630, 160, 860, 350], radius=12, fill=(238, 242, 255), outline=(99, 102, 241), width=2)
    draw.text((745, 195), "Direct Impact Outcomes:", fill=(67, 56, 202), font=get_font(15, bold=True), anchor="mm")
    draw.text((745, 230), "• Trauma Reduction & Suicide Prev.", fill=(15, 23, 42), font=f_sub, anchor="mm")
    draw.text((745, 260), "• Prevention of Hostile Retractions", fill=(15, 23, 42), font=f_sub, anchor="mm")
    draw.text((745, 290), "• Section 15A Armed Police Pickets", fill=(15, 23, 42), font=f_sub, anchor="mm")
    draw.text((745, 320), "• Evidentiary Due Process (BNSS)", fill=(15, 23, 42), font=f_sub, anchor="mm")

    out_path = os.path.join(ASSETS_DIR, "s5_impacts_flow.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 5 impacts: {out_path}")

# -------------------------------------------------------------
# 5. Slide 6: 2D/3D Scatter Risk Clusters
# -------------------------------------------------------------
def generate_s6_scatter_clusters():
    w, h = 800, 800
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    f_axis = get_font(14, bold=True)

    origin_x, origin_y = 120, 680
    x_axis_len = 580
    y_axis_len = 540
    z_dx, z_dy = 100, -80

    draw.polygon([
        (origin_x, origin_y),
        (origin_x + x_axis_len, origin_y),
        (origin_x + x_axis_len + z_dx, origin_y + z_dy),
        (origin_x + z_dx, origin_y + z_dy)
    ], fill=(248, 250, 252, 220), outline=(203, 213, 225, 200), width=2)

    draw.polygon([
        (origin_x, origin_y),
        (origin_x + z_dx, origin_y + z_dy),
        (origin_x + z_dx, origin_y + z_dy - y_axis_len),
        (origin_x, origin_y - y_axis_len)
    ], fill=(241, 245, 249, 220), outline=(203, 213, 225, 200), width=2)

    for step in range(1, 6):
        gx = origin_x + step * (x_axis_len // 6)
        draw.line([(gx, origin_y), (gx + z_dx, origin_y + z_dy)], fill=(226, 232, 240), width=1)
        gy = origin_y - step * (y_axis_len // 6)
        draw.line([(origin_x, gy), (origin_x + z_dx, gy + z_dy)], fill=(226, 232, 240), width=1)

    draw.line([(origin_x, origin_y), (origin_x + x_axis_len, origin_y)], fill=(15, 23, 42), width=3)
    draw.line([(origin_x, origin_y), (origin_x, origin_y - y_axis_len)], fill=(15, 23, 42), width=3)
    draw.line([(origin_x, origin_y), (origin_x + z_dx, origin_y + z_dy)], fill=(15, 23, 42), width=3)

    draw.text((origin_x + x_axis_len // 2, origin_y + 35), "Acoustic Speech Perturbation (Jitter % / Tremor)", fill=(15, 23, 42), font=f_axis, anchor="mm")
    draw.text((origin_x - 30, origin_y - y_axis_len // 2), "Linguistic Threat\nValence Score", fill=(15, 23, 42), font=f_axis, anchor="mm")

    import random
    random.seed(42)

    for _ in range(85):
        px = int(random.gauss(230, 45))
        py = int(random.gauss(580, 40))
        r = random.randint(5, 8)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(16, 185, 129, 220), outline=(5, 150, 105))

    for _ in range(75):
        px = int(random.gauss(380, 50))
        py = int(random.gauss(450, 45))
        r = random.randint(5, 8)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(245, 158, 11, 220), outline=(217, 119, 6))

    for _ in range(60):
        px = int(random.gauss(490, 45))
        py = int(random.gauss(330, 40))
        r = random.randint(5, 8)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(249, 115, 22, 220), outline=(194, 65, 12))

    for _ in range(45):
        px = int(random.gauss(600, 40))
        py = int(random.gauss(210, 35))
        r = random.randint(6, 9)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(220, 38, 38, 230), outline=(153, 27, 27))

    lx = 140
    ly = 45
    legends = [
        ("Stable (DDS 0-35)", (16, 185, 129)),
        ("Moderate (DDS 36-60)", (245, 158, 11)),
        ("High Risk (DDS 61-80)", (249, 115, 22)),
        ("Critical (DDS 81-100)", (220, 38, 38))
    ]
    for idx, (lbl, col) in enumerate(legends):
        bx = lx + idx * 155
        draw.ellipse([bx, ly, bx + 14, ly + 14], fill=col, outline=(15, 23, 42), width=1)
        draw.text((bx + 22, ly + 7), lbl, fill=(15, 23, 42), font=get_font(12, bold=True), anchor="lm")

    out_path = os.path.join(ASSETS_DIR, "s6_scatter_clusters.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 6 scatter clusters: {out_path}")

# -------------------------------------------------------------
# 6. Slide 7: Survey Donut / Pie Charts
# -------------------------------------------------------------
def generate_s7_survey_charts():
    w, h = 900, 380
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    f_q = get_font(15, bold=True)
    f_pct = get_font(24, bold=True)
    f_leg = get_font(13, bold=False)

    cx1, cy1, r1 = 200, 200, 100
    angle1_yes = int(88.4 * 3.6)
    draw.pieslice([cx1 - r1, cy1 - r1, cx1 + r1, cy1 + r1], start=-90, end=-90 + angle1_yes, fill=(30, 58, 138))
    draw.pieslice([cx1 - r1, cy1 - r1, cx1 + r1, cy1 + r1], start=-90 + angle1_yes, end=270, fill=(147, 197, 253))
    ir = 50
    draw.ellipse([cx1 - ir, cy1 - ir, cx1 + ir, cy1 + ir], fill=(255, 255, 255))
    draw.text((cx1, cy1), "88.4%", fill=(30, 58, 138), font=f_pct, anchor="mm")

    draw.text((20, 35), "Do you think unmonitored witness intimidation", fill=(15, 23, 42), font=f_q)
    draw.text((20, 60), "leads to hostile retractions in atrocity trials?", fill=(15, 23, 42), font=f_q)

    draw.rectangle([320, 160, 336, 176], fill=(30, 58, 138))
    draw.text((345, 168), "Yes (88.4%)", fill=(15, 23, 42), font=f_leg, anchor="lm")
    draw.rectangle([320, 195, 336, 211], fill=(147, 197, 253))
    draw.text((345, 203), "No (11.6%)", fill=(15, 23, 42), font=f_leg, anchor="lm")

    cx2, cy2 = 640, 200
    angle2_yes = int(91.2 * 3.6)
    draw.pieslice([cx2 - r1, cy2 - r1, cx2 + r1, cy2 + r1], start=-90, end=-90 + angle2_yes, fill=(15, 118, 110))
    draw.pieslice([cx2 - r1, cy2 - r1, cx2 + r1, cy2 + r1], start=-90 + angle2_yes, end=270, fill=(153, 246, 228))
    draw.ellipse([cx2 - ir, cy2 - ir, cx2 + ir, cy2 + ir], fill=(255, 255, 255))
    draw.text((cx2, cy2), "91.2%", fill=(15, 118, 110), font=f_pct, anchor="mm")

    draw.text((470, 35), "Would continuous voice AI check-ins increase", fill=(15, 23, 42), font=f_q)
    draw.text((470, 60), "victim willingness to testify safely in court?", fill=(15, 23, 42), font=f_q)

    draw.rectangle([760, 160, 776, 176], fill=(15, 118, 110))
    draw.text((785, 168), "Yes (91.2%)", fill=(15, 23, 42), font=f_leg, anchor="lm")
    draw.rectangle([760, 195, 776, 211], fill=(153, 246, 228))
    draw.text((785, 203), "No (8.8%)", fill=(15, 23, 42), font=f_leg, anchor="lm")

    out_path = os.path.join(ASSETS_DIR, "s7_survey_charts.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 7 survey charts: {out_path}")

# -------------------------------------------------------------
# 7. Slide 9: Tech Stack Serpentine Track
# -------------------------------------------------------------
def generate_s9_metro_ribbon():
    w, h = 1000, 380
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    f_node = get_font(16, bold=True)
    f_tech = get_font(13, bold=False)

    track_color = (30, 58, 138, 255)
    tw = 22

    # Draw serpentine curve connecting the 4 hubs smoothly
    draw.arc([80, 50, 320, 290], start=90, end=270, fill=track_color, width=tw)
    draw.line([(200, 50), (450, 50)], fill=track_color, width=tw)
    draw.arc([330, 50, 570, 290], start=270, end=90, fill=track_color, width=tw)
    draw.line([(450, 290), (700, 290)], fill=track_color, width=tw)
    draw.arc([580, 50, 820, 290], start=90, end=270, fill=track_color, width=tw)
    draw.line([(700, 50), (920, 50)], fill=track_color, width=tw)

    hubs = [
        (150, 170, "Backend\nCore", ["fastAPI", "Python 3.11", "Uvicorn ASGI", "PostgreSQL", "CAP JSON-LD"], (241, 245, 249), (30, 58, 138)),
        (400, 170, "AI / ML\nEngine", ["NumPy/SciPy DSP", "Tremor Detector", "IndicNLP Lexicons", "Russell 2D Affect", "Gemini 2.5 Flash"], (254, 242, 242), (220, 38, 38)),
        (650, 170, "Frontend\n& Viz", ["Web Audio FFT", "Chart.js Curves", "Tailwind CSS", "FontAwesome 6", "Leaflet GIS Map"], (254, 252, 232), (217, 119, 6)),
        (870, 170, "DevOps &\nSecurity", ["In-Memory RAM", "DPDP 2023 Compliant", "Docker Container", "AES-256 GCM", "Cloud PaaS"], (236, 253, 245), (16, 185, 129))
    ]

    for (hx, hy, name, items, bg, border) in hubs:
        hr = 52
        draw.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=bg, outline=border, width=4)
        draw.text((hx, hy), name, fill=(15, 23, 42), font=f_node, anchor="mm", align="center")

        for idx, it in enumerate(items):
            iy = hy + 70 + idx * 24
            draw.text((hx, iy), "• " + it, fill=(51, 65, 85), font=f_tech, anchor="mm")

    out_path = os.path.join(ASSETS_DIR, "s9_metro_ribbon.png")
    img.save(out_path, "PNG")
    print(f"[+] Saved Slide 9 metro ribbon: {out_path}")

if __name__ == "__main__":
    generate_s2_wheel()
    generate_s3_flowchart()
    generate_s3_funnel()
    generate_s4_feasibility_tree()
    generate_s4_challenges_flow()
    generate_s5_benefits_flow()
    generate_s5_impacts_flow()
    generate_s6_scatter_clusters()
    generate_s7_survey_charts()
    generate_s9_metro_ribbon()
    print("\nALL PRESENTATION ASSETS GENERATED SUCCESSFULLY!")
