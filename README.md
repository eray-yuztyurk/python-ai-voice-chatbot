# Voice AI Chatbot

A voice-enabled AI chatbot with automatic fallback mechanisms for reliability. Talk or type, get intelligent responses with voice output.

## What It Does

- **Voice Input**: Record your voice → automatic transcription (Faster-Whisper Base model)
- **Text Input**: Type your questions directly
- **Smart AI**: Automatic fallback chain (Groq → Gemini → Local TinyLlama)
- **Voice Output**: Responses converted to speech (Edge-TTS → gTTS → Piper)
- **Offline Ready**: Falls back to local models if APIs fail

## Quick Start

1. Clone and install:
```bash
git clone https://github.com/eray-yuztyurk/python-ai-voice-assistant.git
cd python-ai-voice-assistant
pip install -r requirements.txt
```

2. Set up your API keys:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

3. Run:
```bash
python3 -m src.main
# or
./run.sh
```

## Project Structure

```
src/
├── api/              # Gradio web interface
├── services/         # Core logic (STT, LLM, TTS, chatbot)
├── config/           # Settings and constants
└── utils/            # Helper functions
```

## Configuration

The application uses **automatic fallback chains** - models are tried in order until one works. These chains are built-in and work automatically. 

What you **can** customize in `.env`:

### API Keys (Required for cloud models)
```bash
GROQ_API_KEY=gsk_...              # Get free at: https://console.groq.com/
GOOGLE_API_KEY=AIza...            # Get free at: https://makersuite.google.com/app/apikey
```

### Optional Settings
```bash
# Server settings
SERVER_HOST=127.0.0.1
SERVER_PORT=7860
OPEN_BROWSER=true

# TTS voice settings (only affects Edge-TTS engine)
TTS_RATE=+12%        # Speed: -50% to +100%
TTS_VOLUME=+5%       # Volume: -50% to +50%
TTS_PITCH=+0Hz       # Pitch: -50Hz to +50Hz

# File paths
AUDIO_OUTPUT_DIR=./data/audio/output_audio
AUDIO_INPUT_DIR=./data/audio/input_audio
```

## How It Works

### Automatic Fallback Chains (Built-in, cannot be changed via .env)

**LLM (Language Model):**
1. **Groq API** (llama-3.3-70b) - Fast, requires API key
2. **Gemini API** (gemini-1.5-flash) - Fallback, requires API key  
3. **Local TinyLlama** - Offline fallback, slow but always works

**STT (Speech-to-Text):**
- Uses: **Faster-Whisper Base** model (hardcoded)

**TTS (Text-to-Speech):**
1. **Edge-TTS** - High quality, online (respects .env voice settings)
2. **gTTS** - Google TTS, online fallback
3. **Piper** - Offline fallback

**Language Detection:**
- Automatic (fasttext → langid)
- Supports: English, Turkish, German, French, Spanish

## Tech Stack

### Core Technologies

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-4.14.0-FF7C00?style=flat&logo=gradio&logoColor=white)

### AI/ML Frameworks & Libraries

![LangChain](https://img.shields.io/badge/🦜_LangChain-Framework-121212?style=flat)
![Transformers](https://img.shields.io/badge/🤗_Transformers-yellow?style=flat)
![Faster Whisper](https://img.shields.io/badge/Faster--Whisper-CTranslate2-blue?style=flat)

### APIs & Services

![Groq](https://img.shields.io/badge/Groq_API-LLaMA_3.3-F55036?style=flat)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-1.5_Flash-4285F4?style=flat&logo=google&logoColor=white)
![Edge TTS](https://img.shields.io/badge/Edge--TTS-Microsoft-00A4EF?style=flat)

### Complete Library List

**Speech-to-Text:**
- faster-whisper (CTranslate2 optimized)
- transformers (HuggingFace Whisper models)
- torch, accelerate, soundfile, librosa

**Language Models:**
- langchain-groq (Groq API integration)
- langchain-google-genai (Gemini integration)
- langchain-huggingface (Local TinyLlama)

**Text-to-Speech:**
- edge-tts (Microsoft Edge TTS)
- gTTS (Google Text-to-Speech)
- piper (offline TTS)

**Language Detection:**
- fasttext (primary)
- langid (fallback)

**Utilities:**
- gradio (web interface)
- scipy (audio I/O)
- python-dotenv (environment config)

## Advanced: Changing Models (requires code editing)

If you want different models than the defaults, you need to edit the source code:

**Change STT model:** Edit line 16 in [src/services/chatbot.py](src/services/chatbot.py#L16)
```python
STT_MODEL = "Faster-Whisper - Base"  # Available: Tiny, Base, Small, Medium, Large-V2
```

**Change LLM models or order:** Edit [src/services/llm.py](src/services/llm.py)
- Groq model: Line 73 in `api_groq_initializer()`
- Gemini model: Line 48 in `api_gemini_initializer()`
- Fallback order: Lines 103-130 in `llm_initializer_with_fallback()`

**All available models:** See [src/config/ai_model_names.py](src/config/ai_model_names.py)

## Troubleshooting

**Python version warning**: Upgrade to Python 3.10+ recommended (3.9 works but EOL)

**No LLM available**: Add at least one API key (GROQ_API_KEY or GOOGLE_API_KEY) to `.env`

**Import errors**: Always run with `python3 -m src.main` from project root

**Audio issues**: Check `data/audio/` directories exist and are writable

**API rate limits**: System will automatically fall back to next available option

## License

MIT
