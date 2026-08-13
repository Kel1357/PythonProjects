import python_weather
import asyncio
async def get_weather_celsius(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather=await client.get(city)
        print(f"Current Temperature: {weather.temperature}°C")
        print(f"Feels Like Temperature: {weather.feels_like}°C")
        print("Upcoming Forecasts:")
        for daily in weather.daily_forecasts:
            print(f"{daily.date}: {daily.temperature}°C")
async def get_weather_fahrenheit(city):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather=await client.get(city)
        print(f"Current Temperature: {weather.temperature}°F")
        print(f"Feels Like Temperature: {weather.feels_like}°F")
        print("Upcoming Forecasts:")
        for daily in weather.daily_forecasts:
            print(f"{daily.date}: {daily.temperature}°F")
async def get_weather_kelvin(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather=await client.get(city)
        kelvin_temp=weather.temperature+273.15
        print(f"Current Temperature: {kelvin_temp:.2f}K")
        print(f"Feels Like Temperature: {weather.feels_like}K")
        print("Upcoming Forecasts:")
        for daily in weather.daily_forecasts:
            kelvin_temp=daily.temperature + 273.15
            print(f"{daily.date}: {kelvin_temp:.2f}K")
async def get_data(city):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather=await client.get(city)
        print(f"Description: {weather.description}")
        print(f"Humidity: {weather.humidity}%")
        print(f"Wind Speed: {weather.wind_speed}kph")
        print(f"Pressure: {weather.pressure}hPa")
        print(f"Visibility: {weather.visibility}km")
        print(f"Cloud Coverage: {weather.cloud_cover}%")
if __name__ =='__main__':
    city=input("Enter city name:=")
    while True:
        print(f"\nWeather Report for {city}:")
        print("1. Temperature In Celsius(°C)")
        print("2. Temperature In Fahrenheit(°F)")
        print("3. Temperature In Kelvin(K)")
        print("4. Additional Weather Related Information")
        print("0. Exit")
        try:
            n=int(input("Enter the Choice:="))
            if n==1:
                asyncio.run(get_weather_celsius(city))
            elif n==2:
                asyncio.run(get_weather_fahrenheit(city))
            elif n==3:
                asyncio.run(get_weather_kelvin(city))
            elif n==4:
                asyncio.run(get_data(city))
            elif n==0:
                print("Program Exited Successfully")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Value, Please Try Again")

