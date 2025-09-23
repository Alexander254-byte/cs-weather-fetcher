import requests

API_KEY = "f5e2ffc80353b26127bc7544f657e776"  
CITY = "Nairobi"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Current temperature in {CITY}: {temp}°C")
    print(f"Weather: {description}")
else:
    print(f"Error fetching weather data. Status code: {response.status_code}")
    print(f"Response: {response.text}")  # Debug: Shows API error details