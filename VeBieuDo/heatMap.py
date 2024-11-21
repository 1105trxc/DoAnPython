import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"d:\hocTap\CODE\3\DoAnPython\Cleaning\dataDaLamSach.csv")

def Draw():
    # Lọc các cột số trong dữ liệu
    numerical_columns = data.select_dtypes(include=['float64', 'int64'])

    # Tính ma trận tương quan
    correlation_matrix = numerical_columns.corr()

    # Vẽ Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Heatmap biểu diễn mối liên hệ tương quan giữa các dữ liệu", fontsize=16)
    plt.show()
