import pandas as pd
import numpy as np

# Đọc dữ liệu
#data = pd.read_csv(r"D:\hocTap\CODE\doAnPytthon\weather_classification_data.csv", encoding='utf-8')
data = pd.read_csv('weather_classification_data.csv', encoding='utf-8')


# 1. Kiểm tra giá trị null
print("Số lượng giá trị null trong mỗi cột:")
print(data.isnull().sum())

# Thay thế giá trị null
for col in data.columns:
    if data[col].dtype in ['float64', 'int64']:  # Cột số
        data[col].fillna(data[col].mean(), inplace=True)
    elif data[col].dtype == 'object':  # Cột phân loại
        data[col].fillna(data[col].mode()[0], inplace=True)

# 2. Xử lý giá trị ngoại lệ bằng IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

print("Số lượng hàng trước khi xử lý ngoại lệ:", len(data))
for col in data.select_dtypes(include=['float64', 'int64']).columns:
    data = remove_outliers(data, col)
print("Số lượng hàng sau khi xử lý ngoại lệ:", len(data))

# 3. Chuyển đổi kiểu dữ liệu (nếu cần)
if 'Temperature' in data.columns:
    data['Temperature'] = data['Temperature'].astype(float)

# 4. Loại bỏ dữ liệu trùng lặp
data.drop_duplicates(inplace=True)

# 5. Chuẩn hóa dữ liệu phân loại - Viết hoa chữ cái đầu
for col in data.select_dtypes(include=['object']).columns:
    data[col] = data[col].str.capitalize()

# 6. Loại bỏ cột không cần thiết
columns_to_drop = ['Unnecessary_Column']  # Thay tên cột phù hợp
data.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# 7. Thay đổi tên cột (Thêm đơn vị):
data.rename(columns={
    'Temperature': 'Temperature (\u00b0C)', 
    'Humidity': 'Humidity (%)', 
    'Wind Speed': 'Wind Speed (mph)', 
    'Atmospheric Pressure': 'Atmospheric Pressure (hPa)'
}, inplace=True)

# 8. Lưu dữ liệu đã làm sạch
#data.to_csv(r"D:\hocTap\CODE\doAnPytthon\Cleaning\dataDaLamSach.csv", index=False, encoding='utf-8-sig')
data.to_csv('dataDaLamSach.csv', index=False, encoding='utf-8-sig')

print("Dữ liệu đã làm sạch:")
print(data.head())
