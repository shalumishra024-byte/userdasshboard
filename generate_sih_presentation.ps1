$ErrorActionPreference = "Stop"

Write-Host "[*] Launching PowerPoint COM Application..."
$ppt = New-Object -ComObject PowerPoint.Application

$pres = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoTrue)
$pres.PageSetup.SlideWidth = 960
$pres.PageSetup.SlideHeight = 540

# Colors (BGR hex integer calculation: R + G*256 + B*65536)
$cNavy     = 15 + 23*256 + 42*65536      # #0F172A (Slate 900)
$cCardNavy = 30 + 41*256 + 59*65536      # #1E293B (Slate 800)
$cAmber    = 245 + 158*256 + 11*65536    # #F59E0B (Amber 500)
$cDeepAmber= 180 + 83*256 + 9*65536      # #B45309 (Amber 700)
$cWhite    = 255 + 255*256 + 255*65536   # #FFFFFF
$cSlateDark= 30 + 41*256 + 59*65536      # #1E293B
$cSlateText= 51 + 65*256 + 85*65536      # #334155
$cMutedGray= 100 + 116*256 + 139*65536   # #64748B
$cLightBg  = 248 + 250*256 + 252*65536   # #F8FAFC
$cBorder   = 226 + 232*256 + 240*65536   # #E2E8F0
$cGreen    = 16 + 185*256 + 129*65536    # #10B981
$cRed      = 220 + 38*256 + 38*65536     # #DC2626
$cBlue     = 2 + 132*256 + 199*65536     # #0284C7

function Set-Header($slide, $category, $title) {
    # Top banner bar
    $topBar = $slide.Shapes.AddShape(1, 0, 0, 960, 68)
    $topBar.Fill.Solid()
    $topBar.Fill.ForeColor.RGB = $cNavy
    $topBar.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    # Category and PS tag
    $tBox = $slide.Shapes.AddTextbox(1, 35, 8, 700, 20)
    $tBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr = $tBox.TextFrame.TextRange
    $tr.Text = "SMART INDIA HACKATHON 2025 | PROBLEM STATEMENT ID: 94 | NHAA 14566"
    $tr.Font.Name = "Segoe UI"
    $tr.Font.Size = 10
    $tr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr.Font.Color.RGB = $cAmber

    # Title
    $titleBox = $slide.Shapes.AddTextbox(1, 35, 27, 750, 36)
    $titleBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titler = $titleBox.TextFrame.TextRange
    $titler.Text = $title
    $titler.Font.Name = "Segoe UI"
    $titler.Font.Size = 17
    $titler.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titler.Font.Color.RGB = $cWhite

    # Right branding badge
    $badge = $slide.Shapes.AddTextbox(1, 780, 14, 150, 40)
    $br = $badge.TextFrame.TextRange
    $br.Text = "SAMVEDNA AI`nTeam Portal"
    $br.Font.Name = "Segoe UI"
    $br.Font.Size = 9
    $br.Font.Color.RGB = $cMutedGray
    $br.ParagraphFormat.Alignment = 3 # right

    # Bottom footer line
    $botBar = $slide.Shapes.AddShape(1, 0, 520, 960, 20)
    $botBar.Fill.Solid()
    $botBar.Fill.ForeColor.RGB = $cNavy
    $botBar.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    $fBox = $slide.Shapes.AddTextbox(1, 35, 521, 890, 18)
    $fr = $fBox.TextFrame.TextRange
    $fr.Text = "SIH 2025 Idea Submission Template | PS ID: 94 | Dynamic Distress Prediction System"
    $fr.Font.Name = "Segoe UI"
    $fr.Font.Size = 8
    $fr.Font.Color.RGB = $cMutedGray
}

