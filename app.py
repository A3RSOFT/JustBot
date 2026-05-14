from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

BOTS_FILE = "bots.json"

def load_bots():
    if not os.path.exists(BOTS_FILE):
        return {}

    with open(BOTS_FILE, "r") as f:
        return json.load(f)

def save_bots(data):
    with open(BOTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    return jsonify({
        "success": True,
        "message": "Main bot login successful",
        "username": username
    })

@app.route("/create_childbot", methods=["POST"])
def create_childbot():
    room = request.form.get("room")
    child_username = request.form.get("child_username")

    bots = load_bots()

    for bot in bots.values():
        if bot["room"] == room:
            return jsonify({
                "success": False,
                "message": "Only 1 child bot allowed per room"
            })

    if child_username in bots:
        return jsonify({
            "success": False,
            "message": "Child bot username already in use"
        })

    bots[child_username] = {
        "room": room,
        "masters": [],
        "welcome": True,
        "spin": True
    }

    save_bots(bots)

    return jsonify({
        "success": True,
        "message": "Child bot created successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
