import pandas as pd

file_path = 'D:\\PY_prj\DoAnPython\weather_classification_data.csv'  

output_file = 'D:\\Py_prj\\DoAnPython\\hnq\\filtered_visibility.csv'


try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print("The file does not exist. Please check the path again.")
    exit()

try:
    min_visibility = float(input("Enter the minimum VVisibility (km) value: "))
    while (min_visibility < 0):
        min_visibility = float(input("Invalid input, please try again."))
    max_visibility = float(input("Enter the maximum Visibility (km) value:: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Lọc dữ liệu theo khoảng giá trị
filtered_data = data[(data['Visibility (km)'] >= min_visibility) & 
                     (data['Visibility (km)'] <= max_visibility)]

# Kiểm tra nếu không có dữ liệu nào thỏa mãn
if filtered_data.empty:
    print("No data available in the specified range.")
else:
    # Xuất dữ liệu đã lọc ra file CSV
    filtered_data.to_csv(output_file, index=False)
    print(f"The filtered data has been saved to the file: {output_file}")
