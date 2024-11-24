import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from VeBieuDo.bieuDoTheoKhuVuc import *   
from VeBieuDo.bieuDoTheoMua import *
from VeBieuDo.heatMap import *
from CRUD.CRUD import *
from HamTienIch.locDuLieu import *
from HamTienIch.sapXepGiam import *
from HamTienIch.sapXepTang import *

# Load data from CSV file
try:
    data = pd.read_csv(r"dataDaLamSach.csv")
except FileNotFoundError:
    messagebox.showerror("Error", "File not found!")
    data = pd.DataFrame()

class CSVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Đồ án cuối kì")
        # # Initialize data
        self.data = data.copy()
        self.original_data = self.data.copy()  
        # Center the main window
        self.center_window(400, 300)
        
        # UI Components
        self.create_widgets()

    def center_window(self, width, height):
        """Đặt cửa sổ chính giữa màn hình."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position to center the window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Set the geometry of the window
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Frame for table
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(fill=tk.BOTH, expand=True)

        # Control buttons
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(fill=tk.X)

        ttk.Button(self.control_frame, text="Show Data", command=self.show_data_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Add Row", command=self.add_row).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Delete Row", command=self.delete_row).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Visualize", command=self.visualize_data).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Sort", command=self.filter_data).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Filter", command=self.filter_data).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Update", command=self.show_data_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Save CSV", command=self.save_csv).pack(fill=tk.X, padx=5, pady=5)
    
    def show_data_window(self, additional_button=None, rows_per_page=10):
        """Hiển thị dữ liệu trong một cửa sổ mới với phân trang"""
        if self.data.empty:
            messagebox.showwarning("Warning", "No data to display!")
            return
        
        # Tạo cửa sổ mới
        data_window = tk.Toplevel(self.root)
        data_window.title("Data View")
        data_window.geometry("1400x300")
        self.center_toplevel(data_window, 1400, 300)
        
        # Frame chứa Treeview
        frame = ttk.Frame(data_window)
        frame.pack(fill=tk.BOTH, expand=True)
        #Tạo thanh cuộn
        
        x_scroll = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
        y_scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(
            frame, 
            columns=list(self.data.columns), 
            show="headings", 
            xscrollcommand=x_scroll.set, 
            yscrollcommand=y_scroll.set
        )

        # Thiết lập thanh cuộn hoạt động
        x_scroll.config(command=self.tree.xview)
        y_scroll.config(command=self.tree.yview)

        # Đặt thanh cuộn
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Đặt Treeview
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # # Tạo Treeview
        for col in self.data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=tk.CENTER)
        # Gọi hàm Read 
        current_page = 1
        page_data, total_pages = Read(self.data, page=current_page, page_size=rows_per_page)

        # Thêm dữ liệu vào Treeview
        def load_page_data(page):
            page_data, _ = Read(self.data, page=page, page_size=rows_per_page)
            # Xóa dữ liệu cũ trong Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            # Thêm dữ liệu mới
            for _, row in page_data.iterrows():
                self.tree.insert("", tk.END, values=list(row))
        load_page_data(current_page)

        # Nút chuyển trang
        def next_page():
            nonlocal current_page
            if current_page < total_pages:
                current_page += 1
                load_page_data(current_page)
                page_label.config(text=f"Page {current_page}/{total_pages}")
        def prev_page():
            nonlocal current_page
            if current_page > 1:
                current_page -= 1
                load_page_data(current_page)
                page_label.config(text=f"Page {current_page}/{total_pages}")
        # Tạo thanh điều hướng
        nav_frame = ttk.Frame(data_window)
        nav_frame.pack(fill=tk.X, pady=10)

        page_label = ttk.Label(nav_frame, text=f"Page {current_page}/{total_pages}")
        page_label.pack(side=tk.LEFT)

        # Nút chuyển trang tiếp theo
        prev_button = ttk.Button(nav_frame, text="Previous Page", command=prev_page)
        prev_button.pack(side=tk.LEFT, padx=10, pady=10)
       
        # Nút quay lại trang trước
        next_button = ttk.Button(nav_frame, text="Next Page", command=next_page)
        next_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        if additional_button:
            additional_button(data_window, self.tree)

        # Nút đóng cửa sổ
        ttk.Button(data_window, text="Close", command=data_window.destroy).pack(pady=10)    
    def center_toplevel(self, window, width, height):
        """Đặt cửa sổ con ở giữa màn hình."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    def add_row(self):

        """Add a new row to the data by calling Create from CRUD."""
        # Tạo cửa sổ nhập liệu
        input_window = tk.Toplevel(self.root)
        input_window.title("Nhập thông tin thời tiết")
        input_window.geometry("400x400")
        self.center_toplevel(input_window, 400, 400)
        # Tạo các trường nhập liệu
        labels = [
            "Temperature (°C)", "Humidity (%)", "Wind Speed (mph)", "Precipitation (%)", 
            "Cloud Cover", "Atmospheric Pressure (hPa)", "UV Index", "Season", 
            "Visibility (km)", "Location", "Weather Type"
        ]
        
        entries = {}
        frame = ttk.Frame(input_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        for label in labels:
            row = ttk.Frame(input_window)
            row.pack(fill=tk.X, pady=5)

            lbl = ttk.Label(row, text=label)
            lbl.pack(side=tk.LEFT, padx=5)

            entry = ttk.Entry(row)
            entry.pack(side=tk.LEFT, fill=tk.X, padx=5)
            entries[label] = entry

        # Hàm để xử lý khi nhấn nút "Thêm"
        def on_add():
            try:
                data_input = {label: entries[label].get() for label in labels}
                # Thêm hàng mới vào DataFrame thông qua hàm Create
                self.data = Create(self.data, data_input)
                messagebox.showinfo("Thông báo", "Thêm dữ liệu thành công!")
                input_window.destroy()  # Đóng cửa sổ nhập liệu

            except ValueError:
                messagebox.showerror("Lỗi", "Dữ liệu nhập vào không hợp lệ, vui lòng kiểm tra lại!")

        # Nút thêm dữ liệu
        ttk.Button(input_window, text="Thêm", command=on_add).pack(pady=10)
    def delete_row(self):
        """Hiển thị cửa sổ để người dùng chọn dòng cần xóa."""
        if self.data.empty:
            messagebox.showerror("Lỗi", "Không có dữ liệu để xóa.")
            return

        # Hàm xử lý khi chọn dòng để xóa
        def on_delete(data_window, tree):
            selected_item = tree.selection()
            if selected_item:
                # Lấy chỉ số dòng từ Treeview
                selected_row = tree.index(selected_item[0])  # Lấy chỉ số dòng của phần tử được chọn
                # Gọi hàm Delete để xóa dòng
                self.data = Delete(self.data, selected_row)
                # Cập nhật lại bảng dữ liệu
                for item in tree.get_children():
                    tree.delete(item)
                for index, row in self.data.iterrows():
                    tree.insert("", "end", values=row.tolist())
                messagebox.showinfo("Thông báo", "Xóa thành công!")
            else:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dòng để xóa.")

        def add_delete_button(data_window, tree):
            ttk.Button(data_window, text="Xóa", command=lambda: on_delete(data_window, tree)).pack(pady=10)
        
        # Hiển thị cửa sổ dữ liệu và thêm nút xóa
        self.show_data_window(additional_button=add_delete_button)

    def visualize_data(self):
        """Hiển thị menu để vẽ biểu đồ."""
        def show_plot(plot_function):
            """Hàm gọi hàm vẽ biểu đồ tương ứng."""
            plot_function()

        menu = tk.Toplevel()
        menu.title("Chọn biểu đồ để hiển thị")
        menu.geometry("400x300")
        self.center_toplevel(menu, 400, 300)
        
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
            ("Nhiệt độ trung bình theo khu vực", drawNhietDoTheoKhuVuc),
            ("Tốc độ gió trung bình theo khu vực", drawSucGioTheoKhuVuc),
            ("Khả năng có mưa theo khu vực", drawKhaNangMuaTheoKhuVuc),
            ("Độ ẩm trung bình theo khu vực", drawDoAmTheoKhuVuc),
            ("Biến động chỉ số UV theo khu vực", drawUVTheoKhuVuc)
        ]

        options_theo_mua = [
            ("Nhiệt độ trung bình theo mùa", drawNhietDoTheoMua),
            ("Tốc độ gió trung bình theo mùa", drawSucGioTheoMua),
            ("Khả năng có mưa theo mùa", drawKhaNangMuaTheoMua),
            ("Biến động chỉ số UV theo mùa", drawUVTheoMua)
        ]
        options_heatmap = [
            ("Heatmap", DrawHeatMap)
        ]

        # Thêm các nút vào tab "Vẽ theo khu vực"
        for label, func in options_khu_vuc:
            btn = ttk.Button(tab_khu_vuc, text=label, command=lambda f=func: show_plot(f))
            btn.pack(fill=tk.X, padx=10, pady=5)

        # Thêm các nút vào tab "Vẽ theo mùa"
        for label, func in options_theo_mua:
            btn = ttk.Button(tab_theo_mua, text=label, command=lambda f=func: show_plot(f))
            btn.pack(fill=tk.X, padx=10, pady=5)

        # Thêm các nút vào tab heatmap
        for label, func in options_heatmap:
            btn = ttk.Button(tab_heat, text=label, command=lambda f=func: show_plot(f))
            btn.pack(fill=tk.X, padx=10, pady=5)

        # Nút đóng ở cuối cửa sổ
        ttk.Button(menu, text="Đóng", command=menu.destroy).pack(pady=10)

    def filter_data(self):
        """Hàm tạo cửa sổ lọc với hai tab riêng biệt cho lọc số và lọc chuỗi"""
        # Tạo cửa sổ con
        sort_window = tk.Toplevel(self.root)
        sort_window.title("Chọn kiểu lọc")
        sort_window.geometry("400x400")
        
        # Tạo Notebook (tab)
        notebook = ttk.Notebook(sort_window)
        notebook.pack(padx=10, pady=10, fill="both", expand=True)

        # Tạo Tab 1 - Lọc theo kiểu số
        tab_numeric = ttk.Frame(notebook)
        notebook.add(tab_numeric, text="Lọc kiểu số")
        
        # Nhập tên cột
        column_label = tk.Label(tab_numeric, text="Nhập tên cột:")
        column_label.pack(pady=5)
        column_entry = tk.Entry(tab_numeric)
        column_entry.pack(pady=5)

        # Nhập giá trị tối thiểu và tối đa
        min_label = tk.Label(tab_numeric, text="Nhập giá trị tối thiểu:")
        min_label.pack(pady=5)
        min_entry = tk.Entry(tab_numeric)
        min_entry.pack(pady=5)

        max_label = tk.Label(tab_numeric, text="Nhập giá trị tối đa:")
        max_label.pack(pady=5)
        max_entry = tk.Entry(tab_numeric)
        max_entry.pack(pady=5)

        # Nút lọc theo kiểu số
        def apply_numeric_filter():
            column = column_entry.get()
            try:
                min_val = float(min_entry.get())
                max_val = float(max_entry.get())
            except ValueError:
                messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập giá trị số hợp lệ cho tối thiểu và tối đa.")
                return
            # Kiểm tra xem cột có tồn tại trong dữ liệu không
            if column not in self.original_data.columns:
                messagebox.showerror("Lỗi", f"Cột '{column}' không tồn tại trong dữ liệu.")
                return
            # Lọc dữ liệu từ self.original_data thay vì self.data
            filtered_data = locKieuSo(self.original_data, column, min_val, max_val)
            if filtered_data is not None:
                self.data = filtered_data  # Cập nhật self.data tạm thời
                self.show_data_window()
                messagebox.showinfo("Lọc thành công", "Dữ liệu đã được lọc và hiển thị.")
            else:
                messagebox.showwarning("Không có dữ liệu", "Không tìm thấy dữ liệu thỏa mãn.")

        numeric_button = tk.Button(tab_numeric, text="Lọc theo kiểu số", command=apply_numeric_filter)
        numeric_button.pack(pady=10)

        # Tạo Tab 2 - Lọc theo kiểu chuỗi
        tab_string = ttk.Frame(notebook)
        notebook.add(tab_string, text="Lọc kiểu chuỗi")

        # Nhập tên cột và điều kiện lọc cho chuỗi
        column_label_string = tk.Label(tab_string, text="Nhập tên cột:")
        column_label_string.pack(pady=5)
        column_entry_string = tk.Entry(tab_string)
        column_entry_string.pack(pady=5)

        condition_label = tk.Label(tab_string, text="Nhập điều kiện lọc:")
        condition_label.pack(pady=5)
        condition_entry = tk.Entry(tab_string)
        condition_entry.pack(pady=5)

        # Nút lọc theo kiểu chuỗi
        def apply_string_filter():
            column = column_entry_string.get()
            condition = condition_entry.get()
            filtered_data = locKieuString(self.original_data, column, condition)
            if filtered_data is not None:
                self.data = filtered_data  # Cập nhật self.data tạm thời
                self.show_data_window()
                messagebox.showinfo("Lọc thành công", "Dữ liệu đã được lọc và hiển thị.")
            else:
                messagebox.showwarning("Không có dữ liệu", "Không tìm thấy dữ liệu thỏa mãn.")

        string_button = tk.Button(tab_string, text="Lọc theo kiểu chuỗi", command=apply_string_filter)
        string_button.pack(pady=10)

        # Nút khôi phục dữ liệu gốc
        def reset_data():
            self.data = self.original_data.copy()  # Khôi phục dữ liệu về trạng thái gốc
            self.show_data_window()
            messagebox.showinfo("Khôi phục thành công", "Dữ liệu đã được khôi phục về trạng thái ban đầu.")

        reset_button = tk.Button(sort_window, text="Khôi phục dữ liệu gốc", command=reset_data)
        reset_button.pack(pady=10)
        
    def save_csv(self):
        """Save data to the same CSV file."""
        try:
            self.data.to_csv(r"dataDaLamSach.csv", index=False)  # Lưu vào file CSV cũ
            messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu vào dataDaLamSach.csv")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {str(e)}")
# Run the applicationcls
root = tk.Tk()
app = CSVApp(root)
root.mainloop()