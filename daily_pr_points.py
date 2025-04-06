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

        # Ensure keys exist
        data.setdefault("users", {})
        data.setdefault("history", [])
        data.setdefault("metadata", {})

        return data, contents.sha
    except Exception as e:
        raise Exception(f"Failed to load existing points.json: {str(e)}")


def save_points_data(data, sha):
    content = json.dumps(data, indent=2)
    commit_msg = f"Auto-update PR points on {datetime.now(timezone.utc).isoformat()}"
    repo.update_file("points.json", commit_msg, content, sha)


def can_merge_pr(pr):
    return pr.mergeable_state == "clean" and pr.mergeable


def already_counted(pr, history):
    return any(entry["pr_number"] == pr.number for entry in history)


def main():
    points_data, sha = load_points_data()
    processed_prs = 0
    history = points_data["history"]
    user_days = {}

    for entry in history:
        username = entry["username"]
        pr_day = datetime.fromisoformat(entry["date"]).date()
        if pr_day >= EVENT_START_DATE:
            user_days.setdefault(username, set()).add(pr_day)

    for pr in repo.get_pulls(state='open'):
        username = pr.user.login
        pr_date = pr.created_at.date()

        if pr_date < EVENT_START_DATE or already_counted(pr, history):
            continue

        if username in user_days and pr_date in user_days[username]:
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

            # Add PR entry to history
            history.append({
                "username": username,
                "points": POINTS_PER_PR,
                "pr_number": pr.number,
                "date": datetime.now(timezone.utc).isoformat(),
                "reason": f"{EVENT_NAME}: PR #{pr.number}"
            })

            # Update user_days
            user_days.setdefault(username, set()).add(pr_date)

            # Ensure user exists
            user_entry = points_data["users"].setdefault(username, {
                "points": 0,
                "social_media_points": 0
            })

            # Recalculate only if manual override is not set
            if not user_entry.get("manual_override", False):
                unique_days = len(user_days[username])
                user_entry["points"] = unique_days * POINTS_PER_PR

            processed_prs += 1
            print(f"PR #{pr.number} by @{username} merged.")

        except Exception as e:
            print(f"Processing error: {str(e)}")
            continue

    # Update metadata
    total_points = sum(u["points"] for u in points_data["users"].values())
    points_data["total_points"] = total_points
    points_data["last_updated"] = datetime.now(timezone.utc).isoformat()
    points_data["metadata"].update({
        "event": EVENT_NAME,
        "points_per_pr": POINTS_PER_PR,
        "event_start_date": EVENT_START_DATE.isoformat(),
        "total_participants": len(points_data["users"]),
        "total_points_distributed": total_points
    })

    if processed_prs > 0:
        save_points_data(points_data, sha)
        print("✅ points.json updated.")
    else:
        print("✅ No new PRs processed today.")


if __name__ == "__main__":
    main()
