# UTF-8 with BOM
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
$cSlateDark= 15 + 23*256 + 42*65536      # #0F172A (Headings / bold lead)
$cSlateText= 51 + 65*256 + 85*65536      # #334155 (Slate 700 body text)
$cMutedGray= 100 + 116*256 + 139*65536   # #64748B
$cLightBg  = 248 + 250*256 + 252*65536   # #F8FAFC
$cBorder   = 226 + 232*256 + 240*65536   # #E2E8F0
$cGreen    = 16 + 185*256 + 129*65536    # #10B981
$cRed      = 220 + 38*256 + 38*65536     # #DC2626
$cBlue     = 2 + 132*256 + 199*65536     # #0284C7
$cPurple   = 124 + 58*256 + 237*65536    # #7C3AED

# Soft tint colors for badges
$cSoftAmberBg = 254 + 243*256 + 199*65536 # #FEF3C7
$cSoftSlateBg = 241 + 245*256 + 249*65536 # #F1F5F9

$assetsDir = "D:\SAMVEDNA\extracted_assets"
$bulletChar = [char]0x2022

function Set-Header($slide, $category, $title) {
    # Top banner bar
    $topBar = $slide.Shapes.AddShape(1, 0, 0, 960, 68)
    $topBar.Fill.Solid()
    $topBar.Fill.ForeColor.RGB = $cNavy
    $topBar.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    # Category and PS tag
    $tBox = $slide.Shapes.AddTextbox(1, 35, 8, 720, 20)
    $tBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr = $tBox.TextFrame.TextRange
    $tr.Text = "SMART INDIA HACKATHON 2025 | PROBLEM STATEMENT ID: SIH25042 | $category"
    $tr.Font.Name = "Segoe UI"
    $tr.Font.Size = 10
    $tr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr.Font.Color.RGB = $cAmber

    # Title
    $titleBox = $slide.Shapes.AddTextbox(1, 35, 27, 740, 36)
    $titleBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titler = $titleBox.TextFrame.TextRange
    $titler.Text = $title
    $titler.Font.Name = "Segoe UI"
    $titler.Font.Size = 17
    $titler.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $titler.Font.Color.RGB = $cWhite

    # Right branding badge
    $badge = $slide.Shapes.AddTextbox(1, 770, 14, 160, 40)
    $br = $badge.TextFrame.TextRange
    $br.Text = "DEEPSEQ`r`nTeam STORM SURGE (77056)"
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
    $fr.Text = "SIH 2025 Idea Submission Template | PS ID: SIH25042 | Identifying Taxonomy & Assessing Biodiversity from eDNA Datasets"
    $fr.Font.Name = "Segoe UI"
    $fr.Font.Size = 8
    $fr.Font.Color.RGB = $cMutedGray
}

function Create-Card($slide, $x, $y, $w, $h, $title, $items, $accentColor, $fontSize = 8.8) {
    $card = $slide.Shapes.AddShape(5, $x, $y, $w, $h)
    $card.Fill.Solid()
    $card.Fill.ForeColor.RGB = $cLightBg
    $card.Line.ForeColor.RGB = $accentColor
    $card.Line.Weight = 1.5

    # Header with 22pt left padding and 12pt top padding
    $tBox = $slide.Shapes.AddTextbox(1, ($x + 22), ($y + 12), ($w - 38), 24)
    $tr = $tBox.TextFrame.TextRange
    $tr.Text = $title
    $tr.Font.Name = "Segoe UI"
    $tr.Font.Size = 11.5
    $tr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $tr.Font.Color.RGB = $accentColor

    # Body with 22pt left padding and 38pt top offset
    $bBox = $slide.Shapes.AddTextbox(1, ($x + 22), ($y + 38), ($w - 38), ($h - 48))
    $bBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $trBody = $bBox.TextFrame.TextRange

    $bChar = [char]0x2022
    $fullText = ""
    foreach ($item in $items) {
        if ($item.StartsWith("  -")) {
            $fullText += "$item`r`n"
        } else {
            $fullText += "$bChar $item`r`n"
        }
    }
    $trBody.Text = $fullText.TrimEnd()
    $trBody.Font.Name = "Segoe UI"
    $trBody.Font.Size = $fontSize
    $trBody.Font.Color.RGB = $cSlateText

    # Format bold lead-in for lines with colon and add subtle paragraph spacing
    $pCount = $trBody.Paragraphs().Count
    for ($p = 1; $p -le $pCount; $p++) {
        $para = $trBody.Paragraphs($p)
        $para.ParagraphFormat.SpaceAfter = 3
        $txt = $para.Text
        $colonIdx = $txt.IndexOf(":")
        if ($colonIdx -gt 0) {
            $boldRange = $para.Characters(1, $colonIdx + 1)
            $boldRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
            $boldRange.Font.Color.RGB = $cSlateDark
        }
    }
}

# ==========================================
# SLIDE 1: TITLE PAGE (Faithful to SAMVEDNA Slide 1 composition)
# ==========================================
Write-Host "[*] Building Slide 1 (Title Page)..."
$slide1 = $pres.Slides.Add(1, 12)

$bg1 = $slide1.Shapes.AddShape(1, 0, 0, 960, 540)
$bg1.Fill.Solid()
$bg1.Fill.ForeColor.RGB = $cNavy
$bg1.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

$tBox1 = $slide1.Shapes.AddTextbox(1, 50, 24, 860, 36)
$tr1 = $tBox1.TextFrame.TextRange
$tr1.Text = "SMART INDIA HACKATHON 2025"
$tr1.Font.Name = "Segoe UI"
$tr1.Font.Size = 22
$tr1.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr1.Font.Color.RGB = $cAmber
$tr1.ParagraphFormat.Alignment = 2 # Center

$stBox1 = $slide1.Shapes.AddTextbox(1, 50, 58, 860, 24)
$str1 = $stBox1.TextFrame.TextRange
$str1.Text = "TITLE PAGE -- OFFICIAL IDEA SUBMISSION"
$str1.Font.Name = "Segoe UI"
$str1.Font.Size = 12
$str1.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$str1.Font.Color.RGB = $cWhite
$str1.ParagraphFormat.Alignment = 2

