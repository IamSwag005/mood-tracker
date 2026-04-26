from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='static')
CORS(app)

DATA_FILE = 'moods.json'

def load_moods():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_moods(moods):
    with open(DATA_FILE, 'w') as f:
        json.dump(moods, f, indent=2)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/moods', methods=['GET'])
def get_moods():
    return jsonify(load_moods())

@app.route('/api/moods', methods=['POST'])
def add_mood():
    data = request.get_json()
    moods = load_moods()

    entry = {
        'id': int(datetime.now().timestamp() * 1000),
        'mood': data.get('mood'),
        'emoji': data.get('emoji'),
        'note': data.get('note', ''),
        'date': datetime.now().strftime('%Y-%m-%d'),
        'time': datetime.now().strftime('%H:%M'),
    }

    moods.insert(0, entry)
    save_moods(moods)

    return jsonify(entry), 201

@app.route('/api/moods/<int:mood_id>', methods=['DELETE'])
def delete_mood(mood_id):
    moods = load_moods()
    moods = [m for m in moods if m['id'] != mood_id]
    save_moods(moods)
    return jsonify({'success': True})

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)

    port = int(os.environ.get("PORT", 10000))  # IMPORTANT FIX
    app.run(host="0.0.0.0", port=port)