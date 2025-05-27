import google.generativeai as genai
import gradio as gr

# Initialize Gemini
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-pro")

# Define warm, human-centered functions
def query_leave_policy():
    return ("Sure. According to Taiwan’s Labor Standards Act, "
            "you accumulate one day of paid leave for each month of work. "
            "Would you like me to check your remaining balance?")

def schedule_meeting(topic):
    return (f"Got it! I’ve scheduled an HR meeting for you with the topic: ‘{topic}’. "
            "Let me know if you'd like to adjust the time or invite others.")

def generate_kpi(role):
    return (f"Absolutely. Here are three key performance indicators for a {role}:\n"
            "1. Task completion rate\n"
            "2. Internal communication satisfaction\n"
            "3. Timely project delivery\n"
            "Let me know if you'd like to tailor these to your team.")

# Routing function
def siiha_agent(user_input):
    user_input = user_input.lower()
    if any(kw in user_input for kw in ["vacation", "leave", "paid leave", "time off"]):
        return query_leave_policy()
    elif any(kw in user_input for kw in ["meeting", "schedule", "hr strategy"]):
        return schedule_meeting("HR Strategy Discussion")
    elif any(kw in user_input for kw in ["kpi", "performance", "recruiter", "metrics"]):
        return generate_kpi("recruiter")
    else:
        return "I'm here to support you. Could you rephrase that or give me a bit more context?"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 SIIHA × Gemini: A Human-Centered AI Agent for HR")
    gr.Markdown("Ask me anything about HR strategy, leave policies, or performance metrics.")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your message", placeholder="e.g., How many leave days do I have left?")

    def respond(message, chat_history):
        response = siiha_agent(message)
        chat_history.append((message, response))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
