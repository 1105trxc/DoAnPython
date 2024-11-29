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
# Hàm để thêm nhãn giá trị trên đường
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
def drawNhietDoTheoKhuVuc():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Temperature (°C)', errorbar=None, hue='Location', legend=False)
    plt.title('Nhiệt độ trung bình theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Nhiệt độ trung bình (°C)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawSucGioTheoKhuVuc():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Wind Speed (mph)', errorbar=None, hue='Location', legend=False)
    plt.title('Tốc độ Gió trung bình theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Tốc độ Gió trung bình (mph)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawKhaNangMuaTheoKhuVuc():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Precipitation (%)', errorbar=None, hue='Location', legend=False)
    plt.title('Khả năng có mưa theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Khả năng có mưa (%)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawDoAmTheoKhuVuc():
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=data, x='Location', y='Humidity (%)', errorbar=None, hue='Location', legend=False)
    plt.title('Độ ẩm trung bình theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Độ ẩm trung bình (%)', fontsize=12)
    plt.grid(axis='y')
    addValueLabelsBar(ax)
    plt.show()

def drawUVTheoKhuVuc():
    uv_location = data.groupby('Location')['UV Index'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    ax = sns.lineplot(data=uv_location, x='Location', y='UV Index', marker='o', color='orange', linewidth=2.5)
    plt.title('Biến động chỉ số UV theo khu vực', fontsize=16)
    plt.xlabel('Khu vực', fontsize=12)
    plt.ylabel('Chỉ số UV trung bình  ', fontsize=12)
    plt.grid(True)
    addValueLabelsLine(ax)
    plt.show()



