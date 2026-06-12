import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(location):

   
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={location}"
        f"&appid={API_KEY}&units=metric"
    )

 
    response = requests.get(url)

  
    data = response.json()


    if data["cod"] != 200:

        return {
            "error": (
                "Kindly enter correct city "
                "and country name."
            )
        }


    user_country = location.split(",")[-1].strip().lower()

  
    api_country = data["sys"]["country"].lower()

  
    country_map = {
        "india": "in",
        "usa": "us",
        "uk": "gb",
        "france": "fr",
        "germany": "de"
    }

   
    expected_country = country_map.get(
        user_country,
        user_country
    )

    if expected_country != api_country:

        return {
            "error": (
                "Location not found. "
                "Please enter valid city "
                "and country."
            )
        }

   
    weather_info = {

        "city": data["name"],

        "country": data["sys"]["country"],

        "temperature": data["main"]["temp"],

        "humidity": data["main"]["humidity"],

        "weather": data["weather"][0]["main"],

        "description": data["weather"][0]["description"],

        "wind_speed": data["wind"]["speed"]
    }

    return weather_info