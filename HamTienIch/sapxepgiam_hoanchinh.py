import pandas as pd
file_name=r"C:\DAPython\dataDaLamSach.csv"
output_file=r"C:\DAPython\sorted_output.csv"
def sap_xep(file_name, column_name, ascending=False, output=output_file):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_name)
    
    '''# Kiểm tra xem cột có tồn tại không
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return'''

    # Sắp xếp dữ liệu theo cột
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    
    # Ghi kết quả ra file CSV mới
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu tăng theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sapxep():
    print("1. Temperature (°C)")
    print("2. Humidity (%)")
    print("3. Wind Speed (mph)")
    print("4. Precipitation (%)")
    print("5. Atmospheric Pressure (hPa)")
    print("6. UV Index")
    print("7. Visibility (km)")
    n=int(input("Nhập loại muốn sắp xếp giảm dần: "))
    while(n<1 or n>7):
        n=int(input("Không hợp lệ. Hãy nhập lại: "))
    if n==1:
        sap_xep(file_name,'Temperature (°C)', ascending=False, output=output_file)
    elif n==2:
        sap_xep(file_name,'Humidity (%)', ascending=False, output=output_file)
    elif n==3: 
        sap_xep(file_name,'Wind Speed (mph)', ascending=False, output=output_file)
    elif n==4: 
        sap_xep(file_name,'Precipitation (%)', ascending=False, output=output_file)
    elif n==5: 
        sap_xep(file_name,'Atmospheric Pressure (hPa)', ascending=False, output=output_file)
    elif n==6: 
        sap_xep(file_name,'UV Index', ascending=False, output=output_file)
    elif n==7:
        sap_xep(file_name,'Visibility (km)', ascending=False, output=output_file)
sapxep()