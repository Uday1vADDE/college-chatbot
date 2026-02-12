# app.py
from flask import Flask, request, jsonify
from logic import get_reply  # import chatbot function

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    reply = get_reply(user_message)
    return jsonify({'reply': reply})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
