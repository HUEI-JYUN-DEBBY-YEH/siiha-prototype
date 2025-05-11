# prompt_rewriter.py

def rewrite_prompt(user_input, emotion_label):
    """
    根據分類後的情緒標籤，轉換輸入語氣以利模型更穩定生成。
    """
    if emotion_label == "正向":
        return user_input

    elif emotion_label == "中性":
        return f"使用者提問：「{user_input}」\n請以專業、條列式方式提供清楚說明。"

    elif emotion_label == "焦慮":
        return (
            "我知道這件事可能讓人感到不確定，我會陪你一步步釐清。\n"
            f"我想先請問：在這個狀況中，您最關注的部分是什麼？\n「{user_input}」"
        )

    elif emotion_label == "憤怒":
        return (
            "看起來這個情境確實讓您感受到一些衝突與不滿，我會保持客觀地幫您整理問題。\n"
            f"請您先描述一下具體的事件或背景：「{user_input}」"
        )

    elif emotion_label == "憂鬱":
        return (
            "我明白有些時候會讓人覺得停滯或低落，我會試著幫您從現況找出可能的出口。\n"
            f"請問您遇到的具體難點是什麼？\n「{user_input}」"
        )

    elif emotion_label == "羞愧感":
        return (
            "有些情境確實會讓人懷疑自己的表現，但我們可以回到事件本身來釐清。\n"
            f"能否請您先描述一下那個當下的具體互動？\n「{user_input}」"
        )

    else:
        # 若模型無法判斷，預設為中性處理
        return f"請根據以下問題提供清楚建議：「{user_input}」"
