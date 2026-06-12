from app import app
from flask import render_template, request, jsonify
import subprocess


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    text = request.json.get("text", "")

    output_file = "app/static/audio/output.wav"

    command = [
        "piper/piper.exe",
        "--model",
        "piper/models/en_US-lessac-medium.onnx",
        "--output_file",
        output_file
    ]

    subprocess.run(
        command,
        input=text,
        text=True
    )

    return jsonify({
        "audio": "/static/audio/output.wav"
    })