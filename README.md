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

The application uses **automatic fallback chains** for reliability. You can customize these settings in `.env`:

### Required API Keys
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

### Automatic Fallback Chains

**LLM (Language Model):**
1. **Groq API** (llama-3.3-70b) - Fast, requires API key
2. **Gemini API** (gemini-1.5-flash) - Fallback, requires API key  
3. **Local TinyLlama** - Offline fallback, slow but always works

**STT (Speech-to-Text):**
- Fixed: **Faster-Whisper Base** model
- To change: Edit `STT_MODEL` in [src/services/chatbot.py](src/services/chatbot.py)

**TTS (Text-to-Speech):**
1. **Edge-TTS** - High quality, online (respects voice settings)
2. **gTTS** - Google TTS, online fallback
3. **Piper** - Offline fallback

**Language Detection:**
- Automatic (fasttext → langid)
- Supports: English, Turkish, German, French, Spanish

## Tech Stack

- **Speech-to-Text**: Faster-Whisper (CTranslate2 optimized)
- **LLM**: LangChain (Groq, Gemini, HuggingFace)
- **Text-to-Speech**: Edge-TTS, gTTS, Piper
- **Interface**: Gradio 4.14.0
- **Language Detection**: fasttext, langid

## Changing Models

**To change STT model:** Edit `STT_MODEL` in [src/services/chatbot.py](src/services/chatbot.py#L12)
```python
STT_MODEL = "Faster-Whisper - Base"  # Change to: Small, Medium, Large-V2, etc.
```

**To change LLM models:** Edit functions in [src/services/llm.py](src/services/llm.py)
- `api_groq_initializer()` - Line 73
- `api_gemini_initializer()` - Line 48

**Available models listed in:** [src/config/ai_model_names.py](src/config/ai_model_names.py)

## Troubleshooting

**Python version warning**: Upgrade to Python 3.10+ recommended (3.9 works but EOL)

**No LLM available**: Add at least one API key (GROQ_API_KEY or GOOGLE_API_KEY) to `.env`

**Import errors**: Always run with `python3 -m src.main` from project root

**Audio issues**: Check `data/audio/` directories exist and are writable

**API rate limits**: System will automatically fall back to next available option

## License

MIT
