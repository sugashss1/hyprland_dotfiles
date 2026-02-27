from flask import Blueprint, request, jsonify
from llm import generate_text

chatbot_api = Blueprint("chatbot_api", __name__)

@chatbot_api.route("/api/chat", methods=["POST"])
def chat():

    
    prompt = request.json["message"]
    response = generate_text(prompt)
    return jsonify({"reply": response})
