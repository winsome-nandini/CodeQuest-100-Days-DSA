import json
import requests
import os

# GitHub API Setup
GITHUB_TOKEN = os.getenv("CODEQUEST_ACCESS_TOKEN")
REPO_OWNER = "Abhishek-Sharma182005"
REPO_NAME = "CodeQuest-100-Days-DSA"
LEADERBOARD_FILE = "leaderboard.json"

# Fetch participant data from GitHub
def get_participants():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contributors"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    
    print(f"Error fetching contributors: {response.status_code} - {response.text}")
    return []

# Load leaderboard safely
def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        print("Creating a new leaderboard...")
        with open(LEADERBOARD_FILE, "w") as file:
            json.dump({"participants": []}, file, indent=4)

    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, ValueError):
        print("Leaderboard file is corrupted. Resetting...")
        return {"participants": []}

# Update leaderboard with GitHub contributions
def update_leaderboard():
    leaderboard = load_leaderboard()
    participants = get_participants()

    for participant in participants:
        username = participant["login"]
        commits = participant["contributions"]

        # Score Calculation
        daily_submissions = commits
        social_media_posts = 0.5 * commits  # Assuming each commit has a social post
        total_score = daily_submissions + social_media_posts

        updated_entry = {
            "username": username,
            "total_score": total_score,
            "daily_submissions": daily_submissions,
            "social_media_posts": social_media_posts
        }

        # Update leaderboard
        found = False
        for entry in leaderboard["participants"]:
            if entry["username"] == username:
                entry.update(updated_entry)
                found = True
                break

        if not found:
            leaderboard["participants"].append(updated_entry)

    # Save leaderboard
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

    print("Leaderboard updated successfully!")

# Run update process
if __name__ == "__main__":
    update_leaderboard()
