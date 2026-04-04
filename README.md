# SmartRoom Appliance Monitor

A modern, dark-theme web application for monitoring and controlling binary sensor inputs (fans, lights) across multiple rooms. Built with Flask and featuring a responsive, glassmorphic interface with real-time status tracking and email alerts.

## ✨ Features

### Dashboard & Analytics
- **System Overview Dashboard**: Real-time metrics (total sensors, active inputs, lights on, critical alerts)
- **Activity Log**: Color-coded event timeline with email and state change indicators
- **Quick Controls**: Fast appliance toggles for each room with visual status indicators
- **Responsive Grid**: Auto-adapting layout for desktop, tablet, and mobile devices

### Appliance Management
- **Input Status Form**: Batch update fan and light status for all rooms
- **Real-time Report**: Detailed status table with last-updated timestamps
- **Summary Cards**: Quick view of monitored rooms and active appliances
- **Email Integration**: Send status reports to specified email addresses

### Modern UI/UX
- **Dark Theme Interface**: Purple (#8848f9) primary color with emerald accents
- **Dark Palette System**: Full color scale from near-black to near-white
- **Sidebar Navigation**: Persistent menu with active state highlighting
- **Toggle Switches**: Smooth, accessible appliance state controls
- **Status Badges**: Color-coded ON/OFF visual indicators
- **Glassmorphic Cards**: Frosted glass effect with backdrop blur
- **Smooth Animations**: 200-300ms transitions and hover effects

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask (Python 3.10+) |
| **Templating** | Jinja2 |
| **Styling** | Custom CSS (dark mode) |
| **Icons** | Font Awesome 6.0 |
| **Type** | Server-rendered, no JavaScript framework |
| **Email** | SMTP (Gmail) |

## 📦 Requirements

- Python 3.7+
- Flask
- python-dotenv
- Internet connection (for email notifications)

## ⚡ Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/your-username/SmartRoom-ApplianceMonitor.git
cd SmartRoom-ApplianceMonitor
pip install -r requirements.txt
```

### 2. Configure Email (Optional)

Create a `.env` file:
```env
GMAIL_SENDER=your-email@gmail.com
GMAIL_PASSWORD=your-app-specific-password
```

**Note**: For Gmail, enable 2-factor authentication and generate an [App Password](https://support.google.com/accounts/answer/185833).

### 3. Run the Application

```bash
python appliance_monitor.py
```

Access at: **http://localhost:5000**

## 🎨 Pages & Routes

| Route | Page | Purpose |
|-------|------|---------|
| `/` | **Input Status** | Update appliance states per room |
| `/dashboard` | **System Overview** | Real-time metrics & activity log |
| `/report` | **Status Report** | Detailed appliance status table |

## 📁 Project Structure

```
SmartRoom-ApplianceMonitor/
├── appliance_monitor.py           # Flask app, routes, email service
├── requirements.txt               # Dependencies
├── .env                          # Environment config (not committed)
├── templates/
│   ├── layout.html               # Master layout with sidebar
│   ├── dashboard.html            # System overview page
│   ├── index.html                # Input status form
│   └── report.html               # Status report
├── static/
│   └── style.css                 # Dark theme stylesheet (1100+ lines)
└── ENHANCEMENT_SYNOPSIS.md       # Detailed technical documentation
```

## 🎛️ Configuration

### Room Setup

Edit `appliance_monitor.py` to customize rooms:
```python
ROOMS = ['A-11', 'A-12', 'A-13', 'A-14']  # Customize as needed
```

### Email Settings

The application sends HTML-formatted reports with styled tables:
- Sender: Configured via `GMAIL_SENDER` environment variable
- Template: Dynamically generated with room status colors
- Recipient: User-specified in the web form

### Color Scheme

Customize primary color in `static/style.css`:
```css
--primary: #8848f9;              /* Purple */
--primary-dark: #7c3aed;         /* Darker purple */
--primary-light: #a855f7;        /* Lighter purple */
```

## 📱 Responsive Design

| Breakpoint | Layout |
|------------|--------|
| **Desktop** (>1024px) | Full sidebar + 4-column grid |
| **Tablet** (768px-1024px) | Sidebar + 2-column grid |
| **Mobile** (<768px) | Horizontal nav + 1-column layout |
| **Ultra-mobile** (<480px) | Minimal nav, stacked forms |

## 🔒 Security Considerations

- ✓ Sensitive credentials in `.env` (excluded from git)
- ✓ HTML email templates with embedded styles
- ✓ No authentication (designed for trusted networks)
- ⚠️ Global state (single-user in-memory state)
- 📌 For production: Add CSRF protection, database persistence, user auth

## 🚀 Production Deployment

Deploy with Gunicorn and Nginx:

```bash
pip install gunicorn
gunicorn -w 4 -b localhost:8000 appliance_monitor:app
```

Then configure Nginx as reverse proxy to handle static files and SSL.

## 📊 Data Flow

1. User selects appliance states in **Input Status** form
2. Form submission to `POST /` route
3. Global state variables updated
4. Optional: Email report sent (async recommended)
5. Redirect to **Report** page
6. Can navigate to **Dashboard** for analytics view

## 🔌 API Routes

All server-rendered (no JSON API currently):
- `GET /` → Input form
- `POST /` → Update status & redirect
- `GET /dashboard` → System overview
- `GET /report` → Status report

## 📧 Email Template

HTML report includes:
- Date/time
- Room-by-room status table
- Color-coded ON (green) / OFF (red) badges
- Styled with inline CSS for email clients

## 🎯 Future Enhancements

- [ ] WebSocket for real-time updates
- [ ] Database persistence (SQLite/PostgreSQL)
- [ ] User authentication & multi-user support
- [ ] REST API for third-party integrations
- [ ] Mobile app (React Native / Flutter)
- [ ] Appliance scheduling & automation
- [ ] Usage analytics & energy tracking
- [ ] SMS/Push notifications
- [ ] Dark/Light mode toggle
- [ ] Multi-location support

## 📝 License

See [LICENSE](./LICENSE) file for details.

## 👨‍💻 Author

**Shreyansh** — Modern Python web stack enthusiast

---

**Version**: 2.0 (Dark Theme Redesign - April 2026)

**Latest Features**:
- ✨ Complete dark-theme refresh with glassmorphic design
- 📊 Real-time dashboard with system metrics
- 🎨 Brand new color system (purple primary, emerald/amber accents)
- 📱 Enhanced mobile responsiveness
- ⚡ Improved performance with optimized CSS