# Main Project Banner Card (Rounded rectangle with Dark Navy fill and AMBER BORDER, matching SAMVEDNA)
$mainCard = $slide1.Shapes.AddShape(5, 50, 92, 860, 96)
$mainCard.Fill.Solid()
$mainCard.Fill.ForeColor.RGB = $cCardNavy
$mainCard.Line.ForeColor.RGB = $cAmber
$mainCard.Line.Weight = 2.5

$pTitleBox = $slide1.Shapes.AddTextbox(1, 60, 100, 840, 42)
$ptr = $pTitleBox.TextFrame.TextRange
$ptr.Text = "DEEPSEQ"
$ptr.Font.Name = "Segoe UI"
$ptr.Font.Size = 28
$ptr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$ptr.Font.Color.RGB = $cAmber
$ptr.ParagraphFormat.Alignment = 2

$pSubBox = $slide1.Shapes.AddTextbox(1, 60, 144, 840, 36)
$psr = $pSubBox.TextFrame.TextRange
$psr.Text = "AI-Powered Marine eDNA Taxonomy Identification and Biodiversity Assessment Platform"
$psr.Font.Name = "Segoe UI"
$psr.Font.Size = 12
$psr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$psr.Font.Color.RGB = $cWhite
$psr.ParagraphFormat.Alignment = 2

# Details White Card (Large rounded rectangle matching SAMVEDNA)
$wCard1 = $slide1.Shapes.AddShape(5, 50, 202, 860, 288)
$wCard1.Fill.Solid()
$wCard1.Fill.ForeColor.RGB = $cWhite
$wCard1.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

$dtBox = $slide1.Shapes.AddTextbox(1, 75, 212, 730, 268)
$dtr = $dtBox.TextFrame.TextRange

$dtList = @(
    "Problem Statement ID: SIH25042",
    "Problem Statement Title: Identifying Taxonomy and Assessing Biodiversity from eDNA Datasets",
    "Target Ecosystem: Marine Biodiversity, Deep-Sea Research & Global Repositories (CMLRE, SILVA, NCBI)",
    "Theme: Miscellaneous (Marine Biotechnology & Ecological Surveillance)",
    "PS Category: Software",
    "Team ID: 77056",
    "Team Name: STORM SURGE",
    "Core Innovation: Alignment-Free Nucleotide Transformers (DNABERT-2) + Unsupervised Novel Taxa Discovery (HDBSCAN)",
    "Beneficiaries: Marine Biologists, Conservation Agencies, Environmental Researchers & Policy Authorities"
)

$dText = ""
foreach ($item in $dtList) {
    $dText += "$bulletChar $item`r`n"
}
$dtr.Text = $dText.TrimEnd()
$dtr.Font.Name = "Segoe UI"
$dtr.Font.Size = 10.6
$dtr.Font.Color.RGB = $cSlateText

$pCountD = $dtr.Paragraphs().Count
for ($p = 1; $p -le $pCountD; $p++) {
    $para = $dtr.Paragraphs($p)
    $para.ParagraphFormat.SpaceAfter = 7
    $txt = $para.Text
    $colonIdx = $txt.IndexOf(":")
    if ($colonIdx -gt 0) {
        $boldRange = $para.Characters(1, $colonIdx + 1)
        $boldRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $boldRange.Font.Color.RGB = $cNavy
    }
}

# Add official SIH logo to top-right of white card
$sihLogo = "$assetsDir\p1_img1_17_181x92.jpeg"
if (Test-Path $sihLogo) {
    $slide1.Shapes.AddPicture($sihLogo, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 810, 216, 85, 45)
}

$f1 = $slide1.Shapes.AddTextbox(1, 50, 498, 860, 22)
$fr1 = $f1.TextFrame.TextRange
$fr1.Text = "Smart India Hackathon 2025 | Idea Submission PPT | Slide 1 of 9 | Team STORM SURGE (77056)"
$fr1.Font.Name = "Segoe UI"
$fr1.Font.Size = 8.5
$fr1.Font.Color.RGB = $cMutedGray
$fr1.ParagraphFormat.Alignment = 2

# ==========================================
# SLIDE 2: PROPOSED SOLUTION (3 Vertical Cards)
# ==========================================
Write-Host "[*] Building Slide 2 (Proposed Solution)..."
$slide2 = $pres.Slides.Add(2, 12)
Set-Header $slide2 "MISCELLANEOUS" "Proposed Solution (Describe your Idea / Solution / Prototype)"

$s2_c1 = @(
    "Incomplete Reference Databases: Causes widespread misclassification and complete failure when identifying uncataloged deep-sea species.",
    "Slow, Manual Pipelines: Traditional bioinformatic alignment workflows require weeks of manual curation to process eDNA datasets.",
    "Prohibitive Compute Costs: Exact sequence matching against terabyte databases requires expensive, specialized HPC clusters.",
    "Fragmented Tooling Workflows: Disconnected command-line utilities for filtering, alignment, clustering, and reporting without a unified platform.",
    "Limited Accessibility: Steep technical barriers exclude field marine biologists, conservation officers, and smaller research laboratories."
)
Create-Card $slide2 35 78 285 430 "1. Currently Faced Problems" $s2_c1 $cNavy 8.8

$s2_c2 = @(
    "AI-Based Sequence Classification: Autonomous deep-learning inference independent of incomplete and brittle reference databases.",
    "100x Faster Processing Velocity: Reduces end-to-end eDNA processing time from weeks to hours via GPU-accelerated embeddings.",
    "Unsupervised Novel Taxa Discovery: Uncovers uncataloged marine species using high-dimensional density clustering (HDBSCAN).",
    "Real-Time Biodiversity Metrics: Computes species richness, Shannon diversity index, and relative abundance distributions instantaneously.",
    "Unified End-to-End Platform: Seamless one-click system for FASTQ file upload, quality trimming, AI inference, and rich visual dashboards.",
    "Accessible to All: Intuitive cloud interface empowering field researchers, students, and conservation bodies to analyze eDNA effortlessly."
)
Create-Card $slide2 338 78 285 430 "2. Detailed Proposed Solution (DEEPSEQ)" $s2_c2 $cDeepAmber 8.8

