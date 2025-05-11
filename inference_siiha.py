
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from peft import PeftModel
import torch
from prompt_rewriter import rewrite_prompt

def load_model():
    model_id = "DEBBY-YEH/zephyr-7b-lora-debby-v1"
    base_model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    return base_model, tokenizer

def generate_response(user_input, model, tokenizer):
    rewritten_input = rewrite_prompt(user_input)
    system_prompt = "你是一位友善、理性、支持性強的台灣指令助理，請以繁體中文回答以下內容："
    full_prompt = f"{system_prompt}\n\n{rewritten_input}"

    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        top_k=50,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("：", 1)[-1].strip()


