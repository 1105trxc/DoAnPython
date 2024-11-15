import pandas as pd
file_name=r"C:\DAPython\weather_classification_data.csv"
def loc_du_lieu_csv(file_name, condition, output_file):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(file_name)
    
    # Lọc dữ liệu theo điều kiện
    filtered_data = df[condition(df)]
    
    # Lưu kết quả đã lọc vào file CSV mới
    filtered_data.to_csv(output_file, index=False)
    print(f"Dữ liệu đã được lưu vào file {output_file}")

def xuatlocdulieu():
    print('1. Cloud Cover')
    print('2. Season')
    print('3. Location')
    print('4. Weather Type')
    n=int(input("Nhap loai du lieu muon loc: "))
    while(n<1 or n>4):
        n=int(input('Khong hop le. Hay nhap lai: '))
    if n==1:
        print('1. partly cloudy')
        print('2. clear')
        print('3. overcast')
        k=int(input('Nhap loai du lieu muon loc: '))
        while(k<1 or k>3):
            k=int(input('Khong hop le. Hay nhap lai: '))
        if k==1:
            loc_du_lieu_csv(file_name, lambda df: (df['Cloud Cover'] =='partly cloudy'), r"C:\DAPython\sorted_output_CloudCover(partly cloudy).csv")
        elif k==2:
            loc_du_lieu_csv(file_name, lambda df: (df['Cloud Cover'] =='clear'), r"C:\DAPython\sorted_output_CloudCover(clear).csv")
        elif k==3:
            loc_du_lieu_csv(file_name, lambda df: (df['Cloud Cover'] =='overcast'), r"C:\DAPython\sorted_output_CloudCover(overcast).csv")
    elif n==2:
        print("1. Spring")
        print("2. Summer")
        print("3. Autumn")
        print("4. Winter")
        k=int(input('Nhap loai du lieu muon loc: '))
        while(k<1 or k>4):
            k=int(input('Khong hop le. Hay nhap lai: '))
        if k==1:
            loc_du_lieu_csv(file_name, lambda df: (df['Season'] =='Spring'), r"C:\DAPython\sorted_output_Season(Spring).csv")
        elif k==2:
            loc_du_lieu_csv(file_name, lambda df: (df['Season'] =='Summer'), r"C:\DAPython\sorted_output_Season(Summer).csv")
        elif k==3:
            loc_du_lieu_csv(file_name, lambda df: (df['Season'] =='Autumn'), r"C:\DAPython\sorted_output_Season(Autumn).csv")
        elif k==4:
            loc_du_lieu_csv(file_name, lambda df: (df['Season'] =='Winter'), r"C:\DAPython\sorted_output_Season(Winter).csv")
    elif n==3:
        print("1. inland")
        print("2. mountain")
        print("3. coastal")
        k=int(input('Nhap loai du lieu muon loc: '))
        while(k<1 or k>3):
            k=int(input('Khong hop le. Hay nhap lai: '))
        if k==1:
            loc_du_lieu_csv(file_name, lambda df: (df['Location'] =='inland'), r"C:\DAPython\sorted_output_Location(inland).csv")
        elif k==2:
            loc_du_lieu_csv(file_name, lambda df: (df['Location'] =='mountain'), r"C:\DAPython\sorted_output_Location(mountain).csv")
        elif k==3:
            loc_du_lieu_csv(file_name, lambda df: (df['Location'] =='coastal'), r"C:\DAPython\sorted_output_Location(coastal).csv")
    elif n==4:
        print("1. Rainy")
        print("2. Cloudy")
        print("3. Sunny")
        print("4. Snowy")
        k=int(input('Nhap loai du lieu muon loc: '))
        while(k<1 or k>4):
            k=int(input('Khong hop le. Hay nhap lai: '))
        if k==1:
            loc_du_lieu_csv(file_name, lambda df: (df['Weather Type'] =='Rainy'), r"C:\DAPython\sorted_output_WeatherType(Rainy).csv")
        elif k==2:
            loc_du_lieu_csv(file_name, lambda df: (df['Weather Type'] =='Cloudy'), r"C:\DAPython\sorted_output_WeatherType(Cloudy).csv")
        elif k==3:
            loc_du_lieu_csv(file_name, lambda df: (df['Weather Type'] =='Sunny'), r"C:\DAPython\sorted_output_WeatherType(Sunny).csv")
        elif k==4:
            loc_du_lieu_csv(file_name, lambda df: (df['Weather Type'] =='Snowy'), r"C:\DAPython\sorted_output_WeatherType(Snowy).csv")
xuatlocdulieu()
