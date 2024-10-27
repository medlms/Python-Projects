import requests

def get_weather(city, api_key):
    # OpenWeatherMap API endpoint for current weather data
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # 'metric' for Celsius; use 'imperial' for Fahrenheit
    }
    
