from flask import Flask, render_template, request, send_file, jsonify
import os
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/export_mls", methods=["POST"])
def export_mls():
    title = request.form.get("title")
    description = request.form.get("description")
    bullets = request.form.getlist("bullets")

    content = f"{title}\n\n{description}\n\nHighlights:\n" + "\n".join(f"- {b}" for b in bullets)

    output = BytesIO()
    output.write(content.encode("utf-8"))
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="listing_mls.txt", mimetype="text/plain")
