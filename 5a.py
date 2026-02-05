import tkinter as tk
from tkinter import messagebox

def generate_itinerary():
    time = time_entry.get()
    budget = budget_entry.get()
    interest = interest_var.get()

    messagebox.showinfo(
        "Suggested Itinerary",
        f"Total Time: {time} hrs\n"
        f"Budget: NPR {budget}\n"
        f"Interest: {interest}\n\n"
        "Suggested Tourist Spots:\n"
        "• Pashupatinath Temple\n"
        "• Swayambhunath Stupa\n"
        "• Garden of Dreams"
    )

root = tk.Tk()
root.title("Tourist Spot Optimizer")

tk.Label(root, text="Total Time Available (hrs):").grid(row=0, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=0, column=1)

tk.Label(root, text="Maximum Budget (NPR):").grid(row=1, column=0)
budget_entry = tk.Entry(root)
budget_entry.grid(row=1, column=1)

interest_var = tk.StringVar(value="Culture")
tk.Label(root, text="Interest Type:").grid(row=2, column=0)
tk.OptionMenu(
    root, interest_var, "Culture", "Nature", "Adventure"
).grid(row=2, column=1)

tk.Button(
    root, text="Generate Itinerary",
    command=generate_itinerary
).grid(row=3, column=1)

root.mainloop()
