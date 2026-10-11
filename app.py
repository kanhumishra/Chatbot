
from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Please enter a message."}), 400

    response = get_response(message)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
