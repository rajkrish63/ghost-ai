👻 Ghost Chatbot

Ghost Chatbot is a web-based conversational AI powered by Google Gemini.
It uses a Flask backend to connect with the Gemini API and a HTML/CSS/JS frontend for a simple chat interface.

📂 Project Structure
ghost-chat/
 ├── app.py         # Flask backend server
 ├── index.html     # Frontend (chat UI)
 ├── style.css      # Styling for the chat UI
 └── script.js      # Frontend chat logic

⚡ Features

🗨️ Chat with Ghost (Gemini AI) in your browser

🎨 Dark theme with styled chat bubbles

🔄 Real-time conversation via Flask API

🔑 Easy to configure with your own Gemini API key

🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/ghost-chat.git
cd ghost-chat

2. Install dependencies

Make sure you have Python 3.9+ installed. Then run:

pip install flask flask-cors google-generativeai

3. Add your Gemini API key

In app.py, replace:

API_KEY = "YOUR_API_KEY_HERE"


with your actual Google Gemini API key.

👉 You can generate an API key from Google AI Studio
.

4. Run the Flask server
python app.py

5. Open the app in your browser

Go to:

http://127.0.0.1:5000/


Now you can chat with Ghost 👻!

🖼️ Preview

(Add a screenshot of your chat UI here once running)

🔮 Future Improvements

 Support Markdown & code highlighting in chat

 Add chat history persistence

 Deploy online using Render/Heroku/Vercel

📝 License

This project is licensed under the MIT License.
