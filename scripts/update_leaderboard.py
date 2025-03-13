import json
import requests
import os

GITHUB_TOKEN = ("CODEQUEST_ACCESS_TOKEN")  #os.getenv("CODEQUEST_ACCESS_TOKEN")
REPO_OWNER = "Abhishek-Sharma182005"
REPO_NAME = "-CodeQuest-100-Days-DSA"
LEADERBOARD_FILE = "leaderboard.json"

# Fetch participant data from the GitHub repository
def get_participants():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contributors"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

# Load the existing leaderboard
def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    return {"participants": []}

# Update scores based on contributions
def update_leaderboard():
    leaderboard = load_leaderboard()
    participants = get_participants()
    
    for participant in participants:
        username = participant["login"]
        commits = participant["contributions"]

        # Calculate scores
        daily_submissions = commits
        social_media_posts = 0.5 * commits  # Assume every commit corresponds to a social post

        total_score = daily_submissions + social_media_posts
        updated_entry = {
            "username": username,
            "total_score": total_score,
            "daily_submissions": daily_submissions,
            "social_media_posts": social_media_posts
        }

        # Add/update participant in leaderboard
        found = False
        for entry in leaderboard["participants"]:
            if entry["username"] == username:
                entry.update(updated_entry)
                found = True
                breakimport json

# Load existing leaderboard
try:
    with open("leaderboard.json", "r") as f:
        leaderboard_data = json.load(f)
except (json.JSONDecodeError, FileNotFoundError):
    print("Error: leaderboard.json is empty or missing. Creating a new one.")
    leaderboard_data = {}

print("Loaded Leaderboard:", leaderboard_data)

# Example new scores (Replace this with actual API call)
new_scores = {"participants": [{"name": "Abhishek", "score": 100}]}  # Replace with real data
print("New Scores:", new_scores)

# Save updated leaderboard
with open("leaderboard.json", "w") as f:
    json.dump(new_scores, f, indent=4)

print("Updated Leaderboard Successfully")

        if not found:
            leaderboard["participants"].append(updated_entry)

    # Save updated leaderboard
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

# Run update
if __name__ == "__main__":
    update_leaderboard()
