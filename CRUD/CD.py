import pandas as pd
import os

# Đường dẫn đến file CSV
file_path = 'dataDaLamSach.csv'

# Tải dữ liệu từ file CSV nếu có, nếu không sẽ tạo DataFrame trống với các cột phù hợp
if os.path.exists(file_path):
    data = pd.read_csv(file_path, header=0)  # Đọc dữ liệu và lấy hàng đầu tiên làm tiêu đề
else:
    data = pd.DataFrame(columns=[  # Tạo DataFrame trống với tiêu đề tương ứng
        'Temperature (°C)', 'Humidity (%)', 'Wind Speed (mph)', 'Precipitation (%)',
        'Cloud Cover', 'Atmospheric Pressure (hPa)', 'UV Index', 'Season',
        'Visibility (km)', 'Location', 'Weather Type'
    ])

# Hàm thêm dữ liệu mới
def addData(data):
    try:
        temperature = float(input("Enter Temperature (°C): "))
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
            'Temperature (°C)': temperature,
            'Humidity (%)': humidity,
            'Wind Speed (mph)': wind_speed,
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

# Hàm xóa dữ liệu
def deleteData(data):
    try:
        if data.empty:
            print("No data available to delete.")
            return data

        # Người dùng nhập chỉ số dòng bắt đầu từ 1 (tức là dòng đầu tiên trong data)
        row_to_delete = int(input("Enter the row number to delete (starting from 1): ")) - 1

        # Kiểm tra phạm vi hợp lệ
        if 0 <= row_to_delete < len(data):
            # Xóa dòng và reset lại chỉ mục
            data = data.drop(index=row_to_delete).reset_index(drop=True)
            print("Row deleted successfully!")
        else:
            print("Invalid row number. Please enter a valid row starting from 1.")

        return data

    except ValueError:
        print("Invalid input! Please enter a valid row number.")
        return data

# Hàm lưu dữ liệu vào file CSV
def saveData(data):
    # Loại bỏ cột "Unnamed" nếu xuất hiện
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    # Ghi đè toàn bộ dữ liệu vào file CSV
    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

def showMenu():
    print("\nMenu:")
    print("1. Add data")
    print("2. Delete data")
    print("3. Save and exit")

# Menu chức năng
while True:
    showMenu()
    choice = input("Enter your choice: ")

    if choice == '1':
        data = addData(data)
    elif choice == '2':
        data = deleteData(data)
    elif choice == '3':
        saveData(data)
        break
    else:
        print("Invalid choice. Please select again.")
