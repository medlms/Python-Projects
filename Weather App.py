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
                
        # Extracting weather details
        main = data['main']
        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        
        weather_desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

 # Displaying the weather details
        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        # Error handling for unsuccessful requests
        print("Error: Unable to fetch weather data. Please check the city name or your API key.")
        
# Usage example:
if __name__ == "__main__":
    city = input("Enter the city name: ")
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    get_weather(city, api_key)
        

        
