import tkinter as tk
from datetime import datetime

def calculate_age():
        
        birth_year = int(entry.get())
        current_year = datetime.now().year
        age = current_year - birth_year
        days = age * 365
        result_lbl.config(text=f"Your Age is: {age} years\nApprox Days: {days} days")
    

app = tk.Tk()
app.geometry("900x500")
app.title("Age Calculator")
app.config(bg="#2596be")

lbl = tk.Label(app, text="Enter your Birth Year:", font=("Arial", 16), bg="#2596be", fg="white")
lbl.pack(pady=10)

entry = tk.Entry(app, font=("Arial", 16), justify="center")
entry.pack(pady=10)

btn = tk.Button(app, text="Calculate Age", font=("Arial", 16, "bold"), command=calculate_age)
btn.pack(pady=10)

result_lbl = tk.Label(app, text="", font=("Arial", 16), bg="#2596be", fg="white")
result_lbl.pack(pady=10)

app.mainloop()