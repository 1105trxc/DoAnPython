import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Đọc dữ liệu
data = pd.read_csv(r"d:\hocTap\CODE\3\DoAnPython\Cleaning\dataDaLamSach.csv")

# Hàm để thêm nhãn giá trị trên cột
def addValueLabels(ax):
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 8), textcoords='offset points')
def addValueLabels(ax):
    for line in ax.lines:  # Xử lý từng đường trong biểu đồ
        for x, y in zip(line.get_xdata(), line.get_ydata()):
            ax.annotate(f'{y:.2f}',  # In giá trị với 2 chữ số thập phân
                        (x, y), 
                        textcoords="offset points",
                        xytext=(0, 5),  # Dịch chuyển nhãn lên trên
                        ha='center', 
                        fontsize=10, 
                        color='black')

# Hàm vẽ các biểu đồ
def drawNhietDo():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Temperature (°C)', errorbar=None, hue='Location', legend=False)
    plt.title('Nhiệt độ trung bình theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Nhiệt độ trung bình (°C)', fontsize=12)
    plt.grid(axis='y')
    addValueLabels(ax)
    plt.show()

def drawSucGio():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Wind Speed (mph)', errorbar=None, hue='Location', legend=False)
    plt.title('Tốc độ Gió trung bình theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Tốc độ Gió trung bình (mph)', fontsize=12)
    plt.grid(axis='y')
    addValueLabels(ax)
    plt.show()

def drawKhaNangMua():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Precipitation (%)', errorbar=None, hue='Location', legend=False)
    plt.title('Khả năng có mưa theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Khả năng có mưa (%)', fontsize=12)
    plt.grid(axis='y')
    addValueLabels(ax)
    plt.show()

def drawDoAm():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Humidity (%)', errorbar=None, hue='Location', legend=False)
    plt.title('Độ ẩm trung bình theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Độ ẩm trung bình (%)', fontsize=12)
    plt.grid(axis='y')
    addValueLabels(ax)
    plt.show()

def drawUV():
    uv_location = data.groupby('Location')['UV Index'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    ax = sns.lineplot(data=uv_location, x='Location', y='UV Index', marker='o', color='orange', linewidth=2.5)
    plt.title('Biến động chỉ số UV theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Chỉ số UV trung bình  ', fontsize=12)
    plt.grid(True)
    addValueLabels(ax)
    plt.tight_layout()  
    plt.show()

# Menu để chọn biểu đồ
def Draw():
    while True:
        print("\nChọn loại biểu đồ muốn vẽ:")
        print("1. Nhiệt độ trung bình theo khu vực")
        print("2. Tốc độ gió trung bình theo khu vực")
        print("3. Khả năng có mưa theo khu vực")
        print("4. Độ ẩm trung bình theo khu vực")
        print("5. Biến động chỉ số UV theo khu vực")
        print("6. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            drawNhietDo()
        elif choice == '2':
           drawSucGio()
        elif choice == '3':
            drawKhaNangMua()
        elif choice == '4':
           drawDoAm()
        elif choice == '5':
            drawUV()
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


