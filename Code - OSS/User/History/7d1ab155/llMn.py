from flask import Blueprint, request, jsonify, session
from firestore import (
    create_task,
    update_task,
    delete_task,
)
from datetime import datetime
from auth import login_required,no_user_required
from google.cloud import firestore
db = firestore.Client(project="multi-tanant")

tasks_api = Blueprint("tasks_api", __name__)

@tasks_api.route("/api/tasks", methods=["GET"])
@login_required
def get_tasks():
    if "tenant_id" not in session:
        return {"error": "unauthorized"}, 401

    role = session.get("role")
    tenant_id = session.get("tenant_id")
    company_name = session.get("company")
    user_email = session.get("email")

    # CEO: all tasks for the company
    if role == "ceo":
        tasks = (
            db.collection("tasks")
            .where("company", "==", company_name)
            .order_by("created_at")
            .stream()
        )
    # Manager: tasks assigned to the manager
    elif role == "manager":
        tasks = (
            db.collection("tasks")
            .where("tenant_id", "==", tenant_id)
            .order_by("created_at")
            .stream()
        )

    # Employee: tasks assigned to the employee
    else:
        tasks = (
            db.collection("tasks")
            .where("assigned_to", "==", user_email)
            .order_by("created_at")
            .stream()
        )

    return jsonify([
        {
            "id": doc.id,
            **doc.to_dict()
        }
        for doc in tasks
    ])




@tasks_api.route("/api/tasks", methods=["POST"])
@login_required
@no_user_required
def add_task():
    data = request.json

    create_task({
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
def edit_task(task_id):
    update_task(task_id, request.json)
    return {"status": "ok"}

@tasks_api.route("/api/tasks/<task_id>", methods=["DELETE"])
@login_required
@no_user_required
def remove_task(task_id):
    delete_task(task_id)
    return {"status": "ok"}


@tasks_api.route("/api/user-by-manager-id", methods=["GET"])
@login_required
def get_user_by_manager_id():
    id=session.get("db_id")

    users = db.collection('users').where(firebase.firestore.FieldPath.documentId(), '==', id).get()

    return jsonify([
        {
            "id": doc.id,
            **doc.to_dict()
        }
        for doc in users
    ])



