import pandas as pd
import os

# Đường dẫn đến file CSV
file_path = 'E:\\DoAnPython\\weather_classification_data.csv'

# Tải dữ liệu từ file CSV nếu có, nếu không sẽ tạo DataFrame trống với các cột phù hợp
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    data = pd.DataFrame(columns=[
        'Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
        'Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season',
        'Visibility (km)', 'Location', 'Weather Type'
    ])

# Hàm thêm dữ liệu mới
def add_data(data):
    try:
        temperature = float(input("Enter Temperature (°F): "))
        humidity = float(input("Enter Humidity (%): "))
        wind_speed = float(input("Enter Wind Speed (mph): "))
        precipitation = float(input("Enter Precipitation (%): "))
        cloud_cover = input("Enter Cloud Cover (e.g., partly cloudy, clear, overcast): ")
        pressure = float(input("Enter Atmospheric Pressure (hPa): "))
        uv_index = int(input("Enter UV Index: "))
        season = input("Enter Season (Winter, Spring, Summer, Autumn): ")
        visibility = float(input("Enter Visibility (km): "))
        location = input("Enter Location (inland, mountain, coastal): ")
        weather_type = input("Enter Weather Type (Rainy, Sunny, Cloudy, Snowy): ")

        # Tạo hàng mới dưới dạng DataFrame để đảm bảo cấu trúc khớp với DataFrame gốc
        new_row = pd.DataFrame([{
            'Temperature': temperature,
            'Humidity': humidity,
            'Wind Speed': wind_speed,
            'Precipitation (%)': precipitation,
            'Cloud Cover': cloud_cover,
            'Atmospheric Pressure': pressure,
            'UV Index': uv_index,
            'Season': season,
            'Visibility (km)': visibility,
            'Location': location,
            'Weather Type': weather_type
        }])

        # Thêm hàng mới vào đầu DataFrame
        data = pd.concat([new_row, data], ignore_index=True)
        print("Data added successfully!")
        return data

    except ValueError:
        print("Invalid input! Please enter the correct data types.")
        return data

# Hàm lưu dữ liệu vào file CSV
def save_data(data):
    # Ghi đè toàn bộ dữ liệu vào file CSV
    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

# Gọi hàm thêm dữ liệu và lưu dữ liệu
data = add_data(data)
save_data(data)