$s2_c3 = @(
    "Core System Capabilities: Integrated modular ecosystem:",
    "  - AI Classification: DNABERT-2 captures deep sequence grammar.",
    "  - Real-Time Analysis: Rapid batch inference delivers metrics in minutes.",
    "  - Cloud Platform: Serverless architecture eliminates idle costs.",
    "  - Biodiversity Metrics: Automated richness, evenness & abundance.",
    "  - Novelty Discovery: Unsupervised clustering isolates candidate new species.",
    "  - One-Click Pipeline: Complete workflow replacing multi-tool scripts.",
    "End-to-End Workflow: Sample -> Sequencing -> AI Pipeline -> Embedding -> Clustering -> Classification -> Result",
    "Interactive Live Deliverables: Hosted Website (Live Prototype) | Video Demo | Source Code Repository | Figma Interactive UI Design"
)
Create-Card $slide2 640 78 285 430 "3. Innovation & Key Deliverables" $s2_c3 $cGreen 8.7

# ==========================================
# SLIDE 3: TECHNICAL APPROACH (2 Wide Cards)
# ==========================================
Write-Host "[*] Building Slide 3 (Technical Approach)..."
$slide3 = $pres.Slides.Add(3, 12)
Set-Header $slide3 "MISCELLANEOUS" "Technologies to be Used and Implementation Methodology"

$s3_c1 = @(
    "Raw Sequence Ingestion & Quality Filtering: Ingests raw eDNA FASTQ reads. Executes automated quality trimming and adapter removal via fastp (Q > 30) to isolate 18S rRNA / COI marker genes.",
    "Nucleotide Foundation Transformers: Pre-trained DNABERT-2 / Nucleotide Transformer encodes 6-mer DNA tokens into dense 768-dimensional latent vector embeddings without sequence alignment.",
    "Dual-Track Classification & Discovery: Two parallel inference streams:",
    "  - Supervised Stream: Contrastive representation learning (SupCon) cross-referenced with SILVA and NCBI databases for rapid species assignment.",
    "  - Unsupervised Stream: HDBSCAN density clustering groups uncharacterized sequences, isolating candidate novel marine species.",
    "Hierarchical Taxonomy Mapping: Systematic top-down confidence mapping: Domain -> Kingdom -> Phylum -> Class -> Order -> Family -> Genus -> Species.",
    "Downstream Biological Translation: Novel taxa sequences routed for gene extraction, CRISPR exploration, and trait discovery across marine biotechnology."
)
Create-Card $slide3 35 78 430 430 "1. Technologies & Biological Methodology" $s3_c1 $cNavy 8.8

# Right card with clean cropped Flow of Project diagram + Taxonomic cone
$card_s3r = $slide3.Shapes.AddShape(5, 480, 78, 445, 430)
$card_s3r.Fill.Solid()
$card_s3r.Fill.ForeColor.RGB = $cLightBg
$card_s3r.Line.ForeColor.RGB = $cDeepAmber
$card_s3r.Line.Weight = 1.5

$tBox_s3r = $slide3.Shapes.AddTextbox(1, 506, 90, 400, 24)
$tr_s3r = $tBox_s3r.TextFrame.TextRange
$tr_s3r.Text = "2. Implementation Methodology & Pipeline"
$tr_s3r.Font.Name = "Segoe UI"
$tr_s3r.Font.Size = 11.5
$tr_s3r.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s3r.Font.Color.RGB = $cDeepAmber

$flowCleanImg = "$assetsDir\p3_flow_clean.png"
$coneImg      = "$assetsDir\p3_img3_108_273x574.jpeg"

if (Test-Path $flowCleanImg) {
    $slide3.Shapes.AddPicture($flowCleanImg, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 504, 116, 280, 255)
}
if (Test-Path $coneImg) {
    $slide3.Shapes.AddPicture($coneImg, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 792, 116, 120, 255)
}

$s3_steps = $slide3.Shapes.AddTextbox(1, 504, 380, 408, 120)
$s3_steps.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$s3_sr = $s3_steps.TextFrame.TextRange
$s3_sr.Text = "$bulletChar Step 1 (Sampling & Sequencing): Marine water collection & high-throughput eDNA sequencing.`r`n$bulletChar Step 2 (Quality Filtering): fastp trims adapter noise and isolates target marker genes.`r`n$bulletChar Step 3 (Transformer Embeddings): DNABERT-2 generates dense sequence vector representations.`r`n$bulletChar Step 4 (Clustering & Novelty): HDBSCAN groups biological homology and isolates novel taxa.`r`n$bulletChar Step 5 (Biodiversity Dashboard): Real-time abundance curves and interactive geospatial heatmaps."
$s3_sr.Font.Name = "Segoe UI"
$s3_sr.Font.Size = 8.5
$s3_sr.Font.Color.RGB = $cSlateText

$pCountS3 = $s3_sr.Paragraphs().Count
for ($p = 1; $p -le $pCountS3; $p++) {
    $para = $s3_sr.Paragraphs($p)
    $para.ParagraphFormat.SpaceAfter = 2
    $txt = $para.Text
    $colonIdx = $txt.IndexOf(":")
    if ($colonIdx -gt 0) {
        $boldRange = $para.Characters(1, $colonIdx + 1)
        $boldRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $boldRange.Font.Color.RGB = $cSlateDark
    }
}

# ==========================================
# SLIDE 4: FEASIBILITY AND VIABILITY (3 Vertical Cards)
# ==========================================
Write-Host "[*] Building Slide 4 (Feasibility & Viability)..."
$slide4 = $pres.Slides.Add(4, 12)
Set-Header $slide4 "MISCELLANEOUS" "Feasibility Analysis, Potential Challenges & Mitigation Strategies"

$s4_c1 = @(
    "AI/ML Foundation Viability: Proven efficacy of transformer architectures for genomics; abundant open datasets on NCBI SRA, SILVA, and CMLRE for training and validation.",
    "Mature Bioinformatics Ecosystem: Robust integration with established open-source tools (fastp, BioPython, PyTorch, FAISS, HDBSCAN).",
    "Severe Cost Reduction: 90%+ cheaper than manual outsourced bioinformatics consulting and commercial Sanger/NGS software licenses.",
    "Scalable Serverless Compute: Cloud GPU autoscaling handles terabyte-scale environmental metagenomics datasets with zero idle compute costs.",
    "Operational Feasibility: Designed for field researchers; simple web/mobile UI requires no command-line bioinformatics expertise."
)
Create-Card $slide4 35 78 285 430 "1. Feasibility Analysis" $s4_c1 $cGreen 8.8

