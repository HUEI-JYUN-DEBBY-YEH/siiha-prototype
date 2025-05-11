# commit_logs.py
# ✅ 將 logs.jsonl 推送至 Hugging Face Datasets Repo: DEBBY-YEH/siiha-feedback-logs
# 使用 HF_TOKEN secret，自動上傳當日 log 檔

import os
import json
import shutil
from datetime import datetime
from huggingface_hub import HfApi, Repository

# === 設定 ===
HF_TOKEN = os.environ.get("HF_TOKEN")
REPO_ID = "DEBBY-YEH/siiha-feedback-logs"
LOCAL_LOG = "logs.jsonl"
LOCAL_CLONE_DIR = "_temp_dataset_repo"

# === 日期處理 ===
now = datetime.utcnow()
log_date_str = now.strftime("%Y%m%d")
remote_log_path = f"logs/logs_{log_date_str}.jsonl"

# === 步驟 1: Clone datasets repo ===
print("🔄 Cloning datasets repo...")
repo_url = f"https://{HF_TOKEN}@huggingface.co/datasets/{REPO_ID}"
repo = Repository(LOCAL_CLONE_DIR, clone_from=repo_url, use_auth_token=HF_TOKEN)
repo.git_pull()

# === 步驟 2: 複製 log 檔到指定位置 ===
print("📄 Copying log file...")
os.makedirs(os.path.join(LOCAL_CLONE_DIR, "logs"), exist_ok=True)
dest_path = os.path.join(LOCAL_CLONE_DIR, remote_log_path)
shutil.copyfile(LOCAL_LOG, dest_path)

# === 步驟 3: Commit + Push ===
print("🚀 Committing and pushing...")
repo.git_add([dest_path])
repo.git_commit(f"Add log {log_date_str}")
repo.git_push()

print(f"✅ Uploaded logs to: {REPO_ID}/{remote_log_path}")
