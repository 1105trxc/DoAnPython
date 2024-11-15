import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Đọc dữ liệu
data = pd.read_csv(r"D:\hocTap\CODE\Python\doAn\weather_classification_data.csv")

# Hàm để thêm nhãn giá trị trên cột
def add_value_labels(ax):
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 8), textcoords='offset points')
def add_value_labels(ax):
    for line in ax.lines:  # Xử lý từng đường trong biểu đồ
        for x, y in zip(line.get_xdata(), line.get_ydata()):
            ax.annotate(f'{y:.2f}',  # In giá trị với 2 chữ số thập phân
                        (x, y), 
                        textcoords="offset points",
                        xytext=(0, 5),  # Dịch chuyển nhãn lên trên
                        ha='center', 
                        fontsize=10, 
                        color='black')

# Vẽ Bar Plot cho nhiệt độ theo mùa
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=data, x='Season', y='Temperature', errorbar=None, hue='Season', legend=False)
plt.title('Nhiệt độ Trung bình theo mùa', fontsize=16)
plt.xlabel('Mùa', fontsize=12)
plt.ylabel('Nhiệt độ Trung bình (°C)', fontsize=12)
plt.grid(axis='y')
add_value_labels(ax)
plt.show()

# Vẽ Bar Plot cho tốc độ gió theo mùa
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=data, x='Season', y='Wind Speed', errorbar=None, hue='Season', legend=False)
plt.title('Tốc độ Gió Trung bình theo mùa', fontsize=16)
plt.xlabel('Mùa', fontsize=12)
plt.ylabel('Tốc độ Gió Trung bình (km/h)', fontsize=12)
plt.grid(axis='y')
add_value_labels(ax)
plt.show()

# Vẽ Bar Plot cho lượng mưa theo mùa
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=data, x='Season', y='Precipitation (%)', errorbar=None, hue='Season', legend=False)
plt.title('Lượng Mưa Trung bình theo mùa', fontsize=16)
plt.xlabel('Mùa', fontsize=12)
plt.ylabel('Lượng Mưa Trung bình (%)', fontsize=12)
plt.grid(axis='y')
add_value_labels(ax)
plt.show()

# Vẽ Bar Plot cho lượng mưa theo mùa với các cột riêng biệt
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=data, x='Season', y='Humidity', errorbar=None, hue='Season', legend=False)
plt.title('Lượng Mưa Trung bình theo mùa', fontsize=16)
plt.xlabel('Mùa', fontsize=12)
plt.ylabel('Độ ẩm (%)', fontsize=12)
plt.grid(axis='y')
add_value_labels(ax)
plt.show()

uv_season = data.groupby('Season')['UV Index'].mean().reset_index()
# Vẽ biểu đồ Line Plot cho UV theo mùa
plt.figure(figsize=(8, 6))
ax = sns.lineplot(data=uv_season, x='Season', y='UV Index', marker='o', color='orange', linewidth=2.5)
plt.title('Biến động chỉ số UV theo mùa', fontsize=16)
plt.xlabel('Mùa', fontsize=12)
plt.ylabel('Chỉ số UV trung bình', fontsize=12)
plt.grid(True)
add_value_labels(ax)
plt.tight_layout()  # Điều chỉnh không gian giữa các nhãn
plt.show()


