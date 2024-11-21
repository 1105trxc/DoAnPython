import pandas as pd
file_name = r"dataDaLamSach.csv"  # File nguồn
output_file = r"outPut.csv"  # File kết quả
def sapXep(file_name, column_name, ascending=True, output_file=None):
      # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_name)

    # Sắp xếp dữ liệu theo cột
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    
    # Nếu không có output_file, sử dụng giá trị mặc định
    if output_file is None:
        output_file = r"outPut.csv"

    # Ghi kết quả ra file CSV mới
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu {'tăng' if ascending else 'giảm'} theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sapXepTang():
    print("1. Temperature (°C)")
    print("2. Humidity (%)")
    print("3. Wind Speed (mph)")
    print("4. Precipitation (%)")
    print("5. Atmospheric Pressure (hPa)")
    print("6. UV Index")
    print("7. Visibility (km)")

    n = int(input("Nhập loại muốn sắp xếp giảm dần: "))
    
    while n < 1 or n > 7:
        n = int(input("Không hợp lệ. Hãy nhập lại: "))
    
    # Truyền đúng tham số vào hàm sapXep
    if n == 1:
        sapXep(file_name, 'Temperature (°C)', ascending=True, output_file=output_file)
    elif n == 2:
        sapXep(file_name, 'Humidity (%)', ascending=True, output_file=output_file)
    elif n == 3: 
        sapXep(file_name, 'Wind Speed (mph)', ascending=True, output_file=output_file)
    elif n == 4: 
        sapXep(file_name, 'Precipitation (%)', ascending=True, output_file=output_file)
    elif n == 5: 
        sapXep(file_name, 'Atmospheric Pressure (hPa)', ascending=True, output_file=output_file)
    elif n == 6: 
        sapXep(file_name, 'UV Index', ascending=True, output_file=output_file)
    elif n == 7:
        sapXep(file_name, 'Visibility (km)', ascending=True, output_file=output_file)
