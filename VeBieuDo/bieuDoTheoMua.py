import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Đọc dữ liệu
data = pd.read_csv(r"dataDaLamSach.csv")

# Hàm để thêm nhãn giá trị trên cột
def addValueLabelsBar(ax):
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 8), textcoords='offset points')

def addValueLabelsLine(ax):
    for line in ax.lines:
        for x, y in zip(line.get_xdata(), line.get_ydata()):
            ax.annotate(f'{y:.2f}',
                        (x, y), 
                        textcoords="offset points",
                        xytext=(0, 5), 
                        ha='center', 
                        fontsize=10, 
                        color='black')

# Hàm vẽ các biểu đồ
def drawNhietDoTheoMua():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Season', y='Temperature (°C)', errorbar=None, hue='Season', legend=False)
    plt.title('Nhiệt độ trung bình theo mùa', fontsize=16)
    plt.xlabel('Mùa', fontsize=12)
    plt.ylabel('Nhiệt độ trung bình (°C)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawSucGioTheoMua():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Season', y='Wind Speed (mph)', errorbar=None, hue='Season', legend=False)
    plt.title('Tốc độ Gió trung bình theo mùa', fontsize=16)
    plt.xlabel('Mùa', fontsize=12)
    plt.ylabel('Tốc độ Gió trung bình (km/h)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawKhaNangMuaTheoMua():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Season', y='Precipitation (%)', errorbar=None, hue='Season', legend=False)
    plt.title('Khả năng có mưa theo mùa', fontsize=16)
    plt.xlabel('Mùa', fontsize=12)
    plt.ylabel('Khả năng có mưa (%)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawDoAmTheoMua():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Season', y='Humidity (%)', errorbar=None, hue='Season', legend=False)
    plt.title('Độ ẩm trung bình theo mùa', fontsize=16)
    plt.xlabel('Mùa', fontsize=12)
    plt.ylabel('Độ ẩm (%)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawUVTheoMua():
    uv_season = data.groupby('Season')['UV Index'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    ax = sns.lineplot(data=uv_season, x='Season', y='UV Index', marker='o', color='orange', linewidth=2.5)
    plt.title('Biến động chỉ số UV theo mùa', fontsize=16)
    plt.xlabel('Mùa', fontsize=12)
    plt.ylabel('Chỉ số UV trung bình', fontsize=12)
    plt.grid(True)
    addValueLabelsLine(ax)
    plt.show()

# Menu để chọn biểu đồ
def Draw():
    while True:
        print("\nChọn loại biểu đồ muốn vẽ:")
        print("1. Nhiệt độ trung bình theo mùa")
        print("2. Tốc độ gió trung bình theo mùa")
        print("3. Khả năng có mưa theo mùa")
        print("4. Độ ẩm trung bình theo mùa")
        print("5. Biến động chỉ số UV theo mùa")
        print("6. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            drawNhietDoTheoMua()
        elif choice == '2':
           drawSucGioTheoMua()
        elif choice == '3':
            drawKhaNangMuaTheoMua()
        elif choice == '4':
           drawDoAmTheoMua()
        elif choice == '5':
            drawUVTheoMua()
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

