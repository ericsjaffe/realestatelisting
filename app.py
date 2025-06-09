from flask import Flask, render_template, request
from generate import generate_listing
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    description = ""
    if request.method == "POST":
        property_type = request.form.get("property_type")
        bedrooms = request.form.get("bedrooms")
        bathrooms = request.form.get("bathrooms")
        sqft = request.form.get("sqft")
        features = request.form.get("features")
        location = request.form.get("location")
        style = request.form.get("style")

        description = generate_listing(property_type, bedrooms, bathrooms, sqft, features, location, style)
    return render_template("index.html", description=description)

if __name__ == "__main__":
    app.run(debug=True)
