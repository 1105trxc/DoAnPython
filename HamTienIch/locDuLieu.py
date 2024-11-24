import pandas as pd  

def locKieuSo(df, column, min_val, max_val):
    try:
        # Kiểm tra nếu cột không tồn tại trong DataFrame
        if column not in df.columns:
            print(f"Cột '{column}' không tồn tại trong dữ liệu.")
            return None
        
        # Kiểm tra nếu cột có kiểu dữ liệu số
        if not pd.api.types.is_numeric_dtype(df[column]):
            print(f"Cột '{column}' không phải là kiểu số.")
            return None

        # Lọc dữ liệu
        df_filtered = df[(df[column] >= min_val) & (df[column] <= max_val)]
        
        # Kiểm tra nếu không có dòng nào thỏa mãn
        if df_filtered.empty:
            print(f"Không có dữ liệu thỏa mãn điều kiện lọc: {min_val} <= {column} <= {max_val}")
            return None
        return df_filtered
    except ValueError:
        print("Lỗi: Giá trị nhập vào không hợp lệ.")
        return None
    except Exception as e:
        print(f"Lỗi trong quá trình lọc dữ liệu: {e}")
        return None


def locKieuString(df,filter_condition):
    #Lọc dữ liệu kiểu chuỗi từ file CSV dựa trên một điều kiện và hiển thị kết quả.
    try:
        # Lọc dữ liệu theo điều kiện
        df_filtered = df[filter_condition(df)]

        # Kiểm tra nếu không có dữ liệu sau khi lọc
        if df_filtered.empty:
            print("Không có dữ liệu thỏa mãn điều kiện lọc.")
            return None

        # Hiển thị kết quả lọc
        print("Dữ liệu sau khi lọc:")
        print(df_filtered)

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
        locKieuSo(file_name, 'Temperature (°C)', output_file)
    elif n == 2:
        locKieuSo(file_name, 'Humidity (%)', output_file)
    elif n == 3:
        locKieuSo(file_name, 'Wind Speed (mph)', output_file)
    elif n == 4:
        locKieuSo(file_name, 'Precipitation (%)', output_file)
    elif n == 5:
        print('1. Partly cloudy')
        print('2. Clear')
        print('3. Overcast')
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 3:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locKieuString(file_name, lambda df: (df['Cloud Cover'] == 'Partly cloudy'), output_file)
        elif k == 2:
            locKieuString(file_name, lambda df: (df['Cloud Cover'] == 'Clear'), output_file)
        elif k == 3:
            locKieuString(file_name, lambda df: (df['Cloud Cover'] == 'Overcast'), output_file)
    elif n == 6:
        locKieuSo(file_name, 'Atmospheric Pressure (hPa)', output_file)
    elif n == 7:
        locKieuSo(file_name, 'UV Index', output_file)
    elif n == 8:
        print("1. Spring")
        print("2. Summer")
        print("3. Autumn")
        print("4. Winter")
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 4:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locKieuString(file_name, lambda df: (df['Season'] == 'Spring'), output_file)
        elif k == 2:
            locKieuString(file_name, lambda df: (df['Season'] == 'Summer'), output_file)
        elif k == 3:
            locKieuString(file_name, lambda df: (df['Season'] == 'Autumn'), output_file)
        elif k == 4:
            locKieuString(file_name, lambda df: (df['Season'] == 'Winter'), output_file)
    elif n == 9:
        locKieuSo(file_name, 'Visibility (km)', output_file)
    elif n == 10:
        print("1. Inland")
        print("2. Mountain")
        print("3. Coastal")
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 3:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locKieuString(file_name, lambda df: (df['Location'] == 'Inland'), output_file)
        elif k == 2:
            locKieuString(file_name, lambda df: (df['Location'] == 'Mountain'), output_file)
        elif k == 3:
            locKieuString(file_name, lambda df: (df['Location'] == 'Coastal'), output_file)
    else:
        print("1. Rainy")
        print("2. Cloudy")
        print("3. Sunny")
        print("4. Snowy")
        k = int(input('Nhập loại dữ liệu muốn lọc: '))
        while k < 1 or k > 4:
            k = int(input('Không hợp lệ. Hãy nhập lại: '))
        
        if k == 1:
            locKieuString(file_name, lambda df: (df['Weather Type'] == 'Rainy'), output_file)
        elif k == 2:
            locKieuString(file_name, lambda df: (df['Weather Type'] == 'Cloudy'), output_file)
        elif k == 3:
            locKieuString(file_name, lambda df: (df['Weather Type'] == 'Sunny'), output_file)
        elif k == 4:
            locKieuString(file_name, lambda df: (df['Weather Type'] == 'Snowy'), output_file)
