# commit_logs.py
from huggingface_hub import upload_file
from pathlib import Path
import os

# 讀取 Hugging Face token
token = os.getenv("HF_WRITE_TOKEN")
if not token:
    raise ValueError("❌ HF_WRITE_TOKEN 環境變數未設置")

# 資料集目標資訊
repo_id = "DEBBY-YEH/siiha-feedback-logs"
path = Path("logs.jsonl")

# 檢查檔案存在
if not path.exists():
    raise FileNotFoundError("❌ logs.jsonl 不存在，無法上傳")

# 上傳 logs.jsonl
upload_file(
    path_or_file=path,
    path_in_repo="logs.jsonl",  # 可以改名成含時間戳記的 logs 檔案
    repo_id=repo_id,
    repo_type="dataset",
    token=token,
    overwrite=True,
)
