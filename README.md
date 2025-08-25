👻 Ghost Chatbot

A sleek AI-powered chatbot built with Flask + Gemini API and a modern chat UI (HTML, CSS, JS).








🌟 Features

✅ Chat with Ghost (Gemini AI) in your browser
✅ Stylish dark-themed chat UI with bubble design
✅ Flask backend + Google Generative AI integration
✅ Lightweight & easy to run locally
✅ Ready to deploy on Render/Heroku

📂 Project Structure
ghost-chat/
 ├── app.py         # Flask backend (API + static file server)
 ├── index.html     # Chat interface (frontend)
 ├── style.css      # Styling for chat UI
 └── script.js      # Handles user input & API calls

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/your-username/ghost-chat.git
cd ghost-chat

2️⃣ Install dependencies

Make sure you have Python 3.9+ installed:

pip install flask flask-cors google-generativeai

3️⃣ Set up your Gemini API Key

In app.py, replace:

API_KEY = "YOUR_API_KEY_HERE"


with your own Google Gemini API Key.
👉 Get it from Google AI Studio
.

4️⃣ Run the Flask server
python app.py

5️⃣ Open in browser

Visit:


(https://ghost-ai-1.onrender.com/)
🖼️ Preview

💻 Chat UI
(screenshot placeholder — you can drop one here later)

🔮 Roadmap

 Add Markdown & syntax highlighting for code replies

 Enable chat history

 Add voice input/output 🎤🔊

 Deploy online with Render / Heroku / Vercel

📝 License

This project is licensed under the MIT License.
Feel free to use and improve!
