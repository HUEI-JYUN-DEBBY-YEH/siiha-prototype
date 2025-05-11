from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch
from emotion_classifier import EmotionClassifier
from prompt_rewriter import rewrite_prompt

# 初始化情緒分類器
emotion_model = EmotionClassifier()

def load_model():
    base_model = "HuggingFaceH4/zephyr-7b-beta"
    lora_path = "DEBBY-YEH/zephyr-7b-lora-debby-v1"

    tokenizer = AutoTokenizer.from_pretrained(base_model, use_fast=True)
    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    model = PeftModel.from_pretrained(model, lora_path)

    return model.eval(), tokenizer

def generate_response(user_input, model, tokenizer):
    # 執行情緒分類
    emotion_label = emotion_model.predict_emotion(user_input)
    # 根據情緒調整 prompt
    rewritten_prompt = rewrite_prompt(user_input, emotion_label)

    # Tokenize 並產生回應
    inputs = tokenizer(rewritten_prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response
