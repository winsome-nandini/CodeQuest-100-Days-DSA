import json
import requests

# Example API URL (Replace with actual API)
API_URL = "https://api.example.com/submissions"

# Fetch submissions
response = requests.get(API_URL, headers={"Authorization": "Bearer YOUR_API_TOKEN"})
submissions = response.json()

# Calculate scores
leaderboard = {"participants": []}
for submission in submissions:
    name = submission["username"]
    score = submission["score"]

    leaderboard["participants"].append({"name": name, "score": score})

# Save updated leaderboard
with open("leaderboard.json", "w") as f:
    json.dump(leaderboard, f, indent=4)

print("Updated scores successfully.")
