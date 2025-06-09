# Real Estate Listing Writer (Advanced)

Generate a full real estate listing with GPT, including:
- Auto-generated title
- Listing description
- Bullet point highlights
- Image upload
- PDF + MLS export

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Add your `.env`:
```
OPENAI_API_KEY=your-key
```

3. Run it:
```
flask run
```

## Deploy to Render
- Add your OpenAI API key
- Set start command: `gunicorn app:app`
