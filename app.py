import os
from flask import Flask, render_template, request
from flask_caching import Cache
import requests

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = '8e0e3a41490b5d8afda55687c835b32d'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Cache configuration
CACHE_TTL = int(os.environ.get('CACHE_TTL', 600))  # Default 10 minutes
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = CACHE_TTL
cache = Cache(app)

@cache.memoize(timeout=CACHE_TTL)
def get_weather_cached(city):
    """Fetch weather data for a given city from OpenWeatherMap API (cached)."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {'error': 'City not found'}
        elif response.status_code == 401:
            return {'error': 'Invalid API key'}
        else:
            return {'error': f'Error fetching weather: {str(e)}'}
    except requests.exceptions.RequestException as e:
        return {'error': f'Network error: {str(e)}'}

def get_weather(city):
    """Fetch weather data for a given city (wrapper that clears cache on miss)."""
    return get_weather_cached(city)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if city:
            weather_data = get_weather(city)
            if weather_data.get('error'):
                error = weather_data['error']
                weather_data = None
        else:
            error = 'Please enter a city name'
    
    return render_template('index.html', 
                         weather_data=weather_data, 
                         error=error,
                         api_key_set=API_KEY != 'YOUR_API_KEY_HERE')

if __name__ == '__main__':
    app.run(debug=True)
