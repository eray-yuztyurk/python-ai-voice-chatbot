"""
Speech-to-Text (STT) Inference Module
"""
from transformers import pipeline
from src.config.ai_model_names import transformers_whisper_stt_models, faster_whisper_stt_models, stt_models
from faster_whisper import WhisperModel
import gradio as gr

stt_transformers_loaded_models = {}
stt_faster_whisper_loaded_models = {}

def load_stt_transformers_model(model_name):
    """
    Load a Whisper STT model from Hugging Face Transformers.
    Args:
        model_name (str): The name of the model to load.
    Returns:
        pipeline: The loaded STT pipeline.
    """

    if model_name in stt_transformers_loaded_models:
        pipeline_stt = stt_transformers_loaded_models[model_name]
        return pipeline_stt
    
    else:
        model_id = transformers_whisper_stt_models.get(model_name)
        pipeline_stt = pipeline(
            "automatic-speech-recognition", 
            model=model_id,
            chunk_length_s=30,
            )

        stt_transformers_loaded_models[model_name] = pipeline_stt
        return pipeline_stt

def load_stt_faster_whisper_model(model_name):
    """
    Load a Faster-Whisper STT model.
    Args:
        model_name (str): The name of the model to load.
    Returns:
        WhisperModel: The loaded Faster-Whisper model.
    """

    if model_name in stt_faster_whisper_loaded_models:
        model = stt_faster_whisper_loaded_models[model_name]
        return model
    
    else:
        model_id = faster_whisper_stt_models.get(model_name)
        model = WhisperModel(model_id)

        stt_faster_whisper_loaded_models[model_name] = model
        return model
    
def stt_transformers_inference(model_name, audio_file_path):
    """
    Transcribe audio using HuggingFace Transformers Whisper models.
    
    Args:
        model_name (str): Name of the Whisper model to use
        audio_file_path (str): Path to audio file
        
    Returns:
        str: Transcribed text or error message
    """
    try:
        pipeline_stt = load_stt_transformers_model(model_name)
        model_output = pipeline_stt(audio_file_path, batch_size=16, return_timestamps=True)

        transcribed_text = model_output['text']
        return transcribed_text

    except Exception as e:
        return f"Error during STT inference: {str(e)}"
    
def stt_faster_whisper_inference(model_name, audio_file_path):
    """
    Transcribe audio using optimized Faster-Whisper models (CTranslate2).
    
    Args:
        model_name (str): Name of the Faster-Whisper model to use
        audio_file_path (str): Path to audio file
        
    Returns:
        str: Transcribed text or error message
    """

    try:
        model = load_stt_faster_whisper_model(model_name)
        segments, info = model.transcribe(audio_file_path)

        transcribed_text = " ".join([segment.text for segment in segments])
        return transcribed_text

    except Exception as e:
        return f"Error during STT inference: {str(e)}"

def stt_inference(model_name, audio_file_path):
    """
    Main STT entry point - automatically routes to correct model type.
    
    Args:
        model_name (str): Model name (determines Faster-Whisper vs Transformers)
        audio_file_path (str): Path to audio file to transcribe
        
    Returns:
        str: Transcribed text
    """

    if "faster-whisper" in model_name.lower():
        return stt_faster_whisper_inference(model_name, audio_file_path)
    else:
        return stt_transformers_inference(model_name, audio_file_path)
