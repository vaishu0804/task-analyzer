from datetime import datetime

def detect_cycle(task_map):
    visited = set()
    stack = set()

    def dfs(task_id):
        if task_id in stack:
            return True
        if task_id in visited:
            return False

        visited.add(task_id)
        stack.add(task_id)

        for child in task_map.get(task_id, {}).get("dependencies", []):
            if dfs(child):
                return True

        stack.remove(task_id)
        return False

    for t in task_map:
        if dfs(t):
            return True
    return False


def score_task(task, all_tasks, mode="smart"):
    score = 0
    explanation = []

    # Urgency
    due = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
    days_left = (due - datetime.today().date()).days
    urgency = 20 if days_left < 0 else max(0, 10 - days_left)
    explanation.append(f"Urgency: {urgency}")

    # Importance
    importance = task["importance"]
    explanation.append(f"Importance: {importance}")

    # Effort
    effort_score = max(0, 10 - task["estimated_hours"])
    explanation.append(f"Effort Score: {effort_score}")

    # Dependencies (tasks blocked)
    dependents = sum(1 for t in all_tasks if task["id"] in t.get("dependencies", []))
    dependency_score = dependents * 5
    explanation.append(f"Dependency Score: {dependency_score}")

    # Modes
    if mode == "fast":
        score = effort_score
    elif mode == "impact":
        score = importance * 2
    elif mode == "deadline":
        score = urgency * 2
    else:
        score = urgency + (importance * 1.5) + effort_score + dependency_score

    return score, explanation
    