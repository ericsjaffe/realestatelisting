import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_listing(property_type, bedrooms, bathrooms, sqft, features, location, style):
    prompt = f"""
Write a real estate listing in a {style} tone for the following:
- Type: {property_type}
- Bedrooms: {bedrooms}
- Bathrooms: {bathrooms}
- Sqft: {sqft}
- Features: {features}
- Location: {location}
"""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def generate_title_and_bullets(property_type, bedrooms, bathrooms, sqft, features, location, style):
    prompt = f"""
Based on the following property details, generate:
1. A short, compelling real estate listing title
2. 4 bullet point highlights

- Type: {property_type}
- Bedrooms: {bedrooms}
- Bathrooms: {bathrooms}
- Sqft: {sqft}
- Features: {features}
- Location: {location}
"""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        output = response.choices[0].message.content.strip().split("\n")
        title = output[0].replace("Title:", "").strip()
        bullets = [line.strip("- ").strip() for line in output if line.startswith("-")]
        return title, bullets
    except Exception as e:
        return "Generated Title Error", ["Error: " + str(e)]
