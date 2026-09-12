
$ErrorActionPreference = "Stop"

Write-Host "[*] Initializing PowerPoint..."
$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoTrue)
$pres.PageSetup.SlideWidth = 960
$pres.PageSetup.SlideHeight = 540

$cNavy     = 15 + 23*256 + 42*65536
$cCardNavy = 30 + 41*256 + 59*65536
$cAmber    = 245 + 158*256 + 11*65536
$cDeepAmber= 180 + 83*256 + 9*65536
$cWhite    = 255 + 255*256 + 255*65536
$cSlateDark= 30 + 41*256 + 59*65536
$cSlateText= 51 + 65*256 + 85*65536
$cMutedGray= 100 + 116*256 + 139*65536
$cLightBg  = 248 + 250*256 + 252*65536
$cGreen    = 16 + 185*256 + 129*65536
$cRed      = 220 + 38*256 + 38*65536

function Set-Header($slide, $category, $title) {
    $topBar = $slide.Shapes.AddShape(1, 0, 0, 960, 68)
    $topBar.Fill.Solid()
    $topBar.Fill.ForeColor.RGB = $cNavy
    $topBar.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    $tBox = $slide.Shapes.AddTextbox(1, 35, 8, 700, 20)
    $tBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr = $tBox.TextFrame.TextRange
    $tr.Text = "SMART INDIA HACKATHON 2025 | PROBLEM STATEMENT ID: 94 | NHAA 14566"
    $tr.Font.Name = "Segoe UI"
    $tr.Font.Size = 10
    $tr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr.Font.Color.RGB = $cAmber

    $titleBox = $slide.Shapes.AddTextbox(1, 35, 27, 750, 36)
    $titleBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titler = $titleBox.TextFrame.TextRange
    $titler.Text = $title
    $titler.Font.Name = "Segoe UI"
    $titler.Font.Size = 17
    $titler.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titler.Font.Color.RGB = $cWhite

    $badge = $slide.Shapes.AddTextbox(1, 780, 14, 150, 40)
    $br = $badge.TextFrame.TextRange
    $br.Text = "SAMVEDNA AI`nTeam Portal"
    $br.Font.Name = "Segoe UI"
    $br.Font.Size = 9
    $br.Font.Color.RGB = $cMutedGray
    $br.ParagraphFormat.Alignment = 3

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

function Create-Card($slide, $x, $y, $w, $h, $title, $textLines, $accentColor) {
    $card = $slide.Shapes.AddShape(5, $x, $y, $w, $h)
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
    
    $full = [string]::Join("`n", $textLines)
    $br.Text = $full
}

# Slide 1: Title
Write-Host "[*] Creating Slide 1..."
$s1 = $pres.Slides.Add(1, 12)
$bg1 = $s1.Shapes.AddShape(1, 0, 0, 960, 540)
$bg1.Fill.Solid()
$bg1.Fill.ForeColor.RGB = $cNavy
$bg1.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

$tb1 = $s1.Shapes.AddTextbox(1, 50, 28, 860, 36)
$r = $tb1.TextFrame.TextRange
$r.Text = "SMART INDIA HACKATHON 2025"
$r.Font.Name = "Segoe UI"
$r.Font.Size = 22
$r.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$r.Font.Color.RGB = $cAmber
$r.ParagraphFormat.Alignment = 2

$tb2 = $s1.Shapes.AddTextbox(1, 50, 64, 860, 24)
$r2 = $tb2.TextFrame.TextRange
$r2.Text = "TITLE PAGE -- OFFICIAL IDEA SUBMISSION"
$r2.Font.Name = "Segoe UI"
$r2.Font.Size = 12
$r2.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$r2.Font.Color.RGB = $cWhite
$r2.ParagraphFormat.Alignment = 2

$mCard = $s1.Shapes.AddShape(5, 50, 98, 860, 98)
$mCard.Fill.Solid()
$mCard.Fill.ForeColor.RGB = $cCardNavy
$mCard.Line.ForeColor.RGB = $cAmber
$mCard.Line.Weight = 2

$ptb = $s1.Shapes.AddTextbox(1, 60, 106, 840, 44)
$r3 = $ptb.TextFrame.TextRange
$r3.Text = "SAMVEDNA AI"
$r3.Font.Name = "Segoe UI"
$r3.Font.Size = 28
$r3.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$r3.Font.Color.RGB = $cAmber
$r3.ParagraphFormat.Alignment = 2

$psb = $s1.Shapes.AddTextbox(1, 60, 150, 840, 38)
$r4 = $psb.TextFrame.TextRange
$r4.Text = "AI-Powered Dynamic Mental Health Monitoring and Distress Prediction System (NHAA 14566)"
$r4.Font.Name = "Segoe UI"
$r4.Font.Size = 12
$r4.Font.Color.RGB = $cWhite
$r4.ParagraphFormat.Alignment = 2

$wC = $s1.Shapes.AddShape(5, 50, 208, 860, 275)
$wC.Fill.Solid()
$wC.Fill.ForeColor.RGB = $cWhite
$wC.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

$dtBox = $s1.Shapes.AddTextbox(1, 75, 220, 810, 250)
$dtr = $dtBox.TextFrame.TextRange
$dtr.Font.Name = "Segoe UI"
$dtr.Font.Size = 11.5
$dtr.Font.Color.RGB = $cSlateDark
$dtr.Text = @"
? Problem Statement ID: 94
? Problem Statement Title: AI-based Dynamic Mental Health Monitoring and Distress Prediction System
? Target Ecosystem: National Helpline Against Atrocities (NHAA 14566), Integrated Portal and SC/ST (PoA) Act 1989
? Theme: Smart Automation / Security and Surveillance (Vulnerable Community and Victim Protection)
? PS Category: Software
? Team ID: [Enter Your Team ID on Portal]
? Team Name: [Enter Your Registered Team Name]
? Core Innovation: In-Memory Voice Stress Analytics (Jitter/Shimmer DSP) + Multilingual Indic Emotion AI
? Beneficiaries: Atrocity complainants, rape/gang rape survivors, threatened witnesses and SC/ST families
"@

# Slide 2: Proposed Solution
Write-Host "[*] Creating Slide 2..."
$s2 = $pres.Slides.Add(2, 12)
Set-Header $s2 "PROPOSED SOLUTION" "Proposed Solution (Describe your Idea / Solution / Prototype)"

$s2_lines1 = @(
    "? Multi-Channel Periodic Engagement: Proactive check-ins via Web Portal, Mobile App, Chatbot, SMS and automated IVRS follow-up calls.",
    "? Dual-Engine In-Memory Analysis:",
    "  - Voice Stress Analytics (<25ms DSP): Measures pitch jitter, shimmer, HNR and 4-10Hz vocal cord tremor without saving audio.",
    "  - Multilingual Emotion AI (<5ms NLP): Identifies intimidation, social ostracism and threats across Hindi, Bengali, Tamil, Telugu, English.",
    "? Dynamic Distress Score (DDS 0-100): Continuously aggregates multi-modal signals into a longitudinal psychological well-being index.",
    "? Automated Crisis Triage: Triggers instant alerts to counselors and district authorities when risk thresholds are breached."
)
Create-Card $s2 35 80 285 425 "1. Detailed Proposed Solution" $s2_lines1 $cNavy

$s2_lines2 = @(
    "? Replaces One-Time Aid with Continuous Care: Traditional mechanisms only offer post-complaint financial relief; SAMVEDNA AI monitors well-being across investigation, trial and rehabilitation.",
    "? Prevents 'Trauma Freezing' and Silent Suffering: Detects escalating fear, court intimidation and suicidal ideation before a fatal crisis occurs.",
    "? Protects Vulnerable Atrocity Complainants: Tailored for victims under the SC/ST (PoA) Act 1989 facing boycott or retaliation.",
    "? Actionable Multi-Tier Interventions: Automatically routes cases for witness protection, legal aid, medical aid, or emergency relocation."
)
Create-Card $s2 338 80 285 425 "2. How It Addresses Problem" $s2_lines2 $cDeepAmber

$s2_lines3 = @(
    "? Involuntary Acoustic Biomarkers: Measures glottal frequency perturbations (Jitter > 1.04%, HNR < 12dB) that cannot be masked even when speaking calmly.",
    "? Explainable AI (XAI) for Due Process: Decomposes distress scores into court-admissible SHAP evidence cards adhering to Section 61 BNSS standards.",
    "? Zero Raw-Audio Retention (Privacy First): Audio is processed in volatile RAM buffers and wiped in <25ms; 100% DPDP Act 2023 compliant.",
    "? District, State and National Dashboards: Centralized oversight to monitor vulnerable atrocity cases across jurisdictions."
)
Create-Card $s2 640 80 285 425 "3. Innovation and Uniqueness" $s2_lines3 $cGreen

# Slide 3: Technical Approach
Write-Host "[*] Creating Slide 3..."
$s3 = $pres.Slides.Add(3, 12)
Set-Header $s3 "TECHNICAL APPROACH" "Technologies to be Used and Implementation Methodology"

$s3_lines1 = @(
    "? Backend and API Architecture: Python 3.11+, FastAPI (asynchronous REST and WebSocket channels), Uvicorn ASGI server.",
    "? Audio DSP and Voice Stress Core: NumPy, SciPy (normalized autocorrelation, 75-500Hz bandpass filter, spectral power density), Librosa.",
    "? NLP and Threat Intelligence: Vectorized Regex Lexicons, Russell 2D Circumplex (Valence-Arousal mapping) across 5 Indian languages.",
    "? Conversational Empathy AI: Google Gemini API (Interactions API / 2.5 Flash) with deterministic local offline safety fallback.",
    "? Monitoring Dashboards: Tailwind CSS, Chart.js (longitudinal distress trajectories), Leaflet.js (district threat heatmaps).",
    "? Authority Dispatch Integration: CAP (Common Alerting Protocol) JSON-LD for NHAA 14566, ERSS 112 CAD and CCTNS webhooks."
)
Create-Card $s3 35 80 430 425 "1. Technologies and Frameworks" $s3_lines1 $cNavy

$s3_lines2 = @(
    "Step 1: Multi-Channel Check-in Ingestion",
    "  - Web Portal, Mobile App, WhatsApp Chatbot, SMS or automated IVRS calls (NHAA 14566).",
    "Step 2: Dual In-Memory Processing (<30ms)",
    "  - Voice Stress Analytics: Autocorrelation F0 pitch, Jitter, Shimmer, HNR, 4-10Hz tremor.",
    "  - Multilingual Emotion AI: Threat mining, intimidation markers, and Russell affect mapping.",
    "Step 3: Dynamic Distress Scoring (DDS Engine)",
    "  - Multi-Modal Fusion: DDS = 0.28*Voice + 0.28*NLP + 0.20*Context + 0.16*Lang + 0.08*Env.",
    "  - Non-linear safety triggers for weapon threats, severe intimidation and self-harm.",
    "Step 4: Longitudinal Trajectory and Predictive Escalation",
    "  - Identifies negative trend lines indicating emerging post-complaint psychological breakdown.",
    "Step 5: Automated Alert and Multi-Tier Dashboards",
    "  - Dispatches actionable risk alerts to district welfare officers, legal aid, and counselors.",
    "  - Generates court-admissible SHAP evidence cards adhering to Section 61 BNSS standards."
)
Create-Card $s3 480 80 445 425 "2. Implementation Methodology and Pipeline" $s3_lines2 $cDeepAmber

# Slide 4: Feasibility and Viability
Write-Host "[*] Creating Slide 4..."
$s4 = $pres.Slides.Add(4, 12)
Set-Header $s4 "FEASIBILITY AND VIABILITY" "Feasibility Analysis, Potential Challenges and Mitigation Strategies"

$s4_lines1 = @(
    "? Zero Hardware Cost: Operates via standard smartphones, web browsers, and low-cost automated IVRS telephony for non-smartphone users.",
    "? Ultra-Low Compute Overhead: Full DSP voice stress and NLP scoring executes in <35ms on basic multi-core CPUs without requiring GPUs.",
    "? Bandwidth Resilient: Uses in-memory 16kHz mono audio streams; operational even on low-speed 2G/3G networks in rural SC/ST habitations.",
    "? Operational Readiness: Fully functional working prototype already developed and verified across multi-device check-in scenarios."
)
Create-Card $s4 35 80 285 425 "1. Feasibility Analysis" $s4_lines1 $cGreen

$s4_lines2 = @(
    "? Ambient Rural Noise: Livestock, traffic, or loud household environments distorting vocal stress features.",
    "? Victim Fear and Non-Cooperation: Fear that speaking honestly will provoke retaliation or breach confidentiality.",
    "? Dialect and Linguistic Diversity: Slang, code-switching (Hinglish/Tanglish), and localized idioms across atrocity victims.",
    "? False Alarm Fatigue: Over-alerting authorities during normal crying, emotional venting, or loud speaking."
)
Create-Card $s4 338 80 285 425 "2. Potential Challenges and Risks" $s4_lines2 $cRed

$s4_lines3 = @(
    "? Glottal Harmonic Filtering: Harmonics-to-Noise Ratio (HNR) isolates vocal cords from ambient noise; noise capped at only 8% of DDS.",
    "? DPDP Act 2023 Compliance: Zero audio persistence builds trust; victims know audio is wiped immediately from RAM.",
    "? Multilingual Indic Corpus: Dedicated lexicons across 5 languages accommodating romanized spelling and phonetic variations.",
    "? 2D Affect Disambiguation: Russell model separates Arousal from Valence; venting with relief is not escalated as crisis."
)
Create-Card $s4 640 80 285 425 "3. Mitigation Strategies" $s4_lines3 $cNavy

# Slide 5: Impact and Benefits
Write-Host "[*] Creating Slide 5..."
$s5 = $pres.Slides.Add(5, 12)
Set-Header $s5 "IMPACT AND BENEFITS" "Potential Impact on Target Audience and Multi-Dimensional Benefits"

$s5_lines1 = @(
    "? Rape and Gang Rape Survivors: Continuous trauma tracking to prevent post-assault depression, panic, and suicide.",
    "? Threatened Witnesses and Families: Early detection of intimidation, coercion, and social boycott during ongoing trials.",
    "? SC/ST Atrocity Complainants: Proactive safety net under SC/ST (PoA) Act 1989 ensuring victims receive rehabilitation and protection.",
    "? Grievous Hurt and Arson Victims: Monitoring recovery milestones and identifying urgent financial or medical relief needs."
)
Create-Card $s5 35 80 285 425 "1. Target Audience Impact" $s5_lines1 $cNavy

$s5_lines2 = @(
    "? Early Crisis Detection: Catches psychological deterioration weeks before acute mental breakdown, self-harm, or witness hostility.",
    "? Timely Intervention Deployment: Directly triggers designated officers for counseling, relocation, police protection, or compensation release.",
    "? Strengthened Justice Delivery: Complainants feel supported by the state, reducing case withdrawals due to fear or exhaustion.",
    "? Agency Coordination: Bridges welfare departments, legal aid authorities (NALSA), police, and district administrations."
)
Create-Card $s5 338 80 285 425 "2. Systemic and Administrative Benefits" $s5_lines2 $cDeepAmber

$s5_lines3 = @(
    "? SDG 3 (Good Health and Well-being): Target 3.4 -- Mental health support, trauma reduction, and suicide prevention among victims.",
    "? SDG 5 (Gender Equality): Target 5.2 -- Elimination of violence and institutional secondary trauma against women.",
    "? SDG 10 (Reduced Inequalities): Target 10.2 -- Protecting vulnerable SC/ST and marginalized communities from systemic exploitation.",
    "? SDG 16 (Peace, Justice and Strong Institutions): Target 16.1 and 16.2 -- Ending atrocities, protecting witnesses, and ensuring fair trials."
)
Create-Card $s5 640 80 285 425 "3. UN SDGs and Statutory Alignment" $s5_lines3 $cGreen

# Slide 6: Research and References
Write-Host "[*] Creating Slide 6..."
$s6 = $pres.Slides.Add(6, 12)
Set-Header $s6 "RESEARCH AND REFERENCES" "Details / Links of Reference Literature, Datasets and Statutory Work"

$s6_lines1 = @(
    "? National Helpline Against Atrocities (NHAA 14566): Operational framework by Ministry of Social Justice and Empowerment, Govt. of India.",
    "? SC and ST (Prevention of Atrocities) Act, 1989: Statutory mandates for victim relief, economic rehabilitation, and witness protection.",
    "? National Crime Records Bureau (NCRB 2022): 'Crime in India Report' -- Documenting atrocity registration, trial delays, and conviction rates.",
    "? Trauma and Victimology Research: Porges (2011) Polyvagal Theory on vocal cord tension and tonic immobility under prolonged intimidation."
)
Create-Card $s6 35 80 430 205 "1. Institutional Framework and Victim Research" $s6_lines1 $cNavy

$s6_lines2 = @(
    "? RAVDESS and CREMA-D: Validated multi-actor databases (14,700+ clips) calibrating acoustic distress, panic, and tremor thresholds.",
    "? EMO-DB Database: Technical Univ. of Berlin benchmark for frequency perturbation (Jitter) under psychological duress.",
    "? IndicNLP and Parallel Corpora: Lexical threat models across Hindi, Bengali, Tamil, Telugu, and English distress expressions.",
    "? Synthetic Augmentation: Urban and rural noise injection (0-20 dB SNR) ensuring robustness in real-world Indian settings."
)
Create-Card $s6 480 80 445 205 "2. Acoustic and Linguistic Datasets" $s6_lines2 $cDeepAmber

$s6_lines3 = @(
    "? Russell's Circumplex Affect Model: Russell, J.A. (1980) Journal of Personality and Social Psychology -- 2D Valence-Arousal mapping.",
    "? Explainable AI (SHAP): Lundberg and Lee (NeurIPS 2017) -- Cooperative game-theory attribution for court-admissible evidence cards.",
    "? Statutory Standards: Digital Personal Data Protection (DPDP) Act 2023 (MeitY) and Section 61 Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023.",
    "? Interoperability Standards: ITU-T Emergency Communications and Common Alerting Protocol (CAP v1.2) for ERSS 112 / CCTNS CAD dispatch."
)
Create-Card $s6 35 295 890 210 "3. Technical References and Statutory Compliance" $s6_lines3 $cGreen

Write-Host "[*] Saving Presentation..."

$dDownloadsPptx = "C:\Users\ACER\Downloads\SAMVEDNA_AI_SIH_Presentation.pptx"
$dDesktopPptx   = "C:\Users\ACER\Desktop\SAMVEDNA_AI_SIH_Presentation.pptx"
$dStaticPptx    = "C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\backend\static\SAMVEDNA_AI_SIH_Presentation.pptx"

$dDownloadsPdf  = "C:\Users\ACER\Downloads\SAMVEDNA_AI_SIH_Presentation.pdf"
$dDesktopPdf    = "C:\Users\ACER\Desktop\SAMVEDNA_AI_SIH_Presentation.pdf"
$dStaticPdf     = "C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\backend\static\SAMVEDNA_AI_SIH_Presentation.pdf"

$pres.SaveAs($dDownloadsPptx)
Write-Host "[+] Saved PPTX: $dDownloadsPptx"

$pres.SaveAs($dDesktopPptx)
Write-Host "[+] Saved PPTX: $dDesktopPptx"

$pres.SaveAs($dStaticPptx)
Write-Host "[+] Saved PPTX: $dStaticPptx"

$pres.SaveAs($dDownloadsPdf, 32)
Write-Host "[+] Saved PDF: $dDownloadsPdf"

$pres.SaveAs($dDesktopPdf, 32)
Write-Host "[+] Saved PDF: $dDesktopPdf"

$pres.SaveAs($dStaticPdf, 32)
Write-Host "[+] Saved PDF: $dStaticPdf"

$pres.Close()
$ppt.Quit()
Write-Host "[+] ALL FILES CREATED SUCCESSFULLY!"
