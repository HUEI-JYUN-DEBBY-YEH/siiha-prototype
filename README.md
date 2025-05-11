# 🤖 SIIHA: Self-Improving Instructional HR Assistant (Zephyr-7B-LoRA)
A Taiwan-based, human-centered AI assistant designed to support workplace learning, emotional alignment, and fair HR practices — powered by a Zephyr-7B language model fine-tuned with LoRA.

## ✨ Features
🧠 Instruction-following SFT base: Fine-tuned on HR, workplace, and communication tasks
💬 Supports Traditional Chinese prompts
🧘 Taiwanese conversational persona: Warm, neutral tone that invites reflection and respects cultural nuances
😌 Emotion-aware prompting: Dynamically rewrites user queries based on emotional tone (anxiety, anger, sadness, shame)
🔄 Self-improving loop ready: Designed for future feedback logging and retrainability

## 🧠 Dialogue Style & Language Enhancement
為了更貼合台灣職場文化與安全互動場景，SIIHA 採用以下語調與處理方式：

###🤖 台灣語境人格調整（中性 × 指導式）
- 全面採用 繁體中文 回應
- 使用 中性溫和、具指導性語氣，鼓勵使用者釐清問題而非立即下結論
- 針對使用者情緒不穩定時，不急於認同或貼標籤，避免誤導

### 🧠 Prompt Rewriting × 情緒辨識
系統內建情緒辨識與 Prompt Rewriter，根據輸入語氣自動轉寫，再送入模型：

支援四大情緒細類：
- 焦慮（Anxiety）：幫助釐清焦慮來源，引導更穩定描述
- 憤怒（Anger）：引導理性表述，避免強化對立語言
- 憂鬱（Sadness）：溫和回應並鼓勵說出具體經歷
- 羞愧（Shame）：保持尊重與自我肯定語氣，避免傷害信心

## 🗂 Example Prompts
➤ 中文輸入（正向）
```bash
請幫我設計一段人資新人入職歡迎詞。
```
➤ 情緒偏激（憤怒）
```bash
這什麼爛制度，升遷根本沒公平！
```
➡️ 轉寫後送入模型：
```
看起來這個情境確實讓您感受到一些衝突與不滿，我會保持客觀地幫您整理問題。
請您先描述一下具體的事件或背景：「這什麼爛制度，升遷根本沒公平！」
```

## 🧱 Tech Stack
- HuggingFaceH4/zephyr-7b-beta base model
- peft + LoRA 微調：DEBBY-YEH/zephyr-7b-lora-debby-v1
- 中文情緒分類模型：IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment
- Prompt rewriter 語氣引導模組
- Gradio 前端部署

##🔮 Future Plans
- Feedback logging via thumbs-up/down
- Self-retrain data bootstrapping loop
- Multilingual or domain-specific versions

## 👤 Creator
Debby Yeh｜Taiwan-based NLP engineer candidate exploring AI for fairer HR systems
🔗 Portfolio｜🔗 Hugging Face｜🔗 Medium