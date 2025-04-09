
import requests
def get_weather(city, API):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        
        data = response.json()
        print(response.json())
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city}:")
        print(f"\tTemperature: {temp}°C")
        print(f"\tCondition: {weather}")
        print(f"\tHumidity: {humidity}%")
        print(f"\tWind Speed: {wind_speed} m/s")
    else:
        print("City not found or error fetching data.")

API = "01a778b1a43402824bd0eae515475627"  
city = input("Enter city name: ")
get_weather(city, API)