$s4_c2 = @(
    "Machine Learning Accuracy: Risk of false taxonomic assignments when processing degraded eDNA fragments or PCR amplification artifacts.",
    "Severe Reference Database Gaps: 80%+ of deep-sea marine organisms remain unsequenced, causing traditional alignment tools to fail completely.",
    "Data Availability & Quality: Marine field samples contain chimeric sequences, primer dimers, and extreme variations in read quality.",
    "Metagenomic Scalability & Latency: Processing multi-gigabyte FASTQ files containing tens of millions of reads risks memory overflow."
)
Create-Card $slide4 338 78 285 430 "2. Potential Challenges & Risks" $s4_c2 $cRed 8.8

$s4_c3 = @(
    "Contrastive DNA Pattern Learning: SupCon trains models to identify biological grammar rather than exact string matches, ensuring resilience on degraded fragments.",
    "Unsupervised Novel Taxa Discovery: Density-based clustering (HDBSCAN) isolates unknown species into distinct taxonomic clusters without requiring known references.",
    "Automated Preprocessing & Filtering: Rigorous fastp pipeline trims low-confidence bases (Q<30) and filters chimera sequences before model inference.",
    "Alignment-Free Vector Indexing: Replaces slow sequence alignment with FAISS vector indexing, delivering O(1) similarity lookups in milliseconds.",
    "Multi-Source Taxonomic Consensus: Integrates cross-checks across SILVA, NCBI, and CMLRE records to ensure validated, consistent taxonomic labeling."
)
Create-Card $slide4 640 78 285 430 "3. Mitigation Strategies" $s4_c3 $cNavy 8.8

# ==========================================
# SLIDE 5: IMPACT AND BENEFITS (3 Vertical Cards)
# ==========================================
Write-Host "[*] Building Slide 5 (Impact & Benefits)..."
$slide5 = $pres.Slides.Add(5, 12)
Set-Header $slide5 "MISCELLANEOUS" "Potential Impact on Target Audience & Multi-Dimensional Benefits"

$s5_c1 = @(
    "Marine Biologists & Oceanographers: Accelerates species identification 100x directly from seawater samples, bypassing destructive bottom-trawling and manual morphology.",
    "Ecological & Conservation Agencies: Provides automated early-warning monitoring for endangered species, invasive marine organisms, and ecosystem collapse signals.",
    "Universities & Academic Labs: Lowers the financial barrier of bioinformatics research, enabling smaller collegiate institutions without supercomputers to analyze eDNA.",
    "Policy Makers & Marine Authorities: Supplies quantifiable, verifiable biodiversity indices to support Marine Protected Area (MPA) designations and maritime policy compliance."
)
Create-Card $slide5 35 78 285 430 "1. Target Audience Impact" $s5_c1 $cNavy 8.8

$s5_c2 = @(
    "100x Faster Turnaround: Reduces analysis turnaround from weeks down to hours, enabling real-time ecological decision-making on research vessels.",
    "Unprecedented Novel Species Discovery: First-of-its-kind unsupervised discovery pipeline uncovering previously invisible, unculturable deep-sea marine biodiversity.",
    "Database-Independent Resilience: Maintains high classification performance even in unexplored oceanic trenches where reference genomes do not exist.",
    "Unified Metagenomic Platform: Single end-to-end web portal replacing 5+ fragmented CLI tools for QC, embedding, clustering, and biodiversity dashboarding.",
    "Economic Cost Elimination: Dramatically cuts sequencing interpretation costs, freeing budgetary funds for field conservation expeditions."
)
Create-Card $slide5 338 78 285 430 "2. Solution Benefits & Advantages" $s5_c2 $cDeepAmber 8.8

$s5_c3 = @(
    "UN SDG 14 (Life Below Water):",
    "  - Target 14.2: Sustainably manage and protect marine ecosystems to avoid significant adverse impacts.",
    "  - Target 14.a: Increase scientific knowledge, research capacity, and marine technology transfer.",
    "UN SDG 13 (Climate Action): Continuous biomonitoring detects climate-driven marine migrations, coral bleaching impacts, and ocean acidification stresses.",
    "UN SDG 15 (Life on Land & Freshwaters): Versatile architecture easily extends to freshwater rivers, lakes, and endangered wetland biomes.",
    "Global Research Collaboration: Standardizes biodiversity data formats (Darwin Core / CSV / JSON) for seamless global scientific exchange."
)
Create-Card $slide5 640 78 285 430 "3. UN SDGs & Global Alignment" $s5_c3 $cGreen 8.7

# ==========================================
# SLIDE 6: TECHNICAL PIPELINE (2 Cards - Cluster Analysis & 6-Stage Diagram)
# ==========================================
Write-Host "[*] Building Slide 6 (Technical Pipeline)..."
$slide6 = $pres.Slides.Add(6, 12)
Set-Header $slide6 "MISCELLANEOUS" "Technical Pipeline and Deep Learning Architecture"

# Left Card: High-Dimensional eDNA Embeddings Cluster Analysis
$card_s6l = $slide6.Shapes.AddShape(5, 35, 78, 430, 430)
$card_s6l.Fill.Solid()
$card_s6l.Fill.ForeColor.RGB = $cLightBg
$card_s6l.Line.ForeColor.RGB = $cNavy
$card_s6l.Line.Weight = 1.5

$tBox_s6l = $slide6.Shapes.AddTextbox(1, 62, 90, 390, 24)
$tr_s6l = $tBox_s6l.TextFrame.TextRange
$tr_s6l.Text = "1. High-Dimensional eDNA Embeddings Cluster Analysis"
$tr_s6l.Font.Name = "Segoe UI"
$tr_s6l.Font.Size = 11.5
$tr_s6l.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s6l.Font.Color.RGB = $cNavy

$cluster2DImg = "$assetsDir\p6_img4_167_1600x744.jpeg"
$cluster3DImg = "$assetsDir\p6_img5_168_555x504.jpeg"

if (Test-Path $cluster2DImg) {
    $slide6.Shapes.AddPicture($cluster2DImg, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 56, 116, 388, 185)
}
if (Test-Path $cluster3DImg) {
    $slide6.Shapes.AddPicture($cluster3DImg, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 56, 310, 150, 145)
}