function Create-Card($slide, $x, $y, $w, $h, $title, $items, $accentColor) {
    $card = $slide.Shapes.AddShape(5, $x, $y, $w, $h) # 5 = msoShapeRoundedRectangle
    $card.Fill.Solid()
    $card.Fill.ForeColor.RGB = $cLightBg
    $card.Line.ForeColor.RGB = $accentColor
    $card.Line.Weight = 1.5

    $tBox = $slide.Shapes.AddTextbox(1, ($x + 10), ($y + 8), ($w - 20), 26)
    $tr = $tBox.TextFrame.TextRange
    $tr.Text = $title
    $tr.Font.Name = "Segoe UI"
    $tr.Font.Size = 11.5
    $tr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr.Font.Color.RGB = $accentColor

    $bBox = $slide.Shapes.AddTextbox(1, ($x + 10), ($y + 34), ($w - 20), ($h - 40))
    $bBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $br = $bBox.TextFrame.TextRange
    $br.Font.Name = "Segoe UI"
    $br.Font.Size = 9.2
    $br.Font.Color.RGB = $cSlateText
    
    $fullText = ""
    foreach ($item in $items) {
        $fullText += "$item`n"
    }
    $br.Text = $fullText.TrimEnd()
}

# ==========================================
# SLIDE 1: TITLE PAGE
# ==========================================
Write-Host "[*] Building Slide 1 (Title Page)..."
$slide1 = $pres.Slides.Add(1, 12)

$bg1 = $slide1.Shapes.AddShape(1, 0, 0, 960, 540)
$bg1.Fill.Solid()
$bg1.Fill.ForeColor.RGB = $cNavy
$bg1.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

$tBox1 = $slide1.Shapes.AddTextbox(1, 50, 28, 860, 36)
$tr1 = $tBox1.TextFrame.TextRange
$tr1.Text = "SMART INDIA HACKATHON 2025"
$tr1.Font.Name = "Segoe UI"
$tr1.Font.Size = 22
$tr1.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr1.Font.Color.RGB = $cAmber
$tr1.ParagraphFormat.Alignment = 2 # Center

$stBox1 = $slide1.Shapes.AddTextbox(1, 50, 64, 860, 24)
$str1 = $stBox1.TextFrame.TextRange
$str1.Text = "TITLE PAGE -- OFFICIAL IDEA SUBMISSION"
$str1.Font.Name = "Segoe UI"
$str1.Font.Size = 12
$str1.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$str1.Font.Color.RGB = $cWhite
$str1.ParagraphFormat.Alignment = 2

# Main Project Banner Card
$mainCard = $slide1.Shapes.AddShape(5, 50, 98, 860, 98)
$mainCard.Fill.Solid()
$mainCard.Fill.ForeColor.RGB = $cCardNavy
$mainCard.Line.ForeColor.RGB = $cAmber
$mainCard.Line.Weight = 2

$pTitleBox = $slide1.Shapes.AddTextbox(1, 60, 106, 840, 44)
$ptr = $pTitleBox.TextFrame.TextRange
$ptr.Text = "SAMVEDNA AI"
$ptr.Font.Name = "Segoe UI"
$ptr.Font.Size = 28
$ptr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$ptr.Font.Color.RGB = $cAmber
$ptr.ParagraphFormat.Alignment = 2

$pSubBox = $slide1.Shapes.AddTextbox(1, 60, 150, 840, 38)
$psr = $pSubBox.TextFrame.TextRange
$psr.Text = "AI-Powered Dynamic Mental Health Monitoring and Distress Prediction System (NHAA 14566)"
$psr.Font.Name = "Segoe UI"
$psr.Font.Size = 12
$psr.Font.Color.RGB = $cWhite
$psr.ParagraphFormat.Alignment = 2

# Details White Card
$wCard1 = $slide1.Shapes.AddShape(5, 50, 208, 860, 275)
$wCard1.Fill.Solid()
$wCard1.Fill.ForeColor.RGB = $cWhite
$wCard1.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

$dtBox = $slide1.Shapes.AddTextbox(1, 75, 220, 810, 250)
$dtr = $dtBox.TextFrame.TextRange
$dtr.Font.Name = "Segoe UI"
$dtr.Font.Size = 11.5
$dtr.Font.Color.RGB = $cSlateDark

