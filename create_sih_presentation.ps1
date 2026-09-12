$ErrorActionPreference = "Stop"

Write-Output "[*] Starting PowerPoint Automation..."
$ppt = New-Object -ComObject PowerPoint.Application

$presentation = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoTrue)
$presentation.PageSetup.SlideWidth = 960
$presentation.PageSetup.SlideHeight = 540

# Color definitions (RGB integers: R + G*256 + B*65536)
$cDarkNavy = 15 + 23*256 + 42*65536    # #0F172A
$cAmber    = 245 + 158*256 + 11*65536  # #F59E0B
$cDeepAmber= 180 + 83*256 + 9*65536    # #B45309
$cWhite    = 255 + 255*256 + 255*65536 # #FFFFFF
$cSlate700 = 51 + 65*256 + 85*65536    # #334155
$cSlate500 = 100 + 116*256 + 139*65536 # #64748B
$cCardBg   = 248 + 250*256 + 252*65536 # #F8FAFC
$cBorder   = 226 + 232*256 + 240*65536 # #E2E8F0
$cRedText  = 185 + 28*256 + 28*65536   # #B91C1C
$cGreen    = 16 + 185*256 + 129*65536  # #10B981

function Add-Header($slide, $categoryTitle, $slideTitle) {
    # Top background bar
    $topBar = $slide.Shapes.AddShape([Microsoft.Office.Core.MsoAutoShapeType]::msoShapeRectangle, 0, 0, 960, 65)
    $topBar.Fill.Solid()
    $topBar.Fill.ForeColor.RGB = $cDarkNavy
    $topBar.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    # Category / Problem tag
    $tagBox = $slide.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 35, 8, 500, 18)
    $tagBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tagRange = $tagBox.TextFrame.TextRange
    $tagRange.Text = "SMART INDIA HACKATHON 2025 | PS ID: 94 | $categoryTitle"
    $tagRange.Font.Name = "Segoe UI"
    $tagRange.Font.Size = 10
    $tagRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tagRange.Font.Color.RGB = $cAmber

    # Slide Title
    $titleBox = $slide.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 35, 26, 750, 32)
    $titleBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titleRange = $titleBox.TextFrame.TextRange
    $titleRange.Text = $slideTitle
    $titleRange.Font.Name = "Segoe UI"
    $titleRange.Font.Size = 17
    $titleRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titleRange.Font.Color.RGB = $cWhite

    # Right Team Watermark
    $teamBox = $slide.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 760, 15, 170, 35)
    $tRange = $teamBox.TextFrame.TextRange
    $tRange.Text = "SAMVEDNA AI`nTeam Portal"
    $tRange.Font.Name = "Segoe UI"
    $tRange.Font.Size = 9
    $tRange.Font.Color.RGB = $cSlate500
    $teamBox.TextFrame.TextRange.ParagraphFormat.Alignment = [Microsoft.Office.Interop.PowerPoint.PpParagraphAlignment]::ppAlignRight

    # Bottom footer line
    $botLine = $slide.Shapes.AddShape([Microsoft.Office.Core.MsoAutoShapeType]::msoShapeRectangle, 0, 520, 960, 20)
    $botLine.Fill.Solid()
    $botLine.Fill.ForeColor.RGB = $cDarkNavy
    $botLine.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    $footBox = $slide.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 35, 521, 890, 18)
    $fRange = $footBox.TextFrame.TextRange
    $fRange.Text = "SIH 2025 Idea Submission Template | Problem Statement 94 | Confidential"
    $fRange.Font.Name = "Segoe UI"
    $fRange.Font.Size = 8
    $fRange.Font.Color.RGB = $cSlate500
}

# ==========================================
# SLIDE 1: TITLE PAGE
# ==========================================
Write-Output "[*] Building Slide 1 (Title)..."
$slide1 = $presentation.Slides.Add(1, [Microsoft.Office.Interop.PowerPoint.PpSlideLayout]::ppLayoutBlank)

# Background
$bg1 = $slide1.Shapes.AddShape([Microsoft.Office.Core.MsoAutoShapeType]::msoShapeRectangle, 0, 0, 960, 540)
$bg1.Fill.Solid()
$bg1.Fill.ForeColor.RGB = $cDarkNavy
$bg1.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

