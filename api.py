from flask import Flask, request, jsonify
from support_bot import classify_intent, generate_response, summarize_conversation

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    category = classify_intent(user_message)
    response = generate_response(category, user_message)

    return jsonify({
        "intent": category,
        "response": response
    })


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    conversation = data.get("conversation")

    summary = summarize_conversation(conversation)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)