from flask import Flask, render_template, request, send_file
from generate import generate_listing, generate_title_and_bullets
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from xhtml2pdf import pisa
from io import BytesIO

load_dotenv()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/", methods=["GET", "POST"])
def index():
    description = ""
    title = ""
    bullets = []
    image_url = ""
    if request.method == "POST":
        property_type = request.form.get("property_type")
        bedrooms = request.form.get("bedrooms")
        bathrooms = request.form.get("bathrooms")
        sqft = request.form.get("sqft")
        features = request.form.get("features")
        location = request.form.get("location")
        style = request.form.get("style")

        file = request.files.get("media")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(image_path)
            image_url = image_path

        description = generate_listing(property_type, bedrooms, bathrooms, sqft, features, location, style)
        title, bullets = generate_title_and_bullets(property_type, bedrooms, bathrooms, sqft, features, location, style)

    return render_template("index.html", description=description, title=title, bullets=bullets, image_url=image_url)

@app.route("/export_pdf", methods=["POST"])
def export_pdf():
    title = request.form.get("title")
    description = request.form.get("description")
    bullets = request.form.getlist("bullets")
    image_url = request.form.get("image_url")

    html = render_template("pdf_template.html", title=title, description=description, bullets=bullets, image_url=image_url)
    pdf = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode("utf-8")), dest=pdf)
    pdf.seek(0)
    return send_file(pdf, as_attachment=True, download_name="listing.pdf", mimetype="application/pdf")

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

content = f"{title}\n\n{description}\n\nHighlights:\n" + "\n".join(f"- {b}" for b in bullets)

{description}

Highlights:
" + "
".join(f"- {b}" for b in bullets)
    output = BytesIO()
    output.write(content.encode("utf-8"))
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="listing_mls.txt", mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
