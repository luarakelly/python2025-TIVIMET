import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_MAP_KEY = os.getenv("OPEN_WEATHER_MAP_KEY")

def get_weather_for_city(city_name, api_key):
    """
    Fetch current weather for the given city using OpenWeatherMap API.
    Returns a tuple: (weather description, temperature in Celsius)
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to get weather data: HTTP {response.status_code}")
        return None

    data = response.json()
    weather_desc = data["weather"][0]["description"]  # weather description
    temp_celsius = data["main"]["temp"]              # temperature in Celsius
    return weather_desc, temp_celsius

def main():
    if OPEN_WEATHER_MAP_KEY is None:
        print("No API key found. Make sure OPEN_WEATHER_MAP_KEY is set in your .env file.")
        return

    city = input("Enter the city name: ").strip()
    result = get_weather_for_city(city, OPEN_WEATHER_MAP_KEY)
    
    if result is None:
        print("Could not retrieve weather information. Please check the city name or your API key.")
    else:
        desc, temp = result
        print(f"The weather in {city} is: {desc}")
        print(f"Temperature: {temp:.1f} °C")

main()
