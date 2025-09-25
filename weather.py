import tkinter as tk
import requests

API_KEY = "f5e2ffc80353b26127bc7544f657e776"
CITY = "Nairobi"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

if response.status_code == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    label = tk.Label(root, text=f"{CITY}: {temp}°C\n{desc}", font=("Arial", 14))
    label.pack(pady=50)
else:
    label = tk.Label(root, text="Error fetching weather", font=("Arial", 14))
    label.pack(pady=50)

root.mainloop()