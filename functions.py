# functions.py

from notion_api import write_task_to_notion

# Define warm, human-centered functions
def query_leave_policy():
    return ("Of course. Based on Taiwan’s Labor Standards Act, "
            "you earn one day of paid leave for every full month you work. "
            "Would you like me to check your remaining balance or help with a leave application?")

def schedule_meeting(topic):
    return (f"Got it. I’ve prepared a draft for an HR meeting on: ‘{topic}’. "
            "Let me know if you'd like to change the time, format, or invite specific team members.")

def generate_kpi(role):
    return (f"Sure. Here are three suggested KPIs for a {role}:\n"
            "1. Task completion rate\n"
            "2. Internal communication effectiveness\n"
            "3. Project delivery timeliness\n"
            "Happy to help tailor them to your team’s context.")

def recruit_interns():
    print("[SIIHA] Calling Notion: recruit_interns")
    title = "Recruit 2 engineering interns"
    category = "Recruitment"
    generated_plan = "Target onboarding date: July"
    
    try:
        write_task_to_notion(title=title, category=category, generated_plan=generated_plan)
        print("[SIIHA] Notion write successful.")
    except Exception as e:
        print(f"[SIIHA] Notion write failed: {e}")
        
    return (
        "Understood. I can help you outline a hiring plan for 2 engineering interns, "
        "targeting July onboarding. Do you need help drafting the JD or coordinating interviews?"
    )

def respond_to_emotion():
    return ("Thank you for sharing. It sounds like you're under a lot of stress right now. "
            "Would you like to talk to someone, take a wellness day, or log a reflection note for now? "
            "I'm here to support you, not just with tasks, but with how you're feeling.")