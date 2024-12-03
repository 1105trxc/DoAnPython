import pandas as pd
from tkinter import messagebox
file_path = r"dataDaLamSach.csv"
# Tải dữ liệu từ file CSV nếu có, nếu không sẽ tạo DataFrame trống với các cột phù hợp
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    data = pd.DataFrame(columns=[
        'Temperature (°C)', 'Humidity (%)', 'Wind Speed (mph)', 'Precipitation (%)',
        'Cloud Cover', 'Atmospheric Pressure (hPa)', 'UV Index', 'Season',
        'Visibility (km)', 'Location', 'Weather Type'
    ])
    
# Hàm thêm dữ liệu
def Create(data, data_input, error_label):
    try:
        # Kiểm tra và chuyển đổi các giá trị từ input
        def validate_field(key, value):
            """Hàm kiểm tra giá trị theo từng trường."""
            if key == "Temperature (°C)" and not (-25 <= value <= 71):
                raise ValueError("Nhiệt độ phải nằm trong khoảng -25 đến 71°C.")
            if key == "Humidity (%)" and not (0 <= value <= 110):
                raise ValueError("Độ ẩm phải nằm trong khoảng 0% đến 110%.")
            if key == "Wind Speed (km/h)" and not (0 <= value <= 40):
                raise ValueError("Tốc độ gió phải nằm trong khoảng 0 đến 40 km/h.")
            if key == "Precipitation (%)" and not (0 <= value <= 110):
                raise ValueError("Lượng mưa phải nằm trong khoảng 0% đến 110%.")
            if key == "Atmospheric Pressure (hPa)" and not (900 <= value <= 1100):
                raise ValueError("Áp suất khí quyển phải nằm trong khoảng 900 đến 1110 hPa.")
            if key == "UV Index" and not (0 <= value <= 13):
                raise ValueError("Chỉ số UV phải nằm trong khoảng 0 đến 13.")
            if key == "Visibility (km)" and not (0 <= value <= 20):
                raise ValueError("Tầm nhìn phải nằm trong khoảng 0 đến 20 km.")
            return value

        # Lấy và kiểm tra từng trường số
        temperature = validate_field("Temperature (°C)", float(data_input["Temperature (°C)"]))
        humidity = validate_field("Humidity (%)", float(data_input["Humidity (%)"]))
        wind_speed = validate_field("Wind Speed (mph)", float(data_input["Wind Speed (mph)"]))
        precipitation = validate_field("Precipitation (%)", float(data_input["Precipitation (%)"]))
        pressure = validate_field("Atmospheric Pressure (hPa)", float(data_input["Atmospheric Pressure (hPa)"]))
        uv_index = validate_field("UV Index", int(data_input["UV Index"]))
        visibility = validate_field("Visibility (km)", float(data_input["Visibility (km)"]))

        # Kiểm tra các trường dạng chuỗi
        cloud_cover = data_input["Cloud Cover"].strip()
        if not cloud_cover:
            raise ValueError("Mây không được để trống!")
        cloud_cover = cloud_cover.capitalize()

        season = data_input["Season"].strip()
        if not season:
            raise ValueError("Mùa không được để trống!")
        season = season.capitalize()

        location = data_input["Location"].strip()
        if not location:
            raise ValueError("Vị trí không được để trống!")
        location = location.capitalize()

        weather_type = data_input["Weather Type"].strip()
        if not weather_type:
            raise ValueError("Loại thời tiết không được để trống!")
        weather_type = weather_type.capitalize()

        # Tạo hàng mới dưới dạng DataFrame
        new_row = pd.DataFrame([{
            'Temperature (°C)': temperature,
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
        }], columns=data.columns)

        # Thêm hàng mới vào DataFrame gốc
        updated_data = pd.concat([new_row, data], ignore_index=True)

        # Xóa thông báo lỗi trước đó (nếu có)
        error_label.config(text="")
        return updated_data  # Trả về DataFrame đã cập nhật

    except ValueError as e:
        # Hiển thị thông báo lỗi trực tiếp trên GUI nếu có lỗi
        error_message = f"Dữ liệu nhập vào không hợp lệ: {e}"
        error_label.config(text=error_message, foreground="red")
        return None  # Trả về None để thông báo lỗi


