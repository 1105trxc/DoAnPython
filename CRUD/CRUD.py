import pandas as pd
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


'''
# Hàm đọc dữ liệu
def Read(data, rows_per_page=10):
    """Phân trang và trả về một hàm để lấy dữ liệu cho từng trang."""
    if data.empty:
        return None, 0  # Trả về None và 0 trang nếu không có dữ liệu
    
    # Tổng số dòng và số trang
    total_rows = len(data)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page  # Tính số trang cần thiết

    # Hàm hiển thị dữ liệu trên một trang
    def display_page(page):
        start_idx = (page - 1) * rows_per_page  # Chỉ số bắt đầu
        end_idx = min(start_idx + rows_per_page, total_rows)  # Chỉ số kết thúc
        page_data = data.iloc[start_idx:end_idx]  # Lấy dữ liệu của trang hiện tại
        return page_data

    return display_page, total_pages
'''

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

# Hàm cập nhật dữ liệu
def Update(data):
    try:
        if data.empty:
            print("Không tồn tại dữ liệu.")
            return data

        # Lấy chỉ số hàng cần cập nhật
        index = int(input("Nhập hàng bạn muốn cập nhật dữ liệu: ")) - 1
        if index < 0 or index >= len(data):
            print("Giá trị không hợp lệ.")
            return data

        # Nhập giá trị mới
        print("Hãy nhập vào giá trị bạn muốn thay đổi:")
        for col in data.columns:
            new_value = input(f"{col} (giá trị hiện tại: {data.at[index, col]}): ") #hiển thị giá trị tại hàng và cột 
            if col == "Cloud Cover":
                    # Các giá trị hợp lệ cho Cloud Cover
                    valid_cloudy = ["Partly cloudy", "Clear", "Overcast"]
                    while new_value not in valid_cloudy:
                        print(f"Giá trị không hợp lệ ở {col}. Chúng phải nằm trong {valid_cloudy}. Hãy thử lại.")
                        new_value = input(f"{col} (giá trị hiện tại: {data.at[index, col]}): ")
            elif col == "Season":
                    # Các giá trị hợp lệ cho Season
                    valid_seasons = ["Winter", "Spring", "Autumn", "Summer"]
                    while new_value not in valid_seasons:
                        print(f"Giá trị không hợp lệ ở {col}. Chúng phải nằm trong  {valid_seasons}. Hãy thử lại.")
                        new_value = input(f"{col} (giá trị hiện tại: {data.at[index, col]}): ")
            elif col == "Location":
                    # Các giá trị hợp lệ cho Locatiom
                    valid_location = ["Inland", "Mountain", "Coastal"]
                    while new_value not in valid_location:
                        print(f"Giá trị không hợp lệ ở {col}. Chúng phải nằm trong {valid_location}.  Hãy thử lại.")
                        new_value = input(f"{col} (giá trị hiện tại: {data.at[index, col]}): ")
            elif col == "Weather Type":
                    # Các giá trị hợp lệ cho Weather
                    valid_weather = ["Rainy", "Cloudy", "Sunny", "Snowy"]
                    while new_value not in valid_weather:
                        print(f"Giá trị không hợp lệ ở {col}. Chúng phải nằm trong {valid_weather}. Hãy thử lại.")
                        new_value = input(f"{col} (giá trị hiện tại: {data.at[index, col]}): ")
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
                            if col == 'Temperature (°C)': pass
                            else:
                                while new_value < 0:
                                    new_value = float(input(f"Giá trị không hợp lệ tại {col}. Phải là một số lớn hơn hoặc bằng 0. Hãy thử lại:"))
                            break  # Thoát khỏi vòng lặp nếu chuyển đổi thành công
                        except ValueError:
                            print(f"Giá trị của {col} Không hợp lệ. Hãy điền vào một số.")
                            new_value = input(f"Nhập vào giá trị mới cho {col} (giá trị hiện tại: {data.at[index, col]}): ")
                data.at[index, col] = new_value  # Cập nhật giá trị sau khi chuyển đổi thành công
        print(f"Hàng {index} đã được cập nhật thành công!")
        return data

    except ValueError:
        print("Không hợp lệ, vui lòng nhập lại giá trị hợp lệ.")
        return data

# Lưu dữ liệu vào file CSV
def saveData(data):
    data.to_csv(file_path, index=False)
    print(f"Dữ liệu đã được lưu vào {file_path}")

