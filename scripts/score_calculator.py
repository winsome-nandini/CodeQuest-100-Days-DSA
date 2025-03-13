import os
import json
import requests
import pandas as pd

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "YourGitHubUsername"
REPO_NAME = "CodeQuest"
LEADERBOARD_FILE = "leaderboard.json"

def fetch_pull_requests():
    """Fetches all open pull requests from GitHub"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls?state=all"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else []

def analyze_code_quality(file_url):
    """Checks code quality using Flake8 for Python files"""
    response = requests.get(file_url)
    if response.status_code == 200:
        with open("temp.py", "w") as f:
            f.write(response.text)
        result = os.popen("flake8 temp.py --count").read().strip()
        return 5 - int(result) if result.isdigit() else 5  # Score 0-5 based on errors
    return 0

def update_leaderboard():
    """Fetches PRs, assigns scores, and updates leaderboard"""
    submissions = fetch_pull_requests()
    leaderboard = {}

    for pr in submissions:
        user = pr["user"]["login"]
        files_url = pr["url"] + "/files"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        files_response = requests.get(files_url, headers=headers).json()

        code_quality_score = 5
        for file in files_response:
            if file["filename"].endswith(".py"):
                code_quality_score = analyze_code_quality(file["raw_url"])

        streak_points = 3 if user in leaderboard and leaderboard[user]["streak"] >= 7 else 0

        leaderboard[user] = {
            "total_score": leaderboard.get(user, {}).get("total_score", 0) + 10 + streak_points + code_quality_score,
            "streak": leaderboard.get(user, {}).get("streak", 0) + 1
        }

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=4)

if __name__ == "__main__":
    update_leaderboard()
