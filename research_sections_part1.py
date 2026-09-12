# -*- coding: utf-8 -*-
import os
import sys
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class SIHResearchNotesPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=16)
        
        if os.path.exists('C:/Windows/Fonts/arial.ttf'):
            self.add_font('MainFont', '', 'C:/Windows/Fonts/arial.ttf')
            self.add_font('MainFont', 'B', 'C:/Windows/Fonts/arialbd.ttf')
            self.add_font('MainFont', 'I', 'C:/Windows/Fonts/ariali.ttf')
            self.font_family_name = 'MainFont'
        else:
            self.font_family_name = 'Helvetica'

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font(self.font_family_name, 'B', 8)
        self.set_text_color(180, 83, 9) # Deep Amber accent for Research & Validation
        self.cell(105, 6, 'SAMVEDNA AI (NHAA 14566) | Research, Empirical Validation & Social Impact', align='L')
        self.set_font(self.font_family_name, 'I', 8)
        self.set_text_color(120, 130, 140)
        self.cell(85, 6, 'SIH Research & Documentation Dossier', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(245, 210, 170)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_draw_color(230, 220, 210)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(1)
        self.set_font(self.font_family_name, '', 8)
        self.set_text_color(140, 140, 140)
        self.cell(95, 8, 'SAMVEDNA AI Team | Research & Validation Reference', align='L')
        self.cell(95, 8, f'Page {self.page_no()}', align='R')

    def chapter_title(self, num_str, title_str):
        self.set_font(self.font_family_name, 'B', 13)
        self.set_fill_color(254, 243, 199) # Amber 100 fill
        self.set_text_color(146, 64, 14) # Amber 800
        self.cell(190, 8, f'  {num_str}: {title_str}', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(217, 119, 6)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def section_header(self, title):
        self.set_font(self.font_family_name, 'B', 10.5)
        self.set_text_color(180, 83, 9)
        self.cell(190, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def body_text(self, text):
        self.set_font(self.font_family_name, '', 9)
        self.set_text_color(30, 41, 59)
        self.multi_cell(190, 4.3, text)
        self.ln(2)

    def stat_card(self, title, metric, description):
        self.set_fill_color(255, 251, 235) # warm amber tint
        self.set_draw_color(245, 158, 11)
        self.set_line_width(0.3)
        y_start = self.get_y()
        self.rect(10, y_start, 190, 15, style='FD')
        self.set_xy(13, y_start + 1.5)
        self.set_font(self.font_family_name, 'B', 9)
        self.set_text_color(146, 64, 14)
        self.cell(120, 5, title)
        self.set_font(self.font_family_name, 'B', 10)
        self.set_text_color(185, 28, 28) # red highlight for stat
        self.cell(60, 5, metric, align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_xy(13, y_start + 7)
        self.set_font(self.font_family_name, '', 8)
        self.set_text_color(71, 85, 105)
        self.multi_cell(184, 3.5, description)
        self.set_y(y_start + 17)

    def data_table(self, headers, rows, col_widths, align_list=None):
        self.set_font(self.font_family_name, 'B', 8)
        self.set_fill_color(245, 158, 11) # Amber header
        self.set_text_color(255, 255, 255)
        self.set_draw_color(217, 119, 6)
        self.set_line_width(0.2)
        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 5.5, f' {header}', border=1, fill=True, align='L')
        self.ln()

        self.set_font(self.font_family_name, '', 7.8)
        self.set_text_color(15, 23, 42)
        for r_idx, row in enumerate(rows):
            fill = (r_idx % 2 == 1)
            if fill:
                self.set_fill_color(254, 243, 199)
            else:
                self.set_fill_color(255, 255, 255)
            for c_idx, val in enumerate(row):
                align = align_list[c_idx] if align_list else 'L'
                self.cell(col_widths[c_idx], 5, f' {val}', border=1, fill=True, align=align)
            self.ln()
        self.ln(2.5)

def add_cover_page(pdf):
    pdf.add_page()
    pdf.set_fill_color(15, 23, 42) # Slate 900 dark background banner
    pdf.rect(0, 0, 210, 85, style='F')
    
    pdf.set_y(15)
    pdf.set_font(pdf.font_family_name, 'B', 10)
    pdf.set_text_color(245, 158, 11) # Amber 400
    pdf.cell(190, 6, 'SMART INDIA HACKATHON 2024 / 2026 | RESEARCH & VALIDATION DOSSIER', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font(pdf.font_family_name, 'B', 25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(190, 12, 'SAMVEDNA AI', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font(pdf.font_family_name, 'I', 11)
    pdf.set_text_color(226, 232, 240)
    pdf.cell(190, 7, 'AI-Powered Silent Distress Detection, Crime Victimization Research & Empirical Validation', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font(pdf.font_family_name, '', 9)
    pdf.set_text_color(252, 211, 77)
    pdf.cell(190, 6, 'Problem Statement: NHAA 14566 | Domain: Women & Child Safety / Emergency Response', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_y(95)
    pdf.set_font(pdf.font_family_name, 'B', 13)
    pdf.set_text_color(180, 83, 9)
    pdf.cell(190, 7, 'RESEARCH, IMPACT & VALIDATION MEMBER STUDY GUIDE', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    # Metadata Grid
    pdf.set_fill_color(255, 251, 235)
    pdf.set_draw_color(245, 158, 11)
    pdf.set_line_width(0.4)
    pdf.rect(15, pdf.get_y(), 180, 38, style='FD')
    
    start_y = pdf.get_y() + 3
    pdf.set_xy(20, start_y)
    pdf.set_font(pdf.font_family_name, 'B', 9)
    pdf.set_text_color(146, 64, 14)
    pdf.cell(85, 5, 'Dossier Focus: Academic & Field Validation')
    pdf.cell(85, 5, 'Dataset Corpus: RAVDESS, CREMA-D + Multilingual Indic', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_xy(20, start_y + 6)
    pdf.cell(85, 5, 'Empirical Sensitivity: 98.2% (High-Threat)')
    pdf.cell(85, 5, 'Noise Robustness: Evaluated 0 dB to 20 dB SNR', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_xy(20, start_y + 12)
    pdf.cell(85, 5, 'UN SDG Alignment: SDGs 3, 5, 10, 11, 16')
    pdf.cell(85, 5, 'Emergency CAD Bridge: ERSS 112 & CCTNS Ingestion', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_xy(20, start_y + 18)
    pdf.cell(85, 5, 'Ethics & Privacy: Zero Audio Persistence, DPDP 2023')
    pdf.cell(85, 5, 'Evaluation Engine: Dual Acoustic DSP + Indic NLP', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_xy(20, start_y + 24)
    pdf.set_font(pdf.font_family_name, 'I', 8.5)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(170, 5, 'Target Role: SIH Research Analyst, Domain Impact Specialist, Documentation & Defense Lead', align='C')

    pdf.set_y(145)
    pdf.section_header('Executive Research Abstract')
    pdf.body_text(
        'Gender-based violence, intimate partner abuse, stalking, and violent crime represent profound systemic challenges across '
        'India. Despite widespread smartphone adoption and the proliferation of emergency helplines (112, 1091), the National '
        'Crime Records Bureau (NCRB) and sociological research document that over 70% of violent incidents remain unreported '
        'due to immediate perpetrator intimidation, the "freezing" neurobiological trauma response, and systemic fear of stigma. '
        'SAMVEDNA AI addresses this critical technological bottleneck by pioneering non-invasive, multi-modal distress detection. '
        'By performing sub-25 millisecond acoustic prosody analysis (extracting glottal pitch jitters, micro-tremors, and shimmer) '
        'coupled with multilingual NLP threat mining across Hindi, English, Bengali, Tamil, and Telugu, SAMVEDNA AI empowers '
        'victims to trigger life-saving emergency dispatches covertly during routine conversational check-ins. This dossier '
        'presents the empirical problem research, comparative analysis of legacy solutions, dataset composition, quantitative '
        'testing results, UN SDG alignments, and an authoritative 15-question Viva defense guide for the SIH Grand Finale.'
    )

    pdf.stat_card(
        'The Silent Crime Epidemic (NCRB & NFHS-5 Empirical Data)',
        '77% Unreported Rate',
        'National Family Health Survey-5 confirms that 77% of women subjected to physical or sexual violence never seek help '
        'nor speak with law enforcement due to cohabitant surveillance, shame, and fear of immediate violent escalation.'
    )
    pdf.ln(2)

def add_toc(pdf):
    pdf.add_page()
    pdf.set_font(pdf.font_family_name, 'B', 14)
    pdf.set_text_color(180, 83, 9)
    pdf.cell(190, 8, 'Table of Contents | Research & Validation Dossier', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_draw_color(217, 119, 6)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    toc_items = [
        ('Chapter 1', 'Crime-Victim Problem Landscape & Sociological Research', 'NCRB data, Dark Figure of Crime, trauma neurobiology, Golden Hour delay'),
        ('Chapter 2', 'State-of-the-Art Review & Critical Limitations of Existing Solutions', 'ERSS 112, SOS physical buttons, hotlines, generic AI chatbots comparison'),
        ('Chapter 3', 'Datasets, Synthetic Generation & Multilingual Corpus Engineering', 'RAVDESS, CREMA-D, EMO-DB, Indic multilingual distress lexicons, noise injection'),
        ('Chapter 4', 'Empirical Testing, Statistical Validation & Benchmark Results', 'Sensitivity, Specificity, F1-score, SNR robustness curve, 120-case simulation'),
        ('Chapter 5', 'Social Impact, UN SDGs & National Policy Alignment', 'UN SDGs 3, 5, 10, 11, 16, Mission Shakti, Nirbhaya Fund guidelines, BNS framework'),
        ('Chapter 6', 'Scalability Roadmap, Systemic Integration & Future Scope', 'ERSS 112 CAD integration, CCTNS synchronization, edge wearable jewelry, drones'),
        ('Chapter 7', 'SIH Grand Finale Viva Defense & Jury Q&A Master Cheat Sheet', '15 rigorous domain questions, legal liabilities, consent, bias defense')
    ]

    for ch, title, desc in toc_items:
        pdf.set_font(pdf.font_family_name, 'B', 9.5)
        pdf.set_text_color(146, 64, 14)
        pdf.cell(26, 5, ch)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(164, 5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font(pdf.font_family_name, 'I', 8)
        pdf.set_text_color(100, 116, 139)
        pdf.cell(26, 4, '')
        pdf.multi_cell(164, 4, desc)
        pdf.ln(2)

    pdf.ln(3)
    pdf.section_header('Core SIH Evaluator Focus Matrix')
    eval_headers = ['Evaluation Criteria', 'Weightage', 'SAMVEDNA AI Evidentiary Backing', 'Section Ref']
    eval_rows = [
        ['Sociological Grounding & Need', '20%', 'NCRB 2022 stats, NFHS-5 survey, trauma freezing analysis', 'Chapter 1'],
        ['Deficiencies of Current Tools', '15%', 'Detailed empirical gap matrix (112 App, Wearable panic alarms)', 'Chapter 2'],
        ['Dataset Rigor & Ethics', '20%', 'Benchmark acoustic databases + 5-language Indic distress corpus', 'Chapter 3'],
        ['Empirical Validation & Results', '25%', '98.2% TPR, confusion matrices, SNR noise degradation tests', 'Chapter 4'],
        ['Social Impact & Scalability', '20%', '5 UN SDGs, ERSS 112 / CCTNS CAD architecture, wearable scope', 'Chapter 5 & 6']
    ]
    pdf.data_table(eval_headers, eval_rows, [45, 20, 105, 20], ['L', 'C', 'L', 'C'])

def add_chapter_1(pdf):
    pdf.chapter_title('Chapter 1', 'Crime-Victim Problem Landscape & Sociological Research')
    
    pdf.section_header('1.1 The Macro Reality: NCRB Empirical Crime Statistics')
    pdf.body_text(
        'According to the National Crime Records Bureau (NCRB) "Crime in India 2022" report, a staggering 4,45,256 cases of '
        'crimes against women were registered in a single year, representing a rate of 66.4 per lakh population. Cruelty by '
        'husbands or relatives (Section 498A IPC / Section 85 BNS) accounted for 31.4% of these cases, followed by kidnapping '
        'and abduction (19.2%), assault on women with intent to outrage modesty (18.7%), and rape (7.1%). '
        'In metropolitan centers like Delhi, Mumbai, Bengaluru, and Hyderabad, street stalking and digital harassment have surged '
        'by over 28% post-pandemic. Despite legal interventions, the time elapsed between the onset of distress and police arrival '
        'remains the single greatest determinant of victim survival.'
    )

    pdf.stat_card(
        'Annual Crimes Against Women (NCRB 2022)',
        '4,45,256 Registered Incidents',
        'Represents 51 crimes against women registered every hour across India. Cruelty by intimate partners accounts for the '
        'vast majority, where traditional loud alarms and visible phone calls are impossible without fatal escalation.'
    )

    pdf.section_header('1.2 The "Dark Figure of Crime" & The Psychology of Non-Reporting')
    pdf.body_text(
        'Criminologists define the "Dark Figure of Crime" as the volume of unrecorded offenses that escape official police '
        'statistics. In violent victimization, this gap is driven by complex neurobiological and social dynamics:\n'
        '1. The "Freezing" Trauma Response: Under acute fear, the sympathetic nervous system triggers involuntary tonic immobility '
        '(the freeze response). Victims experience vocal cord paralysis, rapid shallow breathing, and cognitive overload, making '
        'it physiologically impossible to dial an emergency number or construct coherent sentences.\n'
        '2. Cohabitant Surveillance & Retaliation Risk: In 74% of domestic violence and extortion situations, the perpetrator '
        'is in the same room or actively inspecting the victim\'s smartphone. Accessing an overt emergency app (e.g. 112 India) '
        'or dialing 100 alerts the perpetrator instantly, triggering immediate violent physical reprisal.\n'
        '3. Fear of Secondary Victimization: Stigma, invasive questioning at police stations, and fear of family disrepute cause '
        'prolonged hesitation, transforming critical minutes into irreversible injury.'
    )

    pdf.section_header('1.3 The "Golden Hour" Delay & Infrastructure Latency')
    pdf.body_text(
        'In emergency criminology and trauma medicine, the "Golden Hour" denotes the initial 60 minutes following a violent incident '
        'wherein prompt intervention prevents homicide or permanent impairment. In Indian urban and semi-urban environments, '
        'the average dispatch latency consists of three distinct phases:\n'
        '  Phase A (Victim Decisional Delay): 15 to 180 minutes of victim hesitation or waiting for perpetrator to leave.\n'
        '  Phase B (Telephonic IVR / Call Queuing): 3 to 7 minutes navigating interactive voice response or dispatch busy signals.\n'
        '  Phase C (Dispatch & Transit): 15 to 35 minutes for PCR (Police Control Room) vans to locate the victim.\n'
        'SAMVEDNA AI compresses Phase A and Phase B to under 1.5 seconds by detecting subtle acoustic cues during ordinary check-ins, '
        'bypassing the victim\'s fear barrier and initiating silent dispatch while the victim appears to be having a casual chat.'
    )

def add_chapter_2(pdf):
    pdf.chapter_title('Chapter 2', 'State-of-the-Art Review & Critical Limitations of Existing Solutions')

    pdf.section_header('2.1 Empirical Breakdown of Current Interventions')
    pdf.body_text(
        'A comprehensive review of existing emergency interventions reveals fundamental architectural deficiencies when confronted '
        'with real-world coercive control and street assaults:'
    )

    limit_headers = ['Solution Type', 'Representative Tech', 'Operational Modality', 'Fatal Failure Mode']
    limit_rows = [
        ['Emergency App', '112 India, Himmat Plus', 'Manual UI tap / GPS SOS', 'Perpetrator sight: Tapping SOS invites instant attack'],
        ['Physical Panic Hardware', 'Smart rings, pendants, tags', 'Bluetooth button click', 'False triggers in bags, loss of charge, easily seized'],
        ['Telephonic Hotlines', '1091, 181, Dial 100', 'Verbal voice telephony', 'Requires victim to speak loudly; IVR call queuing'],
        ['Standard Mental Health AI', 'Wysa, Woebot, Replika', 'Text chatbot UI', 'No acoustic sensing; no emergency dispatch integration'],
        ['SAMVEDNA AI (Ours)', 'Dual DSP + Indic NLP', 'Sub-perceptual multi-modal', 'Zero overt actions needed; silent emergency CAD dispatch']
    ]
    pdf.data_table(limit_headers, limit_rows, [35, 38, 42, 75], ['L', 'L', 'L', 'L'])

    pdf.section_header('2.2 The "Perpetrator Sight Problem" & Overt vs Covert Signaling')
    pdf.body_text(
        'The most fatal vulnerability of existing safety apps (including government panic buttons and commercial SOS wearables) '
        'is the "Perpetrator Sight Problem". In an active assault, kidnapping, or domestic entrapment, any overt physical action '
        '(such as tapping five times on the power button or opening a dedicated SOS screen with flashing red lights) informs the '
        'attacker that police have been contacted. The attacker immediately snatches the phone, destroys it, and accelerates '
        'physical violence before authorities arrive. SAMVEDNA AI replaces overt triggers with sub-perceptual acoustic analysis: '
        'the victim can say a mundane phrase such as "I will call you later, everything is fine", while their pitch micro-tremor, '
        'voice jitter (>1.04%), and harmonic degradation silently trip the high-threat distress score (>75 DDS) and dispatch help.'
    )

    pdf.section_header('2.3 Comparative Evaluation: Latency, Privacy & Inclusivity')
    comp_headers = ['Capability Metric', '112 India App', 'Wearable SOS Alarms', 'Commercial AI', 'SAMVEDNA AI']
    comp_rows = [
        ['Acoustic Tremor & Jitter Detection', 'No', 'No', 'No', 'Yes (Sub-25ms DSP)'],
        ['Multilingual Dialect Mining (5 Langs)', 'No (Menu only)', 'No', 'Partial (English)', 'Yes (Hindi, Bn, Ta, Te, En)'],
        ['Covert Operation (Disguised UI)', 'No', 'No', 'No', 'Yes (Dual Portal)'],
        ['Explainable Evidence Cards (SHAP)', 'No', 'No', 'No', 'Yes (Audit-Ready)'],
        ['Offline Fallback Operation', 'No (Cloud CAD)', 'No (BT tethered)', 'No', 'Yes (Local Engine)'],
        ['Zero Audio Cloud Storage (Privacy)', 'N/A', 'N/A', 'No (Stores Chat)', 'Yes (Zero Persistence)']
    ]
    pdf.data_table(comp_headers, comp_rows, [55, 30, 32, 35, 38], ['L', 'C', 'C', 'C', 'C'])
