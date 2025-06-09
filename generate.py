import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_listing(property_type, bedrooms, bathrooms, sqft, features, location, style):
    prompt = f"""
Write a real estate listing in a {style} tone for the following property:
- Type: {property_type}
- Bedrooms: {bedrooms}
- Bathrooms: {bathrooms}
- Square footage: {sqft}
- Key Features: {features}
- Location: {location}
Use persuasive and professional language suitable for MLS or Zillow.
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
