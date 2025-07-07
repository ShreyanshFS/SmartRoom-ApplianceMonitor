# This Code only supports Boolean inputs: 1 or 0
# 1 denotes ON, and 0 denotes OFF

print('''This Code only supports boolean inputs 
That's 1 or 0
Here,
1 Denotes ON
&
0 Denotes OFF''')

# Required Libraries
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email Input
TO = input('Enter Email for Response = ')

# Room Configuration
rooms = ['A-11', 'A-12', 'A-13', 'A-14']
light = []
fan = []

# HTML Templates
free_text = """<tr>
    <td>TIMEDATE</td>
    <td>ROOMNO</td>"""

free_end = """</tr>"""

TEXT_START = """<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: Arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}
td, th {
    border: 1px solid #000000; 
    text-align: center;
    padding: 8px;
}
tr {
    text-align: center;
}
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

TEXT_END = """</table>
</body>
</html>"""

# Infinite Monitoring Loop
while True:
    now = datetime.datetime.now().isoformat()
    TEXT_MID = ""
    light.clear()
    fan.clear()

    # Collect Input for Each Room
    for room in rooms:
        fan_status = int(input(f"Please enter the status of fan in {room} (1/0) = "))
        light_status = int(input(f"Please enter the status of light in {room} (1/0) = "))
        fan.append(fan_status)
        light.append(light_status)

    # Generate HTML Content for Each Room
    for i in range(len(rooms)):
        temp = free_text.replace("ROOMNO", rooms[i])
        temp = temp.replace("TIMEDATE", now)
        TEXT_MID += temp

        # Light Status
        if light[i] == 1:
            TEXT_MID += """<td bgcolor="#00FF00">ON</td>"""
        else:
            TEXT_MID += """<td bgcolor="#FF0000">OFF</td>"""

        # Fan Status
        if fan[i] == 1:
            TEXT_MID += """<td bgcolor="#00FF00">ON</td>"""
        else:
            TEXT_MID += """<td bgcolor="#FF0000">OFF</td>"""

        TEXT_MID += free_end

    # Final Email Body
    TEXT = TEXT_START + TEXT_MID + TEXT_END

    # Setup Email
    gmail_sender = 'appliances.status@gmail.com'
    gmail_passwd = 'rvwsbrpwiolvpesh'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Statistics of fan and light from the hostel"
    msg['From'] = gmail_sender
    msg['To'] = TO

    HTML_TEXT = MIMEText(TEXT, 'html')
    msg.attach(HTML_TEXT)

    # Send Email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        server.sendmail(gmail_sender, [TO], msg.as_string())
        server.quit()
        print('Email sent successfully.')

    except Exception as e:
        print('Error sending email:', str(e))

    # Wait before next run
    time.sleep(30)
