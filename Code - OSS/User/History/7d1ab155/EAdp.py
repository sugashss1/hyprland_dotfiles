from flask import Blueprint, request, jsonify, session
from firestore import (
    get_tasks_for_tenant,
    create_task,
    update_task,
    delete_task,
)
from auth import login_required

tasks_api = Blueprint("tasks_api", __name__)

@tasks_api.route("/api/tasks", methods=["GET"])
@login_required
def get_tasks():
    if "tenant_id" not in session:
        return {"error": "unauthorized"}, 401

    tenant_id = session.get("tenant_id")

    tasks = get_tasks_for_tenant(tenant_id)

    return jsonify([
        {**doc.to_dict(), "id": doc.id}
        for doc in tasks
    ])


@tasks_api.route("/api/tasks", methods=["POST"])
@login_required
def add_task():
    create_task(
        title=request.json["title"],
        tenant_id=session.get("tenant_id"),
        created_by=session.get("email"),
    )
    return {"status": "ok"}

@tasks_api.route("/api/tasks/<task_id>", methods=["PUT"])
@login_required
def edit_task(task_id):
    update_task(task_id, request.json)
    return {"status": "ok"}

@tasks_api.route("/api/tasks/<task_id>", methods=["DELETE"])
@login_required
def remove_task(task_id):
    delete_task(task_id)
    return {"status": "ok"}
