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
        try:
            temperature = float(data_input["Temperature (°C)"])  # Kiểm tra nếu là số
        except ValueError:
            raise ValueError("Nhiệt độ phải là một số hợp lệ!")  # Nếu không phải số, báo lỗi

        try:
            humidity = float(data_input["Humidity (%)"])
        except ValueError:
            raise ValueError("Độ ẩm phải là một số hợp lệ!")  # Nếu không phải số, báo lỗi

        try:
            wind_speed = float(data_input["Wind Speed (mph)"])
        except ValueError:
            raise ValueError("Tốc độ gió phải là một số hợp lệ!")  # Nếu không phải số, báo lỗi

        try:
            precipitation = float(data_input["Precipitation (%)"])
        except ValueError:
            raise ValueError("Lượng mưa phải là một số hợp lệ!")  # Nếu không phải số, báo lỗi

        cloud_cover = data_input["Cloud Cover"]
        if not cloud_cover:  # Kiểm tra nếu Cloud Cover trống
            raise ValueError("Mây không được để trống!")

        try:
            pressure = float(data_input["Atmospheric Pressure (hPa)"])
        except ValueError:
            raise ValueError("Áp suất không khí phải là một số hợp lệ!")  # Nếu không phải số, báo lỗi

        try:
            uv_index = int(data_input["UV Index"])
        except ValueError:
            raise ValueError("Chỉ số UV phải là một số nguyên hợp lệ!")  # Nếu không phải số nguyên, báo lỗi

        season = data_input["Season"]
        if not season:  # Kiểm tra nếu Season trống
            raise ValueError("Mùa không được để trống!")

        try:
            visibility = float(data_input["Visibility (km)"])
        except ValueError:
            raise ValueError("Tầm nhìn phải là một số hợp lệ!")  # Nếu không phải số, báo lỗi

        location = data_input["Location"]
        if not location:  # Kiểm tra nếu Location trống
            raise ValueError("Vị trí không được để trống!")

        weather_type = data_input["Weather Type"]
        if not weather_type:  # Kiểm tra nếu Weather Type trống
            raise ValueError("Loại thời tiết không được để trống!")

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
        error_label.config(text="")  # Đảm bảo rằng text được xóa đi khi không có lỗi
        return updated_data  # Trả về DataFrame đã cập nhật

    except ValueError as e:
        # Hiển thị thông báo lỗi trực tiếp trên GUI nếu có lỗi chuyển đổi dữ liệu
        error_message = f"Dữ liệu nhập vào không hợp lệ: {e}"  # Lấy thông báo lỗi chi tiết
        error_label.config(text=error_message, foreground="red")  # Hiển thị lỗi với màu đỏ
        return None  # Trả về None để thông báo lỗi đã xảy ra

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

