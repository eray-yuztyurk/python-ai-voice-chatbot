import os
import tempfile
import time
import scipy.io.wavfile as wav

from src.services.stt import stt_inference
from src.services.llm import chat_with_llm, llm_initializer_with_fallback
from src.services.tts import tts_converter_with_fallback
from src.config.settings import DEFAULT_STT_MODEL

print("🔄 Initializing LLM...")
llm_model = llm_initializer_with_fallback()

auto_audio = True

def transcribe_audio(audio_input):
    """
    Convert recorded audio from microphone to text.
    
    Args:
        audio_input (tuple): (sample_rate, audio_array) from Gradio Audio component
        
    Returns:
        str: Transcribed text or error message
    """
    if audio_input is None:
        return ""
    
    sample_rate, audio_array = audio_input
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_audio.name, sample_rate, audio_array)
    
    user_text = stt_inference(DEFAULT_STT_MODEL, temp_audio.name)
    os.remove(temp_audio.name)
    
    return user_text if user_text else "❌ Could not transcribe audio"


def process_query(text_input, auto_voice_response=True):
    """
    Process user query through LLM and generate audio response.
    
    Args:
        text_input (str): User's text query
        auto_voice_response (bool): Whether to auto-play audio response
        
    Returns:
        tuple: (response_text, audio_file_path)
    """
    
    global auto_audio
    auto_audio = auto_voice_response

    if not text_input or not text_input.strip():
        return "⚠️ Please provide text input", None
    
    user_text = text_input.strip()
    
    llm_response = chat_with_llm(user_text, llm_model)
    if not llm_response or llm_response.startswith("❌"):
        return llm_response, None
    
    output_filename = f"response_{int(time.time())}"
    audio_path = tts_converter_with_fallback(output_filename, llm_response)
    
    return llm_response, audio_path