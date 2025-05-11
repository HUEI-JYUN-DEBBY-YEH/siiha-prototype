def rewrite_prompt(user_input:str):
    emotional_patterns = {
        "焦慮": {
            "keywords": ["好焦慮", "壓力好大", "我怕", "緊張", "心跳很快"],
            "preface": "你的訊息透露出一種焦慮或不安的情緒。我們先一起釐清你遇到的情境與問題。"
        },
        "憤怒": {
            "keywords": ["我受夠了", "超級爛", "氣死我", "爛透了", "不能忍"],
            "preface": "這段話中包含強烈的不滿或憤怒，我會協助你釐清問題並聚焦在具體事件上。"
        },
        "憂鬱": {
            "keywords": ["我不想活", "好累", "沒用", "無助", "沒人懂"],
            "preface": "這段話可能隱含較深的情緒低落，我們先理性討論發生了什麼，協助你釐清情緒來源。"
        },
        "羞愧": {
            "keywords": ["對不起", "都是我不好", "我很丟臉", "不敢講"],
            "preface": "你提到的內容可能帶有羞愧或自責感，我會幫你以中立的視角釐清事件，避免自責過度。"
        }
    }

    for category, content in emotional_patterns.items():
        if any(word in user_input for word in content["keywords"]):
            preface = content["preface"]
            return f"{preface}請根據以下問題提供清楚建議：『{user_input}』你是怎麼想的？"

    return f"請根據以下問題提供清楚建議：『{user_input}』你是怎麼想的？"
