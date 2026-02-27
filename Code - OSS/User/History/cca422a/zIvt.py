from google.cloud import firestore

db = firestore.Client(project="multi-tanant")

def get_user_by_email(email):
    users = db.collection("users").where("email", "==", email).limit(1).stream()
    return next(users, None)

def create_user(data):
    db.collection("users").add(data)

def get_tasks_for_tenant(tenant_id):
    return (
        db.collection("tasks")
        .where("tenant_id", "==", tenant_id)
        .order_by("created_at")
        .stream()
    )

def create_task(title, tenant_id, created_by):
    db.collection("tasks").add({
        "title": title,
        "done": False,
        "tenant_id": tenant_id,
        "created_by": created_by,
        "created_at": datetime.utcnow(),
    })

def update_task(task_id, data):
    db.collection("tasks").document(task_id).update(data)

def delete_task(task_id):
    db.collection("tasks").document(task_id).delete()
