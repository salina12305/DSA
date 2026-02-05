import tkinter as tk
import threading
import time

def fetch_weather(city, label):
    time.sleep(1)  # Simulated API delay
    label.config(text=f"{city}: 25°C, Humidity 65%")

def start_fetch():
    for city, label in labels.items():
        threading.Thread(
            target=fetch_weather,
            args=(city, label)
        ).start()

root = tk.Tk()
root.title("Multithreaded Weather Data Collector")

cities = ["Kathmandu", "Pokhara", "Biratnagar", "Nepalgunj", "Dhangadhi"]
labels = {}

for i, city in enumerate(cities):
    lbl = tk.Label(root, text=f"{city}: Waiting...")
    lbl.grid(row=i, column=0)
    labels[city] = lbl

tk.Button(
    root,
    text="Fetch Weather",
    command=start_fetch
).grid(row=6, column=0)

root.mainloop()
