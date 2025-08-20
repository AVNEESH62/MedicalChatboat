from flask import Flask, request, jsonify

app = Flask(__name__)

# Health-check route
@app.route("/")
def home():
    return "Hello, Medical Chatbot is running!"

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    # For now, just echo back (later you’ll connect AI logic here)
    response = f"You said: {user_input}"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
