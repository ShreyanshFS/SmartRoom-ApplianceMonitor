from flask import Flask, render_template, request, redirect, url_for
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Room Configuration
ROOMS = ['A-11', 'A-12', 'A-13', 'A-14']

# Global variables to store current status
current_fan_status = {}
current_light_status = {}
last_update = None
email_recipient = None

def send_email_report(fan_status, light_status, timestamp, recipient):
    """Send HTML email report"""
    # Generate HTML Content
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<style>
table {{
    font-family: Arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}}
td, th {{
    border: 1px solid #000000;
    text-align: center;
    padding: 8px;
}}
tr {{
    text-align: center;
}}
.status-on {{
    background-color: #d4edda;
    color: #155724;
}}
.status-off {{
    background-color: #f8d7da;
    color: #721c24;
}}
</style>
</head>
<body>
<b>Below is the list of all the rooms and respective appliances:</b>
<br><br>
<table>
<tr>
    <th>Date//Time</th>
    <th>Room No.</th>
    <th>Fan</th>
    <th>Light</th>
</tr>"""

    for room in ROOMS:
        html_content += f"""
<tr>
    <td>{timestamp}</td>
    <td>{room}</td>
    <td class="{'status-on' if fan_status[room] else 'status-off'}">{'ON' if fan_status[room] else 'OFF'}</td>
    <td class="{'status-on' if light_status[room] else 'status-off'}">{'ON' if light_status[room] else 'OFF'}</td>
</tr>"""

    html_content += """
</table>
</body>
</html>"""

    # Email setup
    gmail_sender = os.getenv('GMAIL_SENDER', 'appliances.status@gmail.com')
    gmail_passwd = os.getenv('GMAIL_PASSWORD', 'rvwsbrpwiolvpesh')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Statistics of fan and light from the hostel"
    msg['From'] = gmail_sender
    msg['To'] = recipient

    HTML_TEXT = MIMEText(html_content, 'html')
    msg.attach(HTML_TEXT)

    # Send Email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        server.sendmail(gmail_sender, [recipient], msg.as_string())
        server.quit()
        print('Email sent successfully.')
        return True
    except Exception as e:
        print('Error sending email:', str(e))
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_fan_status, current_light_status, last_update, email_recipient

    if request.method == 'POST':
        email_recipient = request.form.get('email')

        # Clear previous status
        current_fan_status.clear()
        current_light_status.clear()

        # Get status for each room
        for room in ROOMS:
            fan_status = request.form.get(f'fan_{room}') == '1'
            light_status = request.form.get(f'light_{room}') == '1'
            current_fan_status[room] = fan_status
            current_light_status[room] = light_status

        last_update = datetime.datetime.now().isoformat()

        # Send email if recipient provided
        if email_recipient:
            send_email_report(current_fan_status, current_light_status, last_update, email_recipient)

        return redirect(url_for('report'))

    return render_template('index.html', rooms=ROOMS)

@app.route('/report')
def report():
    if not current_fan_status or not current_light_status:
        return redirect(url_for('index'))

    return render_template('report.html',
                         rooms=ROOMS,
                         fan_status=current_fan_status,
                         light_status=current_light_status,
                         timestamp=last_update)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
