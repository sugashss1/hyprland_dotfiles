from firestore import create_project,create_task,create_user
from auth import hash_password
from datetime import datetime

# ============================================================
# USERS (CEO → MANAGER → USERS)
# tenant_id starts from 1 and increments per user
# manager_id refers to superior's tenant_id
# ============================================================

# CEO (Top-level user)
# create_user({
#     "full_name": "Arjun Rao",
#     "email": "ceo@acme.com",
#     "password_hash": hash_password("Ceo@123"),
#     "role": "ceo",
#     "tenant_id": 1,
#     "manager_id": None,                 # CEO has no superior
#     "company": "Acme Technologies",
#     "created_at": datetime.utcnow()
# })

# # Manager reporting to CEO
# create_user({
#     "full_name": "Rahul Mehta",
#     "email": "manager1@acme.com",
#     "password_hash": hash_password("Manager@123"),
#     "role": "manager",
#     "tenant_id": 2,
#     "manager_id": 1,                    # Reports to CEO
#     "company": "Acme Technologies",
#     "created_at": datetime.utcnow()
# })

# # Second Manager reporting to CEO
# create_user({
#     "full_name": "Neha Verma",
#     "email": "manager2@acme.com",
#     "password_hash": hash_password("Manager@456"),
#     "role": "manager",
#     "tenant_id": 3,
#     "manager_id": 1,                    # Reports to CEO
#     "company": "Acme Technologies",
#     "created_at": datetime.utcnow()
# })

# # User reporting to Manager 1
# create_user({
#     "full_name": "Anita Sharma",
#     "email": "user1@acme.com",
#     "password_hash": hash_password("User@123"),
#     "role": "user",
#     "tenant_id": 4,
#     "manager_id": 2,                    # Reports to Manager 1
#     "company": "Acme Technologies",
#     "created_at": datetime.utcnow()
# })

# # User reporting to Manager 2
# create_user({
#     "full_name": "Vikram Singh",
#     "email": "user2@acme.com",
#     "password_hash": hash_password("User@456"),
#     "role": "user",
#     "tenant_id": 5,
#     "manager_id": 3,                    # Reports to Manager 2
#     "company": "Acme Technologies",
#     "created_at": datetime.utcnow()
# })


# # ============================================================
# # PROJECTS (Created by CEO)
# # manager_id refers to project owner (CEO tenant_id)
# # ============================================================

# create_project({
#     "project_name": "ERP System Upgrade",
#     "description": "Migrate ERP from on-prem to cloud",
#     "company_name": "Acme Technologies",
#     "start_date": datetime.fromisoformat("2025-01-01"),
#     "due_date": datetime.fromisoformat("2025-06-30"),
#     "manager_id": 1,                    # CEO owns project
#     "created_by": "ceo@acme.com"
# })

# create_project({
#     "project_name": "Mobile App Revamp",
#     "description": "UI/UX redesign and performance improvements",
#     "company_name": "Acme Technologies",
#     "start_date": datetime.fromisoformat("2025-02-01"),
#     "due_date": datetime.fromisoformat("2025-05-15"),
#     "manager_id": 1,                    # CEO owns project
#     "created_by": "ceo@acme.com"
# })


# # ============================================================
# # TASKS
# # ============================================================

# # CEO assigns task to Manager
# create_task({
#     "task_type": "PROJECT",
#     "project_name": "ERP System Upgrade",
#     "company": "Acme Technologies",
#     "title": "Define ERP roadmap",
#     "description": "Prepare milestones and risk assessment",
#     "created_by": "ceo@acme.com",
#     "assigned_to": "manager1@acme.com",
#     "start_date": datetime.fromisoformat("2025-01-05"),
#     "due_date": datetime.fromisoformat("2025-01-20"),
#     "tenant_id": 1
# })

# # Manager assigns task to User
# create_task({
#     "task_type": "PROJECT",
#     "project_name": "ERP System Upgrade",
#     "company": "Acme Technologies",
#     "title": "Database migration plan",
#     "description": "Design schema and rollback strategy",
#     "created_by": "manager1@acme.com",
#     "assigned_to": "user1@acme.com",
#     "start_date": datetime.fromisoformat("2025-01-15"),
#     "due_date": datetime.fromisoformat("2025-02-10"),
#     "tenant_id": 2
# })

# # Manager assigns another task to a different user
# create_task({
#     "task_type": "PROJECT",
#     "project_name": "Mobile App Revamp",
#     "company": "Acme Technologies",
#     "title": "Frontend performance optimization",
#     "description": "Improve load time and reduce bundle size",
#     "created_by": "manager2@acme.com",
#     "assigned_to": "user2@acme.com",
#     "start_date": datetime.fromisoformat("2025-02-05"),
#     "due_date": datetime.fromisoformat("2025-03-01"),
#     "tenant_id": 3
# })

# # User receives a personal (GOAL) task from Manager
# create_task({
#     "task_type": "GOAL",
#     "project_name": None,
#     "company": "Acme Technologies",
#     "title": "Complete Flask training",
#     "description": "Finish internal backend training module",
#     "created_by": "manager1@acme.com",
#     "assigned_to": "user1@acme.com",
#     "start_date": datetime.fromisoformat("2025-01-10"),
#     "due_date": datetime.fromisoformat("2025-01-31"),
#     "tenant_id": 4
# })
