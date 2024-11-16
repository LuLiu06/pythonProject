import requests


def get_weather_for_city():
    api_key = "0622b354835a8009f0ab7d2139c6aa29"
    city = input("Enter the name of a municipality: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print("Failed to fetch weather data. Please check the city name or API key.")


get_weather_for_city()