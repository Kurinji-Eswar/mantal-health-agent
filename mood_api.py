from flask import Flask, request, jsonify
from mood_utils import detect_mood

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    text = data.get("text", "")
    mood = detect_mood(text)
    return jsonify({"mood": mood})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
