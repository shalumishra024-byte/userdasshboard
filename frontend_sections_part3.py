# -*- coding: utf-8 -*-
from fpdf.enums import XPos, YPos

def add_section_5(pdf):
    pdf.chapter_title('5', 'Centralized Multilingual i18n Localization Engine (translations.js)')
    
    pdf.section_heading('5.1 Dictionary Structure Across 5 Indic Languages')
    pdf.body_p('SAMVEDNA AI operates in five constitutional languages: Hindi (hi), English (en), Bengali (bn), Tamil (ta), and Telugu (te). Localization strings are centralized in translations.js under the global TRANSLATIONS object, covering all UI labels, navigation buttons, scenario presets, hotlines, and conversational placeholders.')

    pdf.section_heading('5.2 Dynamic DOM Replacement via data-i18n Attributes')
    pdf.body_p('The application updates text nodes in real time without triggering a full page reload or destroying active Web Audio streams:')
    pdf.code_block('function applyLocalization(lang) {\n  const dict = TRANSLATIONS[lang] || TRANSLATIONS.en;\n  document.querySelectorAll("[data-i18n]").forEach(el => {\n    const key = el.getAttribute("data-i18n");\n    if (dict[key]) el.textContent = dict[key];\n  });\n  // Localize form input placeholders\n  document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {\n    const key = el.getAttribute("data-i18n-placeholder");\n    if (dict[key]) el.placeholder = dict[key];\n  });\n}')

    pdf.section_heading('5.3 State Persistence in LocalStorage')
    pdf.body_p('When a user changes their language via the header dropdown, changeLanguage(newLang) stores the selection in localStorage under samvedna_selected_lang. Upon subsequent visits or page reloads, the client automatically restores the selected language, syncing both the UI labels and SpeechRecognition locale.')

def add_section_6(pdf):
    pdf.chapter_title('6', 'Victim Omnichannel Portal: Components, State & Interactions')
    
    pdf.section_heading('6.1 Interactive Voice Check-In Card')
    pdf.body_p('The voice check-in card serves as the primary acoustic ingestion portal:')
    pdf.bullet('Microphone Toggle Button', 'Initiates Web Audio API capture, changes styling to an emergency red active pulse, and starts the elapsed seconds timer.')
    pdf.bullet('HTML5 Waveform Canvas', 'Renders real-time acoustic oscillations with dynamic stroke gradients.')
    pdf.bullet('Audio File Upload (handleAudioUpload)', 'Allows survivors to upload recorded phone threats or voice notes directly from their file manager, converted via FileReader to binary Blobs.')

    pdf.section_heading('6.2 Emotional State & Vocal Biomarker Display')
    pdf.body_p('Upon check-in completion, the emotional state card renders objective physiological metrics:')
    pdf.bullet('Primary Vocal Emotion Badge', 'Displays classified states such as Anxious/Agitated, Tense/Hesitant, Severe Distress/Tremor, or Calm/Steady with color-coded tags.')
    pdf.bullet('Acoustic Confidence Meter', 'Percentage confidence calculated from F0 harmonic strength.')
    pdf.bullet('Vocal Stress Score Gauge', 'Progress bar reflecting acoustic autonomic strain.')

    pdf.section_heading('6.3 Quick Situational Scenario Presets')
    pdf.body_p('For users unable to type long paragraphs, four quick scenario chips populate the check-in input: (1) Acute Threat & Fear (dhamki); (2) Impending Court Deposition Anxiety; (3) Caste Boycott & Social Isolation (hookah-paani band); and (4) Calmer Recovery Day.')

    pdf.section_heading('6.4 Conversational Empathy Chat Interface')
    pdf.body_p('The chat window provides real-time dialogue with Gemini Flash-Lite:')
    pdf.bullet('Message Bubble History', 'Distinguishes user messages (sky-blue right-aligned) from AI responses (slate-800 left-aligned with Gemini badge).')
    pdf.bullet('Live Typing Indicator', 'Displays animated bouncing dots (showTypingIndicator) while awaiting backend response.')
    pdf.bullet('XAI & Intervention Cards', 'Renders transparent Explainable AI contribution factors and statutory Section 15A protection directives directly below the relevant response bubble.')

    pdf.section_heading('6.5 One-Touch Emergency SOS Trigger')
    pdf.body_p('A prominent, pulsing red button in the header triggers triggerEmergencySOS(). It immediately sends an unthrottled CRITICAL check-in payload to the backend, activating police nodal alerts and displaying local emergency hotline numbers.')

def add_section_7(pdf):
    pdf.chapter_title('7', 'Official Caseworker & Counsellor Dashboard UI Architecture')
    
    pdf.section_heading('7.1 Tri-Panel Navigation (switchOfficialSubTab)')
    pdf.body_p('The institutional dashboard is segmented into three specialized operational sub-panels:')
    pdf.bullet('1. District Atrocity Overview (subpanel-district)', 'High-level triage metrics for District Magistrates and Superintendents of Police, displaying Total Active Atrocity Cases, Critical Cases Under Watch, Active Protection Alerts, and High-Risk Village Hotspots.')
    pdf.bullet('2. Counsellor Case Dossier (subpanel-counsellor)', 'In-depth clinical and legal management for assigned caseworkers, featuring victim selectors, FIR details, sections invoked, hearing countdowns, and clinical case note submission.')
    pdf.bullet('3. Deep Analytics Console (subpanel-analytics)', 'Longitudinal epidemiological trends, risk distribution across trial stages, and multi-modal biomarker correlations.')

    pdf.section_heading('7.2 Live Case Dossier Management (loadCounsellorDossier)')
    pdf.body_p('Selecting a victim profile (e.g. VIC-MP-2024-881) dynamically queries GET /api/v1/victim/profile/{id}, populating the masked survivor identity (Ms. S*** B***), community affiliation (SC/ST), Special Court name, accused bail status alert banner, and past clinical session notes.')

def add_section_8(pdf):
    pdf.chapter_title('8', 'Chart.js Longitudinal Trajectory & Regional Visualizations')
    
    pdf.section_heading('8.1 Longitudinal Distress Trajectory Line Chart')
    pdf.body_p('Constructed using Chart.js on canvas element #longitudinalDistressChart. It plots historical check-in dates on the X-axis against composite DDS scores (0 to 100) on the Y-axis. Features a shaded red threshold zone at DDS >= 80.0, visually warning caseworkers when a victim is in an escalating crisis trajectory.')

    pdf.section_heading('8.2 Legal Stage Vulnerability Doughnut Chart')
    pdf.body_p('Visualizes the active caseload distribution across trial milestones: Accused Bail Hearing, Chargesheet Filing, Special Court Deposition, and Compensation Disbursement, highlighting where systemic bottlenecks occur.')

    pdf.section_heading('8.3 Multi-Modal Impact Factor Radar Chart')
    pdf.body_p('Illustrates the relative weight contribution of each distress modality (Acoustic Prosody 28%, NLP Threat 28%, Clinical Trauma 20%, Legal Vulnerability 16%, Engagement Consistency 8%) for the active case.')
