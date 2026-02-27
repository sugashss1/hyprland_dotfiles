from flask import Blueprint, request, jsonify
from llm import generate_text
from auth import login_required
from routes.tasks_api import get_tasks


chatbot_api = Blueprint("chatbot_api", __name__)

@chatbot_api.route("/api/chat", methods=["POST"])
@login_required
def chat():
    user_prompt = request.json["message"]

    # Initialize chat history for this session
    if "chat_history" not in session:
        session["chat_history"] = []

    chat_history = session["chat_history"]

    # Get visible tasks using existing logic
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

    # Build conversation history context
    history_context = "\n".join([
        f"{m['role'].upper()}: {m['content']}"
        for m in chat_history
    ])

    # Final prompt with clear separation
    final_prompt = f"""
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

Respond helpfully and consistently with prior conversation.
"""

    # Generate AI response
    reply = generate_text(final_prompt)

    # Persist to session (limit to last 10 turns)
    chat_history.append({"role": "user", "content": user_prompt})
    chat_history.append({"role": "assistant", "content": reply})

    session["chat_history"] = chat_history[-20:]  # 10 user+assistant pairs
    session.modified = True

    return jsonify({"reply": reply})
