
"""
Voice AI Chatbot - Gradio Interface
"""
from src.services.chatbot import transcribe_audio, process_query, auto_audio
import gradio as gr

with gr.Blocks(title="🎙️ Voice AI Chatbot") as _ui:
    gr.Markdown("<h1 align='center'>🎙️ Voice AI Chatbot</h1>")
    gr.Markdown("Record your voice or type text, then ask AI anything!")
    
    with gr.Row():
        with gr.Column():
            
            text_input = gr.Textbox(
                label="📝 Type your question",
                placeholder="Type your message or use voice recording...",
                lines=3
            )

            auto_voice_reply = gr.Checkbox(
                label="🔊 Auto-play voice response",
                value=True
            )
            
            with gr.Accordion("🎤 Leave your message as voice?", open=False):
                audio_input = gr.Audio(
                    sources=["microphone"],
                    type="numpy",
                    label="Record your voice message"
                )

            submit_btn = gr.Button("Ask AI 🚀", variant="primary")
        
        with gr.Column():
            response_text = gr.Textbox(
                label="💬 AI Response",
                lines=8,
                interactive=False
            )
            
            with gr.Accordion("🎤 Voice response", open=False):
                response_audio = gr.Audio(
                    label="🔊 Listen to response",
                    type="filepath",
                    autoplay=auto_audio
                )
    
    audio_input.change(
        fn=transcribe_audio,
        inputs=[audio_input],
        outputs=text_input
    )
    
    submit_btn.click(
        fn=process_query,
        inputs=[text_input, auto_voice_reply],
        outputs=[response_text, response_audio]
    )
