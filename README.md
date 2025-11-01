# Client Automation Platform (starter)

Simple Flask-based automation API demo.

## Endpoints
- POST /generate-report  -> schedule report generation (JSON body)
- POST /send-email      -> queue an email (placeholder)
- POST /schedule-task   -> schedule a task (JSON body)

## Run locally
1. python -m venv venv
2. source venv/bin/activate   # or venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. python app.py

## Notes
- This is a starter scaffold. Replace placeholder logic with real report generation and integrate an email provider for production.
