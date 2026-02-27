from flask import Blueprint, request, jsonify, session
from firestore import (
    get_tasks_for_tenant,
    create_task,
    update_task,
    delete_task,
)

tasks_api = Blueprint("tasks_api", __name__)

@tasks_api.route("/api/tasks", methods=["GET"])
def get_tasks():
    if "tenant_id" not in session:
        return {"error": "unauthorized"}, 401

    tenant_id = session.get("tenant_id")

    tasks = (
        db.collection("tasks")
        .where("tenant_id", "==", tenant_id)
        .order_by("created_at")
        .stream()
    )

    return jsonify([
        {**doc.to_dict(), "id": doc.id}
        for doc in tasks
    ])


@tasks_api.route("/api/tasks", methods=["POST"])
def add_task():
    create_task(
        title=request.json["title"],
        tenant_id=session.get("tenant_id"),
        created_by=session.get("email"),
    )
    return {"status": "ok"}

@tasks_api.route("/api/tasks/<task_id>", methods=["PUT"])
def edit_task(task_id):
    update_task(task_id, request.json)
    return {"status": "ok"}

@tasks_api.route("/api/tasks/<task_id>", methods=["DELETE"])
def remove_task(task_id):
    delete_task(task_id)
    return {"status": "ok"}
