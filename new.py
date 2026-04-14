import requests
import matplotlib.pyplot as plt

username = input("Enter GitHub username: ")

headers = {"User-Agent": "Mozilla/5.0"}

profile_url = f"https://api.github.com/users/{username}"
profile_response = requests.get(profile_url, headers=headers)

if profile_response.status_code != 200:
    print("GitHub user not found")
    exit()

profile_data = profile_response.json()

print("\nGitHub Profile Info")
print("Name:", profile_data.get("name"))
print("Public Repositories:", profile_data.get("public_repos"))
print("Followers:", profile_data.get("followers"))
print("Following:", profile_data.get("following"))

repos_url = f"https://api.github.com/users/{username}/repos"
repos_data = requests.get(repos_url, headers=headers).json()

language_count = {}

for repo in repos_data:
    lang = repo["language"]
    if lang:
        language_count[lang] = language_count.get(lang, 0) + 1

plt.bar(language_count.keys(), language_count.values())
plt.xlabel("Languages")
plt.ylabel("Repositories")
plt.title("GitHub Language Usage")
plt.show()