$detailsText = @"
• Problem Statement ID -- 94
• Problem Statement Title -- AI-based Dynamic Mental Health Monitoring and Distress Prediction System
• Target Ecosystem -- National Helpline Against Atrocities (NHAA 14566), Integrated Portal & SC/ST (PoA) Act 1989
• Theme -- Smart Automation / Security & Surveillance (Women & Vulnerable Section Safety)
• PS Category -- Software
• Team ID -- [Enter Your Team ID]
• Team Name (Registered on portal) -- [Enter Your Registered Team Name]
• Core Capabilities -- Voice Stress Analytics, Multilingual Emotion AI, Dynamic Distress Scoring & Authority CAD Alerts
• Target Beneficiaries -- Atrocity complainants, rape/gang rape survivors, threatened witnesses & SC/ST families
"@
$dtr.Text = $detailsText

$f1 = $slide1.Shapes.AddTextbox(1, 50, 494, 860, 22)
$fr1 = $f1.TextFrame.TextRange
$fr1.Text = "Smart India Hackathon 2025 | Idea Submission PPT | Slide 1 of 6"
$fr1.Font.Name = "Segoe UI"
$fr1.Font.Size = 8.5
$fr1.Font.Color.RGB = $cMutedGray
$fr1.ParagraphFormat.Alignment = 2

# ==========================================
# SLIDE 2: PROPOSED SOLUTION
# ==========================================
Write-Host "[*] Building Slide 2 (Proposed Solution)..."
$slide2 = $pres.Slides.Add(2, 12)
Set-Header $slide2 "PROPOSED SOLUTION" "Proposed Solution (Describe your Idea / Solution / Prototype)"

$s2_c1 = @(
    "• Multi-Channel Periodic Engagement: Proactive check-ins via Web Portal, Mobile App, Chatbot, SMS & automated IVRS follow-up calls.",
    "• Dual-Engine In-Memory Analysis:",
    "  - Voice Stress Analytics (<25ms DSP): Measures pitch jitter, shimmer, HNR & 4-10Hz vocal cord tremor without saving audio.",
    "  - Multilingual Emotion AI (<5ms NLP): Identifies intimidation, social ostracism & threats across Hindi, Bengali, Tamil, Telugu, English.",
    "• Dynamic Distress Score (DDS 0-100): Continuously aggregates multi-modal signals into a longitudinal psychological well-being index.",
    "• Automated Crisis Triage: Triggers instant alerts to counselors and district authorities when risk thresholds are breached."
)
Create-Card $slide2 35 80 285 425 "1. Detailed Proposed Solution" $s2_c1 $cNavy

$s2_c2 = @(
    "• Replaces One-Time Aid with Continuous Care: Traditional mechanisms only offer post-complaint financial relief; SAMVEDNA AI monitors well-being across investigation, trial & rehabilitation.",
    "• Prevents 'Trauma Freezing' & Silent Suffering: Detects escalating fear, court intimidation & suicidal ideation before a fatal crisis occurs.",
    "• Protects Vulnerable Atrocity Complainants: Tailored for victims under the SC/ST (PoA) Act 1989 facing boycott or retaliation.",
    "• Actionable Multi-Tier Interventions: Automatically routes cases for witness protection, legal aid, medical aid, or emergency relocation."
)
Create-Card $slide2 338 80 285 425 "2. How It Addresses Problem" $s2_c2 $cDeepAmber

$s2_c3 = @(
    "• Involuntary Acoustic Biomarkers: Measures glottal frequency perturbations (Jitter > 1.04%, HNR < 12dB) that cannot be masked even when speaking calmly.",
    "• Explainable AI (XAI) for Due Process: Decomposes distress scores into court-admissible SHAP evidence cards adhering to Section 61 BNSS standards.",
    "• Zero Raw-Audio Retention (Privacy First): Audio is processed in volatile RAM buffers and wiped in <25ms; 100% DPDP Act 2023 compliant.",
    "• District, State & National Dashboards: Centralized oversight to monitor vulnerable atrocity cases across jurisdictions."
)
Create-Card $slide2 640 80 285 425 "3. Innovation & Uniqueness" $s2_c3 $cGreen

