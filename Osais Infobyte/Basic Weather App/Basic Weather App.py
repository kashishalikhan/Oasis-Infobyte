import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

API_KEY = "82c0bc52be4150e375de8804189ef80d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city):
    try:
        response = requests.get(f"{BASE_URL}appid={API_KEY}&q={city}")
        data = response.json()
        if data["cod"] != "404":
            return data
        else:
            messagebox.showerror("Error", "City Not Found")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")

def display_weather(data):
    city, country = data["name"], data["sys"]["country"]
    temp_k = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]
    wind_speed, humidity = data["wind"]["speed"], data["main"]["humidity"]
    icon_id = data["weather"][0]["icon"]
    
    temp = temp_k - 273.15 if unit_var.get() == "Celsius" else (temp_k - 273.15) * 9/5 + 32
    temp_unit = "°C" if unit_var.get() == "Celsius" else "°F"

    weather_info = f"City: {city}, {country}\nTemperature: {temp:.2f} {temp_unit}\nWeather: {weather_desc}\nWind Speed: {wind_speed} m/s\nHumidity: {humidity}%"
    weather_display.config(text=weather_info)

    icon_data = requests.get(f"http://openweathermap.org/img/wn/{icon_id}.png").content
    icon_image = ImageTk.PhotoImage(Image.open(io.BytesIO(icon_data)).resize((100, 100)))
    weather_icon.config(image=icon_image)
    weather_icon.image = icon_image

def show_weather():
    city = city_entry.get()
    if city:
        data = get_weather_data(city)
        if data:
            display_weather(data)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

def reset():
    city_entry.delete(0, tk.END)
    weather_display.config(text="")
    weather_icon.config(image="")
    unit_var.set("Celsius")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.configure(bg="#e0e0e0")

tk.Label(root, text="Enter City Name:", bg="#e0e0e0", font=("Helvetica", 14)).pack(pady=10)
city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=10)

tk.Button(root, text="Get Weather", command=show_weather, font=("Helvetica", 14), bg="#4CAF50", fg="white").pack(pady=10)

weather_display = tk.Label(root, bg="#e0e0e0", font=("Helvetica", 14))
weather_display.pack(pady=10)

weather_icon = tk.Label(root, bg="#e0e0e0")
weather_icon.pack(pady=10)

unit_var = tk.StringVar(value="Celsius")
tk.Radiobutton(root, text="Celsius", variable=unit_var, value="Celsius", bg="#e0e0e0", font=("Helvetica", 14)).pack(pady=5)
tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value="Fahrenheit", bg="#e0e0e0", font=("Helvetica", 14)).pack(pady=5)

tk.Button(root, text="Reset", command=reset, font=("Helvetica", 14), bg="#f44336", fg="white").pack(pady=10)

root.mainloop()