$capBox_s6 = $slide6.Shapes.AddTextbox(1, 215, 310, 235, 185)
$capBox_s6.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$cr_s6 = $capBox_s6.TextFrame.TextRange
$cr_s6.Text = "$bulletChar Latent Space Clustering: Nucleotide transformer encodes DNA sequences into 768-dim embeddings indexed via Qdrant/FAISS.`r`n`r`n$bulletChar Novelty Isolation: Outlier clusters with high biological cohesion but low database similarity are flagged as putative novel marine taxa."
$cr_s6.Font.Name = "Segoe UI"
$cr_s6.Font.Size = 8.5
$cr_s6.Font.Color.RGB = $cSlateText

$pCountS6 = $cr_s6.Paragraphs().Count
for ($p = 1; $p -le $pCountS6; $p++) {
    $para = $cr_s6.Paragraphs($p)
    $txt = $para.Text
    $colonIdx = $txt.IndexOf(":")
    if ($colonIdx -gt 0) {
        $boldRange = $para.Characters(1, $colonIdx + 1)
        $boldRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $boldRange.Font.Color.RGB = $cSlateDark
    }
}

# Right Card: 6-Stage End-to-End Processing Pipeline (with embedded diagram)
$card_s6r = $slide6.Shapes.AddShape(5, 480, 78, 445, 430)
$card_s6r.Fill.Solid()
$card_s6r.Fill.ForeColor.RGB = $cLightBg
$card_s6r.Line.ForeColor.RGB = $cDeepAmber
$card_s6r.Line.Weight = 1.5

$tBox_s6r = $slide6.Shapes.AddTextbox(1, 506, 90, 405, 24)
$tr_s6r = $tBox_s6r.TextFrame.TextRange
$tr_s6r.Text = "2. 6-Stage Technical Pipeline & Architecture"
$tr_s6r.Font.Name = "Segoe UI"
$tr_s6r.Font.Size = 11.5
$tr_s6r.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s6r.Font.Color.RGB = $cDeepAmber

$pipeImg = "$assetsDir\p6_img3_166_2048x1430.jpeg"
if (Test-Path $pipeImg) {
    $slide6.Shapes.AddPicture($pipeImg, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 502, 116, 402, 285)
}

$pipeDescBox = $slide6.Shapes.AddTextbox(1, 506, 412, 405, 85)
$pipeDescBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$pdr_s6 = $pipeDescBox.TextFrame.TextRange
$pdr_s6.Text = "$bulletChar End-to-End Execution: Objectives -> Data Preparation (fastp) -> Model Processing (DNABERT-2 / HDBSCAN) -> Analysis & Interpretation -> Dashboard & Insights -> Cloud Deployment (AWS / GCP)."
$pdr_s6.Font.Name = "Segoe UI"
$pdr_s6.Font.Size = 8.5
$pdr_s6.Font.Color.RGB = $cSlateText

$pCountP = $pdr_s6.Paragraphs().Count
for ($p = 1; $p -le $pCountP; $p++) {
    $para = $pdr_s6.Paragraphs($p)
    $txt = $para.Text
    $colonIdx = $txt.IndexOf(":")
    if ($colonIdx -gt 0) {
        $boldRange = $para.Characters(1, $colonIdx + 1)
        $boldRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $boldRange.Font.Color.RGB = $cSlateDark
    }
}

# ==========================================
# SLIDE 7: RESEARCH AND REFERENCES (2 Top Cards + 1 Wide Bottom Card)
# ==========================================
Write-Host "[*] Building Slide 7 (Research & References)..."
$slide7 = $pres.Slides.Add(7, 12)
Set-Header $slide7 "MISCELLANEOUS" "Details / Links of Reference Literature, Datasets & Statutory Work"

$s7_c1 = @(
    "Nucleotide Transformer Foundation Models: Dalla-Torre, H., et al. (2024). 'Nucleotide Transformer: Building and evaluating foundation models for genomics', Nature Methods, 21(2), 246-256. [doi:10.1038/s41592-024-02523-z]",
    "Hierarchical Density-Based Clustering (HDBSCAN): McInnes, L., Healy, J., & Astels, S. (2017). 'hdbscan: Hierarchical density based clustering for data science', Journal of Open Source Software, 2(11), 205. [https://hdbscan.readthedocs.io]",
    "Contrastive Learning in Genomics: Zheng et al. (2025). 'Self-supervised contrastive learning on foundation genomic models for alignment-free metagenomics', arXiv:2509.25274."
)
Create-Card $slide7 35 78 430 205 "1. Genomic Foundation Models & Machine Learning" $s7_c1 $cNavy 8.6

$s7_c2 = @(
    "Centre for Marine Living Resources & Ecology (CMLRE): Ministry of Earth Sciences, Govt. of India -- Ongoing Indian Ocean deep-sea biodiversity and marine eDNA sampling cruises.",
    "SILVA Ribosomal RNA Database Project: Curated, high-quality ribosomal RNA sequence database (18S / 16S / 28S) for taxonomic validation and tree calibration. [https://www.arb-silva.de]",
    "NCBI GenBank Taxonomy Database: National Center for Biotechnology Information comprehensive genetic sequence repository and global taxonomic backbone. [https://www.ncbi.nlm.nih.gov]"
)
Create-Card $slide7 480 78 445 205 "2. Reference Databases & Institutional Framework" $s7_c2 $cDeepAmber 8.6

# Bottom Card: Stakeholder Validation & Community Survey Statistics
$card_s7b = $slide7.Shapes.AddShape(5, 35, 295, 890, 212)
$card_s7b.Fill.Solid()
$card_s7b.Fill.ForeColor.RGB = $cLightBg
$card_s7b.Line.ForeColor.RGB = $cGreen
$card_s7b.Line.Weight = 1.5

$tBox_s7b = $slide7.Shapes.AddTextbox(1, 62, 307, 845, 24)
$tr_s7b = $tBox_s7b.TextFrame.TextRange
$tr_s7b.Text = "3. Stakeholder Validation & Community Survey Statistics"
$tr_s7b.Font.Name = "Segoe UI"
$tr_s7b.Font.Size = 11.5
$tr_s7b.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s7b.Font.Color.RGB = $cGreen

