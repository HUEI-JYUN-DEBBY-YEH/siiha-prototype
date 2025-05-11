import gradio as gr
from inference_siiha import load_model, generate_response

# 載入模型
model, tokenizer = load_model()

# 定義 Gradio 介面
def chat_with_siiha(user_input):
    return generate_response(user_input, model, tokenizer)

iface = gr.Interface(
    fn=chat_with_siiha,
    inputs=gr.Textbox(lines=4, placeholder="請輸入一段話，例如：可以幫我撰寫一封人資信件嗎？"),
    outputs="text",
    title="🤖 SIIHA Demo Assistant",
    description="由 Zephyr-7B LoRA 微調而成的指令型助理，可回應具台灣語境的任務指示",
)

if __name__ == "__main__":
    iface.launch()
