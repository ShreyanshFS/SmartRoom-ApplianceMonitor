# SmartRoom Appliance Monitor - Presentation Update Guide

**Updated**: April 2026  
**Version**: 2.0 (Dark Theme Redesign)

This guide provides the content, visuals, and specifications for updating the PowerPoint presentation with the new dark-theme frontend enhancements.

---

## 📊 Presentation Structure

### Slide 1: Title Slide
**Title**: SmartRoom Appliance Monitor v2.0  
**Subtitle**: Modern Dark-Theme Web Interface for Real-Time Appliance Control  
**Visual**: Dark background (#1a1a2e), purple accent border (4px, #8848f9)  
**Content**: 
- Project name in large font (white)
- Version badge (v2.0 - Dark Theme)
- Date and author
- Icon: Control/Dashboard symbol

---

### Slide 2: Executive Summary
**Title**: What's New in v2.0?

**Bullet Points**:
- ✨ Complete UI redesign with dark theme
- 📊 Real-time dashboard with system metrics
- 🎨 Modern color system (purple primary, emerald/amber accents)
- 📱 Enhanced mobile responsiveness (3 breakpoints)
- ⚡ Improved performance & accessibility
- 🔄 New routes: Dashboard, Input Status, Report

**Color Scheme Box**:
```
Primary:    #8848f9 (Purple)
Accent 1:   #10b981 (Emerald - Active)
Accent 2:   #f59e0b (Amber - Warning)
Accent 3:   #ef4444 (Rose - Critical)
Background: #0f172a (Near-Black)
Surface:    #1e293b, #334155 (Dark Slate)
```

---

### Slide 3: User Interface Overview
**Title**: Dark Theme Interface - Key Features

**Four-Column Layout** (with mockup thumbnails):

#### Column 1: Dashboard Page
- **Mockup**: Show dashboard.html screenshot
- **Features**:
  - 4 Stat cards (Total Sensors, Active, Lights ON, Alerts)
  - Appliance control grid
  - Activity log with indicators
  - Color: Purple primary with emerald badges

#### Column 2: Input Status Page
- **Mockup**: Show index.html screenshot
- **Features**:
  - Email input field
  - Summary cards
  - Room toggle switches
  - Submit button (purple gradient)
  - Color: Dark background, white text

#### Column 3: Report Page
- **Mockup**: Show report.html screenshot
- **Features**:
  - Real-time status table
  - Status badges (ON/OFF)
  - Timestamp display
  - Room-by-room breakdown
  - Color: Emerald (ON), Rose (OFF)

#### Column 4: Sidebar Navigation
- **Mockup**: Show sidebar from any page
- **Features**:
  - Brand logo area
  - 3 navigation items (Dashboard, Input Status, Report)
  - System status indicator (with pulse animation)
  - Active state highlighting

**Visual Style Note**: All mockups use dark theme (#0f172a background, #ffffff text, #8848f9 accents)

---

### Slide 4: Design System
**Title**: Color Palette & Component Design

**Layout**: Two sections

#### Section A: Color System
**Color Grid** (8x3):
1. **Primary Colors**:
   - #8848f9 Base Purple
   - #7c3aed Dark Purple
   - #a855f7 Light Purple

2. **Semantic Colors**:
   - #10b981 Emerald (Active/Success)
   - #f59e0b Amber (Warning)
   - #ef4444 Rose (Critical/Error)

3. **Neutral Scale**:
   - #0f172a (Slate-950 - background)
   - #1e293b (Slate-800 - surface)
   - #334155 (Slate-700 - hover)
   - #64748b (Slate-500 - text secondary)
   - #e2e8f0 (Slate-200 - text primary)
   - #ffffff (White - text on colored)

#### Section B: Key Components
**Visual mockups** of:

1. **Stat Card**
   ```
   [Icon Badge: emerald] 
   Large Metric Value
   "Label"
   ```

2. **Status Badge**
   ```
   ON (emerald background)    |    OFF (rose background)
   ```

3. **Toggle Switch**
   ```
   OFF State → [ON State]
   (color changes from slate to purple)
   ```

4. **Appliance Card**
   ```
   Room Name
   [Fan Toggle] [Light Toggle]
   Status indicators below
   ```

---

### Slide 5: Architecture Diagram
**Title**: Application Architecture

**Three-Layer Diagram**:

```
┌─────────────────────────────────────────┐
│       FRONTEND LAYER (Templates)        │
├─────────────────────────────────────────┤
│ Layout.html (Master)                    │
│  ├─ Sidebar Navigation                  │
│  ├─ Header with System Status           │
│  ├─ Main Content Area                   │
│  └─ Footer                              │
│                                         │
│ Templates (extend layout.html):         │
│  ├─ Dashboard.html (Stats & Log)        │
│  ├─ Index.html (Input Form)             │
│  └─ Report.html (Status Table)          │
└─────────────────────────────────────────┘
              ↑ Jinja2 Rendering
┌─────────────────────────────────────────┐
│      BACKEND LAYER (Flask Routes)       │
├─────────────────────────────────────────┤
│ appliance_monitor.py                    │
│  ├─ GET / → Render index form           │
│  ├─ POST / → Update state → Redirect    │
│  ├─ GET /dashboard → Render stats       │
│  └─ GET /report → Render table          │
│                                         │
│ Global State (In-Memory):               │
│  ├─ fan_status (dict)                   │
│  ├─ light_status (dict)                 │
│  └─ last_update (timestamp)             │
└─────────────────────────────────────────┘
               ↑ HTTP Routes
┌─────────────────────────────────────────┐
│      STYLING LAYER (CSS System)         │
├─────────────────────────────────────────┤
│ static/style.css (1100+ lines)          │
│  ├─ CSS Custom Properties (:root)       │
│  ├─ Sidebar & Navigation Styles         │
│  ├─ Card Component Styles               │
│  ├─ Form & Toggle Styles                │
│  └─ Responsive Breakpoints              │
│     (Desktop, Tablet, Mobile)           │
└─────────────────────────────────────────┘
```

**Data Flow Arrow**:
```
User Form Input → POST /
  ↓
Global State Updated (fan_status, light_status)
  ↓
[Optional] Send Email Report (SMTP)
  ↓
Redirect to GET /report
  ↓
Display Status Table (via report.html)
```

---

### Slide 6: Responsive Design
**Title**: Mobile-First Responsive Layout

**Three Device Mockups** (side-by-side):

#### Desktop (>1024px)
```
┌──────────────────────────────────┐
│ [Sidebar]   [Main Content Area]  │
│   Logo          [Header]         │
│   Dashboard     ┌──────────────┐  │
│   Input Status  │ Stat Card 1  │  │
│   Report        │ Stat Card 2  │  │
│   Status        │ Stat Card 3  │  │
│   [System]      │ Stat Card 4  │  │
│                 └──────────────┘  │
│                 ┌──────────────┐  │
│                 │              │  │
│                 │ 2-Col Grid   │  │
│                 │              │  │
│                 └──────────────┘  │
└──────────────────────────────────┘
```
**Feature**: 4-column layout, full sidebar visible, stats in 2x2 grid

#### Tablet (768px-1024px)
```
┌──────────────┐
│ [Sidebar]    │
│  Logo        │
│  Dash ▼      │  [Main Content Area]
│  Input ▼     │  ┌──────────────┐
│  Report ▼    │  │ Stat Card 1  │
│  Status ▼    │  │ Stat Card 2  │
│              │  └──────────────┘
│              │  ┌──────────────┐
│              │  │ 2-Col Grid   │
│              │  └──────────────┘
└──────────────┘
```
**Feature**: Sidebar collapsed to icons, 2-column content grid

#### Mobile (<768px)
```
┌──────────────┐
│ [Mobile Nav] │
│ ☰ Dashboard  │
│   🔹 • •     │
├──────────────┤
│ [Content]    │
│              │
│ Stat Card 1  │
│              │
│ Stat Card 2  │
│              │
│ 1-Col Grid   │
│              │
└──────────────┘
```
**Feature**: Horizontal navigation, single-column layout, full-width cards

**CSS Media Queries Table**:
| Breakpoint | Layout | Features |
|------------|--------|----------|
| >1024px | Desktop | Full sidebar, 4-col grid |
| 768-1024px | Tablet | Sidebar icons, 2-col grid |
| <768px | Mobile | Horizontal nav, 1-col layout |
| <480px | Ultra-mobile | Stacked nav, minimal spacing |

---

### Slide 7: Technology Stack
**Title**: Tech Stack & Dependencies

**Backend Framework**:
- **Framework**: Flask (Python 3.10+)
- **Templating**: Jinja2
- **Server**: Werkzeug (development), Gunicorn (production)
- **Email**: SMTP (Gmail integration via .env)

**Frontend**:
- **Type**: Server-rendered HTML/CSS (No JavaScript framework)
- **Styling**: Custom CSS (1100+ lines, CSS variables)
- **Icons**: Font Awesome 6.0
- **Fonts**: Inter + system fallbacks

**Configuration**:
- **.env File**: Stores GMAIL_SENDER, GMAIL_PASSWORD
- **Dependencies File**: requirements.txt
- **Database**: In-memory state (dict-based, single-user)

**Dependencies**:
```
flask
python-dotenv
```

**Optional (Production)**:
```
gunicorn
```

---

### Slide 8: File Structure & Routes
**Title**: Project Organization

**Directory Tree**:
```
SmartRoom-ApplianceMonitor/
├── appliance_monitor.py           [Flask app, routes, email]
├── requirements.txt               [pip dependencies]
├── .env                          [Configuration secrets]
├── README.md                     [User documentation]
├── ENHANCEMENT_SYNOPSIS.md       [Technical details]
├── templates/
│   ├── layout.html               [Master layout + sidebar]
│   ├── dashboard.html            [System overview]
│   ├── index.html                [Input status form]
│   ├── report.html               [Status report]
│   └── base.html                 [Legacy redirect]
└── static/
    └── style.css                 [Dark theme stylesheet]
```

**API Routes Table**:

| Endpoint | Method | Purpose | Template | Status |
|----------|--------|---------|----------|--------|
| `/` | GET | Show input form | index.html | 200 OK |
| `/` | POST | Update state → redirect | - | 302 Redirect |
| `/dashboard` | GET | System overview | dashboard.html | 200 OK |
| `/report` | GET | Status report | report.html | 200 OK |

---

### Slide 9: Data Flow & Email Integration
**Title**: User Workflow & Email Reports

**Process Flow Diagram**:

```
1. USER INTERACTION
   ┌─────────────────────────────┐
   │ User opens /                │
   │ Sees Input Status Form      │
   │ - Email input field         │
   │ - Room toggles (F/L)        │
   │ - Summary cards             │
   └─────────────────────────────┘
              ↓ User submits form (POST /)

2. BACKEND PROCESSING
   ┌─────────────────────────────┐
   │ Flask processes POST request│
   │ Updates global state:       │
   │ - fan_status[room]          │
   │ - light_status[room]        │
   │ - last_update = now()       │
   └─────────────────────────────┘
              ↓

3. EMAIL NOTIFICATION (Optional)
   ┌─────────────────────────────┐
   │ Generates HTML email        │
   │ Creates styled table:       │
   │ - Room names                │
   │ - Fan status (color badges) │
   │ - Light status (color)      │
   │ - Timestamp                 │
   │ Sends via SMTP (Gmail)      │
   └─────────────────────────────┘
              ↓ If email configured

4. REDIRECT & DISPLAY
   ┌─────────────────────────────┐
   │ Redirect to /report         │
   │ Display report.html         │
   │ Shows:                      │
   │ - Status summary cards      │
   │ - Detailed status table     │
   │ - Navigation links          │
   └─────────────────────────────┘
              ↓

5. ANALYTICS VIEW (Optional)
   ┌─────────────────────────────┐
   │ User can navigate to        │
   │ /dashboard to see:          │
   │ - 4 metric cards            │
   │ - Activity log              │
   │ - Quick controls            │
   └─────────────────────────────┘
```

**Email Template Example**:
```
┌─────────────────────────────────┐
│ SmartRoom Status Report         │
│ Date: 2026-04-04 09:18:45       │
├─────────────────────────────────┤
│ Room  │  Fan  │  Light          │
├───────┼───────┼─────────────────┤
│ A-11  │ ON    │ OFF             │
│       │(green)│ (red)           │
├───────┼───────┼─────────────────┤
│ A-12  │ OFF   │ ON              │
│       │(red)  │ (green)         │
├───────┼───────┼─────────────────┤
│ A-13  │ ON    │ ON              │
│       │(green)│ (green)         │
├───────┼───────┼─────────────────┤
│ A-14  │ OFF   │ OFF             │
│       │(red)  │ (red)           │
└─────────────────────────────────┘
```

---

### Slide 10: Feature Highlights
**Title**: What Makes v2.0 Special

**Six Feature Boxes** (2x3 grid):

1. **Dark Theme**
   - 🌙 Emerald/Purple color scheme
   - Eye-friendly interface
   - Glassmorphic design elements

2. **Real-Time Dashboard**
   - 📊 4 key metrics (Total, Active, Lights ON, Alerts)
   - Activity log with indicators
   - Quick appliance controls

3. **Responsive Design**
   - 📱 Desktop/Tablet/Mobile optimized
   - Touch-friendly toggle switches
   - Adaptive layouts

4. **Email Integration**
   - 📧 Automatic report sending
   - Styled HTML templates
   - Color-coded status indicators

5. **Modern UI Components**
   - ✨ Status badges
   - Toggle switches
   - Summary cards
   - Activity timeline

6. **Performance**
   - ⚡ Server-rendered (no JS framework)
   - Fast page loads
   - Optimized CSS (1100 lines)

---

### Slide 11: Security & Considerations
**Title**: Security & Future Roadmap

**Security Measures** (Left Column):
✓ Sensitive credentials in .env (excluded from git)  
✓ HTML-safe email templates  
✓ Server-side state management  
✓ No sensitive data in URLs  
✓ Flask auto-escaping enabled  
✓ CORS headers considered  
✓ Input validation on routes  

**⚠️ Limitations** (Right Column):
- No user authentication (trusted network only)
- Single-user in-memory state
- No database persistence
- No real-time WebSocket updates
- Limited to local error handling

**Production Checklist**:
- [ ] Add CSRF protection
- [ ] Implement database (SQLite/PostgreSQL)
- [ ] Deploy with Gunicorn + Nginx
- [ ] Add SSL/TLS certificates
- [ ] Set up proper logging
- [ ] Implement user authentication
- [ ] Add automated tests

---

### Slide 12: Deployment Guide
**Title**: Getting Started - Installation & Running

**Step 1: Clone Repository**
```bash
git clone https://github.com/your-username/SmartRoom-ApplianceMonitor
cd SmartRoom-ApplianceMonitor
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Configure (Optional)**
```bash
# Create .env file
echo "GMAIL_SENDER=your-email@gmail.com" > .env
echo "GMAIL_PASSWORD=your-app-password" >> .env
```

**Step 4: Run Application**
```bash
python appliance_monitor.py
```

**Step 5: Access Web Interface**
- Open browser: **http://localhost:5000**
- Navigate to Dashboard, Input Status, or Report

**Production Deployment**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 appliance_monitor:app
```

**Then configure Nginx** as reverse proxy for SSL and static files.

---

### Slide 13: Future Enhancements & Roadmap
**Title**: v2.1+ Planned Features

**Near Term** (Q2 2026):
- [ ] WebSocket for real-time updates
- [ ] SQLite database persistence
- [ ] User authentication with roles
- [ ] Mobile app (React Native starter)

**Medium Term** (Q3-Q4 2026):
- [ ] REST API endpoints
- [ ] Appliance scheduling
- [ ] Energy usage tracking
- [ ] SMS/Push notifications

**Long Term** (2027):
- [ ] Multi-location support
- [ ] Machine learning anomaly detection
- [ ] Integration with smart home hubs
- [ ] Advanced analytics & reports
- [ ] Dark/Light mode toggle
- [ ] Multi-language support

---

### Slide 14: Q&A / Contact
**Title**: Questions?

**Key Takeaways**:
1. ✨ Modern dark-theme UI with 3 responsive pages
2. 📊 Real-time dashboard and activity tracking
3. 🎨 Professional color system (purple + emerald + amber + rose)
4. 📱 Mobile-first responsive design
5. ⚡ Server-rendered architecture (no JavaScript framework)
6. 🚀 Easy to deploy and customize

**Links**:
- GitHub: github.com/[username]/SmartRoom-ApplianceMonitor
- Documentation: See ENHANCEMENT_SYNOPSIS.md
- Demo: http://localhost:5000

**Contact**: [Your Email/LinkedIn]

---

## 📐 Design Specifications for PPTX Update

### Font & Text
- **Heading Font**: Arial Bold, 44pt, #ffffff
- **Subheading Font**: Arial, 28pt, #a855f7 (light purple)
- **Body Font**: Arial, 16pt, #e2e8f0 (light slate)
- **Code Font**: Courier New, 12pt, #10b981 (emerald)

### Colors (Hex Codes)
- **Background**: #0f172a (Slate-950)
- **Secondary Background**: #1e293b (Slate-800)
- **Primary Accent**: #8848f9 (Purple)
- **Success Accent**: #10b981 (Emerald)
- **Warning Accent**: #f59e0b (Amber)
- **Error Accent**: #ef4444 (Rose)
- **Text Primary**: #ffffff (White)
- **Text Secondary**: #e2e8f0 (Light Slate)

### Layout Guidelines
- **Slide Aspect**: 16:9 widescreen
- **Margin**: 0.5" on all sides
- **Column Width**: Use 3-column grid for multi-section layouts
- **Visual Hierarchy**: Heading → Subheading → Body (consistent sizing)

### Image Recommendations
- **Dashboard Screenshot**: 1200x800px PNG
- **Input Form Screenshot**: 1200x800px PNG
- **Report Page Screenshot**: 1200x800px PNG
- **Architecture Diagram**: Vector diagram (SVG/High-res PNG)
- **Color Palette**: Grid showing all 12 colors with hex codes

---

## 🔄 Manual PPTX Update Process

### Using PowerPoint Desktop/Online

1. **Open** `SmartRoom_ApplianceMonitor.pptx`
2. **For Each Slide** (refer to content above):
   - Replace title and content
   - Update background to #0f172a (dark slate)
   - Use specified fonts and colors
   - Add mockup images where indicated
3. **Save** with same filename
4. **Export** as PDF for stakeholder sharing

### Using Python (Alternative)

```python
# Example using python-pptx library
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

prs = Presentation('SmartRoom_ApplianceMonitor.pptx')
# Add/modify slides with dark theme colors
# Code available in ENHANCEMENT_SYNOPSIS.md
```

---

## ✅ Verification Checklist

- [ ] Slide 1: Title slide with dark background and purple accent
- [ ] Slide 2: Executive summary with 6 key features listed
- [ ] Slide 3: UI overview with 4 screenshot mockups
- [ ] Slide 4: Design system with color palette (12 colors + 4 components)
- [ ] Slide 5: Architecture diagram (3-layer + data flow)
- [ ] Slide 6: Responsive design (3 device mockups)
- [ ] Slide 7: Tech stack (6 sections, clear formatting)
- [ ] Slide 8: File structure (directory tree + routes table)
- [ ] Slide 9: Data flow (5-step process + email template)
- [ ] Slide 10: Feature highlights (6 boxes, emojis)
- [ ] Slide 11: Security & roadmap (dual columns)
- [ ] Slide 12: Deployment guide (5-step process + commands)
- [ ] Slide 13: Future enhancements (3 quarters, checkboxes)
- [ ] Slide 14: Q&A slide with key takeaways

---

**Last Updated**: April 2026  
**Total Slides Recommended**: 14  
**Estimated Update Time**: 2-3 hours (manual)  
**Tools Needed**: PowerPoint 2016+ or Google Slides