# ==========================================
# SLIDE 3: TECHNICAL APPROACH
# ==========================================
Write-Host "[*] Building Slide 3 (Technical Approach)..."
$slide3 = $pres.Slides.Add(3, 12)
Set-Header $slide3 "TECHNICAL APPROACH" "Technologies to be Used & Implementation Methodology"

$s3_c1 = @(
    "• Backend & API Architecture: Python 3.11+, FastAPI (asynchronous REST & WebSocket channels), Uvicorn ASGI server.",
    "• Audio DSP & Voice Stress Core: NumPy, SciPy (normalized autocorrelation, 75-500Hz bandpass filter, spectral power density), Librosa.",
    "• NLP & Threat Intelligence: Vectorized Regex Lexicons, Russell 2D Circumplex (Valence-Arousal mapping) across 5 Indian languages.",
    "• Conversational Empathy AI: Google Gemini API (Interactions API / 2.5 Flash) with deterministic local offline safety fallback.",
    "• Monitoring Dashboards: Tailwind CSS, Chart.js (longitudinal distress trajectories), Leaflet.js (district threat heatmaps).",
    "• Authority Dispatch Integration: CAP (Common Alerting Protocol) JSON-LD for NHAA 14566, ERSS 112 CAD & CCTNS webhooks."
)
Create-Card $slide3 35 80 430 425 "1. Technologies & Frameworks" $s3_c1 $cNavy

$s3_c2 = @(
    "[Periodic Interactions: Web | Chatbot | IVRS | NHAA 14566 | SMS]",
    "                               │",
    "                               ▼",
    "[FastAPI In-Memory RAM Buffer (Zero Disk Storage)]",
    "       ├──> Acoustic Voice Analytics (<25ms DSP): Pitch Jitter, Shimmer, HNR, Tremor",
    "       └──> Multilingual Emotion AI (<5ms NLP): Threats, Intimidation, Ostracism",
    "                               │",
    "                               ▼",
    "[Dynamic Distress Scoring (DDS) & Longitudinal Trend Engine]",
    "• Formula: DDS = 0.28*Voice + 0.28*NLP + 0.20*Context + 0.16*Lang + 0.08*Env",
    "• Non-linear overrides for imminent danger, weapon threat & suicidal ideation",
    "                               │",
    "               ┌───────────────┴───────────────┐",
    "               ▼ (DDS < 60: Low/Moderate)       ▼ (DDS >= 60: High/Critical Escalation)",
    "[Empathetic Support & Follow-up]   [AUTOMATED MULTI-TIER CRISIS ALERTS]",
    "• Grounding exercises & check-ins  • District Official & Counselor Alerts",
    "• Routine longitudinal logging     • Witness Protection & Legal Aid Trigger",
    "• NHAA counseling suggestions      • District / State / National Dashboard Sync",
    "                                   • Court-Admissible SHAP Evidence Cards"
)
Create-Card $slide3 480 80 445 425 "2. Implementation Methodology & Pipeline" $s3_c2 $cDeepAmber

# ==========================================
# SLIDE 4: FEASIBILITY AND VIABILITY
# ==========================================
Write-Host "[*] Building Slide 4 (Feasibility & Viability)..."
$slide4 = $pres.Slides.Add(4, 12)
Set-Header $slide4 "FEASIBILITY AND VIABILITY" "Feasibility Analysis, Potential Challenges & Mitigation Strategies"

$s4_c1 = @(
    "• Zero Hardware Cost: Operates via standard smartphones, web browsers, and low-cost automated IVRS telephony for non-smartphone users.",
    "• Ultra-Low Compute Overhead: Full DSP voice stress and NLP scoring executes in <35ms on basic multi-core CPUs without requiring GPUs.",
    "• Bandwidth Resilient: Uses in-memory 16kHz mono audio streams; operational even on low-speed 2G/3G networks in rural SC/ST habitations.",
    "• Operational Readiness: Fully functional working prototype already developed and verified across multi-device check-in scenarios."
)
Create-Card $slide4 35 80 285 425 "1. Feasibility Analysis" $s4_c1 $cGreen

