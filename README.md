# Smart Task Analyzer

A mini application that intelligently scores, prioritizes, and
recommends tasks based on urgency, importance, effort, and
dependencies.\
This project was developed as part of a **Software Development Intern
Technical Assessment**.

## Features

### Intelligent Multi-Factor Task Scoring

-   Urgency (based on due date)
-   Importance (1--10 scale)
-   Effort (estimated hours)
-   Dependencies (tasks that block others)

### Multiple Prioritization Strategies

-   Smart Balance
-   Fastest Wins
-   High Impact
-   Deadline Driven

### Circular Dependency Detection

### âœ” REST API Endpoints

-   POST `/api/tasks/analyze/`
-   GET `/api/tasks/suggest/`

### Functional Frontend

HTML/CSS/JS interface for inputting tasks and viewing sorted results.

## Project Structure

    task-analyzer/
    ├── backend/
    │   ├── manage.py
    │   ├── task_analyzer/
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── tasks/
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── views.py
    │   │   ├── scoring.py
    │   │   ├── urls.py
    │   │   └── tests.py
    │   └── requirements.txt
    ├── frontend/
    │   ├── index.html
    │   ├── styles.css
    │   └── script.js
    └── README.md
 

## Setup Instructions

### 1. Clone Repo

    git clone https://github.com/vaishu0804/task-analyzer.git
    cd task-analyzer-main/backend

### 2. Create Virtual Environment

    python3 -m venv venv
    source venv/bin/activate

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run Migrations

    python manage.py migrate

### 5. Start Server

    python manage.py runserver

### 6. Run Frontend

Open:

    frontend/index.html

## Algorithm Explanation

### 1. Urgency

    if due < today: urgency = 20
    else: urgency = max(0, 10 - days_left)

### 2. Importance

    importance_score = importance * 1.5

### 3. Effort

    effort_score = max(0, 10 - estimated_hours)

### 4. Dependencies

    dependency_score = dependents_count * 5

### Final Smart Score

    total_score = urgency + (importance*1.5) + effort_score + dependency_score

## Sorting Modes

  Mode              Priority
  ----------------- -------------
  Smart Balance     All factors
  Fastest Wins      Low effort
  High Impact       Importance
  Deadline Driven   Urgency

## Edge Cases

-   Circular dependencies detected via DFS
-   Past due tasks get high urgency
-   Invalid fields validated
-   Negative/zero hours corrected

## Design Decisions

-   Scoring extracted into dedicated module
-   JSON used for bulk task operations
-   DFS chosen for cycle detection
-   Multiple modes added per requirements

## Unit Tests Included

-   Importance affects score
-   Low-effort tasks score higher
-   Overdue tasks get high urgency

## Time Breakdown

  Task            Time
  --------------- ------------
  Analysis        15m
  Algorithm       35m
  Backend setup   25m
  API coding      40m
  Scoring logic   45m
  Frontend        35m
  Testing         20m
  README          20m
  **Total**       **3h 55m**

## Final Notes

This project demonstrates algorithmic thinking, clean backend design,
and functional UI integration.
