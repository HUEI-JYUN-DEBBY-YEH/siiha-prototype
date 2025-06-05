# 🤖 SIIHA × Gemini × Notion Integration

This prototype demonstrates how **SIIHA** (System for Intent-Informed Human Assistance) integrates **Google Gemini API** with **Notion**, enabling a human-centered conversational assistant that can:

- Detect user intent from natural language queries
- Trigger structured task generation using Gemini function calling
- Automatically log task plans and fallback responses into Notion for traceability and emotion-aware feedback

---

## 🌟 Key Features

### 🧠 1. Conversational Task Flow with Gemini
- Supports open-ended inputs like:
  - _"We need two engineering interns this summer"_
  - _"Help me design a JD for backend engineers"_
- Gemini interprets intent and triggers structured plans.

### 📥 2. Notion Auto-Logging
- All inputs and outputs are written into a Notion database.
- Columns include:
  - `Title`
  - `Task`
  - `Category`
  - `Generated Plan` (fallback answers from Gemini)
  - `Notes` (for long content > 2000 chars)
  - `User Message`, `Intent`, `Created Date`

### 💡 3. Fallback-Aware Logging
- Even when Gemini cannot classify the intent (e.g., returns `unknown`), fallback answers are captured and pushed to Notion.
- Ensures no user query is lost.

---

## 🛠️ Folder Overview

| File | Description |
|------|-------------|
| `siiha_gemini_english_demo.py` | Main Gradio-based chat interface |
| `functions.py` | Intent routing and Gemini function schemas |
| `notion_api.py` | Handles Notion database write operations with length-aware slicing |
| `create_notion_db.py` | Script to preconfigure a compatible Notion database |
| `*.mp4` | Demo screen recordings of different scenarios |
| `siiha_gemini_notion_flowchart.png` | Integration architecture diagram |

---

## 🎥 Demo Videos

| Scenario | Demo Link |
|----------|-----------|
| Emotional Support Fallback | `SIIHA_Gemini_Notion_Integration_EmotionSupportDemo.mp4` |
| Clear Task Detection | `SIIHA_Gemini_Notion_Integration_TaskAssistantDemo.mp4` |
| Unspecified Queries | `SIIHA_Gemini_Notion_Integration_UnspecifiedTasksDemo.mp4` |

---

## 🧭 Use Cases

- HR and team leaders capturing unclear or evolving needs
- Conversational tracking of workplace emotional signals
- Structured planning in cross-cultural or multilingual contexts

---

## 🔧 Setup Instructions

1. Create a `.env` file with your keys:
```env
GOOGLE_API_KEY=your-gemini-api-key
NOTION_TOKEN=your-notion-token
NOTION_DATABASE_ID=your-database-id

2. Install dependencies:
```
pip install -r requirements.txt

3. Run the demo locally:
```
python siiha_gemini_english_demo.py

## 🧭 Credits & Vision
This is part of the 願筆三部曲技術展示計畫, a human-centered AI research and design initiative by Debby Yeh.
We believe AI should listen before it acts, and this prototype explores how intent understanding, fallback reflection, and emotional logging can co-exist in responsible AI systems.

## 📬 Contact & Contributions
For collaborations or feedback, feel free to reach out via LinkedIn[https://www.linkedin.com/in/debbyyeh/] or open a PR/discussion.