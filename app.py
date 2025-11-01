from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import time
import os
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
scheduler = BackgroundScheduler()
scheduler.start()

def generate_report_task(params=None):
    logging.info("Generating report... params=%s", params)
    # Placeholder logic - replace with real report generation
    time.sleep(1)
    logging.info("Report generated successfully.")

@app.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.json or {}
    # run as background job
    scheduler.add_job(generate_report_task, args=[data], replace_existing=False)
    return jsonify({'status': 'scheduled', 'endpoint': '/generate-report'}), 202

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json or {}
    to = data.get('to')
    subject = data.get('subject', 'No Subject')
    body = data.get('body', '')
    # Placeholder: integrate an email provider (SendGrid, SMTP) here
    logging.info("Pretend sending email to %s subject=%s", to, subject)
    return jsonify({'status': 'queued', 'to': to}), 200

@app.route('/schedule-task', methods=['POST'])
def schedule_task():
    data = request.json or {}
    run_in_seconds = int(data.get('delay', 10))
    scheduler.add_job(generate_report_task, 'date', run_date=None, args=[data], replace_existing=False)
    logging.info("Scheduled ad-hoc task with delay=%s seconds", run_in_seconds)
    return jsonify({'status': 'scheduled', 'delay_seconds': run_in_seconds}), 202

@app.route('/')
def index():
    return jsonify({'message': 'Client Automation Platform API is running'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json or {}
    to = data.get('to')
    subject = data.get('subject', 'No Subject')
    body = data.get('body', '')

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "your_gmail@gmail.com"
    msg['To'] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("your_gmail@gmail.com", "your_app_password")
            server.send_message(msg)
        return jsonify({'status': 'sent', 'to': to}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
