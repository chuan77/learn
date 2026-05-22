# Flask Weather App

A Flask web application that displays current weather information for any city using the OpenWeatherMap API.

## Features

- Search for weather by city name
- Display current temperature, humidity, wind speed, and feels-like temperature
- Weather icons and descriptions
- Responsive design with Bootstrap 5
- Error handling for invalid cities and API issues

## Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key (free)

## Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/chuan/Development/vscode/learn
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenWeatherMap API key:**
   
   - Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Set it as an environment variable:
     ```bash
     export OPENWEATHER_API_KEY=your_api_key_here
     ```
   - Or add it to a `.env` file (create one and add to `.gitignore`)

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open in browser:**
   ```
   http://localhost:5000
   ```

## Project Structure

```
learn/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html     # Main page with weather display
└── static/            # Static assets (CSS, JS, images)
```

## API Information

This app uses the OpenWeatherMap Current Weather Data API. For more details, visit:
https://openweathermap.org/api

## License

MIT License
