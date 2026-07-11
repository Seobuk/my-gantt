"""
WBS Gantt - minimal Flask backend.

- Serves the single-file web app at  http://127.0.0.1:5173/
- Persists the WBS tree to  ../data/wbs.json  (the project's data store)
- Falls back to  ../data/wbs_sample.json  on first run.

Run:
    pip install -r requirements.txt
    python app.py
"""
import json
import os
from flask import Flask, request, jsonify, send_from_directory

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB_DIR = os.path.join(ROOT, "web")
DATA_DIR = os.path.join(ROOT, "data")
DATA_FILE = os.path.join(DATA_DIR, "wbs.json")          # live store (created on first save)
SAMPLE_FILE = os.path.join(DATA_DIR, "wbs_sample.json")  # seed data

app = Flask(__name__)


@app.get("/")
def index():
    return send_from_directory(WEB_DIR, "projects_gantt.html")


@app.get("/api/wbs")
def get_wbs():
    path = DATA_FILE if os.path.exists(DATA_FILE) else SAMPLE_FILE
    if not os.path.exists(path):
        return jsonify([])
    with open(path, encoding="utf-8") as f:
        return jsonify(json.load(f))


@app.post("/api/wbs")
def save_wbs():
    data = request.get_json(force=True)
    if not isinstance(data, list):
        return jsonify({"ok": False, "error": "expected a JSON array"}), 400
    os.makedirs(DATA_DIR, exist_ok=True)
    # 임시 파일에 쓴 뒤 교체: 쓰는 도중 죽어도 wbs.json이 깨지지 않는다
    tmp_path = DATA_FILE + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, DATA_FILE)
    return jsonify({"ok": True, "count": len(data)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5173, debug=True)
