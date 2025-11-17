import os
import google.generativeai as genai
import gradio as gr

# Load API Key from HuggingFace Secret
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# System prompt
SYSTEM_PROMPT = """
You are LuckyCode, an AI Code Assistant created by Laxman.
You explain coding concepts, debug errors, and generate code.
Always provide clean, accurate, and beginner-friendly answers.
"""

# Conversation history
history = [SYSTEM_PROMPT]

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    response = model.generate_content(final_prompt)

    # Return text response
    return response.text if hasattr(response, "text") else str(response)

# Gradio UI
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=5, label="Enter your prompt"),
    outputs=gr.Textbox(lines=12, label="Response"),
    title="LuckyCode AI Assistant",
    description="A Gemini-powered AI Code Assistant created by Laxman"
)

interface.launch()
