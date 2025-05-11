
import gradio as gr
from inference_siiha import load_model, generate_response

model, tokenizer = load_model()

def chat_with_siiha(user_input):
    return generate_response(user_input, model, tokenizer)

with gr.Blocks() as demo:
    gr.Markdown("""
    # 🤖 SIIHA Demo Assistant
    由 Zephyr-7B LoRA 微調而成的指令型助理，可回應具台灣語境的任務指示
    """)
    with gr.Row():
        input_text = gr.Textbox(label="user_input", lines=5, placeholder="請輸入一段職場對話、情緒反應或請求")
        output_text = gr.Textbox(label="output", lines=5)
    with gr.Row():
        clear_btn = gr.Button("清除")
        submit_btn = gr.Button("提交")

    submit_btn.click(fn=chat_with_siiha, inputs=input_text, outputs=output_text)
    clear_btn.click(fn=lambda: ("", ""), inputs=[], outputs=[input_text, output_text])

demo.launch()
