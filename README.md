# 🤖 SIIHA: Self-Improving Instructional HR Assistant (Zephyr-7B-LoRA)

SIIHA is a Taiwan-based, human-centered AI assistant designed to enhance workplace reflection, emotional alignment, and fair HR decision-making — built on a fine-tuned Zephyr-7B language model (via LoRA). The system prioritizes linguistic sensitivity, cultural nuance, and emotional grounding in Mandarin Chinese.

---

## ✨ Key Features

- 🧠 **Instruction-tuned base**: Fine-tuned on HR and workplace communication tasks using Zephyr-7B.
- 💬 **Traditional Chinese support**: Accepts and responds in Traditional Mandarin.
- 🧘 **Culturally adapted tone**: Calm, reflective, and guidance-oriented — aligned with Taiwanese workplace dynamics.
- 😌 **Emotion-aware rewriting**: Auto-detects user sentiment and rewrites inputs based on four emotional dimensions:
  - Anxiety
  - Anger
  - Sadness
  - Shame
- 🔄 **Self-improvement ready**: Designed for future integration of feedback logging and SFT retraining loops.

---

## 🧠 Dialogue Handling & Emotion Adaptation

To ensure psychological safety in emotionally intense workplace queries, SIIHA includes a prompt rewriting module that adapts user input tone before generation.  
Example transformation (input → rewritten prompt):

> Original: `這什麼爛制度，升遷根本沒公平！`  
> Rewritten: `這個情境讓您感受到衝突與不滿。我會幫您客觀整理問題。請先描述具體事件：「這什麼爛制度，升遷根本沒公平！」`

---

## 🧪 Example Prompt

Input
```bash
User: 請幫我設計一段人資新人入職歡迎詞。
```

Output
```markdown
歡迎您加入團隊！我們重視每一位夥伴的貢獻，期待與您共同成長、實現組織的願景與價值。
```

## 🖼 Demo Preview
![SIIHA Demo](https://huggingface.co/spaces/DEBBY-YEH/zephyr-7b-tw-siiha-demo/+/raw/main/siiha_demo.png)

👉 [Try it live on Hugging Face Space](https://huggingface.co/spaces/DEBBY-YEH/zephyr-7b-tw-siiha-demo)

## 🧱 Tech Stack
- 🤖 HuggingFaceH4/zephyr-7b-beta as base model
- 🔧 LoRA fine-tuning with peft
- 🧭 Prompt rewriting + sentiment classification with Erlangshen-Roberta-110M-Sentiment
- 🌐 Gradio UI frontend for interactive testing
- 📘 Built for real-world Mandarin HR inputs in Taiwan

## 🔭 Future Plans
- 🔄 Feedback logging + retraining loop integration
- 🌍 Expandable to other Asian workplace cultures and languages
- 📊 Responsible AI extensions for workplace fairness metrics

## 👩‍💻 Creator
Debby Yeh｜NLP engineer candidate (Taiwan), designing fair, context-aware HR systems through AI.
🔗 [Portfolio (Notion)](https://mango-mapusaurus-5df.notion.site/debby-yeh-portfolio?pvs=4)｜🔗 [Hugging Face](https://huggingface.co/DEBBY-YEH)｜🔗 [Medium](https://medium.com/@debby.yeh1994)

“In emotionally charged workplaces, most HR systems go silent.
SIIHA listens — and responds with care.”
