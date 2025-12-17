"""
AI Voice Chatbot - Main Entry Point
Launches the Gradio web interface with configured settings
"""

if __name__ == "__main__":
    from src.api.gradio_app import _ui
    from src.config.settings import SERVER_HOST, SERVER_PORT, OPEN_BROWSER

    _ui.launch(
        server_name=SERVER_HOST, 
        server_port=SERVER_PORT, 
        inbrowser=OPEN_BROWSER
    )