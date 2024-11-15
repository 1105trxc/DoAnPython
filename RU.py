import pandas as pd

file_path = 'D:\\PY_prj\DoAnPython\weather_classification_data.csv'

# Tải dữ liệu từ file CSV nếu có, nếu không sẽ tạo DataFrame trống với các cột phù hợp
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    data = pd.DataFrame(columns=[
        'Temperature (°F)', 'Humidity (%)', 'Wind Speed (mph)', 'Precipitation (%)',
        'Cloud Cover', 'Atmospheric Pressure (hPa)', 'UV Index', 'Season',
        'Visibility (km)', 'Location', 'Weather Type'
    ])


# Hàm đọc dữ liệu
def read_data(data):
    if data.empty:
        print("No data available.")
    else:
        print("\nWeather Data:")
        print(data)


# Hàm cập nhật dữ liệu
def update_data(data):
    try:
        if data.empty:
            print("No data to update.")
            return data

        # Lấy chỉ số hàng cần cập nhật
        index = int(input("Enter the index of the row to update: "))
        if index < 0 or index >= len(data):
            print("Invalid index.")
            return data

        # Nhập giá trị mới
        print("Enter new values (leave blank to keep current value):")
        for col in data.columns:
            new_value = input(f"{col} (current: {data.at[index, col]}): ") #hiển thị giá trị tại hàng và cột 
            if col == "Cloud Cover":
                    # Các giá trị hợp lệ cho Cloud Cover
                    valid_cloudy = ["partly cloudy", "clear", "overcast"]
                    while new_value not in valid_cloudy:
                        print(f"Invalid value for {col}. Must be one of {valid_cloudy}. Please enter again.")
                        new_value = input(f"{col} (current: {data.at[index, col]}): ")
            elif col == "Season":
                    # Các giá trị hợp lệ cho Season
                    valid_seasons = ["Winter", "Spring", "Autumn", "Summer"]
                    while new_value not in valid_seasons:
                        print(f"Invalid value for {col}. Must be one of {valid_seasons}. Please enter again.")
                        new_value = input(f"{col} (current: {data.at[index, col]}): ")
            elif col == "Location":
                    # Các giá trị hợp lệ cho Locatiom
                    valid_location = ["inland", "mountain", "coastal"]
                    while new_value not in valid_location:
                        print(f"Invalid value for {col}. Must be one of {valid_location}. Please enter again.")
                        new_value = input(f"{col} (current: {data.at[index, col]}): ")
            elif col == "Weather Type":
                    # Các giá trị hợp lệ cho Weather
                    valid_weather = ["Rainy", "Cloudy", "Sunny", "Snowy"]
                    while new_value not in valid_weather:
                        print(f"Invalid value for {col}. Must be one of {valid_weather}. Please enter again.")
                        new_value = input(f"{col} (current: {data.at[index, col]}): ")
            elif new_value.strip():
                # Kiểm tra kiểu dữ liệu của cột và chuyển đổi nếu cần
                if pd.api.types.is_numeric_dtype(data[col]):  # Kiểm tra xem có phải là số hay không
                    while True:  # Lặp lại cho đến khi nhập giá trị hợp lệ
                        try:
                            # Chuyển đổi giá trị nhập vào thành số, phù hợp với kiểu dữ liệu của cột
                            if '.' in new_value:
                                new_value = float(new_value)
                            else:
                                new_value = int(new_value)
                            break  # Thoát khỏi vòng lặp nếu chuyển đổi thành công
                        except ValueError:
                            print(f"The value entered for {col} is invalid. Please enter a valid number.")
                            new_value = input(f"Enter a new value for {col} (current: {data.at[index, col]}): ")
                data.at[index, col] = new_value  # Cập nhật giá trị sau khi chuyển đổi thành công
        print(f"Row {index} updated successfully!")
        return data

    except ValueError:
        print("Invalid input! Please enter the correct data types.")
        return data

# Lưu dữ liệu vào file CSV
def save_data(data):
    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

#  Đọc dữ liệu
read_data(data)

# Gọi hàm cập nhật dữ liệu
update_data(data)

# Lưu dữ liệu sau khi cập nhật
save_data(data)
