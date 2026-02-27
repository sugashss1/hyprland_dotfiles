from flask import Blueprint, request, jsonify, session
from firestore import (
    get_tasks_for_tenant,
    create_task,
    update_task,
    delete_task,
)
from datetime import datetime
from auth import login_required,no_user_required

tasks_api = Blueprint("tasks_api", __name__)

@tasks_api.route("/api/tasks", methods=["GET"])
@login_required
def get_tasks():
    tenant_id = session.get("tenant_id")

    tasks = get_tasks_for_tenant(tenant_id)

    return jsonify([
        {**doc.to_dict(), "id": doc.id}
        for doc in tasks
    ])



@tasks_api.route("/api/tasks", methods=["POST"])
@login_required
@no_user_required
def add_task():
    data = request.json

    create_task({
        "task_type": data["task_type"],               # PROJECT / GOAL
        "project_name": data.get("project_name"),
        "company":session.get("company"),                                    # optional
        "title": data["title"],
        "description": data.get("description", ""),
        "created_by": session["email"],
        "assigned_to": data["assigned_to"],           # email
        "start_date": datetime.fromisoformat(data["start_date"]),
        "due_date": datetime.fromisoformat(data["due_date"]),
        "tenant_id": session["tenant_id"],
    })

    return {"status": "ok"}


@tasks_api.route("/api/tasks/<task_id>", methods=["PUT"])
@login_required
@no_user_required
def edit_task(task_id):
    update_task(task_id, request.json)
    return {"status": "ok"}

@tasks_api.route("/api/tasks/<task_id>", methods=["DELETE"])
@login_required
@no_user_required
def remove_task(task_id):
    delete_task(task_id)
    return {"status": "ok"}
