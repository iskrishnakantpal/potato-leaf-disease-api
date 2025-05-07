# Potato Disease Classification API

## How to deploy on Render
1. Upload this repo to GitHub.
2. Go to https://render.com and create a new Web Service.
3. Connect your GitHub repo.
4. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
5. You will get a public URL for prediction.

## API Endpoint
POST `/predict`
- Form-data param: `file` (image)
