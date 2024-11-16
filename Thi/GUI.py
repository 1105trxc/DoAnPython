import tkinter as tk
from tkinter import messagebox, font
import pandas as pd

# Đọc dữ liệu từ file CSV ban đầu
file_path = 'E:\\DoAnPython\\weather_classification_data.csv'    
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    messagebox.showerror("Error", "File not found!")
    data = pd.DataFrame(columns=[
        'Temperature (°F)', 'Humidity (%)', 'Wind Speed (mph)', 'Precipitation (%)',
        'Cloud Cover', 'Atmospheric Pressure (hPa)', 'UV Index', 'Season',
        'Visibility (km)', 'Location', 'Weather Type'
    ])

# Hàm thêm dữ liệu mới vào DataFrame
def add_data():
    try:
        # Lấy dữ liệu từ các ô nhập
        temperature = float(entry_temperature.get())
        humidity = float(entry_humidity.get())
        wind_speed = float(entry_wind_speed.get())
        precipitation = float(entry_precipitation.get())
        cloud_cover = entry_cloud_cover.get()
        pressure = float(entry_pressure.get())
        uv_index = int(entry_uv_index.get())
        season = entry_season.get()
        visibility = float(entry_visibility.get())
        location = entry_location.get()
        weather_type = entry_weather_type.get()
        
        # Thêm vào DataFrame
        new_row = {
            'Temperature (°F)': temperature,
            'Humidity (%)': humidity,
            'Wind Speed (mph)': wind_speed,
            'Precipitation (%)': precipitation,
            'Cloud Cover': cloud_cover,
            'Atmospheric Pressure (hPa)': pressure,
            'UV Index': uv_index,
            'Season': season,
            'Visibility (km)': visibility,
            'Location': location,
            'Weather Type': weather_type
        }
        global data
        data = data.append(new_row, ignore_index=True)
        
        # Thông báo thành công
        messagebox.showinfo("Success", "Data added successfully!")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid data types.")

# Hàm lưu dữ liệu vào file CSV gốc
def save_data():
    data.to_csv(file_path, index=False)
    messagebox.showinfo("Success", f"Data saved to {file_path}")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Weather Data Generator")
window.geometry("500x600")
window.configure(bg="#f0f8ff")

title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=10)

# Tiêu đề
title_label = tk.Label(window, text="Weather Data Generator", font=title_font, bg="#f0f8ff", fg="#4a4a8b")
title_label.pack(pady=10)

# Frame chứa các trường nhập liệu
frame = tk.Frame(window, bg="#e6f2ff", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Các trường nhập liệu với nhãn
fields = [
    ("Temperature (°F)", "entry_temperature"),
    ("Humidity (%)", "entry_humidity"),
    ("Wind Speed (mph)", "entry_wind_speed"),
    ("Precipitation (%)", "entry_precipitation"),("Cloud Cover", "entry_cloud_cover"),
    ("Atmospheric Pressure (hPa)", "entry_pressure"),
    ("UV Index", "entry_uv_index"),
    ("Season", "entry_season"),
    ("Visibility (km)", "entry_visibility"),
    ("Location", "entry_location"),
    ("Weather Type", "entry_weather_type"),
]

entries = {}
for idx, (label_text, var_name) in enumerate(fields):
    label = tk.Label(frame, text=label_text, font=label_font, bg="#e6f2ff", fg="#4a4a8b")
    label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(frame, font=label_font, width=25, bd=2, relief="solid")
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries[var_name] = entry

# Gán tên các entry để dễ sử dụng
entry_temperature = entries["entry_temperature"]
entry_humidity = entries["entry_humidity"]
entry_wind_speed = entries["entry_wind_speed"]
entry_precipitation = entries["entry_precipitation"]
entry_cloud_cover = entries["entry_cloud_cover"]
entry_pressure = entries["entry_pressure"]
entry_uv_index = entries["entry_uv_index"]
entry_season = entries["entry_season"]
entry_visibility = entries["entry_visibility"]
entry_location = entries["entry_location"]
entry_weather_type = entries["entry_weather_type"]

# Nút thêm dữ liệu và lưu dữ liệu với màu sắc
btn_add = tk.Button(window, text="Add Data", command=add_data, bg="#4a90e2", fg="white", font=label_font, width=15)
btn_add.pack(pady=10)

btn_save = tk.Button(window, text="Save to CSV", command=save_data, bg="#4a90e2", fg="white", font=label_font, width=15)
btn_save.pack(pady=10)

# Chạy ứng dụng
window.mainloop()