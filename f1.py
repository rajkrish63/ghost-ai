from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
from flask_cors import CORS
import os

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)  # Allow frontend JS to call backend

# 🔑 Configure Gemini (replace with your actual API key or set via Render ENV VAR)
API_KEY = os.environ.get("AIzaSyBXyMLeOdakUY_epOBJd4Bc1eyEpKQwHYo")
genai.configure(api_key=API_KEY)

# Initialize Gemini chat model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

@app.route("/")
def index():
    """Serve frontend (index.html)"""
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat_with_ghost():
    """Handle chat messages from frontend"""
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input.strip():
        return jsonify({"reply": "👻 Ghost: I didn’t catch that."})

    try:
        response = chat.send_message(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    # ✅ Render requires host=0.0.0.0 and PORT from environment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
