# -*- coding: utf-8 -*-
from fpdf.enums import XPos, YPos

def add_section_3(pdf):
    pdf.chapter_title('3', 'Voice Prosody & Acoustic Stress Engine (voice_analytics.py)')
    
    pdf.section_heading('3.1 Neurobiology of Vocal Stress in Trauma Survivors')
    pdf.body_p('When an individual experiences acute terror or ongoing trauma, the Autonomic Nervous System (ANS) triggers sympathetic hyper-arousal. This physiological state causes involuntary micro-contractions in the cricothyroid and thyroarytenoid muscles controlling vocal fold tension, produces rapid irregular breathing patterns, and induces subglottal pressure volatility. These physical perturbations are impossible to fake and cannot be voluntarily suppressed, making acoustic prosody an unassailable objective biomarker of human distress.')
    
    pdf.section_heading('3.2 Zero-Disk In-Memory Audio Extraction Pipeline')
    pdf.body_p('To safeguard survivor privacy and meet strict forensic standards, the system performs zero disk I/O. Incoming audio streams are parsed directly from memory buffers (io.BytesIO) using a triple-fallback mechanism:')
    pdf.bullet('Path A: SciPy wavfile', 'Parses RIFF/WAV headers, extracts sampling rate and converts 16/24/32-bit PCM arrays to normalized float32 (-1.0 to +1.0).')
    pdf.bullet('Path B: Python wave module', 'Handles non-standard RIFF chunk structures and multichannel downmixing to mono.')
    pdf.bullet('Path C: Raw 16-bit PCM buffer', 'Interprets headerless raw bytes directly with np.frombuffer using the 16kHz telephony default.')
    
    pdf.section_heading('3.3 Mathematical Formulations of Acoustic Biomarkers')
    pdf.bullet('Fundamental Frequency (F0 Pitch)', 'Calculated across 25ms Hamming-windowed frames with a 10ms hop. F0 represents the rate of vocal fold vibration. Extracted via normalized autocorrelation (finding the peak lag tau in the 75Hz - 500Hz human vocal range):')
    pdf.code_block('R_xx(tau) = sum_{n=0}^{N - tau - 1} x[n] * x[n + tau]  -->  F0 = sample_rate / tau_peak')
    
    pdf.bullet('Vocal Jitter % (Frequency Perturbation)', 'Measures the cycle-to-cycle variability in vocal fold vibration frequency. High jitter (>1.04% MDVP threshold) indicates involuntary laryngeal instability:')
    pdf.code_block('Jitter_pct = ( (1 / (N - 1)) * sum_{i=1}^{N-1} |T_i - T_{i+1}| ) / ( (1 / N) * sum_{i=1}^N T_i ) * 100')
    
    pdf.bullet('Vocal Shimmer % (Amplitude Perturbation)', 'Measures the cycle-to-cycle variability in peak speech amplitude. High shimmer (>3.81%) correlates with subglottal pressure exhaustion and sobbing/shaking voice:')
    pdf.code_block('Shimmer_pct = ( (1 / (N - 1)) * sum_{i=1}^{N-1} |A_i - A_{i+1}| ) / ( (1 / N) * sum_{i=1}^N A_i ) * 100')
    
    pdf.bullet('Harmonics-to-Noise Ratio (HNR in dB)', 'Quantifies the purity of the vocal cord tone against turbulent airflow. Lower HNR (<12 dB) indicates severe breathiness and vocal breakdown:')
    pdf.code_block('HNR_dB = 10 * log10( E_periodic / E_noise )')
    
    pdf.bullet('Vocal Micro-Tremor (4-10 Hz)', 'Isolates involuntary physiological micro-tremors in vocal cord tension via narrow band-pass filtering in the 4-10 Hz modulation spectrum. Directly flags panic.')
    pdf.bullet('13 Mel-Frequency Cepstral Coefficients (MFCCs)', 'Applies FFT, Mel-filterbank weighting (simulating human cochlear response), and Discrete Cosine Transform (DCT) to capture vocal tract timbre.')

    pdf.section_heading('3.4 Acoustic Stress & Emotion Classification Logic')
    pdf.body_p('The acoustic stress score (0 to 100) is aggregated through non-linear feature weighting: base score starts at 20.0, adding up to +35 pts for jitter > 2.0%, +25 pts for pitch volatility > 45 Hz, +20 pts for tremor > 40, and +15 pts for excessive hesitation/pause ratios (>35%). The primary emotion classifier evaluates the joint F0-shimmer space to output states such as Anxious/Agitated, Tense/Hesitant, Severe Distress/Tremor, Flat Affect/Depressive Freeze, or Calm/Steady.')

def add_section_4(pdf):
    pdf.chapter_title('4', 'Multilingual NLP & Threat Intimidation Engine (nlp_engine.py)')
    
    pdf.section_heading('4.1 Multilingual Support Across 5 Indic Languages & Hinglish')
    pdf.body_p('Atrocity survivors communicate in their mother tongue or localized colloquial mixtures. SAMVEDNA AI supports five constitutional languages: Hindi, English, Bengali, Tamil, and Telugu, along with Romanized transliterations (Hinglish, Tanglish, etc.).')
    
    pdf.section_heading('4.2 Domain-Specific Threat & Intimidation Lexicons')
    pdf.body_p('Under Section 15A of the SC/ST PoA Act, witness tampering and intimidation carry stringent penal consequences. The engine maintains calibrated keyword matrices to catch explicit and implicit coercion:')
    pdf.bullet('Hindi / Hinglish Cues', 'dhamki, maar denge, jaan se, badla, case wapas, court mat jao, goli, aaropi, jamnat (bail), dar, dabav, pichha karna.')
    pdf.bullet('Bengali Cues', 'humki, mere phelbo, case tule ne, court, jamin, bhoy korche, akromon, tara korche, khun, otyachar.')
    pdf.bullet('Tamil Cues', 'mirattal, kolai, vazhakai thirumba, needhimandram, jamin, bayam, thaakkudhal, thurathugiraargal.')
    pdf.bullet('Telugu Cues', 'bedirimpu, champesthamu, kesu venakki, court, bail, bhayam, dadi, vedhimmpulu, hathya.')
    pdf.bullet('English Cues', 'threat, kill, revenge, withdraw case, drop complaint, stalk, weapon, accused out on bail, intimidation, retaliate.')

    pdf.section_heading('4.3 Social Boycott & Caste Ostracism Detection')
    pdf.body_p('Social boycotts are insidious non-physical atrocities penalized under Section 3(1)(za) and 3(1)(zb) of the PoA Act. Dominant groups isolate survivors to force FIR retractions. The engine screens for historical ostracism idioms:')
    pdf.bullet('Hindi / Hinglish', 'hookah pani band, paani band, gao se nikal, samajik bahishkar, ration band.')
    pdf.bullet('Bengali', 'samajik boycott, jol bondho, gram theke bohishta, boycott.')
    pdf.bullet('Tamil', 'oor vilakkam, thanneer thadai, samuga purakkanippu, vilakkam.')
    pdf.bullet('Telugu', 'samajika bahishkarana, neeru bandh, gramam nundi bahishkarana.')

    pdf.section_heading('4.4 Crisis & Suicide Ideation Screening')
    pdf.body_p('Severe post-atrocity trauma can precipitate suicidal ideation. The NLP engine searches for helplessness triggers across all five languages (e.g., mar jana, jaan de dunga, kuch nahi bacha, no justice, want to die, cannot take this anymore). Any match immediately flags the check-in as a life-safety crisis.')