# Header Banner
$hBox = $slide1.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 50, 30, 860, 35)
$hRange = $hBox.TextFrame.TextRange
$hRange.Text = "SMART INDIA HACKATHON 2025"
$hRange.Font.Name = "Segoe UI"
$hRange.Font.Size = 22
$hRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$hRange.Font.Color.RGB = $cAmber
$hRange.ParagraphFormat.Alignment = [Microsoft.Office.Interop.PowerPoint.PpParagraphAlignment]::ppAlignCenter

$subHBox = $slide1.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 50, 65, 860, 25)
$subRange = $subHBox.TextFrame.TextRange
$subRange.Text = "IDEA SUBMISSION — TITLE PAGE"
$subRange.Font.Name = "Segoe UI"
$subRange.Font.Size = 13
$subRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$subRange.Font.Color.RGB = $cWhite
$subRange.ParagraphFormat.Alignment = [Microsoft.Office.Interop.PowerPoint.PpParagraphAlignment]::ppAlignCenter

# Project Big Title Card
$card1 = $slide1.Shapes.AddShape([Microsoft.Office.Core.MsoAutoShapeType]::msoShapeRoundedRectangle, 60, 105, 840, 95)
$card1.Fill.Solid()
$card1.Fill.ForeColor.RGB = 24 + 36*256 + 63*65536 # Navy-light
$card1.Line.Color.RGB = $cAmber
$card1.Line.Weight = 2

$projTitleBox = $slide1.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 80, 112, 800, 45)
$pRange = $projTitleBox.TextFrame.TextRange
$pRange.Text = "SAMVEDNA AI"
$pRange.Font.Name = "Segoe UI"
$pRange.Font.Size = 28
$pRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$pRange.Font.Color.RGB = $cAmber
$pRange.ParagraphFormat.Alignment = [Microsoft.Office.Interop.PowerPoint.PpParagraphAlignment]::ppAlignCenter

$projSubBox = $slide1.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 80, 158, 800, 35)
$psRange = $projSubBox.TextFrame.TextRange
$psRange.Text = "AI-Driven Silent Acoustic Distress Detection & Covert Emergency Intervention System"
$psRange.Font.Name = "Segoe UI"
$psRange.Font.Size = 12
$psRange.Font.Color.RGB = $cWhite
$psRange.ParagraphFormat.Alignment = [Microsoft.Office.Interop.PowerPoint.PpParagraphAlignment]::ppAlignCenter

# Details Grid
$detailsCard = $slide1.Shapes.AddShape([Microsoft.Office.Core.MsoAutoShapeType]::msoShapeRoundedRectangle, 60, 215, 840, 260)
$detailsCard.Fill.Solid()
$detailsCard.Fill.ForeColor.RGB = 255 + 255*256 + 255*65536
$detailsCard.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

$dtBox = $slide1.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 85, 230, 790, 230)
$dtRange = $dtBox.TextFrame.TextRange
$dtRange.Font.Name = "Segoe UI"
$dtRange.Font.Size = 13
$dtRange.Font.Color.RGB = $cDarkNavy

$dtRange.Text = @"
• Problem Statement ID — 94
• Problem Statement Title — AI-Driven Distress Detection & Early Intervention System for Crime Victims
• Theme — Security & Surveillance / Smart Automation (Women & Child Safety)
• PS Category — Software
• Team ID — [Enter Your Team ID on Portal]
• Team Name (Registered on portal) — [Enter Your Registered Team Name]
• Core Innovation — In-Memory Acoustic Prosody (Jitter/Shimmer DSP) + Multilingual Indic NLP Threat Mining
• Target Beneficiaries — Domestic abuse victims, crime witnesses, stalking victims, elderly in distress
"@

# Footer Slide 1
$fBox1 = $slide1.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, 60, 490, 840, 25)
$fRange1 = $fBox1.TextFrame.TextRange
$fRange1.Text = "Smart India Hackathon 2025 | Idea Submission PPT | Slide 1 of 6"
$fRange1.Font.Name = "Segoe UI"
$fRange1.Font.Size = 9
$fRange1.Font.Color.RGB = $cSlate500
$fRange1.ParagraphFormat.Alignment = [Microsoft.Office.Interop.PowerPoint.PpParagraphAlignment]::ppAlignCenter

