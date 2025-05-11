from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

class EmotionClassifier:
    def __init__(self):
        self.model_id = "IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_id)
        self.labels = ["negative", "neutral", "positive"]  # 轉換為台灣語境對應見下方函式

    def predict_emotion(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        probs = F.softmax(logits, dim=1)[0]
        pred = torch.argmax(probs).item()
        return self._map_label(self.labels[pred])

    def _map_label(self, label):
        # 可對應為 ['正向', '中性', '負面'] or 更細緻分類
        if label == "positive":
            return "正向"
        elif label == "neutral":
            return "中性"
        else:
            return "情緒偏激"

# 建立實例
emotion_classifier = EmotionClassifier()