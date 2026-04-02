# SmartRoom Appliance Monitor

This Python Flask web application collects the ON/OFF status of fans and lights in multiple rooms and displays a formatted HTML report. It can also automatically email reports to a specified recipient.

## 📋 Features

- Web-based interface for inputting appliance status
- Real-time HTML report display
- Optional email notifications via Gmail
- Fully customizable for any number of rooms
- Responsive web design

## 🔧 Requirements

- Python 3.x
- Internet connection (for sending email, optional)

## 🧪 Installation

```bash
git clone https://github.com/your-username/SmartRoom-ApplianceMonitor.git
cd SmartRoom-ApplianceMonitor
pip install -r requirements.txt
```

## 🚀 Usage

### Local Development

1. **Configure Email (Optional)**:
   - Edit the `.env` file with your Gmail credentials:
     ```
     GMAIL_SENDER=your-email@gmail.com
     GMAIL_PASSWORD=your-app-password
     ```
   - For Gmail, you'll need to enable 2-factor authentication and generate an App Password.

2. **Run the Application**:
   ```bash
   python appliance_monitor.py
   ```

3. **Access the Web Interface**:
   - Open your browser and go to `http://localhost:5000`
   - Fill in the email address (optional) and check the boxes for fan/light status in each room
   - Click "Submit Status" to view the report

### Production Deployment

For production use, consider using a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 appliance_monitor:app
```

## 📁 Project Structure

```
SmartRoom-ApplianceMonitor/
├── appliance_monitor.py    # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   └── report.html
└── static/                 # CSS and static files
    └── style.css
```

## 🔒 Security Notes

- The `.env` file contains sensitive information and should not be committed to version control
- Consider using environment-specific configuration for production
- The app runs on all interfaces (`0.0.0.0`) for local hosting

Created by :- Shreyansh 