# SIIHA: A Human-Centered HR Assistant Using Gemini Function Calling

SIIHA (System for Integrated Interaction in Human-centered Assistance) is a multilingual HR agent powered by Gemini API. It handles real-world employee requests with structured reasoning, function calling, and emotionally aware responses.

This prototype is designed to demonstrate:
- Multi-function orchestration using Gemini Pro
- Natural, warm interaction in English and Mandarin
- Human-centered applications of LLMs in HR

## 1. Demo Video
Watch the demo:
[https://1drv.ms/v/c/c5ea358666ea3108/EcWSRbsVQftPhxQDFs2ZkcMBS-xLAne1j_DKansr70vfGw?e=FNY2z0]

## 2. Key Features
- Conversational Function Calling: Handles multi-intent tasks in a single query
- Emotion-Neutral Reply Design: Ensures psychological safety in workplace scenarios
- Custom Task Agent: Combines Gemini API with Python backend logic
- Bilingual Input Support: Optimized for Mandarin-English workplace queries

## 3. System Flow
- siiha_gemini_english_demo.py: Main demo interface (Gradio)
- functions/schema/*.json: OpenAPI-style function definitions
- task_agent.py: Reasoning + decision engine
- README.md: Current file

##　4. Quickstart
bash
```
git clone https://github.com/HUEI-JYUN-DEBBY-YEH/siiha-prototype.git
cd siiha-prototype
pip install -r requirements.txt
python siiha_gemini_english_demo.py
```
Then open http://127.0.0.1:7860 in your browser.

## 5. Why This Project Matters
This prototype was built to demonstrate how LLMs can enhance trust, clarity, and cultural sensitivity in everyday HR systems.

It is part of a broader vision — using AI not to replace human judgment, but to support fair, kind, and inclusive decision-making in organizations.g