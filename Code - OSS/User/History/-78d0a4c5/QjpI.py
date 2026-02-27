from flask import Blueprint, request, session, jsonify
from firestore import (
    get_manager_id_by_email,
    get_projects_for_tenant,
    update_project,
    delete_project
)
from auth import login_required,no_user_required
from datetime import datetime
from google.cloud import firestore
db = firestore.Client(project="multi-tanant")


projects_api = Blueprint("projects_api", __name__)

@projects_api.route("/api/projects", methods=["POST"])
@login_required
@no_user_required
def add_project():
    if "tenant_id" not in session:
        return {"error": "unauthorized"}, 401

    data = request.json

    create_project({
        "project_name": data["project_name"],
        "description": data["description"],
        "company_name": session.get("company"),      # ✅ from user
        "start_date": datetime.fromisoformat(data["start_date"]),
        "due_date": datetime.fromisoformat(data["due_date"]),
        "manager_id": session.get("tenant_id"),                       # CEO owns project
        "created_by": session.get("email"),           # ✅ audit
    })

    return jsonify({"status": "ok"})


@projects_api.route("/api/projects", methods=["GET"])
@login_required
@no_user_required
def list_projects():
    if "tenant_id" not in session:
        return {"error": "unauthorized"}, 401
    role=session.get(role)
    if role=="manager":
        projects = get_projects_for_tenant(session["tenant_id"])
    elif role=="ceo":
        projects = (
        db.collection("projects")
        .where("company_name", "==", company_name)
        .order_by("due_date")
        .stream()
        )
    else:
        projects=get_projects_for_tenant(session.get("manager_id"))

    return jsonify([
        {**doc.to_dict(), "id": doc.id}
        for doc in projects
    ])



@projects_api.route("/api/projects/<project_id>", methods=["PUT"])
@login_required
def edit_project(project_id):
    update_project(project_id, request.json)
    return {"status": "ok"}


@projects_api.route("/api/projects/<project_id>", methods=["DELETE"])
@login_required
def remove_project(project_id):
    delete_project(project_id)
    return {"status": "ok"}

