# 🧠 Mental Health Check-In Agent

A smart Telegram bot that detects your mood based on your messages, logs the emotions, and replies empathetically. Powered by a custom Flask API and integrated seamlessly with **n8n** workflows.

---

## 🔧 Features

- ✅ Mood detection using Flask-based API  
- 🤖 Telegram bot interaction via n8n  
- 📁 Mood logs stored locally in JSON  
- 🔁 Fully automated message-response workflow  
- 🌐 LocalTunnel support for public API access

---

## 📁 Project Structure

mental-health-agent/
├── mood_api.py # Flask API to handle mood detection
├── mood_utils.py # Mood classification logic
├── requirements.txt # Python package dependencies
├── README.md # Project documentation
├── logs/
│ └── mood_logs.json # Stored mood entries
└── workflows/
└── n8n_mood_workflow.json # Exported n8n workflow


---

## 🚀 Getting Started

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/Kurinji-Eswar/mental-health-agent.git
cd mental-health-agent
python -m venv telegram-env
telegram-env\Scripts\activate  # For Windows
pip install -r requirements.txt

### 2. Run the Flask API
```bash
Copy code
python mood_api.py

3. Expose API using LocalTunnel
```bash
Copy code
npm install -g localtunnel
lt --port 5000

⚠️ Copy the URL shown (e.g., https://your-url.loca.lt) and update the HTTP Request node in n8n.

🤖 n8n Workflow Setup
Open your n8n instance.

Import the file: workflows/n8n_mood_workflow.json.

Configure the nodes:

Telegram Trigger

HTTP Request (points to Flask API URL)

Telegram Send (sends detected mood)

Add your Telegram bot credentials.

Enable the workflow and test by messaging your bot.

📊 Logs
All messages and detected moods are logged in logs/mood_logs.json for review and analysis.

💡 Use Cases
🧘 Self-reflection tool

📓 Daily emotional journaling

💬 AI companion for mental well-being

📈 Mood tracking for health professionals

🌟 Advantages
Simple, modular design

Secure local storage (JSON)

Fully customizable workflow

Easy to integrate with other APIs/tools

🔮 Future Enhancements
📊 Mood analytics dashboard (charts, trends)

📅 Mood-based calendar reminders

🧠 Advanced NLP for emotion detection

🎙️ Voice message mood recognition

📜 License
MIT License
© 2025 Kurinji-Eswar