$s1_desc = $slide7.Shapes.AddTextbox(1, 62, 335, 225, 95)
$s1_desc.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$s1_dr = $s1_desc.TextFrame.TextRange
$s1_dr.Text = "$bulletChar Survey Question 1:`r`nDo you think monitoring biodiversity is important for protecting ecosystems?`r`n`r`nResult: 95.6% YES | 4.4% NO"
$s1_dr.Font.Name = "Segoe UI"
$s1_dr.Font.Size = 8.8
$s1_dr.Font.Color.RGB = $cSlateText

$pie1Img = "$assetsDir\p7_img3_185_1200x742.jpeg"
if (Test-Path $pie1Img) {
    $slide7.Shapes.AddPicture($pie1Img, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 295, 335, 140, 86)
}

$s2_desc = $slide7.Shapes.AddTextbox(1, 496, 335, 235, 95)
$s2_desc.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$s2_dr = $s2_desc.TextFrame.TextRange
$s2_dr.Text = "$bulletChar Survey Question 2:`r`nDo you think eDNA can help detect endangered or invasive species early?`r`n`r`nResult: 96.0% YES | 4.0% NO"
$s2_dr.Font.Name = "Segoe UI"
$s2_dr.Font.Size = 8.8
$s2_dr.Font.Color.RGB = $cSlateText

$pie2Img = "$assetsDir\p7_img4_186_1200x742.jpeg"
if (Test-Path $pie2Img) {
    $slide7.Shapes.AddPicture($pie2Img, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 740, 335, 140, 86)
}

$s7_insight = $slide7.Shapes.AddTextbox(1, 62, 438, 845, 58)
$s7_insight.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$s7_ir = $s7_insight.TextFrame.TextRange
$s7_ir.Text = "$bulletChar Validation Insight: Overwhelming scientific and public consensus (>95%) confirms the critical necessity of automated, non-invasive eDNA biodiversity surveillance systems for conservation management."
$s7_ir.Font.Name = "Segoe UI"
$s7_ir.Font.Size = 8.8
$s7_ir.Font.Color.RGB = $cMutedGray

# ==========================================
# SLIDE 8: UI SCREENS & PROTOTYPE (Web 2x2 & Mobile 3-in-Row)
# ==========================================
Write-Host "[*] Building Slide 8 (UI Screens)..."
$slide8 = $pres.Slides.Add(8, 12)
Set-Header $slide8 "MISCELLANEOUS" "Prototype UI & Application Showcase (Web & Mobile)"

# Left Card: Web Platform
$card_s8l = $slide8.Shapes.AddShape(5, 35, 78, 520, 430)
$card_s8l.Fill.Solid()
$card_s8l.Fill.ForeColor.RGB = $cLightBg
$card_s8l.Line.ForeColor.RGB = $cNavy
$card_s8l.Line.Weight = 1.5

$tBox_s8l = $slide8.Shapes.AddTextbox(1, 62, 90, 475, 24)
$tr_s8l = $tBox_s8l.TextFrame.TextRange
$tr_s8l.Text = "1. Web Platform (Researcher & Laboratory Portal)"
$tr_s8l.Font.Name = "Segoe UI"
$tr_s8l.Font.Size = 11.5
$tr_s8l.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s8l.Font.Color.RGB = $cNavy

$wImg1 = "$assetsDir\p8_img4_203_1600x793.jpeg"
$wImg2 = "$assetsDir\p8_img5_204_1600x783.jpeg"
$wImg3 = "$assetsDir\p8_img7_206_1600x777.jpeg"
$wImg4 = "$assetsDir\p8_img8_207_1600x771.jpeg"

if (Test-Path $wImg1) { $slide8.Shapes.AddPicture($wImg1, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 56, 116, 236, 118) }
if (Test-Path $wImg2) { $slide8.Shapes.AddPicture($wImg2, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 298, 116, 236, 118) }
if (Test-Path $wImg3) { $slide8.Shapes.AddPicture($wImg3, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 56, 242, 236, 118) }
if (Test-Path $wImg4) { $slide8.Shapes.AddPicture($wImg4, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 298, 242, 236, 118) }

$wDescBox = $slide8.Shapes.AddTextbox(1, 56, 372, 480, 125)
$wDescBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$wdr = $wDescBox.TextFrame.TextRange
$wdr.Text = "$bulletChar Web Researcher Portal Capabilities:`r`n  - Drag-and-drop FASTQ upload with automated metadata verification`r`n  - 3D UMAP embedding scatter visualizer (1,000+ points colored by taxa)`r`n  - Rank-Abundance curves and automated Novelty Inspector bar charts`r`n  - Hierarchical taxonomy tree browser & geospatial biodiversity heatmaps"
$wdr.Font.Name = "Segoe UI"
$wdr.Font.Size = 8.8
$wdr.Font.Color.RGB = $cSlateText

$pCountW = $wdr.Paragraphs().Count
for ($p = 1; $p -le $pCountW; $p++) {
    $para = $wdr.Paragraphs($p)
    $txt = $para.Text
    $colonIdx = $txt.IndexOf(":")
    if ($colonIdx -gt 0) {
        $boldRange = $para.Characters(1, $colonIdx + 1)
        $boldRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $boldRange.Font.Color.RGB = $cSlateDark
    }
}

# Right Card: Mobile App
$card_s8r = $slide8.Shapes.AddShape(5, 570, 78, 355, 430)
$card_s8r.Fill.Solid()
$card_s8r.Fill.ForeColor.RGB = $cLightBg
$card_s8r.Line.ForeColor.RGB = $cBlue
$card_s8r.Line.Weight = 1.5

$tBox_s8r = $slide8.Shapes.AddTextbox(1, 592, 90, 315, 24)
$tr_s8r = $tBox_s8r.TextFrame.TextRange
$tr_s8r.Text = "2. Mobile App (Field Observer)"
$tr_s8r.Font.Name = "Segoe UI"
$tr_s8r.Font.Size = 11.5
$tr_s8r.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s8r.Font.Color.RGB = $cBlue

$mImg1 = "$assetsDir\p8_img1_200_922x2048.jpeg"
$mImg2 = "$assetsDir\p8_img2_201_922x2048.jpeg"
$mImg3 = "$assetsDir\p8_img3_202_720x1600.jpeg"

