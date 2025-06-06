# 🧠 SIIHA × Gemini Function Calling × Notion Integration

This prototype demonstrates how to build a task-based HR assistant that understands emotion, supports undefined queries, and logs user–LLM interactions to Notion for review.

> 📍 This is part of the [SIIHA願筆三部曲 Trilogy](https://medium.com/@debby.yeh1994/from-chatbots-to-emotional-systems-why-i-designed-with-feeling-first-495ee3d0d674), showing how human-centered AI design can create systems of trust, care, and cultural resonance.

---

## 🌟 Key Features

### 🧠 Gemini Pro 1.5 API Integration

* Understands diverse HR-related inputs
* Triggers fallback mode for non-task queries
* Returns both direct answers and task-based routing intents

### ⚙️ Function Calling Agent Architecture

* Uses custom rule-based intent router (recruitment, emotion support, unknown...)
* Each intent connects to a corresponding function (e.g. intern recruitment planning)
* Supports fallback response generation when the input is too vague or broad

### 📝 Notion Database Logging

* All queries are logged to Notion, including:

  * Task description
  * Intent classification
  * Gemini-generated response
  * User message (if applicable)
* If the generated response exceeds 2000 characters, the excess is stored in a `Notes` column

---

## 🧪 Demo Scenarios (SIIHA Agent)

### ✅ Supported Tasks

| Type              | Example Input                           | Gemini Action                 |
| ----------------- | --------------------------------------- | ----------------------------- |
| Task - Recruiting | “I want to recruit two interns.”        | Triggers `recruit_interns()`  |
| Emotional Support | “Can I tell you how I’m feeling today?” | Triggers `emotion_response()` |

### 🟨 Fallback Handling (Still Supported)

| Type         | Example Input                   | Gemini Action + Notion Logging       |
| ------------ | ------------------------------- | ------------------------------------ |
| Unspecified  | “Tell me about your story”      | Gemini generates empathetic response |
| Vague JD Ask | “Give me examples of a good JD” | Gemini returns best practices        |

### ❌ Unsupported Yet (future work)

| Type               | Example Input                  | Limitation             |
| ------------------ | ------------------------------ | ---------------------- |
| Specific API Query | “Connect me to HR system X”    | Not implemented        |
| Policy automation  | “Auto-reply when people apply” | No webhook trigger yet |

---

## 🧱 File Structure

```
├── siiha_gemini_english_demo.py        # Main Gradio UI
├── functions.py                         # Task-specific function handlers
├── notion_api.py                        # Notion API writing utility
├── create_notion_db.py                 # (Optional) Auto-create Notion DB
├── config.py                            # API keys and DB ID config
├── *.mp4                                # Demo screen recordings
└── siiha_gemini_notion_flowchart.png    # System diagram
```

---

## 🌐 Notion Schema Reference

| Column         | Type      | Description                                |
| -------------- | --------- | ------------------------------------------ |
| Name           | Title     | Task title                                 |
| Task           | Rich text | Input instruction                          |
| Category       | Select    | Routing category (Recruitment, Emotion...) |
| Intent         | Rich text | Detected intent label                      |
| User Message   | Rich text | Raw user message (if separated)            |
| Generated Plan | Rich text | Gemini response                            |
| Notes          | Rich text | Extra overflow text (if >2000 char)        |
| Created        | Date      | Auto timestamp                             |

---

## 📹 Demo Videos

* \[1/3] Emotion Support Scenario – *"tell me about your story"*
* \[2/3] Recruitment Planner – *"I want to recruit two interns"*
* \[3/3] Handling vague input – *"give me examples of good JD bullet points"*

> See all videos in the repo or in this [Medium writeup](https://medium.com/@debby.yeh1994/🛠️-prototyping-trust-building-human-centered-workflows-with-gemini-notion-8d9ceb528653)

---

## 🔗 Related Medium Trilogy

* (1/3) [From Chatbots to Emotional Systems](https://medium.com/@debby.yeh1994/from-chatbots-to-emotional-systems-why-i-designed-with-feeling-first-495ee3d0d674)
* (2/3) [From Taiwan with Listening: An Asian Response to AI Ethics](https://medium.com/@debby.yeh1994/2-3-from-taiwan-with-listening-an-asian-response-to-ai-ethics-siiha-%E9%A1%98%E7%AD%86%E4%B8%89%E9%83%A8%E6%9B%B2%E4%B9%8B%E4%BA%8C-%E4%BA%9E%E6%B4%B2%E6%96%87%E5%8C%96%E7%9A%84%E5%82%BE%E8%81%BD%E6%99%BA%E6%85%A7-%E5%A6%82%E4%BD%95%E5%9B%9E%E6%87%89-ai-59f443e793f2)
* (3/3) [Prototyping Trust: Building Human-Centered Workflows with Gemini + Notion](https://medium.com/@debby.yeh1994/3-3-prototyping-trust-building-human-centered-workflows-with-gemini-notion-siiha-%E9%A1%98%E7%AD%86%E4%B8%89%E9%83%A8%E6%9B%B2%E4%B9%8B%E4%B8%89-%E8%AE%93-ai-cca5f33052c5)

---

## 💌 Credits

Created by [Debby Yeh](https://www.linkedin.com/in/debby-yeh/), as part of the **願筆召見計畫** and the 3-part series on emotionally intelligent AI.
