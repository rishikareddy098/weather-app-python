import requests
import json

API_KEY = "dae0d6832c5174560f4bbf81d1da26e0"

city = input("Enter city name: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}&units=metric"
)

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["main"]

        print("\n============== Weather Report ==============")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print("=============================================")

    elif response.status_code == 404:
        print("City not found. Please enter a valid city name.")

    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Network error occurred:", e)