if (Test-Path $mImg1) { $slide8.Shapes.AddPicture($mImg1, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 586, 116, 102, 242) }
if (Test-Path $mImg2) { $slide8.Shapes.AddPicture($mImg2, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 696, 116, 102, 242) }
if (Test-Path $mImg3) { $slide8.Shapes.AddPicture($mImg3, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoTrue, 806, 116, 102, 242) }

$mDescBox = $slide8.Shapes.AddTextbox(1, 586, 372, 323, 125)
$mDescBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
$mdr = $mDescBox.TextFrame.TextRange
$mdr.Text = "$bulletChar Mobile Field Observer Capabilities:`r`n  - Lightweight mobile dashboard for research vessels and field stations`r`n  - Base-level ATCG sequence inspection with real-time match confidence`r`n  - Live GPS biodiversity logging and instant novelty alerts in the field"
$mdr.Font.Name = "Segoe UI"
$mdr.Font.Size = 8.8
$mdr.Font.Color.RGB = $cSlateText

$pCountM = $mdr.Paragraphs().Count
for ($p = 1; $p -le $pCountM; $p++) {
    $para = $mdr.Paragraphs($p)
    $txt = $para.Text
    $colonIdx = $txt.IndexOf(":")
    if ($colonIdx -gt 0) {
        $boldRange = $para.Characters(1, $colonIdx + 1)
        $boldRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        $boldRange.Font.Color.RGB = $cSlateDark
    }
}

# ==========================================
# SLIDE 9: TECH STACK & TEAM DETAILS (Structured 4-Col Stack + 6 Member Cards)
# ==========================================
Write-Host "[*] Building Slide 9 (Tech Stack & Team)..."
$slide9 = $pres.Slides.Add(9, 12)
Set-Header $slide9 "MISCELLANEOUS" "Technology Stack & Team Credentials"

# Top Card: Tech Stack Architecture
$card_s9t = $slide9.Shapes.AddShape(5, 35, 78, 890, 195)
$card_s9t.Fill.Solid()
$card_s9t.Fill.ForeColor.RGB = $cLightBg
$card_s9t.Line.ForeColor.RGB = $cDeepAmber
$card_s9t.Line.Weight = 1.5

$tBox_s9t = $slide9.Shapes.AddTextbox(1, 62, 90, 845, 24)
$tr_s9t = $tBox_s9t.TextFrame.TextRange
$tr_s9t.Text = "1. Full-Stack Architecture & Technology Stack"
$tr_s9t.Font.Name = "Segoe UI"
$tr_s9t.Font.Size = 11.5
$tr_s9t.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s9t.Font.Color.RGB = $cDeepAmber

$techCol1 = $slide9.Shapes.AddTextbox(1, 56, 116, 205, 145)
$tc1_r = $techCol1.TextFrame.TextRange
$tc1_r.Text = "Backend & APIs:`r`n$bulletChar FastAPI (Async REST)`r`n$bulletChar Alembic (Migrations)`r`n$bulletChar Redis Cache (In-Memory)`r`n$bulletChar Apache Kafka (Streaming)`r`n$bulletChar Pub-Sub Architecture`r`n$bulletChar Amazon S3 (FASTQ Storage)"
$tc1_r.Font.Name = "Segoe UI"
$tc1_r.Font.Size = 8.8
$tc1_r.Font.Color.RGB = $cSlateText

$techCol2 = $slide9.Shapes.AddTextbox(1, 270, 116, 205, 145)
$tc2_r = $techCol2.TextFrame.TextRange
$tc2_r.Text = "Machine Learning Core:`r`n$bulletChar DNABERT-2 Transformer`r`n$bulletChar HDBSCAN (Density Cluster)`r`n$bulletChar SupCon (Contrastive AI)`r`n$bulletChar PyTorch Deep Learning`r`n$bulletChar HuggingFace Models`r`n$bulletChar FAISS Vector Engine"
$tc2_r.Font.Name = "Segoe UI"
$tc2_r.Font.Size = 8.8
$tc2_r.Font.Color.RGB = $cSlateText

$techCol3 = $slide9.Shapes.AddTextbox(1, 490, 116, 205, 145)
$tc3_r = $techCol3.TextRange
if ($null -eq $tc3_r) { $tc3_r = $techCol3.TextFrame.TextRange }
$tc3_r.Text = "Frontend & Mobile:`r`n$bulletChar Next.js 14 (React)`r`n$bulletChar TypeScript (Strict Typing)`r`n$bulletChar Tailwind CSS (Styling)`r`n$bulletChar ShadCN UI Components`r`n$bulletChar React Native (Mobile App)`r`n$bulletChar Chart.js Visualizations"
$tc3_r.Font.Name = "Segoe UI"
$tc3_r.Font.Size = 8.8
$tc3_r.Font.Color.RGB = $cSlateText

$techCol4 = $slide9.Shapes.AddTextbox(1, 710, 116, 205, 145)
$tc4_r = $techCol4.TextFrame.TextRange
$tc4_r.Text = "DevOps & Cloud:`r`n$bulletChar AWS Serverless Lambda`r`n$bulletChar Modal (Serverless GPU)`r`n$bulletChar AWS SageMaker Pipelines`r`n$bulletChar Docker Containers`r`n$bulletChar Kubernetes Orchestration`r`n$bulletChar CI/CD Automation"
$tc4_r.Font.Name = "Segoe UI"
$tc4_r.Font.Size = 8.8
$tc4_r.Font.Color.RGB = $cSlateText

# Bold the category titles for the 4 tech columns
foreach ($tc in @($tc1_r, $tc2_r, $tc3_r, $tc4_r)) {
    $firstLine = $tc.Paragraphs(1)
    $firstLine.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $firstLine.Font.Color.RGB = $cNavy
}

# Bottom Card: Team STORM SURGE Credentials
$card_s9b = $slide9.Shapes.AddShape(5, 35, 285, 890, 222)
$card_s9b.Fill.Solid()
$card_s9b.Fill.ForeColor.RGB = $cLightBg
$card_s9b.Line.ForeColor.RGB = $cNavy
$card_s9b.Line.Weight = 1.5

$tBox_s9b = $slide9.Shapes.AddTextbox(1, 62, 297, 845, 24)
$tr_s9b = $tBox_s9b.TextFrame.TextRange
$tr_s9b.Text = "2. Team STORM SURGE (Team ID: 77056) -- Multi-Disciplinary Credentials"
$tr_s9b.Font.Name = "Segoe UI"
$tr_s9b.Font.Size = 11.5
$tr_s9b.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
$tr_s9b.Font.Color.RGB = $cNavy

