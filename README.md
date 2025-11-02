# Workout Generator - Web Application

## Overview
A personalized fitness plan creator with a modern web interface built using Flask, HTML, CSS, and JavaScript. This application generates customized workout routines based on user fitness profiles including BMI calculations, age, fitness level, and physical metrics.

## Project Purpose
- Create personalized workout plans for users of all fitness levels
- Calculate and display BMI with health categories
- Provide randomized, structured workout routines
- Web-based interface that can be deployed to the internet
- Demonstrate full-stack web development with Python Flask

## Current State
- ✅ Flask web application with REST API backend
- ✅ Modern, responsive HTML/CSS frontend
- ✅ BMI calculation and categorization
- ✅ Randomized exercise selection from categorized pools
- ✅ Structured workout plans (warm-up, cardio, strength, flexibility, cool-down)
- ✅ Motivational coaching messages
- ✅ Deployment-ready configuration for Replit
- ✅ Running on port 5000 for web deployment

## Recent Changes
- **2025-11-02**: Converted to web application for deployment
  - Created Flask backend (app.py) with REST API
  - Built responsive HTML/CSS frontend (templates/index.html)
  - Added modern styling with gradient design (static/css/style.css)
  - Configured workflow to run on port 5000
  - Set up autoscale deployment configuration
  - Maintained all workout generation logic from original version
  - Added smooth animations and better UX

## Project Architecture
```
.
├── app.py                    # Flask backend with workout generation API
├── templates/
│   └── index.html           # Main web interface
├── static/
│   └── css/
│       └── style.css        # Styling and responsive design
├── main.py                  # Original Tkinter version (archived)
├── .gitignore              # Python gitignore patterns
└── replit.md               # Project documentation
```

## Technical Stack
- **Language**: Python 3.11
- **Backend**: Flask (web framework)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: RESTful JSON API
- **Deployment**: Replit Autoscale (configured)

## Features
1. **User Input Collection (Web Form)**
   - Name, age range, gender
   - Height (cm) and weight (kg)
   - Fitness level (Beginner/Intermediate/Advanced)

2. **BMI Calculation**
   - Automatic BMI calculation from height/weight
   - Health category display (Underweight/Normal/Overweight/Obese)

3. **Workout Plan Generation**
   - Randomized exercise selection
   - Level-appropriate exercises
   - Structured format: warm-up → cardio → strength → flexibility → cool-down
   - Motivational messages

4. **Web UI Features**
   - Responsive design (works on desktop and mobile)
   - Modern gradient styling
   - Smooth animations
   - Scrollable workout plan display
   - Generate and Clear functionality
   - Professional color scheme

## How to Run (Development)
```bash
python app.py
```
The app will be available at http://localhost:5000

## Deployment
This application is configured for Replit Autoscale deployment:
- **Deployment Type**: Autoscale (stateless web application)
- **Port**: 5000
- **Run Command**: `python app.py`

To deploy:
1. Click the "Deploy" button in Replit
2. The app will be published with a public URL
3. Share the URL with users

## API Endpoints
- `GET /` - Main web interface
- `POST /generate` - Generate workout plan (JSON API)
  - Request body: `{name, age_range, gender, height, weight, fitness_level}`
  - Response: Personalized workout plan JSON

## Code Structure
- Flask backend with WorkoutGenerator class
- Exercise database organized by category and fitness level
- RESTful API for workout generation
- Modern, responsive frontend with vanilla JavaScript
- Clean separation of concerns (backend/frontend)

## User Preferences
None specified yet.

## Version History
- **v2.0** (2025-11-02): Web application with Flask backend
- **v1.0** (2025-11-02): Original Tkinter desktop application
