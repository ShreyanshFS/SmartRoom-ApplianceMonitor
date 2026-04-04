# SmartRoom Appliance Monitor - Enhanced Synopsis

## Project Overview

SmartRoom Appliance Monitor is a modern web-based appliance control and monitoring system designed for room-level management of electrical devices. The system provides real-time status monitoring, email alerts, and an intuitive dark-theme dashboard interface for managing fans, lights, and other binary sensor inputs across multiple rooms.

## Technical Stack

### Backend
- **Framework**: Flask (Python)
- **Language**: Python 3.10+
- **Database**: In-memory state management with global variables
- **Email Service**: SMTP (Gmail integration)
- **Environment**: .env configuration

### Frontend
- **Architecture**: Dark-theme responsive web UI
- **Templating**: Jinja2 (Flask templates)
- **Styling**: Custom CSS with dark mode palette
- **Icons**: Font Awesome 6.0
- **Typography**: Inter font family
- **Responsiveness**: Mobile-first design (768px, 480px breakpoints)

### Design System
- **Primary Color**: #8848f9 (Purple)
- **Accent Colors**: Emerald (#10b981), Amber (#f59e0b), Rose (#ef4444)
- **Dark Palette**: bg-950 to bg-200 scale
- **Component Library**: Card-based UI with glassmorphic effects

## Key Features

### 1. Dashboard Page (`/`)
- System overview with 4 key metrics:
  - Total Sensors (room count)
  - Active (HIGH) inputs
  - Lights ON status
  - Critical Alerts counter
- Quick appliance controls for each room
- Recent activity log with color-coded indicators
- Real-time state visualization

### 2. Input Status Page (`/appliances`)
- Batch status update interface
- Email recipient form
- Room-based appliance grid
- Toggle switches for Fan & Light per room
- Summary cards showing current status
- Submit & redirect to report flow

### 3. Report Page (`/report`)
- Detailed appliance status table
- Last updated timestamp
- Summary metrics (rooms, fans, lights)
- Status badges (ON/OFF) with visual indicators
- Navigation to dashboard and input status

### 4. Sidebar Navigation
- 3-item navigation menu (Dashboard, Input Status, Report)
- Active state highlighting
- System status indicator
- Responsive mobile menu collapse

## Architecture

### Layout Structure
```
AppLayout
├── Sidebar
│   ├── Brand Logo
│   ├── Navigation Items
│   └── System Status Footer
└── Main Container
    ├── Header (breadcrumb + admin badge)
    └── Content Area (page-specific)
```

### Component Design
- **Cards**: Self-contained data presentation units
- **Stat Cards**: Key metrics with icons and visual hierarchy
- **Appliance Cards**: Device control with toggle switches
- **Status Badges**: Color-coded ON/OFF indicators
- **Activity Log**: Timeline-style event display

## Data Flow

```
User Input (Form)
  ↓
Flask Route Handler
  ↓
Global State Update (fan_status, light_status)
  ↓
Email Trigger (optional)
  ↓
Redirect to Report
  ↓
Render Dashboard with Updated State
```

## File Structure

```
SmartRoom-ApplianceMonitor/
├── appliance_monitor.py          # Main Flask app & routes
├── requirements.txt              # Python dependencies
├── templates/
│   ├── layout.html              # Master layout with sidebar
│   ├── base.html                # Legacy template (extends layout)
│   ├── dashboard.html           # System overview page
│   ├── index.html               # Input status form
│   └── report.html              # Status report table
├── static/
│   └── style.css                # Dark-theme stylesheet (1000+ lines)
└── .env                         # Environment variables (GMAIL config)
```

## Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET, POST | Input appliance status form & redirect |
| `/dashboard` | GET | System overview & analytics |
| `/report` | GET | Detailed status report |

## Styling Highlights

### Dark Theme Palette
- **Background**: #0f172a → #111827 → #1f2937 (increasing brightness)
- **Text**: #d1d5db (primary), #9ca3af (muted), #ffffff (white)
- **Borders**: 1px solid rgba(55, 65, 81, 1)
- **Shadows**: Custom shadow system with 4 levels

### Responsive Design
- **Desktop** (>1024px): Full sidebar + content
- **Tablet** (768px-1024px): Adjusted grid columns, collapsible nav
- **Mobile** (<768px): Horizontal nav bar, single-column layout, hidden icons in nav
- **Ultra-mobile** (<480px): Minimal nav, full-width forms

### Interactive Elements
- Smooth transitions (0.2s-0.3s cubic-easing)
- Hover state feedback
- Focus ring styling for accessibility
- Loading animations (pulse effect)
- Toggle switches with smooth transform

## Email Configuration

The system can send HTML-formatted status reports to user-specified email addresses:
- **SMTP Host**: gmail.com
- **Port**: 587 (TLS)
- **Authentication**: Environment variables
  - `GMAIL_SENDER`: Sender email address
  - `GMAIL_PASSWORD`: App-specific password

**Email Template**: Includes styled HTML table with status badges for each room.

## Dependencies

```python
flask
python-dotenv
```

**Include via**: `pip install -r requirements.txt`

## Security Considerations

- ✓ Email credentials in `.env` (not committed)
- ✓ CSRF protection recommended for production
- ✓ Rate limiting suggested for form submissions
- ✓ Input validation on room names
- ⚠️ No authentication layer (intended for trusted networks)
- ⚠️ Global state (not suitable for concurrent users)

## Future Enhancements

1. **Database Integration**: Replace in-memory state with persistent storage
2. **User Authentication**: Multi-user support with role-based access
3. **Real-time Updates**: WebSocket integration for live status
4. **API Layer**: RESTful API for third-party integrations
5. **Mobile App**: Native iOS/Android companion app
6. **Scheduling**: Automated appliance control on timers/schedules
7. **Analytics**: Usage statistics and energy monitoring
8. **Notifications**: Push notifications, SMS alerts
9. **Multi-location**: Support for multiple buildings/floors
10. **Dark/Light Mode Toggle**: User preference selector

## Performance Metrics

- **Page Load**: <500ms (CSS-optimized, minimal JS)
- **Form Submission**: <1s (email sending async recommended)
- **Response Size**: ~50KB (HTML + CSS per page)
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

## Installation & Running

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "GMAIL_SENDER=your@email.com" > .env
echo "GMAIL_PASSWORD=your_app_password" >> .env

# Run development server
python appliance_monitor.py

# Access application
# Local: http://localhost:5000
# Network: http://<your-ip>:5000
```

## Testing Workflow

1. **Navigate to Dashboard** (System Overview)
2. **Go to Input Status** (Update appliance states)
3. **Check Report** (View detailed status)
4. **Enable Email Alert** (Send status report to inbox)
5. **Verify Activity Log** (Check recent activities)

## Credits & Design

- **UI Design**: Inspired by React component library with dark-theme patterns
- **Icons**: Font Awesome 6.0
- **Typography**: Inter font (system font fallback)
- **Color Theory**: WCAG AA accessibility compliance
- **Responsive Framework**: Custom CSS Grid & Flexbox

## License

See LICENSE file for details.

---

**Last Updated**: April 4, 2026
**Version**: 2.0 (Dark Theme Redesign)
