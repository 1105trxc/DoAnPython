import pandas as pd  

def locDuLieuTheoKhoangCoDinh(file_name, column, output_file):  
    try:  
        # Đọc file CSV nguồn (file gốc)
        df = pd.read_csv(file_name)  
        
        # Nhập khoảng lọc từ người dùng  
        min_val = float(input(f"Nhập giá trị tối thiểu cho {column}: "))  
        max_val = float(input(f"Nhập giá trị tối đa cho {column}: "))  
        
        # Lọc dữ liệu  
        df_filtered = df[(df[column] >= min_val) & (df[column] <= max_val)]  
        
        # Lưu file kết quả  
        df_filtered.to_csv(output_file, index=False)  
        
        print(f"Đã lọc và lưu dữ liệu vào {output_file}")  
        return df_filtered  
    except Exception as e:  
        print(f"Lỗi trong quá trình lọc dữ liệu: {e}")  
        return None  

def locDuLieuCsv(file_name, filter_condition, output_file):  
    try:  
        # Đọc file CSV nguồn (file gốc)
        df = pd.read_csv(file_name)  
        
        # Lọc dữ liệu theo điều kiện  
        df_filtered = df[filter_condition(df)]  
        
        # Lưu file kết quả  
        df_filtered.to_csv(output_file, index=False)  
        
        print(f"Đã lọc và lưu {len(df_filtered)} dòng dữ liệu vào {output_file}")  
        return df_filtered  
    except Exception as e:  
        print(f"Lỗi trong quá trình lọc dữ liệu: {e}")  
        return None  
def xuatLocDuLieu():
    file_name = r"dataDaLamSach.csv"  # File nguồn
    output_file = r"outPut.csv"  # File kết quả
    
    print('1. Temperature (°C)')
    print('2. Humidity (%)')
    print('3. Wind Speed (mph)')
    print('4. Precipitation (%)')
    print('5. Cloud Cover')
    print('6. Atmospheric Pressure (hPa)')
    print('7. UV Index')
    print('8. Season')
    print('9. Visibility (km)')
    print('10. Location')
    print('11. Weather Type')
    
    n = int(input("Nhập loại dữ liệu muốn lọc: "))
    
    while n < 1 or n > 11:
        n = int(input('Không hợp lệ. Hãy nhập lại: '))
    
    if n == 1:
        locDuLieuTheoKhoangCoDinh(file_name, 'Temperature (°C)', output_file)
    elif n == 2:
        locDuLieuTheoKhoangCoDinh(file_name, 'Humidity (%)', output_file)
    elif n == 3:
        locDuLieuTheoKhoangCoDinh(file_name, 'Wind Speed (mph)', output_file)
    elif n == 4:
        locDuLieuTheoKhoangCoDinh(file_name, 'Precipitation (%)', output_file)
    elif n == 5:
        print('1. Partly cloudy')
        print('2. Clear')
        print('3. Overcast')
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 3:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locDuLieuCsv(file_name, lambda df: (df['Cloud Cover'] == 'Partly cloudy'), output_file)
        elif k == 2:
            locDuLieuCsv(file_name, lambda df: (df['Cloud Cover'] == 'Clear'), output_file)
        elif k == 3:
            locDuLieuCsv(file_name, lambda df: (df['Cloud Cover'] == 'Overcast'), output_file)
    elif n == 6:
        locDuLieuTheoKhoangCoDinh(file_name, 'Atmospheric Pressure (hPa)', output_file)
    elif n == 7:
        locDuLieuTheoKhoangCoDinh(file_name, 'UV Index', output_file)
    elif n == 8:
        print("1. Spring")
        print("2. Summer")
        print("3. Autumn")
        print("4. Winter")
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 4:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locDuLieuCsv(file_name, lambda df: (df['Season'] == 'Spring'), output_file)
        elif k == 2:
            locDuLieuCsv(file_name, lambda df: (df['Season'] == 'Summer'), output_file)
        elif k == 3:
            locDuLieuCsv(file_name, lambda df: (df['Season'] == 'Autumn'), output_file)
        elif k == 4:
            locDuLieuCsv(file_name, lambda df: (df['Season'] == 'Winter'), output_file)
    elif n == 9:
        locDuLieuTheoKhoangCoDinh(file_name, 'Visibility (km)', output_file)
    elif n == 10:
        print("1. Inland")
        print("2. Mountain")
        print("3. Coastal")
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 3:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locDuLieuCsv(file_name, lambda df: (df['Location'] == 'Inland'), output_file)
        elif k == 2:
            locDuLieuCsv(file_name, lambda df: (df['Location'] == 'Mountain'), output_file)
        elif k == 3:
            locDuLieuCsv(file_name, lambda df: (df['Location'] == 'Coastal'), output_file)
    else:
        print("1. Rainy")
        print("2. Cloudy")
        print("3. Sunny")
        print("4. Snowy")
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 4:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locDuLieuCsv(file_name, lambda df: (df['Weather Type'] == 'Rainy'), output_file)
        elif k == 2:
            locDuLieuCsv(file_name, lambda df: (df['Weather Type'] == 'Cloudy'), output_file)
        elif k == 3:
            locDuLieuCsv(file_name, lambda df: (df['Weather Type'] == 'Sunny'), output_file)
        elif k == 4:
            locDuLieuCsv(file_name, lambda df: (df['Weather Type'] == 'Snowy'), output_file)