$s4_c2 = @(
    "• Ambient Rural Noise: Livestock, traffic, or loud household environments distorting vocal stress features.",
    "• Victim Fear & Non-Cooperation: Fear that speaking honestly will provoke retaliation or breach confidentiality.",
    "• Dialect & Linguistic Diversity: Slang, code-switching (Hinglish/Tanglish), and localized idioms across atrocity victims.",
    "• False Alarm Fatigue: Over-alerting authorities during normal crying, emotional venting, or loud speaking."
)
Create-Card $slide4 338 80 285 425 "2. Potential Challenges & Risks" $s4_c2 $cRed

$s4_c3 = @(
    "• Glottal Harmonic Filtering: Harmonics-to-Noise Ratio (HNR) isolates vocal cords from ambient noise; noise capped at only 8% of DDS.",
    "• DPDP Act 2023 Compliance: Zero audio persistence builds trust; victims know audio is wiped immediately from RAM.",
    "• Multilingual Indic Corpus: Dedicated lexicons across 5 languages accommodating romanized spelling and phonetic variations.",
    "• 2D Affect Disambiguation: Russell model separates Arousal from Valence; venting with relief is not escalated as crisis."
)
Create-Card $slide4 640 80 285 425 "3. Mitigation Strategies" $s4_c3 $cNavy

# ==========================================
# SLIDE 5: IMPACT AND BENEFITS
# ==========================================
Write-Host "[*] Building Slide 5 (Impact & Benefits)..."
$slide5 = $pres.Slides.Add(5, 12)
Set-Header $slide5 "IMPACT AND BENEFITS" "Potential Impact on Target Audience & Multi-Dimensional Benefits"

$s5_c1 = @(
    "• Rape & Gang Rape Survivors: Continuous trauma tracking to prevent post-assault depression, panic, and suicide.",
    "• Threatened Witnesses & Families: Early detection of intimidation, coercion, and social boycott during ongoing trials.",
    "• SC/ST Atrocity Complainants: Proactive safety net under SC/ST (PoA) Act 1989 ensuring victims receive rehabilitation and protection.",
    "• Grievous Hurt & Arson Victims: Monitoring recovery milestones and identifying urgent financial or medical relief needs."
)
Create-Card $slide5 35 80 285 425 "1. Target Audience Impact" $s5_c1 $cNavy

$s5_c2 = @(
    "• Early Crisis Detection: Catches psychological deterioration weeks before acute mental breakdown, self-harm, or witness hostility.",
    "• Timely Intervention Deployment: Directly triggers designated officers for counseling, relocation, police protection, or compensation release.",
    "• Strengthened Justice Delivery: Complainants feel supported by the state, reducing case withdrawals due to fear or exhaustion.",
    "• Agency Coordination: Bridges welfare departments, legal aid authorities (NALSA), police, and district administrations."
)
Create-Card $slide5 338 80 285 425 "2. Systemic & Administrative Benefits" $s5_c2 $cDeepAmber

$s5_c3 = @(
    "• SDG 3 (Good Health & Well-being): Target 3.4 -- Mental health support, trauma reduction, and suicide prevention among victims.",
    "• SDG 5 (Gender Equality): Target 5.2 -- Elimination of violence and institutional secondary trauma against women.",
    "• SDG 10 (Reduced Inequalities): Target 10.2 -- Protecting vulnerable SC/ST and marginalized communities from systemic exploitation.",
    "• SDG 16 (Peace, Justice & Strong Institutions): Target 16.1 & 16.2 -- Ending atrocities, protecting witnesses, and ensuring fair trials."
)
Create-Card $slide5 640 80 285 425 "3. UN SDGs & Statutory Alignment" $s5_c3 $cGreen

# ==========================================
# SLIDE 6: RESEARCH AND REFERENCES
# ==========================================
Write-Host "[*] Building Slide 6 (Research & References)..."
$slide6 = $pres.Slides.Add(6, 12)
Set-Header $slide6 "RESEARCH AND REFERENCES" "Details / Links of Reference Literature, Datasets & Statutory Work"

