"""
AI Model Names Configuration
Organized by library/framework for STT and TTS models
"""

# ================================================================================================
# SPEECH-TO-TEXT (STT) MODELS
# ================================================================================================

# Faster-Whisper Models (faster-whisper library - CTranslate2 optimized)
# RAM: ~200-600MB | Speed: Very Fast | Quality: High
faster_whisper_stt_models = {
    "Faster-Whisper - Tiny": "tiny",
    "Faster-Whisper - Base": "base",
    "Faster-Whisper - Small": "small",
    "Faster-Whisper - Medium": "medium",
    "Faster-Whisper - Large-V2": "large-v2"
}

# Transformers Whisper Models (transformers library - PyTorch)
# RAM: ~1-6GB | Speed: Medium | Quality: High
transformers_whisper_stt_models = {
    # Official OpenAI Whisper
    "Whisper - Tiny": "openai/whisper-tiny",
    "Whisper - Base": "openai/whisper-base",
    "Whisper - Small": "openai/whisper-small",
    "Whisper - Medium": "openai/whisper-medium",
    "Whisper - Large V1": "openai/whisper-large",
    "Whisper - Large V2": "openai/whisper-large-v2",
    "Whisper - Large V3": "openai/whisper-large-v3",

    # Distil-Whisper (optimized, English-only)
    "Distil-Whisper - Tiny (EN)": "distil-whisper/distil-tiny.en",
    "Distil-Whisper - Base (EN)": "distil-whisper/distil-base.en",
    "Distil-Whisper - Small (EN)": "distil-whisper/distil-small.en",
    "Distil-Whisper - Medium (EN)": "distil-whisper/distil-medium.en",
    "Distil-Whisper - Medium (Multilingual)": "distil-whisper/distil-medium",

    # Specialized Models
    "Whisper - Large-V2 (Noise-Robust)": "biodatlab/whisper-noise-large-v2",
}

# Combined STT models for UI
stt_models = {**faster_whisper_stt_models, **transformers_whisper_stt_models}


# ================================================================================================
# TEXT-TO-SPEECH (TTS) MODELS
# ================================================================================================

# Transformers-based TTS Models (transformers library - PyTorch)
# RAM: ~400MB-2GB | Speed: Medium | Quality: High
transformers_tts_models = {
    # SpeechT5 - Multilingual, high quality
    "SpeechT5 - Multilingual [High | Local]": "microsoft/speecht5_tts",
    
    # Facebook MMS-TTS - 1100+ languages, per-language models
    "MMS-TTS - English [Good | Local]": "facebook/mms-tts-eng",
    "MMS-TTS - Turkish [Good | Local]": "facebook/mms-tts-tur",
    "MMS-TTS - German [Good | Local]": "facebook/mms-tts-deu",
    "MMS-TTS - French [Good | Local]": "facebook/mms-tts-fra",
    "MMS-TTS - Spanish [Good | Local]": "facebook/mms-tts-spa",
    
    # Parler-TTS - Natural, expressive speech
    "Parler-TTS - Mini [High | Local]": "parler-tts/parler-tts-mini-v1",
    "Parler-TTS - Large [Excellent | Local]": "parler-tts/parler-tts-large-v1",
    
    # Bark - Highly realistic, multilingual with effects
    "Bark - Small [Excellent | Local]": "suno/bark-small",
    "Bark - Large [Excellent | Local]": "suno/bark",
}

# Piper TTS Models (piper-tts library - ONNX optimized)
# RAM: ~100-300MB | Speed: Very Fast | Quality: Good-High
piper_tts_models = {
    # English voices
    "Piper - English (Amy) [Fast | Local]": "en_US-amy-low",
    "Piper - English (Amy) [Good | Local]": "en_US-amy-medium",
    "Piper - English (Lessac) [Good | Local]": "en_US-lessac-medium",
    "Piper - English (Libritts) [High | Local]": "en_US-libritts-high",
    
    # Turkish voices
    "Piper - Turkish (Fettah) [Good | Local]": "tr_TR-fettah-medium",
    
    # German voices
    "Piper - German (Thorsten) [Good | Local]": "de_DE-thorsten-medium",
    
    # Spanish voices
    "Piper - Spanish (Davefx) [Good | Local]": "es_ES-davefx-medium",
    
    # French voices
    "Piper - French (Siwis) [Good | Local]": "fr_FR-siwis-medium",
}

# VITS Models (transformers or vits library)
# RAM: ~200-500MB | Speed: Fast | Quality: High
vits_tts_models = {
    "VITS - LJ Speech (EN) [High | Local]": "facebook/mms-tts-eng",
    "VITS - Turkish [High | Local]": "facebook/mms-tts-tur",
}

# Coqui TTS Models (TTS library - advanced features)
# RAM: ~2-6GB | Speed: Slow | Quality: Excellent (voice cloning)
coqui_tts_models = {
    "XTTS-v2 - Multilingual [Excellent | Local]": "tts_models/multilingual/multi-dataset/xtts_v2",
    "XTTS-v2 - Voice Clone [Excellent | Local]": "tts_models/multilingual/multi-dataset/xtts_v2",
}

# API-based TTS (requires internet, free tiers available)
# RAM: ~50MB | Speed: Depends on network | Quality: High
api_tts_models = {
    # Google Text-to-Speech (gTTS library)
    "gTTS - English [Good | API]": "en",
    "gTTS - Turkish [Good | API]": "tr",
    "gTTS - German [Good | API]": "de",
    "gTTS - French [Good | API]": "fr",
    "gTTS - Spanish [Good | API]": "es",
    
    # Microsoft Edge TTS (edge-tts library)
    "Edge-TTS - English (Female) [High | API]": "en-US-AriaNeural",
    "Edge-TTS - English (Male) [High | API]": "en-US-GuyNeural",
    "Edge-TTS - Turkish (Female) [High | API]": "tr-TR-EmelNeural",
    "Edge-TTS - Turkish (Male) [High | API]": "tr-TR-AhmetNeural",
    "Edge-TTS - German (Female) [High | API]": "de-DE-KatjaNeural",
    "Edge-TTS - French (Female) [High | API]": "fr-FR-DeniseNeural",
}

# System TTS (eSpeak-NG - offline, lightweight, basic quality)
# RAM: ~10-50MB | Speed: Very Fast | Quality: Low-Medium
espeak_tts_models = {
    "eSpeak - English [Basic | Local]": "en",
    "eSpeak - Turkish [Basic | Local]": "tr",
    "eSpeak - German [Basic | Local]": "de",
    "eSpeak - French [Basic | Local]": "fr",
    "eSpeak - Spanish [Basic | Local]": "es",
}

# Combined TTS models for UI
tts_models = {
    **transformers_tts_models,
    **piper_tts_models,
    **api_tts_models,
    **espeak_tts_models,
}