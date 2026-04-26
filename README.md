# 🌊 Moodrift — Daily Mood Journal

A minimal, beautiful mood-tracking web app built with Flask + vanilla JS.

## Features
- Log your daily mood with 5 emotion levels
- Add optional notes to each entry
- View your mood history
- Delete any entry
- Data stored locally as JSON

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Then open **http://localhost:5000** in your browser.

## Project Structure

```
├── app.py           # Flask backend (API + static serving)
├── requirements.txt
├── moods.json       # Auto-created — stores your entries
└── static/
    └── index.html   # Frontend (HTML + CSS + JS)
```

## API Endpoints

| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| GET    | `/api/moods`        | Fetch all entries    |
| POST   | `/api/moods`        | Add a new mood entry |
| DELETE | `/api/moods/<id>`   | Delete an entry      |
