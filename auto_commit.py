import os
from datetime import datetime

REPO_PATH = r"D:\All_language\python project\Python-Journey"

if not os.path.exists(REPO_PATH):
    print("❌ Repo path not found!")
    exit()

os.chdir(REPO_PATH)

with open("auto_log.txt", "a") as f:
    f.write(f"Updated on {datetime.now()}\n")

os.system("git add .")
os.system('git commit -m "Auto commit"')
os.system("git push")

print("✅ Commit Done")
