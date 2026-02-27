from google.cloud import firestore
from datetime import datetime

db = firestore.Client(project="multi-tanant")

def get_user_by_email(email):
    users = db.collection("users").where("email", "==", email).limit(1).stream()
    return next(users, None)

def create_user(data):
    db.collection("users").add(data)

def get_user_by_email(email: str):
    users = (
        db.collection("users")
        .where("email", "==", email)
        .limit(1)
        .stream()
    )
    return next(users, None)

def get_next_tenant_id():
    counter_ref = db.collection("counters").document("tenants")

    @firestore.transactional
    def increment(transaction):
        snapshot = counter_ref.get(transaction=transaction)

        if not snapshot.exists:
            transaction.set(counter_ref, {"value": 1})
            return 1

        new_value = snapshot.get("value") + 1
        transaction.update(counter_ref, {"value": new_value})
        return new_value

    transaction = db.transaction()
    return increment(transaction)


def get_manager_id_by_email(manager_email: str):
    user_doc = get_user_by_email(manager_email)
    if not user_doc:
        return None
    return user_doc.id 

def get_tasks_for_tenant(tenant_id):
    return (
        db.collection("tasks")
        .where("tenant_id", "==", tenant_id)
        .order_by("created_at")
        .stream()
    )

def create_task(data):
    db.collection("tasks").add({
        "task_type": data["task_type"],          # PROJECT / GOAL
        "project_id": data.get("project_id"),    # nullable
        "title": data["title"],
        "description": data.get("description", ""),
        "created_by": data["created_by"],
        "assigned_to": data["assigned_to"],
        "start_date": data["start_date"],
        "due_date": data["due_date"],
        "status": "TODO",
        "tenant_id": data["tenant_id"],
        "created_at": datetime.utcnow(),
    })

def update_task(task_id, data):
    db.collection("tasks").document(task_id).update(data)

def delete_task(task_id):
    db.collection("tasks").document(task_id).delete()



def create_project(data):
    db.collection("projects").add({
        "project_name": data["project_name"],
        "company_name": data["company_name"],
        "start_date": data["start_date"],
        "due_date": data["due_date"],
        "is_completed": False,
        "manager_id": data["manager_id"],
        "created_at": datetime.utcnow(),
    })


def get_projects_for_tenant(tenant_id):
    return (
        db.collection("projects")
        .where("tenant_id", "==", tenant_id)
        .order_by("due_date")
        .stream()
    )


def get_projects_for_manager(manager_id):
    return (
        db.collection("projects")
        .where("manager_id", "==", manager_id)
        .stream()
    )


def update_project(project_id, updates):
    db.collection("projects").document(project_id).update(updates)


def delete_project(project_id):
    db.collection("projects").document(project_id).delete()