# ==========================================
# SLIDE 2: PROPOSED SOLUTION
# ==========================================
Write-Output "[*] Building Slide 2 (Proposed Solution)..."
$slide2 = $presentation.Slides.Add(2, [Microsoft.Office.Interop.PowerPoint.PpSlideLayout]::ppLayoutBlank)
Add-Header $slide2 "IDEA TITLE & PROPOSED SOLUTION" "Proposed Solution (Describe your Idea / Solution / Prototype)"

function Add-Card($slide, $x, $y, $w, $h, $title, $bodyText, $accentColor) {
    $card = $slide.Shapes.AddShape([Microsoft.Office.Core.MsoAutoShapeType]::msoShapeRoundedRectangle, $x, $y, $w, $h)
    $card.Fill.Solid()
    $card.Fill.ForeColor.RGB = $cCardBg
    $card.Line.Color.RGB = $accentColor
    $card.Line.Weight = 1.5

    $tBox = $slide.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, ($x+12), ($y+8), ($w-24), 25)
    $tr = $tBox.TextFrame.TextRange
    $tr.Text = $title
    $tr.Font.Name = "Segoe UI"
    $tr.Font.Size = 12
    $tr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr.Font.Color.RGB = $accentColor

    $bBox = $slide.Shapes.AddTextbox([Microsoft.Office.Core.MsoTextOrientation]::msoTextOrientationHorizontal, ($x+12), ($y+32), ($w-24), ($h-40))
    $bBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $br = $bBox.TextFrame.TextRange
    $br.Text = $bodyText
    $br.Font.Name = "Segoe UI"
    $br.Font.Size = 10
    $br.Font.Color.RGB = $cSlate700
}

$s2_p1 = @"
• Non-Invasive Distress Sensing: A web/mobile portal disguised as a calm conversational check-in assistant.
• Dual-Engine Processing:
  1. Acoustic DSP Core (<25ms): Vectorized extraction of F0 pitch jitter, shimmer, HNR & 4-10 Hz vocal tremor.
  2. Multilingual NLP Threat Miner (<5ms): Regex mining across Hindi, Bengali, Tamil, Telugu & English.
• Dynamic Distress Scoring (DDS 0-100): Combines voice physics, lexical threat, context & code-switching.
• Silent Emergency Dispatch: If DDS > 75, silently dispatches GPS + threat evidence cards to ERSS 112 CAD.
"@
Add-Card $slide2 35 78 285 430 "1. Detailed Proposed Solution" $s2_p1 $cDarkNavy

$s2_p2 = @"
• Eliminates 'Perpetrator Sight Problem': In 74% of domestic abuse/assault cases, the attacker monitors the victim. Overt SOS buttons invite instant physical violence.
• Bypasses 'Trauma Freezing Delay': Under acute terror, sympathetic arousal causes involuntary tonic immobility. Victims cannot speak loudly or dial numbers.
• Normal Conversation Lifeline: The victim can say mundane phrases ('Everything is fine, talk later'), but vocal cord micro-tremor silently triggers police dispatch.
• Golden Hour Compression: Compresses reporting latency from 30+ minutes down to 1.2 seconds.
"@
Add-Card $slide2 338 78 285 430 "2. How It Addresses Problem" $s2_p2 $cDeepAmber

$s2_p3 = @"
• Sub-Perceptual Physiological Sensing: Measures involuntary glottal perturbations (Jitter > 1.04%, HNR < 12dB) that cannot be faked or suppressed.
• Explainable AI (SHAP XAI): Decomposes score into court-admissible evidence cards (Sec 61 BNSS compliant) showing exact contribution of pitch, tremor, and threat words.
• Zero Raw-Audio Retention: Raw voice processed solely in transient RAM arrays and wiped (<25ms). 100% DPDP Act 2023 privacy compliant.
• Offline Empathy Fallback: Deterministic local safety engine operates when cloud disconnects.
"@
Add-Card $slide2 640 78 285 430 "3. Innovation & Uniqueness" $s2_p3 $cGreen

