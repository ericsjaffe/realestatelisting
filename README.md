# Real Estate Listing Writer

This is a Flask web app that uses OpenAI GPT-3.5 to generate real estate listing descriptions.

## Features
- Input form for property details
- Custom tone (luxury, family-friendly, etc.)
- AI-generated description
- Ready for Render deployment

## Setup
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Add your `.env` file:
```
OPENAI_API_KEY=your-key-here
```

3. Run locally:
```
flask run
```

4. Deploy to Render:
- Add environment variable `OPENAI_API_KEY`
- Use start command: `gunicorn app:app`
