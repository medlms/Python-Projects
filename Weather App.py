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
    # Making a request to the OpenWeatherMap API
    response = requests.get(base_url, params=params)
    
    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()    
        
