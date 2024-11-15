import pandas as pd
file_name=r"C:\DAPython\weather_classification_data.csv"
def sap_xep_Temperature(file_name, column_name, ascending=True, output_file=r"C:\DAPython\sorted_output_Temperature.csv"):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_name)
    
    # Kiểm tra xem cột có tồn tại không
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return

    # Sắp xếp dữ liệu theo cột
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    
    # Ghi kết quả ra file CSV mới
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sap_xep_Humidity(file_name, column_name, ascending=True, output_file=r"C:\DAPython\sorted_output_Humidity.csv"):
    df = pd.read_csv(file_name)
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sap_xep_WindSpeed(file_name, column_name, ascending=True, output_file=r"C:\DAPython\sorted_output_WindSpeed.csv"):
    df = pd.read_csv(file_name)
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sap_xep_Precipitation(file_name, column_name, ascending=True, output_file=r"C:\DAPython\sorted_output_Precipitation.csv"):
    df = pd.read_csv(file_name)
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sap_xep_AtmosphericPressure(file_name, column_name, ascending=True, output_file=r"C:\DAPython\sorted_output_AtmosphericPressure.csv"):
    df = pd.read_csv(file_name)
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sap_xep_UVIndex(file_name, column_name, ascending=True, output_file=r"C:\DAPython\sorted_output_UVIndex.csv"):
    df = pd.read_csv(file_name)
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sap_xep_Visibility(file_name, column_name, ascending=True, output_file=r"C:\DAPython\sorted_output_Visibility.csv"):
    df = pd.read_csv(file_name)
    if column_name not in df.columns:
        print(f"Lỗi: Cột '{column_name}' không tồn tại. Các cột hiện có: {list(df.columns)}")
        return
    df_sorted = df.sort_values(by=column_name, ascending=ascending)
    df_sorted.to_csv(output_file, index=False)
    print(f"Đã sắp xếp dữ liệu theo cột '{column_name}' và lưu vào file '{output_file}'.")

def sapxep():
    print("1. Temperature")
    print("2. Humidity")
    print("3. Wind Speed")
    print("4. Precipitation")
    print("5. Atmospheric Pressure")
    print("6. UV Index")
    print("7. Visibility")
    n=int(input("Nhap loai muon sap xep: "))
    while(n<1 or n>7):
        n=int(input("Khong hop le. Hay nhap lai: "))
    if n==1:
        sap_xep_Temperature(file_name, 'Temperature', ascending=True)
    elif n==2:
        sap_xep_Humidity(file_name, 'Humidity', ascending=True)
    elif n==3: 
        sap_xep_WindSpeed(file_name,'Wind Speed', ascending=True)
    elif n==4: 
        sap_xep_Precipitation(file_name, 'Precipitation (%)', ascending=True)
    elif n==5: 
        sap_xep_AtmosphericPressure(file_name, 'Atmospheric Pressure', ascending=True)
    elif n==6: 
        sap_xep_UVIndex(file_name, 'UV Index', ascending=True)
    elif n==7:
        sap_xep_Visibility(file_name, 'Visibility (km)', ascending=True)
sapxep()