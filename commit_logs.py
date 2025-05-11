from huggingface_hub import upload_file
from pathlib import Path
import os
import datetime

token = os.getenv("HF_WRITE_TOKEN")
if not token:
    raise ValueError("❌ HF_WRITE_TOKEN 環境變數未設置")

log_path = Path("logs.jsonl")
if not log_path.exists():
    raise FileNotFoundError("❌ logs.jsonl 不存在，無法上傳")

today = datetime.date.today().strftime("%Y%m%d")
target_file = f"logs/logs_{today}.jsonl"

upload_file(
    path_or_fileobj=str(log_path),
    path_in_repo=target_file,
    repo_id="DEBBY-YEH/siiha-feedback-logs",
    repo_type="dataset",
    token=token
)

print(f"✅ 已成功上傳 {target_file} 至 Hugging Face Dataset Repo")