$s6_c1 = @(
    "• National Helpline Against Atrocities (NHAA 14566): Operational framework by Ministry of Social Justice & Empowerment, Govt. of India.",
    "• SC & ST (Prevention of Atrocities) Act, 1989: Statutory mandates for victim relief, economic rehabilitation, and witness protection.",
    "• National Crime Records Bureau (NCRB 2022): 'Crime in India Report' -- Documenting atrocity registration, trial delays, and conviction rates.",
    "• Trauma & Victimology Research: Porges (2011) Polyvagal Theory on vocal cord tension and tonic immobility under prolonged intimidation."
)
Create-Card $slide6 35 80 430 205 "1. Institutional Framework & Victim Research" $s6_c1 $cNavy

$s6_c2 = @(
    "• RAVDESS & CREMA-D: Validated multi-actor databases (14,700+ clips) calibrating acoustic distress, panic, and tremor thresholds.",
    "• EMO-DB Database: Technical Univ. of Berlin benchmark for frequency perturbation (Jitter) under psychological duress.",
    "• IndicNLP & Parallel Corpora: Lexical threat models across Hindi, Bengali, Tamil, Telugu, and English distress expressions.",
    "• Synthetic Augmentation: Urban and rural noise injection (0-20 dB SNR) ensuring robustness in real-world Indian settings."
)
Create-Card $slide6 480 80 445 205 "2. Acoustic & Linguistic Datasets" $s6_c2 $cDeepAmber

$s6_c3 = @(
    "• Russell's Circumplex Affect Model: Russell, J.A. (1980) Journal of Personality & Social Psychology -- 2D Valence-Arousal mapping.",
    "• Explainable AI (SHAP): Lundberg & Lee (NeurIPS 2017) -- Cooperative game-theory attribution for court-admissible evidence cards.",
    "• Statutory Standards: Digital Personal Data Protection (DPDP) Act 2023 (MeitY) & Section 61 Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023.",
    "• Interoperability Standards: ITU-T Emergency Communications & Common Alerting Protocol (CAP v1.2) for ERSS 112 / CCTNS CAD dispatch."
)
Create-Card $slide6 35 295 890 210 "3. Technical References & Statutory Compliance" $s6_c3 $cGreen

# ==========================================
# EXPORT & SAVE
# ==========================================
Write-Host "[*] Saving Presentation to Destinations..."

$destDownloadsPptx = "C:\Users\ACER\Downloads\SAMVEDNA_AI_SIH_Presentation.pptx"
$destDesktopPptx   = "C:\Users\ACER\Desktop\SAMVEDNA_AI_SIH_Presentation.pptx"
$destStaticPptx    = "C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\backend\static\SAMVEDNA_AI_SIH_Presentation.pptx"

$destDownloadsPdf  = "C:\Users\ACER\Downloads\SAMVEDNA_AI_SIH_Presentation.pdf"
$destDesktopPdf    = "C:\Users\ACER\Desktop\SAMVEDNA_AI_SIH_Presentation.pdf"
$destStaticPdf     = "C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\backend\static\SAMVEDNA_AI_SIH_Presentation.pdf"

# Save PPTX
$pres.SaveAs($destDownloadsPptx)
Write-Host "[+] Saved PPTX to: $destDownloadsPptx"

$pres.SaveAs($destDesktopPptx)
Write-Host "[+] Saved PPTX to: $destDesktopPptx"

$pres.SaveAs($destStaticPptx)
Write-Host "[+] Saved PPTX to: $destStaticPptx"

# Save PDF (Directly uploadable to SIH portal)
$pres.SaveAs($destDownloadsPdf, 32) # 32 = ppSaveAsPDF
Write-Host "[+] Exported PDF to: $destDownloadsPdf"

$pres.SaveAs($destDesktopPdf, 32)
Write-Host "[+] Exported PDF to: $destDesktopPdf"

$pres.SaveAs($destStaticPdf, 32)
Write-Host "[+] Exported PDF to: $destStaticPdf"

$pres.Close()
$ppt.Quit()
Write-Host "[+] All SIH Presentation files generated successfully!"
