import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from VeBieuDo.bieuDoTheoKhuVuc import *  # Import tất cả các hàm từ bieuDoTheoKhuVuc.py
from HamTienIch.locDuLieu import * # Import tất cả các hàm từ locDuLieu.py
from VeBieuDo.bieuDoTheoMua import *
file_path = r"dataDaLamSach.csv"
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    messagebox.showerror("Error", f"File {file_path} not found!")
    data = pd.DataFrame()  # Nếu không có dữ liệu, khởi tạo DataFrame rỗng

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

        options = [
            ("Nhiệt độ trung bình theo khu vực", drawNhietDo),
            ("Tốc độ gió trung bình theo khu vực", drawSucGio),
            ("Khả năng có mưa theo khu vực", drawKhaNangMua),
            ("Độ ẩm trung bình theo khu vực", drawDoAm),
            ("Nhiệt độ trung bình theo mùa", drawNhietDoTheoMua),
            ("Tốc độ gió trung bình theo mùa", drawSucGioTheoMua),
            ("Khả năng mưa", drawKhaNangMua),
            ("Độ ẩm trung bình theo mùa", drawDoAmTheoMua),
            ("Biến động chỉ số UV theo mùa", drawUVTheoMua),
            

        ]

        for label, func in options:
            btn = ttk.Button(menu, text=label, command=lambda f=func: show_plot(f))
            btn.pack(fill=tk.X, padx=10, pady=5)

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