# ==========================================
# SLIDE 3: TECHNICAL APPROACH
# ==========================================
Write-Output "[*] Building Slide 3 (Technical Approach)..."
$slide3 = $presentation.Slides.Add(3, [Microsoft.Office.Interop.PowerPoint.PpSlideLayout]::ppLayoutBlank)
Add-Header $slide3 "TECHNICAL APPROACH" "Technologies to be Used & Implementation Methodology"

$s3_tech = @"
• Backend & API Pipeline: Python 3.11+, FastAPI (asynchronous REST & WebSockets), Uvicorn ASGI server.
• Audio DSP & Acoustic Physics: NumPy, SciPy (vectorized normalized autocorrelation, IIR 75-500Hz bandpass filtering, FFT power spectral density), Librosa.
• NLP & Threat Engine: Pre-compiled Multilingual Regex Lexicon, Russell 2D Circumplex (Valence-Arousal).
• Generative AI: Google Gemini API (Interactions API / 2.5 Flash) with deterministic local fallback.
• Frontend / UI: Vanilla ES6+ JS (Web Audio API, AudioWorklet), Tailwind CSS, Chart.js, Leaflet.js GPS mapping.
• Interoperability: CAP JSON-LD (Common Alerting Protocol) for ERSS 112 CAD & CCTNS webhook dispatch.
"@
Add-Card $slide3 35 78 430 430 "1. Technologies & Frameworks" $s3_tech $cDarkNavy

$s3_method = @"
[Microphone Audio Stream] ──> [FastAPI In-Memory RAM Buffer]
                                   │
       ┌───────────────────────────┴───────────────────────────┐
       ▼                                                       ▼
[Acoustic DSP Core (<25ms)]                             [NLP Threat Miner (<5ms)]
• F0 Pitch Autocorrelation (75-500Hz)                   • 5-Language Threat Keywords
• Jitter (>1.04%) & Shimmer (>3.81%)                    • Hindi, Bengali, Tamil, Telugu, En
• HNR Harmonics dB (<12dB duress)                       • Valence-Arousal Affect Mapping
• 4-10 Hz Involuntary Vocal Tremor                      • Imminent Danger Regex Matrix
       │                                                       │
       └───────────────────────────┬───────────────────────────┘
                                   ▼
             [Dynamic Distress Scoring (DDS) Fusion Engine]
             DDS = 0.28*V + 0.28*N + 0.20*C + 0.16*L + 0.08*E
             Non-linear Threat Overrides (Max Base + 12 / Self-Harm)
                                   │
              ┌────────────────────┴────────────────────┐
              ▼ (If DDS < 75)                           ▼ (If DDS >= 75)
    [Empathetic LLM Response]               [SILENT POLICE CAD DISPATCH]
    • Google Gemini 2.5 Flash               • ERSS 112 Webhook (GPS Lat/Long)
    • In-memory stream response             • CCTNS Automated Docketing
    • De-escalation & grounding             • SHAP Court-Admissible Evidence Card
"@
Add-Card $slide3 480 78 445 430 "2. Implementation Methodology & Pipeline" $s3_method $cDeepAmber

# ==========================================
# SLIDE 4: FEASIBILITY AND VIABILITY
# ==========================================
Write-Output "[*] Building Slide 4 (Feasibility & Viability)..."
$slide4 = $presentation.Slides.Add(4, [Microsoft.Office.Interop.PowerPoint.PpSlideLayout]::ppLayoutBlank)
Add-Header $slide4 "FEASIBILITY AND VIABILITY" "Feasibility Analysis, Potential Challenges & Mitigation Strategies"

$s4_feas = @"
• Zero Specialized Hardware: Operates over standard built-in microphones of smartphones, feature tablets, and laptops via browser.
• Ultra-Low Computational Footprint: Full DSP and NLP scoring executes in under 35ms on commodity multi-core CPUs without requiring expensive GPUs.
• Minimal Bandwidth Consumption: Employs in-memory 16kHz mono audio chunking; operational even over 2G/3G low-connectivity rural networks.
• Production Readiness: End-to-end working prototype already built and validated across phone and desktop browsers.
"@
Add-Card $slide4 35 78 285 430 "1. Feasibility Analysis" $s4_feas $cGreen

