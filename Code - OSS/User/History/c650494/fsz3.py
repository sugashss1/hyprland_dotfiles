from flask import Blueprint, request, jsonify
from llm import generate_text
from auth import login_required

chatbot_api = Blueprint("chatbot_api", __name__)

@chatbot_api.route("/api/chat", methods=["POST"])
@login_required
@chatbot_api.route("/api/chat", methods=["POST"])
@login_required
def chat():
    user_prompt = request.json["message"]

    # Call existing get_tasks() endpoint logic
    tasks_response = get_tasks()

    # get_tasks() returns a Flask Response, extract JSON
    tasks = tasks_response.get_json()

    # Build task context
    task_context = "\n".join([
        f"- [{t.get('status')}] {t.get('title')} "
        f"(Project: {t.get('project_name')}, "
        f"Assigned to: {t.get('assigned_to')}, "
        f"Due: {t.get('due_date')})"
        for t in tasks
    ])

    # Final prompt with explicit delimiter
    final_prompt = f"""
TASK CONTEXT:
--------------------
{task_context}
--------------------

USER PROMPT:
<<<{user_prompt}>>>

Answer the user prompt using the task context when applicable.
"""

    response = generate_text(final_prompt)
    return jsonify({"reply": response})
