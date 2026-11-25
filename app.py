
from flask import Flask, jsonify

app = Flask(__name__)

# In-memory notes
notes = [
    {"id": 1, "content": "Learn Docker"},
    {"id": 2, "content": "Practice Kubernetes"},
    {"id": 3, "content": "Explore CI/CD"}
]


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask Notes App!"


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
