from rest_framework.response import Response
from rest_framework.decorators import api_view
from .scoring import score_task, detect_cycle

@api_view(["POST"])
def analyze_tasks(request):
    tasks = request.data.get("tasks", [])
    mode = request.data.get("mode", "smart")

    task_map = {t["id"]: t for t in tasks}

    if detect_cycle(task_map):
        return Response({"error": "Circular dependency detected"}, status=400)

    scored = []
    for t in tasks:
        score, explanation = score_task(t, tasks, mode)
        t["score"] = score
        t["explanation"] = explanation
        scored.append(t)

    scored.sort(key=lambda x: x["score"], reverse=True)
    return Response(scored)


@api_view(["GET"])
def suggest_tasks(request):
    sample = [
        {
            "id": 1,
            "title": "Fix bug",
            "due_date": "2025-11-28",
            "importance": 8,
            "estimated_hours": 2,
            "dependencies": [],
        },
        {
            "id": 2,
            "title": "Create UI",
            "due_date": "2025-11-29",
            "importance": 6,
            "estimated_hours": 5,
            "dependencies": [1],
        },
    ]

    scored = []
    for t in sample:
        score, explanation = score_task(t, sample, "smart")
        t["score"] = score
        t["explanation"] = explanation
        scored.append(t)

    scored.sort(key=lambda x: x["score"], reverse=True)
    return Response(scored[:3])
    
