import json
from datetime import datetime, timezone, date
from github import Github, GithubException
import os

# Constants
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "Abhishek-Sharma182005/CodeQuest-100-Days-DSA"
POINTS_PER_PR = 3
EVENT_START_DATE = date(2025, 4, 1)
EVENT_NAME = "Daily PR Challenge"

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)


def load_points_data():
    try:
        contents = repo.get_contents("points.json")
        data = json.loads(contents.decoded_content.decode())
        return data, contents.sha
    except Exception as e:
        raise Exception(f"Failed to load existing points.json: {str(e)}")


def save_points_data(data, sha):
    content = json.dumps(data, indent=2)
    commit_msg = f"Auto-update PR points on {datetime.now(timezone.utc).isoformat()}"
    repo.update_file("points.json", commit_msg, content, sha)


def main():
    points_data, sha = load_points_data()
    processed_prs = 0

    if "users" not in points_data:
        points_data["users"] = {}

    if "history" not in points_data:
        points_data["history"] = []

    if "metadata" not in points_data:
        points_data["metadata"] = {}

    user_days = {}

    # Step 1: Load previous unique PR days
    for entry in points_data["history"]:
        username = entry["username"]
        pr_day = datetime.fromisoformat(entry["date"]).date()
        if pr_day >= EVENT_START_DATE:
            user_days.setdefault(username, set()).add(pr_day)

    # Step 2: Fetch ALL PRs (open, closed, merged)
    for pr in repo.get_pulls(state='all'):
        if not pr.merged:
            continue

        username = pr.user.login
        pr_date = pr.created_at.date()

        if pr_date < EVENT_START_DATE:
            continue

        # Avoid re-processing already counted PRs
        if any(entry["pr_number"] == pr.number for entry in points_data["history"]):
            continue

        # Track PR date for user
        user_days.setdefault(username, set()).add(pr_date)

        if username not in points_data["users"]:
            points_data["users"][username] = {
                "points": 0,
                "social_media_points": 0
            }

        # Log this PR in history
        points_data["history"].append({
            "username": username,
            "points": POINTS_PER_PR,
            "pr_number": pr.number,
            "date": datetime.now(timezone.utc).isoformat(),
            "reason": f"{EVENT_NAME}: PR #{pr.number}"
        })

        processed_prs += 1
        print(f"PR #{pr.number} by @{username} counted.")

    # Step 3: Update total points per user
    for username, days in user_days.items():
        points_data["users"][username]["points"] = len(days) * POINTS_PER_PR
        if "social_media_points" not in points_data["users"][username]:
            points_data["users"][username]["social_media_points"] = 0

    # Step 4: Update metadata
    points_data["total_points"] = sum(u["points"] for u in points_data["users"].values())
    points_data["last_updated"] = datetime.now(timezone.utc).isoformat()
    points_data["metadata"]["event"] = EVENT_NAME
    points_data["metadata"]["points_per_pr"] = POINTS_PER_PR
    points_data["metadata"]["max_points_per_day"] = POINTS_PER_PR
    points_data["metadata"]["event_start_date"] = EVENT_START_DATE.isoformat()
    points_data["metadata"]["total_participants"] = len(points_data["users"])
    points_data["metadata"]["total_points_distributed"] = points_data["total_points"]

    if processed_prs > 0:
        save_points_data(points_data, sha)
        print("✅ points.json updated.")
    else:
        print("ℹ️ No new PRs to process.")


if __name__ == "__main__":
    main()
