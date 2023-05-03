import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import date, timedelta
import csv
import os

def validate_birth_year(input_str):
    if not input_str:
        return True
    if input_str.isdigit():
        return True
    return False

def validate_period_interval(input_str):
    if not input_str:
        return False
    if input_str.isdigit():
        return True
    return False

def validate_date(year_str, month_str, day_str):
    if not (year_str and month_str and day_str):
        return False
    if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
        return False

    year, month, day = int(year_str), int(month_str), int(day_str)
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def generate_csv():
    birth_year_str = birth_year_entry.get()
    period_start_year_str = period_start_year_entry.get()
    period_start_month_str = period_start_month_entry.get()
    period_start_day_str = period_start_day_entry.get()
    period_interval_str = period_interval_entry.get()

    if not validate_birth_year(birth_year_str):
        messagebox.showerror("Error", "Invalid birth year. Please enter a valid number.")
        return

    if not validate_date(period_start_year_str, period_start_month_str, period_start_day_str):
        messagebox.showerror("Error", "Invalid period start date. Please enter a valid date.")
        return

    if not validate_period_interval(period_interval_str):
        messagebox.showerror("Error", "Invalid period interval. Please enter a valid number.")
        return

    birth_year = int(birth_year_str) if birth_year_str else None
    period_start_date = date(int(period_start_year_str), int(period_start_month_str), int(period_start_day_str))
    period_interval = int(period_interval_str)

    future_period_dates = []
    next_period_date = period_start_date

    if birth_year:
        end_date = date(birth_year + 55, period_start_date.month, period_start_date.day)
    else:
        end_date = date(period_start_date.year + 40, period_start_date.month, period_start_date.day)

    while next_period_date <= end_date:
        future_period_dates.append(next_period_date)
        next_period_date += timedelta(days=period_interval)

    csv_file = 'period_dates.csv'
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Year', 'Month', 'Date'])
        for period_date in future_period_dates:
            csvwriter.writerow([period_date.year, period_date.month, period_date.day])

    messagebox.showinfo("Success", f"Future period dates have been saved in {os.path.abspath(csv_file)}")

root = tk.Tk()
root.title("Girlfriend/Wife Period Calculator")

birth_year_label = tk.Label(root, text="Enter your girlfriend's/wife's birth year (optional):")
birth_year_entry = tk.Entry(root)
birth_year_entry.config(validate='key', validatecommand=(root.register(validate_birth_year), '%P'))

period_start_label = tk.Label(root, text="Enter the most current starting period date (YYYY, MM, DD)")
period_start_year_entry = tk.Entry(root, width=5)
period_start_month_entry = tk.Entry(root, width=3)
period_start_day_entry = tk.Entry(root, width=3)

period_interval_label = tk.Label(root, text="Enter the interval between each period (normally between 21 to 35 days, average 28 days):")
period_interval_entry = tk.Entry(root)
period_interval_entry.config(validate='key', validatecommand=(root.register(validate_period_interval), '%P'))

generate_button = tk.Button(root, text="Generate CSV", command=generate_csv)

birth_year_label.grid(row=0, column=0, sticky=tk.W)
birth_year_entry.grid(row=1, column=0, sticky=tk.W)

period_start_label.grid(row=2, column=0, sticky=tk.W)
period_start_year_entry.grid(row=3, column=0, sticky=tk.W)
period_start_month_entry.grid(row=3, column=1, sticky=tk.W)
period_start_day_entry.grid(row=3, column=2, sticky=tk.W)

period_interval_label.grid(row=4, column=0, sticky=tk.W)
period_interval_entry.grid(row=5, column=0, sticky=tk.W)

generate_button.grid(row=6, column=0, sticky=tk.W)

root.mainloop()