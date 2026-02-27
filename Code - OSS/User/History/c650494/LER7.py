from flask import Blueprint, request, jsonify,session
from llm import generate_text
from auth import login_required
from routes.tasks_api import get_tasks


chatbot_api = Blueprint("chatbot_api", __name__)

@chatbot_api.route("/api/chat", methods=["POST"])
@login_required
def chat():
    user_prompt = request.json["message"]

    # Initialize chat history (session-scoped)
    if "chat_history" not in session:
        session["chat_history"] = []

    chat_history = session["chat_history"]

    # Fetch tasks using existing logic
    tasks_response = get_tasks()
    tasks = tasks_response.get_json()

    # Build task context
    task_context = "\n".join([
        f"- [{t.get('status')}] {t.get('title')} "
        f"(Project: {t.get('project_name')}, "
        f"Assigned to: {t.get('assigned_to')}, "
        f"Due: {t.get('due_date')})"
        for t in tasks
    ])

    # Build chat history context
    history_context = "\n".join([
        f"{m['role'].upper()}: {m['content']}"
        for m in chat_history
    ])

    # Build user/session context
    user_context = f"""
User Email   : {session.get("email")}
User Role    : {session.get("role")}
Tenant ID    : {session.get("tenant_id")}
Company      : {session.get("company")}
"""

    # Final prompt with strict separation
    final_prompt = f"""
USER CONTEXT (read-only):
--------------------
{user_context}
--------------------

TASK CONTEXT:
--------------------
{task_context}
--------------------

CHAT HISTORY:
--------------------
{history_context}
--------------------

USER PROMPT:
<<<{user_prompt}>>>

Respond accurately using the above context. Do not repeat metadata unless asked.
"""

    # Generate AI response
    reply = generate_text(final_prompt)

    # Persist chat history (last 10 turns)
    chat_history.append({"role": "user", "content": user_prompt})
    chat_history.append({"role": "assistant", "content": reply})
    session["chat_history"] = chat_history[-20:]
    session.modified = True

    
    return jsonify({
        "reply": reply,
        "history": session["chat_history"]
    })

@chatbot_api.route("/api/chat/history", methods=["GET"])
@login_required
def chat_history():
    return jsonify({
        "history": session.get("chat_history", [])
    })

