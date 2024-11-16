import pandas as pd

file_path = 'E:\\DoAnPython\\weather_classification_data.csv'  

output_file = 'E:\\DoAnPython\\filtered_precipitation.csv'

try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print("File không tồn tại. Hãy kiểm tra lại đường dẫn.")
    exit()

try:
    min_precipitation = float(input("Nhập giá trị tối thiểu của Precipitation (%): "))
    max_precipitation = float(input("Nhập giá trị tối đa của Precipitation (%): "))
except ValueError:
    print("Vui lòng nhập số hợp lệ.")
    exit()

# Lọc dữ liệu theo khoảng giá trị
filtered_data = data[(data['Precipitation (%)'] >= min_precipitation) & 
                     (data['Precipitation (%)'] <= max_precipitation)]

# Kiểm tra nếu không có dữ liệu nào thỏa mãn
if filtered_data.empty:
    print("Không có dữ liệu nào trong khoảng đã chỉ định.")
else:
    # Xuất dữ liệu đã lọc ra file CSV
    filtered_data.to_csv(output_file, index=False)
    print(f"Dữ liệu đã lọc được lưu vào file: {output_file}")