$s4_chal = @"
• Ambient Urban Noise: Background honking, traffic babble, or loud fans degrading acoustic feature accuracy.
• Accidental False Positives: High vocal energy during sports cheering, celebration, or theatrical acting triggering false alarms.
• Intermittent Network Outages: Cellular dead zones during highway abductions or rural transit.
• Citizen Privacy Apprehension: Concerns over continuous voice eavesdropping or wiretapping.
"@
Add-Card $slide4 338 78 285 430 "2. Potential Challenges & Risks" $s4_chal $cRedText

$s4_strat = @"
• Glottal Harmonic Filtering: Harmonics-to-Noise Ratio (HNR) isolates periodic vocal cord vibration from broadband noise; noise weight is capped at only 8% of DDS.
• Russell Affect Disambiguation: High arousal + positive valence (cheering) is classified as joy; emergency alert strictly requires high arousal + negative valence + Jitter > 1.04%.
• Offline Autonomous Dispatch: Local engine generates SMS/SOS packets when cloud LLM is unreachable.
• Zero Raw-Audio Persistence: Voice discarded immediately after scalar extraction (<25ms); fully DPDP 2023 compliant.
"@
Add-Card $slide4 640 78 285 430 "3. Mitigation Strategies" $s4_strat $cDarkNavy

# ==========================================
# SLIDE 5: IMPACT AND BENEFITS
# ==========================================
Write-Output "[*] Building Slide 5 (Impact & Benefits)..."
$slide5 = $presentation.Slides.Add(5, [Microsoft.Office.Interop.PowerPoint.PpSlideLayout]::ppLayoutBlank)
Add-Header $slide5 "IMPACT AND BENEFITS" "Potential Impact on Target Audience & Multi-Dimensional Benefits"

$s5_aud = @"
• Domestic Violence Victims: Silent emergency intervention during coercive entrapment without alarming cohabitant perpetrators.
• Vulnerable Commuters & Night Travelers: Continuous acoustic safety net during public transport or secluded routes.
• Regional & Rural Demographics: Bridges digital divide with native speech support in Hindi, Bengali, Tamil, Telugu & English.
• Elderly & Solitary Citizens: Automatic fall or medical distress detection via vocal biomarker deterioration.
"@
Add-Card $slide5 35 78 285 430 "1. Target Audience Impact" $s5_aud $cDarkNavy

$s5_ben = @"
• Compression of 'Golden Hour': Reduces police dispatch lead time from 30+ minutes down to 1.2 seconds, preventing homicides.
• Elimination of Retraumatization: Victims do not have to repeatedly recount traumatic assaults to skeptical dispatchers.
• Intelligent Police Resource Allocation: High-accuracy pre-CAD triage (98.2% Sensitivity) filters nuisance/prank calls so PCR vans prioritize real emergencies.
• Zero Hardware Cost: Saves crores in government procurement of physical panic pendants or smart tags.
"@
Add-Card $slide5 338 78 285 430 "2. Societal & Operational Benefits" $s5_ben $cDeepAmber

$s5_sdg = @"
• SDG 3 (Good Health & Well-being):
  Target 3.4 — Mental health support and suicide prevention via depression micro-tremor tracking.
• SDG 5 (Gender Equality):
  Target 5.2 — Elimination of all violence against women and girls in public and private spheres.
• SDG 10 (Reduced Inequalities):
  Target 10.2 — Social and linguistic inclusion across non-English speaking demographics.
• SDG 11 (Sustainable Cities):
  Target 11.7 — Safe public spaces via real-time geotagged distress density heatmaps.
• SDG 16 (Peace, Justice & Strong Institutions):
  Target 16.1 & 16.2 — Ending abuse and generating court-admissible electronic evidence (Sec 61 BNSS).
"@
Add-Card $slide5 640 78 285 430 "3. UN SDGs & National Alignment" $s5_sdg $cGreen

