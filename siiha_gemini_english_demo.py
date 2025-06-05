import google.generativeai as genai
import gradio as gr
from config import GOOGLE_API_KEY
from notion_api import write_task_to_notion
from functions import (
    query_leave_policy,
    schedule_meeting,
    generate_kpi,
    recruit_interns,
    respond_to_emotion
)

# Initialize Gemini
genai.configure(api_key=GOOGLE_API_KEY)
print("[Debug] Current GOOGLE_API_KEY =", GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Intent map
functions = {
    "leave": query_leave_policy,
    "meeting": lambda: schedule_meeting("HR Strategy Discussion"),
    "kpi": lambda: generate_kpi("recruiter"),
    "intern": recruit_interns,
    "emotion": respond_to_emotion
}

def detect_intent(user_input):
    user_input = user_input.lower()
    for intent in functions:
        if intent in user_input:
            return intent
    return None

# Gemini fallback
def gemini_fallback(user_input):
    print("[Gemini] Triggered fallback for:", user_input)
    try:
        # Step 1: Intent classification
        classification_prompt = (
            f"You are an intent classifier for an HR assistant. Given the input: '{user_input}', "
            "choose the most likely intent from this list: leave, meeting, kpi, intern, emotion.\n"
            "Respond with just the intent keyword. If uncertain, respond with 'unknown'."
        )
        classification_response = model.generate_content(classification_prompt)
        intent = classification_response.text.strip().lower()
        print("[Gemini] API response text:", classification_response.text)
        print("[Gemini] Predicted intent:", intent)

        # Step 2a: If known intent, call mapped function
        if intent in functions:
            return functions[intent](), intent

        # Step 2b: If unknown, generate answer anyway
        answer_prompt = (
            f"You are a helpful HR assistant. Answer the following user question as best as you can:\n\n"
            f"User: {user_input}"
        )
        answer_response = model.generate_content(answer_prompt)
        final_answer = answer_response.text.strip()
        print("[Gemini] Final fallback answer:", final_answer)
        return final_answer, intent

    except Exception as e:
        print("[ERROR] Gemini fallback failed:", e)
        return "Sorry, I couldn’t process that.", "error"


# Unified agent
def siiha_agent(user_input):
    intent = detect_intent(user_input)
    if intent:
        print(f"[Routing] Matched rule intent: {intent}")
        response = functions[intent]()
        return response, intent
    return gemini_fallback(user_input)

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 SIIHA × Gemini: Task-Based HR Agent")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your message", placeholder="e.g., I’m feeling burned out this week...")

    def respond(message, chat_history):
        response, intent = siiha_agent(message)

        # Log into Notion
        try:
            print("[SIIHA] Logging interaction to Notion...")
            write_task_to_notion(
                title=message,
                task_description=message,
                category=intent or "unknown",
                generated_plan=f"[🤖 Gemini Answer]\n{response}" if intent == "unknown" else response,
                user_message=message,
                intent=intent or "unknown"
            )
        except Exception as e:
            print("[SIIHA] Notion write failed:", e)

        chat_history.append((message, response))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
