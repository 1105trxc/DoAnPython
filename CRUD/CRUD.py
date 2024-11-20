import pandas as pd

file_path = 'dataDaLamSach.csv'

# Tải dữ liệu từ file CSV nếu có, nếu không sẽ tạo DataFrame trống với các cột phù hợp
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    data = pd.DataFrame(columns=[
        'Temperature (°C)', 'Humidity (%)', 'Wind Speed (mph)', 'Precipitation (%)',
        'Cloud Cover', 'Atmospheric Pressure (hPa)', 'UV Index', 'Season',
        'Visibility (km)', 'Location', 'Weather Type'
    ])

# Hàm thêm dữ liệu mới
def Create(data):
    try:
        temperature = float(input("Nhập vào Temperature (°C): "))
        humidity = float(input("Nhập vào Humidity (%): "))
        wind_speed = float(input("Nhập vào Wind Speed (mph): "))
        precipitation = float(input("Nhập vào Precipitation (%): "))
        cloud_cover = input("Nhập vào Cloud Cover (e.g., partly cloudy, clear, overcast): ")
        pressure = float(input("Nhập vào Atmospheric Pressure (hPa): "))
        uv_index = int(input("Nhập vào UV Index: "))
        season = input("Nhập vào Season (Winter, Spring, Summer, Autumn): ")
        visibility = float(input("Nhập vào Visibility (km): "))
        location = input("Nhập vào Location (inland, mountain, coastal): ")
        weather_type = input("Nhập vào Weather Type (Rainy, Sunny, Cloudy, Snowy): ")

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
        print("Thêm dữ liệu thành công!")
        return data

    except ValueError:
        print("Dữ liệu nhập vào không hợp lệ, vui lòng nhập lại.")
        return data

# Hàm xóa dữ liệu
def Delete(data):
    try:
        if data.empty:
            print("Không tồn tại dữ liệu để xóa.")
            return data

        # Người dùng nhập chỉ số dòng bắt đầu từ 1 (tức là dòng đầu tiên trong data)
        row_to_delete = int(input("Nhập vào số dòng muốn xóa (bắt đầu là 1): ")) - 1

        # Kiểm tra phạm vi hợp lệ
        if 0 <= row_to_delete < len(data):
            # Xóa dòng và reset lại chỉ mục
            data = data.drop(index=row_to_delete).reset_index(drop=True)
            print("Xóa thành công!")
        else:
            print("Giá trị cột nhập vào không hợp lệ. Hãy nhập lại.")

        return data

    except ValueError:
        print("Giá trị nhập vào không hợp lệ.")
        return data


# Hàm đọc dữ liệu
def Read(data, rows_per_page=10):
    # Kiểm tra dữ liệu đầu vào
    if data.empty:
        print("Không tồn tại dữ liệu.")
        return

    # Tổng số dòng và số trang
    total_rows = len(data)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page  # Tính số trang cần thiết

    def print_page(page):
        start_idx = (page - 1) * rows_per_page  # Chỉ số bắt đầu
        end_idx = min(start_idx + rows_per_page, total_rows)  # Chỉ số kết thúc
        page_data = data.iloc[start_idx:end_idx].copy()  # Lấy dữ liệu trang
        page_data.index = range(start_idx + 1, end_idx + 1)  # Đặt lại chỉ số dòng
        print(f"\nTrang {page}/{total_pages}:")
        print(page_data)

    current_page = 1  # Khởi tạo trang đầu tiên
    while True:
        # Hiển thị dữ liệu của trang hiện tại
        print_page(current_page)

        # Yêu cầu người dùng nhập hành động
        action = input(
            f"\nNhập 'n' để sang trang tiếp theo, 'p' về lại trang ở trước, 'q' để thoát (trang hiện tại: {current_page}): "
        ).strip().lower()

        # Xử lý hành động
        if action == 'n' and current_page < total_pages:  # Trang tiếp theo
            current_page += 1
        elif action == 'p' and current_page > 1:  # Trang trước
            current_page -= 1
        elif action == 'q':  # Thoát
            print("Thoát chế độ xem.")
            break
        else:  # Xử lý đầu vào không hợp lệ
            print("Không hợp lệ.")


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

