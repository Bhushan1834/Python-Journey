import os
import time
from datetime import datetime

# =========================
# 🔧 SETTINGS (EDIT THIS)
# =========================
REPO_PATH = REPO_PATH = r"D:\All_language\python project\Python-Journey"
   # <-- Apna repo path daalo
COMMITS_PER_DAY = 3                                   # <-- Kitne commits per day?
COMMIT_MESSAGE = "Daily auto commit 🤖"

# =========================

def make_commit():
    os.chdir(REPO_PATH)

    # File update karo (taaki commit ho sake)
    with open("auto_log.txt", "a") as f:
        f.write(f"Updated on {datetime.now()}\n")

    os.system("git add .")
    os.system(f'git commit -m "{COMMIT_MESSAGE}"')
    os.system("git push")

    print("✅ Commit Done at", datetime.now())


def run_daily():
    interval = 24 * 60 * 60 // COMMITS_PER_DAY  # seconds gap between commits

    while True:
        make_commit()
        time.sleep(interval)


if __name__ == "__main__":
    run_daily()
