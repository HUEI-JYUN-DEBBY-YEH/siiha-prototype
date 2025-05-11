import os
import datetime
from huggingface_hub import HfApi

def upload_logs():
    if not os.path.exists("logs.jsonl"):
        print("❌ logs.jsonl not found. Skipping upload.")
        return

    # Load token from environment variable
    token = os.environ.get("HF_WRITE_TOKEN")
    if not token:
        print("❌ HF_WRITE_TOKEN not set in Space secrets.")
        return

    api = HfApi(token=token)

    # Load logs content
    with open("logs.jsonl", "r", encoding="utf-8") as f:
        content = f.read()

    # Generate dated file name
    today = datetime.date.today().strftime("%Y%m%d")
    target_path = f"logs/logs_{today}.jsonl"

    # Upload to the dataset repo
    api.upload_file(
        path_or_fileobj=content,
        path_in_repo=target_path,
        repo_id="DEBBY-YEH/siiha-feedback-logs",
        repo_type="dataset"
    )

    print(f"✅ Successfully uploaded logs to {target_path}")

# Run immediately at startup
upload_logs()
