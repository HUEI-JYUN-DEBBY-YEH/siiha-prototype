# ✅ 實作 SIIHA 半自動化學習與紀錄模組
# 包含以下三功能：
# 1. 按讚（👍）與檢舉（⚠️）回饋按鈕
# 2. 將 rewired prompt + response 自動記錄到 logs.jsonl
# 3. 可延伸為未來自訓資料集

import gradio as gr
import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs.jsonl")

# 確保 logs.jsonl 檔案存在，避免初始化錯誤
if not LOG_FILE.exists():
    LOG_FILE.write_text("")
    try:
        import commit_logs
        print("✅ Log push completed.")
    except Exception as e:
        print("⚠️ Log push failed:", e)


# 初始化記錄函式
def log_interaction(user_input, rewritten_prompt, response, feedback):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_input": user_input,
        "rewritten_prompt": rewritten_prompt,
        "response": response,
        "feedback": feedback  # 'like', 'flag', or None
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

# 包裝主回應函式，加入 rewiring + 回應 + 記錄邏輯

def wrapped_generate(user_input):
    rewritten = rewrite_prompt(user_input)
    system_prompt = "你是一位友善、理性、支持性強的台灣指令助理，請以繁體中文回答以下內容："
    full_prompt = f"{system_prompt}\n\n{rewritten}"
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        top_k=50,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response_text = response.split("：", 1)[-1].strip()
    return rewritten, response_text

# Gradio UI 組件
def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("### 🧠 SIIHA Demo + Feedback")
        user_input = gr.Textbox(label="user_input")
        output = gr.Textbox(label="output")
        feedback_state = gr.State(value=None)

        with gr.Row():
            submit_btn = gr.Button("提交")
            like_btn = gr.Button("👍")
            flag_btn = gr.Button("⚠️")

        rewritten_box = gr.Textbox(visible=False)

        def run_and_show_feedback(text):
            rewritten, response = wrapped_generate(text)
            rewritten_box.value = rewritten
            return response, rewritten

        def feedback_click(feedback_type, input_text, output_text, rewritten):
            log_interaction(input_text, rewritten, output_text, feedback_type)
            return "已記錄 feedback！"

        submit_btn.click(run_and_show_feedback, inputs=user_input, outputs=[output, rewritten_box])
        like_btn.click(feedback_click, inputs=[gr.State("like"), user_input, output, rewritten_box], outputs=None)
        flag_btn.click(feedback_click, inputs=[gr.State("flag"), user_input, output, rewritten_box], outputs=None)

    return demo