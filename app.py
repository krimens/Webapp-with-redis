from flask import Flask, request, jsonify
from flask_cors import CORS
import redis
import os

app = Flask(__name__)
CORS(app)
# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

STREAM_KEY = "messages"

@app.route('/save', methods=['POST'])
def save_message():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({"status": "Name and message are required!"}), 400

    # Add to Redis Stream
    msg_id = r.xadd(STREAM_KEY, {"name": name, "message": message})
    return jsonify({"status": "Message saved!", "id": msg_id}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    # Get all messages in the stream
    entries = r.xrange(STREAM_KEY, "-", "+")
    messages = []
    for entry_id, fields in entries:
        messages.append({
            "id": entry_id,
            "name": fields.get("name"),
            "message": fields.get("message")
        })
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
