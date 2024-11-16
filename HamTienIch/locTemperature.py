import pandas as pd

file_name = r"C:\DAPython\weather_classification_data.csv"

def loc_du_lieu_theo_khoang_co_dinh(file_name, column_name, output_file):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_name)
    
    # Kiểm tra xem cột cố định có tồn tại không
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return
    
    try:
        # Nhập khoảng giá trị từ người dùng
        min_value = float(input(f"Nhập giá trị nhỏ nhất cho cột '{column_name}': "))
        max_value = float(input(f"Nhập giá trị lớn nhất cho cột '{column_name}': "))
        
        # Lọc dữ liệu trong khoảng [min_value, max_value]
        filtered_data = df[(df[column_name] >= min_value) & (df[column_name] <= max_value)]
        
        # Kiểm tra nếu không có dữ liệu nào thỏa mãn điều kiện
        if filtered_data.empty:
            print("Không có dữ liệu nào nằm trong khoảng giá trị đã nhập.")
            return
        
        # Lưu kết quả đã lọc vào file CSV mới
        filtered_data.to_csv(output_file, index=False)
        print(f"Dữ liệu đã được lọc và lưu vào file {output_file}")
    except ValueError:
        print("Lỗi: Giá trị nhập vào phải là số.")

# Gọi hàm với cột cố định là 'Temperature'
column_name = 'Temperature'
output_file = r"C:\DAPython\filtered_output_loc_temperature.csv"
loc_du_lieu_theo_khoang_co_dinh(file_name, column_name, output_file)
