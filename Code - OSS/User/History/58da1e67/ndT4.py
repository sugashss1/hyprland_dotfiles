from firestore import create_project,create_task,create_user
from datetime import datetime
from auth import hash_password

# # ============================================================
# # SESSION CONTEXTS (SIMULATED)
# # ============================================================

# CEO_SESSION = {
#     "email": "ceo@acme.com",
#     "role": "ceo",
#     "tenant_id": "TENANT_001",
#     "company": "Acme Technologies"
# }

# MANAGER_SESSION = {
#     "email": "manager1@acme.com",
#     "role": "manager",
#     "tenant_id": "TENANT_001",
#     "company": "Acme Technologies"
# }

# USER_SESSION = {
#     "email": "dev1@acme.com",
#     "role": "user",
#     "tenant_id": "TENANT_001",
#     "company": "Acme Technologies"
# }

# # ============================================================
# # CEO ACTIONS
# # ============================================================

# # CEO creates a MANAGER
# create_user({
#     "full_name": "Rahul Mehta",
#     "email": "manager1@acme.com",
#     "password_hash": hash_password("Manager@123"),
#     "role": "manager",
#     "tenant_id": "TENANT_001",
#     "manager_id": "ceo@acme.com",
#     "company": "Acme Technologies",
#     "created_at": datetime.utcnow()
# })

# # CEO creates a USER directly
# create_user({
#     "full_name": "Anita Sharma",
#     "email": "dev1@acme.com",
#     "password_hash": hash_password("User@123"),
#     "role": "user",
#     "tenant_id": "TENANT_001",
#     "manager_id": "manager1@acme.com",
#     "company": "Acme Technologies",
#     "created_at": datetime.utcnow()
# })

# # CEO creates a PROJECT
# create_project({
#     "project_name": "ERP System Upgrade",
#     "description": "Migrate ERP from on-prem to cloud",
#     "company_name": CEO_SESSION["company"],
#     "start_date": datetime.fromisoformat("2025-01-01"),
#     "due_date": datetime.fromisoformat("2025-06-30"),
#     "manager_id": CEO_SESSION["email"],
#     "created_by": CEO_SESSION["email"]
# })

# # CEO creates an INITIAL TASK for Manager
# create_task({
#     "task_type": "PROJECT",
#     "project_name": "ERP System Upgrade",
#     "company": CEO_SESSION["company"],
#     "title": "Prepare overall project roadmap",
#     "description": "Define milestones, risks, and budget",
#     "created_by": CEO_SESSION["email"],
#     "assigned_to": "manager1@acme.com",
#     "start_date": datetime.fromisoformat("2025-01-05"),
#     "due_date": datetime.fromisoformat("2025-01-20"),
#     "tenant_id": CEO_SESSION["tenant_id"]
# })

# # ============================================================
# # MANAGER ACTIONS
# # ============================================================

# # Manager creates another USER
# create_user({
#     "full_name": "Rohit Verma",
#     "email": "dev2@acme.com",
#     "password_hash": hash_password("Dev@123"),
#     "role": "user",
#     "tenant_id": MANAGER_SESSION["tenant_id"],
#     "manager_id": MANAGER_SESSION["email"],
#     "company": MANAGER_SESSION["company"],
#     "created_at": datetime.utcnow()
# })

# # Manager creates PROJECT TASK
# create_task({
#     "task_type": "PROJECT",
#     "project_name": "ERP System Upgrade",
#     "company": MANAGER_SESSION["company"],
#     "title": "Database migration design",
#     "description": "Schema mapping, data validation strategy",
#     "created_by": MANAGER_SESSION["email"],
#     "assigned_to": "dev1@acme.com",
#     "start_date": datetime.fromisoformat("2025-01-15"),
#     "due_date": datetime.fromisoformat("2025-02-10"),
#     "tenant_id": MANAGER_SESSION["tenant_id"]
# })

# # Manager creates a GOAL task (non-project)
# create_task({
#     "task_type": "GOAL",
#     "project_name": None,
#     "company": MANAGER_SESSION["company"],
#     "title": "Improve deployment automation",
#     "description": "Reduce deployment time by 30%",
#     "created_by": MANAGER_SESSION["email"],
#     "assigned_to": "dev2@acme.com",
#     "start_date": datetime.fromisoformat("2025-02-01"),
#     "due_date": datetime.fromisoformat("2025-03-15"),
#     "tenant_id": MANAGER_SESSION["tenant_id"]
# })

# # ============================================================
# # USER ACTIONS (LIMITED)
# # ============================================================

# # User cannot create users or projects
# # User can only receive tasks and update task status (example placeholder)

# # Example: User updating task progress (conceptual)
# update_task("TASK_ID_123", {
#     "status": "IN_PROGRESS",
#     "updated_at": datetime.utcnow(),
#     "updated_by": USER_SESSION["email"]
# })

# ============================================================
# ADDITIONAL EXAMPLES
# ============================================================

# CEO creates another PROJECT
create_project({
    "project_name": "Mobile App Revamp",
    "description": "UI/UX redesign and performance optimization",
    "company_name": CEO_SESSION["company"],
    "start_date": datetime.fromisoformat("2025-03-01"),
    "due_date": datetime.fromisoformat("2025-08-01"),
    "manager_id": CEO_SESSION["email"],
    "created_by": CEO_SESSION["email"]
})

# Manager assigns multiple users to same project (separate tasks)
create_task({
    "task_type": "PROJECT",
    "project_name": "Mobile App Revamp",
    "company": MANAGER_SESSION["company"],
    "title": "Frontend UI redesign",
    "description": "Implement new design system",
    "created_by": MANAGER_SESSION["email"],
    "assigned_to": "dev1@acme.com",
    "start_date": datetime.fromisoformat("2025-03-05"),
    "due_date": datetime.fromisoformat("2025-04-15"),
    "tenant_id": MANAGER_SESSION["tenant_id"]
})

create_task({
    "task_type": "PROJECT",
    "project_name": "Mobile App Revamp",
    "company": MANAGER_SESSION["company"],
    "title": "Backend API optimization",
    "description": "Improve response time and caching",
    "created_by": MANAGER_SESSION["email"],
    "assigned_to": "dev2@acme.com",
    "start_date": datetime.fromisoformat("2025-03-05"),
    "due_date": datetime.fromisoformat("2025-04-30"),
    "tenant_id": MANAGER_SESSION["tenant_id"]
})
