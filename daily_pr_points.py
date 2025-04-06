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


def can_merge_pr(pr):
    return pr.mergeable_state == "clean" and pr.mergeable


def main():
    points_data, sha = load_points_data()
    processed_prs = 0

    # Step 1: Collect user's PR dates from history
    user_days = {}
    for entry in points_data["history"]:
        username = entry["username"]
        pr_day = datetime.fromisoformat(entry["date"]).date()
        if pr_day >= EVENT_START_DATE:
            user_days.setdefault(username, set()).add(pr_day)

    # Step 2: Process new PRs
    for pr in repo.get_pulls(state='open'):
        username = pr.user.login
        pr_date = pr.created_at.date()

        if pr_date < EVENT_START_DATE:
            continue

        pr_day = pr_date

        if username not in points_data["users"]:
            points_data["users"][username] = {
                "points": 0,
                "social_media_points": 0
            }

        # Check if today's date is already counted for this user
        if username in user_days and pr_day in user_days[username]:
            continue

        if not can_merge_pr(pr):
            print(f"PR #{pr.number} not mergeable")
            continue

        try:
            try:
                pr.create_review(event="APPROVE", body="Auto-approved")
            except GithubException as e:
                if "Resource not accessible" in str(e):
                    print(f"Approval error for PR #{pr.number}")
                    continue
                raise

            result = pr.merge(merge_method="squash")
            if not result.merged:
                print(f"Merge failed for PR #{pr.number}")
                continue

            # Add new PR date
            user_days.setdefault(username, set()).add(pr_day)

            # Append to history
            points_data["history"].append({
                "username": username,
                "points": POINTS_PER_PR,
                "pr_number": pr.number,
                "date": datetime.now(timezone.utc).isoformat(),
                "reason": f"{EVENT_NAME}: PR #{pr.number}"
            })

            # Recalculate total points
            unique_days = len(user_days[username])
            points_data["users"][username]["points"] = unique_days * POINTS_PER_PR

            # Ensure social_media_points exists
            if "social_media_points" not in points_data["users"][username]:
                points_data["users"][username]["social_media_points"] = 0

            processed_prs += 1
            print(f"PR #{pr.number} by @{username} merged. Total points: {unique_days * POINTS_PER_PR}")

        except Exception as e:
            print(f"Processing error: {str(e)}")
            continue

    # Update metadata
    points_data["total_points"] = sum(u["points"] for u in points_data["users"].values())
    points_data["last_updated"] = datetime.now(timezone.utc).isoformat()
    points_data["metadata"]["event"] = EVENT_NAME
    points_data["metadata"]["points_per_pr"] = POINTS_PER_PR
    points_data["metadata"]["event_start_date"] = EVENT_START_DATE.isoformat()
    points_data["metadata"]["total_participants"] = len(points_data["users"])
    points_data["metadata"]["total_points_distributed"] = points_data["total_points"]

    if processed_prs > 0:
        save_points_data(points_data, sha)
        print("points.json updated.")
    else:
        print("No new PRs processed today.")


if __name__ == "__main__":
    main()
