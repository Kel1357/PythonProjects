import requests
from datetime import datetime
APIKEY = "3d576fa459cf57ab4039cd0ff50be96d"
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    query_params = {
        "q": city,
        "appid": APIKEY,
        "units": "metric",
    }
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
        json_response = response.json()
        json_weather = json_response["weather"][0]
        json_description = json_weather["description"]
        json_temperature = json_response["main"]["temp"]
        json_feels_like = json_response["main"]["feels_like"]
        json_humidity = json_response["main"]["humidity"]
        json_wind_speed = json_response["wind"]["speed"]
        json_pressure = json_response["main"]["pressure"]
        json_sunrise = json_response["sys"]["sunrise"]
        sunrise_time = datetime.fromtimestamp(json_sunrise)
        json_sunset = json_response["sys"]["sunset"]
        sunset_time = datetime.fromtimestamp(json_sunset)
        json_visibility = json_response["visibility"]
        json_coverage=json_response["clouds"]["all"]
        json_condition_icon = json_weather["icon"]
        json_condition = json_weather["main"]
        return json_description,json_temperature,json_feels_like,json_humidity,json_wind_speed,json_pressure,sunrise_time,sunset_time,json_visibility,json_coverage,json_condition_icon,json_condition
    except requests.exceptions.RequestException:
        return None
    except KeyError,IndexError:
        return None
if __name__ == "__main__":
    city=input("Enter the City:=")
    res = get_weather(city)
    if res:
        description,temperature,feels_like,humidity,wind_speed,pressure,sunrise,sunset,visibility,coverage,condition_icon,condition=res
        print(f"Condition: {condition}({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Temperature Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed}km/h")
        print(f"Pressure: {pressure}hPa")
        print(f"Sunrise: {sunrise.strftime('%H:%M:%S')}")
        print(f"Sunset: {sunset.strftime('%H:%M:%S')}")
        print(f"Visibility: {visibility/1000:.1f}km")
        print(f"Cloud Coverage: {coverage}%")
        print(f"Icon: {condition_icon}")
    else:
        print("Couldn't retrieve weather data")

