# 🤖 SIIHA: Self-Improving Instructional HR Assistant (Zephyr-7B-LoRA)

A Taiwan-based, human-centered AI assistant designed to support workplace learning, emotional alignment, and fair HR practices — powered by a Zephyr-7B language model fine-tuned with LoRA.

---

## ✨ Features

- 🧠 **Instruction-following SFT base**: Fine-tuned on HR, workplace, and communication tasks
- 💬 **Supports Traditional Chinese prompts**
- 😌 **Emotion-aware prompting**: Dynamically rewrites user queries based on emotional tone (e.g., anxiety, anger, sadness, shame)
- 🔄 **Self-improving loop ready**: Designed for future feedback logging and retrainability

---

## 🗂 Example Prompts

### ➤ 中文輸入（正向）
```
請幫我設計一段人資新人入職歡迎詞。
```

### ➤ 情緒偏激（憤怒）
```
這什麼爛制度，升遷根本沒公平！
```
➡️ 轉寫後送入模型：
```
看起來這個情境確實讓您感受到一些衝突與不滿，我會保持客觀地幫您整理問題。
請您先描述一下具體的事件或背景：「這什麼爛制度，升遷根本沒公平！」
```

---

## 🧱 Tech Stack

- `HuggingFaceH4/zephyr-7b-beta` base model
- `peft` + LoRA 微調：`DEBBY-YEH/zephyr-7b-lora-debby-v1`
- 中文情緒分類模型：`IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment`
- Gradio 前端部署

---

## 🔮 Future Plans

- [ ] Feedback logging via thumbs-up/down
- [ ] Self-retrain data bootstrapping loop
- [ ] Multilingual or domain-specific versions

---

## 👤 Creator
**Debby Yeh**｜Taiwan-based NLP engineer candidate exploring AI for fairer HR systems

[🔗 Portfolio](https://www.notion.so/Debby-Yeh-NLP-Application-Engineer-Portfolio-1ca5118474d2801caa58de564fb53e38?pvs=4)｜[🔗 Hugging Face](https://huggingface.co/DEBBY-YEH)｜[🔗 Medium](https://medium.com/@debby_yeh)
