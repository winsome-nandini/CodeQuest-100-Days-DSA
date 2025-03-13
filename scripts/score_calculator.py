import json
import requests
import os

# GitHub API details
GITHUB_TOKEN = os.getenv("CODEQUEST_ACCESS_TOKEN")
REPO_OWNER = "Abhishek-Sharma182005"
REPO_NAME = "CodeQuest-100-Days-DSA"
FILE_PATH = "leaderboard.json"

# GitHub API URLs
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

# Fetch the latest leaderboard file
def get_leaderboard():
    response = requests.get(GITHUB_API_URL, headers=HEADERS)
    if response.status_code == 200:
        content = response.json()["content"]
        return json.loads(requests.utils.unquote(content))  # Decode base64
    return {"participants": []}  # Default if file doesn't exist

# Update leaderboard with new scores
def update_leaderboard():
    leaderboard = get_leaderboard()
    
    # Example score update logic (Modify as needed)
    for participant in leaderboard["participants"]:
        participant["total_score"] += 10  # Increment by 10 (or any logic)
    
    # Convert to JSON
    updated_content = json.dumps(leaderboard, indent=4)

    # Get the latest file SHA
    response = requests.get(GITHUB_API_URL, headers=HEADERS)
    file_sha = response.json()["sha"]

    # Update the file on GitHub
    update_data = {
        "message": "Automated leaderboard update",
        "content": requests.utils.quote(updated_content),  # Encode to base64
        "sha": file_sha  # Required to update the existing file
    }
    response = requests.put(GITHUB_API_URL, headers=HEADERS, json=update_data)

    if response.status_code == 200:
        print("Leaderboard updated successfully on GitHub!")
    else:
        print(f"Error updating file: {response.text}")

# Run the update
if __name__ == "__main__":
    update_leaderboard()