$members = @(
    @{ Name="ANISH SINGH CHAUHAN"; Role="TEAM LEADER"; Degree="B.Tech CSE (DS)`r`n3rd Year"; Domain="Domain: Backend Dev"; Color=$cNavy; IsLeader=$true },
    @{ Name="TRIPTI SHARMA"; Role="TEAM MEMBER"; Degree="B.Tech CSIT`r`n3rd Year"; Domain="Domain: UI/UX Design"; Color=$cDeepAmber; IsLeader=$false },
    @{ Name="KARTIKAY SINGH"; Role="TEAM MEMBER"; Degree="B.Tech CSE (AIML)`r`n3rd Year"; Domain="Domain: Frontend Dev"; Color=$cBlue; IsLeader=$false },
    @{ Name="APURVI KANAUJIA"; Role="TEAM MEMBER"; Degree="B.Tech IT`r`n3rd Year"; Domain="Domain: UX Designer"; Color=$cGreen; IsLeader=$false },
    @{ Name="NAVYA GUPTA"; Role="TEAM MEMBER"; Degree="B.Tech CSE`r`n3rd Year"; Domain="Domain: Frontend Dev"; Color=$cPurple; IsLeader=$false },
    @{ Name="DIVYANSH VERMA"; Role="TEAM MEMBER"; Degree="B.Tech CSE`r`n3rd Year"; Domain="Domain: Backend Dev"; Color=$cRed; IsLeader=$false }
)

$startX = 51
$memW = 136
$gap = 8

for ($i = 0; $i -lt $members.Count; $i++) {
    $m = $members[$i]
    $mx = $startX + $i * ($memW + $gap)
    $my = 328

    # Individual Member Card
    $mc = $slide9.Shapes.AddShape(5, $mx, $my, $memW, 166)
    $mc.Fill.Solid()
    $mc.Fill.ForeColor.RGB = $cWhite
    $mc.Line.ForeColor.RGB = $m.Color
    $mc.Line.Weight = 1.2

    # Header pill badge
    $badgeBox = $slide9.Shapes.AddShape(5, ($mx + 8), ($my + 10), ($memW - 16), 20)
    $badgeBox.Fill.Solid()
    if ($m.IsLeader) {
        $badgeBox.Fill.ForeColor.RGB = $cSoftAmberBg
        $badgeBox.Line.ForeColor.RGB = $cAmber
    } else {
        $badgeBox.Fill.ForeColor.RGB = $cSoftSlateBg
        $badgeBox.Line.ForeColor.RGB = $cBorder
    }
    $badgeBox.Line.Weight = 0.8
    
    $bTr = $badgeBox.TextFrame.TextRange
    $bTr.Text = $m.Role
    $bTr.Font.Name = "Segoe UI"
    $bTr.Font.Size = 7.5
    $bTr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    if ($m.IsLeader) {
        $bTr.Font.Color.RGB = $cDeepAmber
    } else {
        $bTr.Font.Color.RGB = $cSlateDark
    }
    $bTr.ParagraphFormat.Alignment = 2 # Center

    # Member Name
    $nameBox = $slide9.Shapes.AddTextbox(1, ($mx + 4), ($my + 36), ($memW - 8), 38)
    $nameBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $nr = $nameBox.TextFrame.TextRange
    $nr.Text = $m.Name
    $nr.Font.Name = "Segoe UI"
    $nr.Font.Size = 8.5
    $nr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $nr.Font.Color.RGB = $cNavy
    $nr.ParagraphFormat.Alignment = 2

    # Degree & Year
    $degBox = $slide9.Shapes.AddTextbox(1, ($mx + 4), ($my + 74), ($memW - 8), 36)
    $degBox.TextFrame.WordWrap = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $dr = $degBox.TextFrame.TextRange
    $dr.Text = $m.Degree
    $dr.Font.Name = "Segoe UI"
    $dr.Font.Size = 7.8
    $dr.Font.Color.RGB = $cMutedGray
    $dr.ParagraphFormat.Alignment = 2

    # Domain Pill at bottom
    $domBox = $slide9.Shapes.AddShape(5, ($mx + 6), ($my + 124), ($memW - 12), 26)
    $domBox.Fill.Solid()
    $domBox.Fill.ForeColor.RGB = $cLightBg
    $domBox.Line.ForeColor.RGB = $m.Color
    $domBox.Line.Weight = 0.8

    $dmr = $domBox.TextFrame.TextRange
    $dmr.Text = $m.Domain
    $dmr.Font.Name = "Segoe UI"
    $dmr.Font.Size = 7.2
    $dmr.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $dmr.Font.Color.RGB = $m.Color
    $dmr.ParagraphFormat.Alignment = 2
}

# ==========================================
# EXPORT & SAVE
# ==========================================
Write-Host "[*] Saving Presentation to Destinations..."

$destWorkspacePptx = "D:\SAMVEDNA\Storm_Surge_DEEPSEQ_SIH_Presentation.pptx"
$destDownloadsPptx = "C:\Users\hp\Downloads\Storm_Surge_DEEPSEQ_SIH_Presentation.pptx"

$destWorkspacePdf  = "D:\SAMVEDNA\Storm_Surge_DEEPSEQ_SIH_Presentation.pdf"
$destDownloadsPdf  = "C:\Users\hp\Downloads\Storm_Surge_DEEPSEQ_SIH_Presentation.pdf"

# Save PPTX
$pres.SaveAs($destWorkspacePptx)
Write-Host "[+] Saved PPTX to: $destWorkspacePptx"

$pres.SaveAs($destDownloadsPptx)
Write-Host "[+] Saved PPTX to: $destDownloadsPptx"

# Save PDF (Directly uploadable to SIH portal)
$pres.SaveAs($destWorkspacePdf, 32) # 32 = ppSaveAsPDF
Write-Host "[+] Exported PDF to: $destWorkspacePdf"

$pres.SaveAs($destDownloadsPdf, 32)
Write-Host "[+] Exported PDF to: $destDownloadsPdf"

$pres.Close()
$ppt.Quit()
Write-Host "[+] All SIH Presentation files generated successfully!"
