
def rewrite_prompt(user_input):
    emotional_categories = {
        "焦慮": "你的訊息透露出一種焦慮或不安的情緒。我們先一起釐清你遇到的情境與問題。",
        "憤怒": "這段話中包含強烈的不滿或憤怒，我會協助你釐清問題並聚焦在具體事件上。",
        "憂鬱": "這段話可能隱含較深的情緒低落，我們先理性討論發生了什麼，協助你釐清情緒來源。",
        "羞愧": "你提到的內容可能帶有羞愧或自責感，我會幫你以中立的視角釐清事件，避免自責過度。"
    }

    for emotion, preface in emotional_categories.items():
        if any(word in user_input for word in ["好焦慮", "壓力好大", "我怕", "緊張", "心跳很快"]) and emotion == "焦慮":
            return f"{preface}請根據以下問題提供清楚建議：『{user_input}』你是怎麼想的？"
        elif any(word in user_input for word in ["我受夠了", "超級爛", "氣死我", "爛透了", "不能忍"]) and emotion == "憤怒":
            return f"{preface}請根據以下問題提供清楚建議：『{user_input}』你會怎麼理解這段情緒？"
        elif any(word in user_input for word in ["我不想活", "好累", "沒用", "無助", "沒人懂"]) and emotion == "憂鬱":
            return f"{preface}我們不急著解決問題，請協助分析這句話透露的內在狀態：「{user_input}」"
        elif any(word in user_input for word in ["對不起", "都是我不好", "我很丟臉", "不敢講"]) and emotion == "羞愧":
            return f"{preface}請協助客觀釐清以下話語可能產生的誤解與背景：「{user_input}」"

    return f"請根據以下問題提供清楚建議：『{user_input}』你是怎麼想的？"
