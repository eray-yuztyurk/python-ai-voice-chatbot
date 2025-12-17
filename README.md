# Voice AI Chatbot

A voice-enabled AI chatbot that lets you talk or type to get intelligent responses. Built with fallback systems for reliability.

## What It Does

- **Talk to it**: Record your voice, get text transcription
- **Get AI responses**: Uses Gemini, Groq, or local models
- **Hear the answer**: Converts responses to speech automatically
- **Works offline**: Falls back to local models if APIs fail

## Quick Start

1. Clone and install:
```bash
git clone <your-repo>
cd python-ai-llm-stt-tts-translator
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

Edit `.env` to customize:
- API keys (Groq, Google Gemini)
- Default models
- Server settings
- Voice parameters

## Tech Stack

- **Speech-to-Text**: Faster-Whisper, Transformers
- **LLM**: Gemini, Groq, TinyLlama (fallback)
- **Text-to-Speech**: Edge-TTS, gTTS, Piper
- **Interface**: Gradio

## Troubleshooting

**Python version warning**: Upgrade to Python 3.10+ recommended
**API errors**: Check your `.env` file has valid keys
**Import errors**: Make sure you run with `python3 -m src.main`

## License

MIT
