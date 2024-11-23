import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from VeBieuDo.bieuDoTheoKhuVuc import *  
from HamTienIch.locDuLieu import * 
from VeBieuDo.bieuDoTheoMua import *
from VeBieuDo.heatMap import *
file_path = r"dataDaLamSach.csv"
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    messagebox.showerror("Error", f"File {file_path} not found!")
    data = pd.DataFrame()  

class CSVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Đồ án cuối kì")
        
        # Initialize data
        self.data = data.copy()
        
        # UI Components
        self.create_widgets()
        
    def create_widgets(self):
        # Frame for table
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview for displaying data
        self.tree = ttk.Treeview(self.table_frame, columns=list(self.data.columns), show="headings")
        for col in self.data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Add data to Treeview
        self.load_data_to_tree()
        
        # Control buttons
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(fill=tk.X)
        
        ttk.Button(self.control_frame, text="Add Row", command=self.add_row).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Delete Row", command=self.delete_row).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Visualize", command=self.visualize_data).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Save CSV", command=self.save_csv).pack(side=tk.LEFT, padx=5, pady=5)
        
    def load_data_to_tree(self):
        """Load data into the treeview."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for _, row in self.data.iterrows():
            self.tree.insert("", tk.END, values=list(row))
    
    def add_row(self):
        """Add a new row to the data."""
        new_data = {col: "" for col in self.data.columns}
        new_row = pd.DataFrame([new_data])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        self.load_data_to_tree()
    
    def delete_row(self):
        """Delete selected row."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No row selected!")
            return
        row_id = self.tree.index(selected_item[0])
        self.data = self.data.drop(index=row_id).reset_index(drop=True)
        self.load_data_to_tree()
    
    def visualize_data(self):
        """Hiển thị menu để vẽ biểu đồ."""
        def show_plot(plot_function):
            """Hàm gọi hàm vẽ biểu đồ tương ứng."""
            plot_function()

        menu = tk.Toplevel()
        menu.title("Chọn biểu đồ để hiển thị")
        menu.geometry("400x300")

        # Tạo Notebook để chia tab
        notebook = ttk.Notebook(menu)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Tab "Vẽ theo khu vực"
        tab_khu_vuc = ttk.Frame(notebook)
        notebook.add(tab_khu_vuc, text="Vẽ theo khu vực")

        # Tab "Vẽ theo mùa"
        tab_theo_mua = ttk.Frame(notebook)
        notebook.add(tab_theo_mua, text="Vẽ theo mùa")

        tab_heat = ttk.Frame(notebook)
        notebook.add(tab_heat, text="Vẽ heatmap")

        # Danh sách biểu đồ
        options_khu_vuc = [
            ("Nhiệt độ trung bình theo khu vực", drawNhietDo),
            ("Tốc độ gió trung bình theo khu vực", drawSucGio),
            ("Khả năng có mưa theo khu vực", drawKhaNangMua),
            ("Độ ẩm trung bình theo khu vực", drawDoAm),
        ]

        options_theo_mua = [
            ("Nhiệt độ trung bình theo mùa", drawNhietDoTheoMua),
            ("Tốc độ gió trung bình theo mùa", drawSucGioTheoMua),
            ("Khả năng có mưa theo mùa", drawKhaNangMua),
            ("Độ ẩm trung bình theo mùa", drawDoAmTheoMua),
            ("Biến động chỉ số UV theo mùa", drawUVTheoMua),
        ]
        options_heatmap = [
            ("Heatmap",DrawHeatMap),]

        # Thêm các nút vào tab "Vẽ theo khu vực"
        for label, func in options_khu_vuc:
            btn = ttk.Button(tab_khu_vuc, text=label, command=lambda f=func: show_plot(f))
            btn.pack(fill=tk.X, padx=10, pady=5)

        # Thêm các nút vào tab "Vẽ theo mùa"
        for label, func in options_theo_mua:
            btn = ttk.Button(tab_theo_mua, text=label, command=lambda f=func: show_plot(f))
            btn.pack(fill=tk.X, padx=10, pady=5)

        for label, func in options_heatmap:
            btn = ttk.Button(tab_heat, text=label, command=lambda f=func: show_plot(f))
            btn.pack(fill=tk.X, padx=10, pady=5)
        # Nút đóng ở cuối cửa sổ
        ttk.Button(menu, text="Đóng", command=menu.destroy).pack(pady=10)

    def save_csv(self):
        """Save data to a new CSV file."""
        file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file:
            self.data.to_csv(file, index=False)
            messagebox.showinfo("Info", f"Data saved to {file}")

# Run the application
root = tk.Tk()
app = CSVApp(root)
root.mainloop()