# Hàm xóa dữ liệu
def Delete(data, selected_row):
    """Xóa dòng dữ liệu tại chỉ số selected_row."""
    try:
        # Kiểm tra nếu DataFrame không trống
        if data.empty:
            print("Không tồn tại dữ liệu để xóa.")
            return data

        # Kiểm tra phạm vi chỉ số hợp lệ
        if 0 <= selected_row < len(data):
            # Xóa dòng và reset lại chỉ mục
            data = data.drop(index=selected_row).reset_index(drop=True)
            print("Xóa thành công!")
        else:
            print("Chỉ số dòng không hợp lệ.")
        
        return data
    
    except Exception as e:
        print(f"Lỗi xảy ra khi xóa: {str(e)}")
        return data

def Read(data, page=1, page_size=10):
    
    try:
        # Xác định tổng số trang
        total_rows = len(data)
        total_pages = (total_rows + page_size - 1) // page_size
        
        # Xác định chỉ số bắt đầu và kết thúc của trang hiện tại
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size

        # Lấy dữ liệu của trang hiện tại
        page_data = data.iloc[start_idx:end_idx]

        return page_data, total_pages
    except Exception as e:
        raise ValueError(f"Error reading the file: {e}")


def Update(data, index, data_input, error_label):
    try:
        if data.empty:
            raise ValueError("Không có dữ liệu để cập nhật.")
        
        # Kiểm tra xem chỉ số có hợp lệ không
        if index < 0 or index >= len(data):
            raise ValueError("Chỉ số hàng không hợp lệ.")
        
        # Lặp qua các cột và cập nhật giá trị
        for col in data.columns:
            new_value = data_input.get(col)  # Lấy giá trị từ GUI (ví dụ: Entry hoặc combobox)
            if new_value:
                # Kiểm tra các giá trị hợp lệ cho các cột đặc biệt
                if col == "Cloud Cover":
                    valid_cloudy = ["Partly cloudy", "Clear", "Overcast"]
                    if new_value not in valid_cloudy:
                        raise ValueError(f"Giá trị không hợp lệ cho {col}. Phải là trong {valid_cloudy}.")

                elif col == "Season":
                    valid_seasons = ["Winter", "Spring", "Autumn", "Summer"]
                    if new_value not in valid_seasons:
                        raise ValueError(f"Giá trị không hợp lệ cho {col}. Phải là trong {valid_seasons}.")

                elif col == "Location":
                    valid_location = ["Inland", "Mountain", "Coastal"]
                    if new_value not in valid_location:
                        raise ValueError(f"Giá trị không hợp lệ cho {col}. Phải là trong {valid_location}.")

                elif col == "Weather Type":
                    valid_weather = ["Rainy", "Cloudy", "Sunny", "Snowy"]
                    if new_value not in valid_weather:
                        raise ValueError(f"Giá trị không hợp lệ cho {col}. Phải là trong {valid_weather}.")
                elif col in [
                    "Temperature (°C)",
                    "Humidity (%)",
                    "Wind Speed (mph)",
                    "Precipitation (%)",
                    "Atmospheric Pressure (hPa)",
                    "UV Index",
                    "Visibility (km)",
                ]:
                    try:
                        new_value = float(new_value) if '.' in new_value else int(new_value)

                        # Kiểm tra giá trị âm (trừ những cột cho phép âm như nhiệt độ)
                        if col != "Temperature (°C)" and new_value < 0:
                            raise ValueError(f"Giá trị không hợp lệ tại {col}. Phải là một số lớn hơn hoặc bằng 0.")
                        # Kiểm tra khoảng giá trị tùy thuộc vào cột
                        if col == "Humidity (%)" and not (0 <= new_value <= 100):
                            raise ValueError(f"{col} phải nằm trong khoảng từ 0 đến 100.")
                        elif col == "UV Index" and not (0 <= new_value <= 11):
                            raise ValueError(f"{col} phải nằm trong khoảng từ 0 đến 11.")
                        elif col == "Visibility (km)" and new_value < 0:
                            raise ValueError(f"{col} phải lớn hơn hoặc bằng 0.")

                    except ValueError:
                        raise ValueError(f"Giá trị của {col} không hợp lệ. Hãy nhập lại một số.")

                # Cập nhật giá trị mới vào DataFrame
                data.at[index, col] = new_value
        
        # Hiển thị thông báo thành công
        messagebox.showinfo("Cập nhật thành công", f"Hàng {index+1} đã được cập nhật thành công!")
        error_label.config(text="")  # Xóa thông báo lỗi trước đó
        return data

    except ValueError as e:
        # Hiển thị lỗi lên màn hình
        error_label.config(text=f"Dữ liệu nhập vào không hợp lệ: {e}", foreground="red")
        return data

# # Lưu dữ liệu vào file CSV
def saveData(data):
    data.to_csv(file_path, index=False)
    print(f"Dữ liệu đã được lưu vào {file_path}")