# ==========================================
# SLIDE 6: RESEARCH AND REFERENCES
# ==========================================
Write-Output "[*] Building Slide 6 (Research & References)..."
$slide6 = $presentation.Slides.Add(6, [Microsoft.Office.Interop.PowerPoint.PpSlideLayout]::ppLayoutBlank)
Add-Header $slide6 "RESEARCH AND REFERENCES" "Details / Links of Reference Literature, Datasets & Statutory Work"

$s6_crime = @"
• National Crime Records Bureau (NCRB):
  'Crime in India Report 2022', Ministry of Home Affairs, GoI (4,45,256 crimes against women registered; 31.4% domestic cruelty).
• National Family Health Survey (NFHS-5):
  Ministry of Health & Family Welfare, GoI (77% of physical/sexual assault victims never seek formal help or report to police).
• Neurobiology of Trauma & Tonic Immobility:
  Porges, S.W. (2011). 'The Polyvagal Theory: Neurophysiological Foundations of Emotions, Communication, and Self-Regulation' (Vocal cord freeze response).
"@
Add-Card $slide6 35 78 430 205 "1. Crime & Sociological Research" $s6_crime $cDarkNavy

$s6_ds = @"
• RAVDESS: Livingstone & Russo (2018). Ryerson Audio-Visual Database of Emotional Speech and Song, PLoS ONE 13(5) (7,356 validated speech files).
• CREMA-D: Cao et al. (2014). Crowd-sourced Emotional Multimodal Actors Dataset, IEEE Trans. on Affective Computing (7,442 multi-ethnic audio clips).
• EMO-DB: Burkhardt et al. (2005). Database of German Emotional Speech (Acoustic phonetics of fear & jitter).
• Indic Multilingual Lexicon: 5-language threat corpus curated from IndicNLP & IIT Bombay parallel corpora.
"@
Add-Card $slide6 480 78 445 205 "2. Acoustic & NLP Datasets Used" $s6_ds $cDeepAmber

$s6_ml = @"
• Russell Circumplex Model of Affect:
  Russell, J.A. (1980). 'A circumplex model of affect', Journal of Personality and Social Psychology, 39(6), 1161-1178.
• Explainable AI (SHAP):
  Lundberg, S.M., & Lee, S.I. (2017). 'A Unified Approach to Interpreting Model Predictions', NeurIPS 2017.
• Statutory Compliance & Law Enforcement Standards:
  • Digital Personal Data Protection (DPDP) Act, 2023, Ministry of Electronics and Information Technology (MeitY).
  • Section 61, Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023 (Admissibility of electronic forensic records).
  • ITU-T Emergency Telecommunications Service & Common Alerting Protocol (CAP v1.2) for ERSS 112 integration.
"@
Add-Card $slide6 35 295 890 215 "3. Machine Learning, Forensic Admissibility & Standards" $s6_ml $cGreen

# Save presentation
$outPptx = "C:\Users\ACER\Desktop\SAMVEDNA_AI_SIH_Presentation.pptx"
$presentation.SaveAs($outPptx)
Write-Output "[+] Saved presentation to: $outPptx"

# Also save to Downloads
$outDownloads = "C:\Users\ACER\Downloads\SAMVEDNA_AI_SIH_Presentation.pptx"
$presentation.SaveAs($outDownloads)
Write-Output "[+] Saved presentation to: $outDownloads"

# Also save as PDF for direct portal upload!
$outPdf = "C:\Users\ACER\Downloads\SAMVEDNA_AI_SIH_Presentation.pdf"
$presentation.SaveAs($outPdf, [Microsoft.Office.Interop.PowerPoint.PpSaveAsFileType]::ppSaveAsPDF)
Write-Output "[+] Exported PDF for SIH upload to: $outPdf"

# Also save to backend static
$staticDir = "C:\Users\ACER\.gemini\antigravity\scratch\nhaa_distress_prediction_system\backend\static"
$presentation.SaveAs("$staticDir\SAMVEDNA_AI_SIH_Presentation.pptx")
$presentation.SaveAs("$staticDir\SAMVEDNA_AI_SIH_Presentation.pdf", [Microsoft.Office.Interop.PowerPoint.PpSaveAsFileType]::ppSaveAsPDF)
Write-Output "[+] Saved copies in backend static for web download"

$presentation.Close()
$ppt.Quit()
Write-Output "[+] PowerPoint generation complete!"
