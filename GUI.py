import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from VeBieuDo.bieuDoTheoKhuVuc import *   
from VeBieuDo.bieuDoTheoMua import *
from VeBieuDo.heatMap import *
from CRUD.CRUD import *
from HamTienIch.locDuLieu import *
from HamTienIch.sapXep import *
from PIL import Image, ImageTk
from datetime import datetime

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
        # Center the main window
        self.center_window(800, 600)  # Adjusted window size

        self.data = data.copy()
        self.original_data = self.data.copy()
        # Customize the theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "TMenubutton",
            font=("Helvetica", 14),
            background="#4CAF50",
            foreground="white",
            relief="raised",
        )
        self.style.map(
            "TMenubutton", background=[("active", "#45a049")], foreground=[("active", "white")]
        )
        
        # UI Component
        self.create_widgets()
        self.update_time()

    def center_window(self, width, height):
        """Đặt cửa sổ chính giữa màn hình."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Main content area
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.load_image()
        # Add Title Label
        self.title_label = tk.Label(
            self.main_frame,
            text="App Thời Tiết",
            font=("Helvetica", 30, "bold"),
            bg="#f0f0f0",
            fg="#333333",
        )
        self.title_label.pack(pady=20)
        # Create menu button with a dropdown menu
        self.menu_button = ttk.Menubutton(self.root, text="Menu", style="TMenubutton")
        self.menu_button.pack(side=tk.TOP, padx=10, pady=10)
        #Time
        self.time_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.time_label.place(relx=1, rely=0.9, anchor="se")  # Đặt ở góc dưới bên phải
        #Logo
        self.logo = Image.open("logo2.png") 
        self.logo = self.logo.resize((50, 50), Image.Resampling.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(self.logo)

        self.logo_label = tk.Label(self.root, image=self.logo_image)
        self.logo_label.place(relx=0, rely=0.95, anchor="sw")  # Đặt logo ở góc dưới bên trái


        # Dropdown menu
        self.menu = tk.Menu(self.menu_button, tearoff=0, bg="#EFEFEF", fg="#333333", font=("Helvetica", 12))
        self.menu_button["menu"] = self.menu
        
        # Add menu items
        self.menu.add_command(label="Show Data", command=self.show_data_window)
        self.menu.add_command(label="Add Row", command=self.add_row)
        self.menu.add_command(label="Delete Row", command=self.delete_row)
        self.menu.add_command(label="Visualize", command=self.visualize_data)
        self.menu.add_command(label="Sort", command=self.sort_data)
        self.menu.add_command(label="Filter", command=self.filter_data)
        self.menu.add_command(label="Update", command=self.update_data)
        self.menu.add_command(label="Save CSV", command=self.save_csv)

        # Footer
        self.footer_label = tk.Label(
            self.root,
            text="© 2024 Đồ án cuối kì",
            font=("Helvetica", 10),
            bg="#66CDAA",
            fg="black",
            height=2,
            width=30
        )
        self.footer_label.pack(side="bottom", fill="x")  # Đặt Label ở dưới và kéo dài ngang màn hình
    def load_image(self):
        """Load and display the image in the center of the window."""
        # Load the image using Pillow
        image = Image.open("weather1.png")  # Replace with your image file path
        image = image.resize((800, 400), Image.Resampling.LANCZOS)  # Updated for Pillow 10+
        self.photo = ImageTk.PhotoImage(image)

        # Add the image to a label
        self.image_label = tk.Label(self.main_frame, image=self.photo)
        self.image_label.pack(pady=10)
    def update_time(self):
        # Lấy thời gian hiện tại
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=f"Time: {current_time}")
        # Lặp lại mỗi giây
        self.root.after(1000, self.update_time)

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
        prev_button.pack(side=tk.LEFT, padx=2, pady=2)
       
        # Nút quay lại trang trước
        next_button = ttk.Button(nav_frame, text="Next Page", command=next_page)
        next_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        if additional_button:
            additional_button(data_window, self.tree, nav_frame)

        # Nút đóng cửa sổ
        ttk.Button(data_window, text="Close", command=data_window.destroy).pack(pady=2)    
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
        input_window.geometry("400x500")
        self.center_toplevel(input_window, 400, 500)
        # Tạo frame chính để chứa các thành phần giao diện
        main_frame = ttk.Frame(input_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        combo_fields = {
            "Cloud Cover": ["Partly cloudy", "Clear", "Overcast", "Cloudy"],
            "Season": ["Spring", "Summer", "Fall", "Winter"],
            "Location": ["Inland", "Mountain", "Coastal"],
            "Weather Type": ["Rainy", "Cloudy", "Sunny", "Snowy"]
        }

        # Các trường dữ liệu còn lại (nhập liệu tự do)
        text_fields = [
            "Temperature (°C)", "Humidity (%)", "Wind Speed (mph)", "Precipitation (%)",
            "Atmospheric Pressure (hPa)", "UV Index", "Visibility (km)"
        ]

        entries = {}

        # Tạo các trường combobox
        for i, (label, values) in enumerate(combo_fields.items()):
            ttk.Label(main_frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            combobox = ttk.Combobox(main_frame, values=values, state="readonly")
            combobox.grid(row=i, column=1, pady=5, padx=10)
            combobox.set(values[0])  # Thiết lập giá trị mặc định
            entries[label] = combobox

        # Tạo các trường nhập liệu tự do
        offset = len(combo_fields)
        for i, label in enumerate(text_fields, start=offset):
            ttk.Label(main_frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entry = ttk.Entry(main_frame, width=30)
            entry.grid(row=i, column=1, pady=5, padx=10)
            entries[label] = entry

        # Nhãn hiển thị lỗi
        error_label = ttk.Label(main_frame, text="", foreground="red")
        error_label.grid(row=len(combo_fields) + len(text_fields) + 1, column=0, columnspan=2, pady=5, sticky="ew")
        def on_add():
            """Hàm xử lý khi nhấn nút 'Thêm'."""
            # Lấy dữ liệu từ các trường nhập liệu và combobox
            data_input = {label: (widget.get() if isinstance(widget, ttk.Combobox) else widget.get())
                        for label, widget in entries.items()}

            # Gọi hàm Create để thêm hàng mới
            updated_data = Create(self.data, data_input, error_label)

            if updated_data is not None:
                self.data = updated_data  # Cập nhật dữ liệu mới
                self.original_data = self.data.copy()  # Cập nhật bản sao dữ liệu gốc
                messagebox.showinfo("Thông báo", "Thêm dữ liệu thành công!")
                self.save_csv()  # Lưu dữ liệu vào CSV nếu cần
                input_window.destroy()  # Đóng cửa sổ nhập liệu
            else:
                # Nếu dữ liệu không hợp lệ, hiển thị thông báo lỗi
                messagebox.showerror("Lỗi", "Dữ liệu nhập vào không hợp lệ, vui lòng kiểm tra lại!")

        # Nút thêm dữ liệu
        ttk.Button(main_frame, text="Thêm", command=on_add).grid(
            row=len(combo_fields) + len(text_fields), column=0, columnspan=2, pady=20
        )

   
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

        def add_delete_button(data_window, tree, nav_frame):
            ttk.Button(nav_frame, text="Delete", command=lambda: on_delete(data_window, tree)).pack(side=tk.LEFT,padx=2,pady=2)
            
        # Hiển thị cửa sổ dữ liệu và thêm nút xóa
        self.show_data_window(additional_button=lambda data_window, tree, nav_frame: add_delete_button(data_window, tree, nav_frame))

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
            ("Độ ẩm trung bình theo mùa", drawDoAmTheoMua),
            ("Biến động chỉ số UV theo mùa", drawUVTheoMua)
        ]
        options_heatmap = [
            ("Heatmap", drawHeatMap)
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

        # Lấy danh sách tên cột từ dữ liệu gốc
        columns = list(self.original_data.columns)

        # Tạo Tab 1 - Lọc theo kiểu số
        tab_numeric = ttk.Frame(notebook)
        notebook.add(tab_numeric, text="Lọc kiểu số")
        numeric_columns = [
            col for col in self.original_data.columns
            if pd.api.types.is_numeric_dtype(self.original_data[col])
        ]
        
        # Nhập cột
        column_label = tk.Label(tab_numeric, text="Chọn cột:")
        column_label.pack(pady=5)
        column_combo = ttk.Combobox(tab_numeric, values=numeric_columns)
        column_combo.pack(pady=5)
        
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
            column = column_combo.get()  # Lấy tên cột từ ComboBox
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
            else:
                messagebox.showwarning("Không có dữ liệu", "Không tìm thấy dữ liệu thỏa mãn.")

        numeric_button = tk.Button(tab_numeric, text="Lọc theo kiểu số", command=apply_numeric_filter)
        numeric_button.pack(pady=10)

        # Tạo Tab 2 - Lọc theo kiểu chuỗi
        tab_string = ttk.Frame(notebook)
        notebook.add(tab_string, text="Lọc kiểu chuỗi")

        string_columns = [
            col for col in self.original_data.columns
            if self.original_data[col].dropna().map(type).eq(str).all()
        ]
        # Nhập cột
        column_label_string = tk.Label(tab_string, text="Chọn cột:")
        column_label_string.pack(pady=5)
        column_combo_string = ttk.Combobox(tab_string, values= string_columns)
        column_combo_string.pack(pady=5)

        condition_label = tk.Label(tab_string, text="Nhập điều kiện lọc:")
        condition_label.pack(pady=5)
        condition_entry = tk.Entry(tab_string)
        condition_entry.pack(pady=5)

        # Nút lọc theo kiểu chuỗi
        def apply_string_filter():
            # Lọc cột có kiểu dữ liệu là chuỗi
            string_columns = self.original_data.select_dtypes(include=["string"]).columns
            # Cập nhật giá trị cho ComboBox
            column_combo_string["values"] = string_columns

            column = column_combo_string.get()  # Lấy tên cột từ ComboBox
            condition = condition_entry.get()
            filtered_data = locKieuString(self.original_data, column, condition)
            if filtered_data is not None:
                self.data = filtered_data  # Cập nhật self.data tạm thời
                self.show_data_window()
            else:
                messagebox.showwarning("Không có dữ liệu", "Không tìm thấy dữ liệu thỏa mãn.")

        string_button = tk.Button(tab_string, text="Lọc theo kiểu chuỗi", command=apply_string_filter)
        string_button.pack(pady=10)

        # Khôi phục dữ liệu gốc
        def reset_data():
            self.data = self.original_data.copy()  # Khôi phục dữ liệu về trạng thái gốc
            self.show_data_window()
            messagebox.showinfo("Khôi phục thành công", "Dữ liệu đã được khôi phục về trạng thái ban đầu.")

        reset_button = tk.Button(sort_window, text="Khôi phục dữ liệu gốc", command=reset_data)
        reset_button.pack(pady=10)

        
    def update_data(self):  
        """Hiển thị cửa sổ để người dùng chọn dòng cần cập nhật."""  
        if self.data.empty:  
            messagebox.showerror("Lỗi", "Không có dữ liệu để cập nhật.")  
            return  
        def is_number(value):
            """Kiểm tra xem giá trị có phải là số hợp lệ hay không."""
            try:
                float(value)
                return True
            except ValueError:
                return False

        def validate_and_convert(data_input):
            """Xác minh và chuyển đổi giá trị đầu vào."""
            try:
                for key, value in data_input.items():
                    # Chỉ kiểm tra các trường số
                    if key not in ["Cloud Cover", "Season", "Location", "Weather Type"]:
                        if not is_number(value):
                            raise ValueError(f"Vui lòng nhập một giá trị hợp lệ cho '{key}'.")
                        value = float(value)
                        # Kiểm tra giá trị trong khoảng hợp lệ
                        if key == "Temperature (°C)" and not (-25 <= value <= 71):
                            raise ValueError("Nhiệt độ phải nằm trong khoảng -25 đến 71°C.")
                        if key == "Humidity (%)" and not (0 <= value <= 110):
                            raise ValueError("Độ ẩm phải nằm trong khoảng 0% đến 110%.")
                        if key == "Wind Speed (mph)" and not (0 <= value <= 40):
                            raise ValueError("Tốc độ gió phải nằm trong khoảng 0 đến 40 mph.")
                        if key == "Precipitation (%)" and not (0 <= value <= 110):
                            raise ValueError("Lượng mưa phải nằm trong khoảng 0% đến 110%.")
                        if key == "Atmospheric Pressure (hPa)" and not (900 <= value <= 1100):
                            raise ValueError("Áp suất khí quyển phải nằm trong khoảng 900 đến 1110 hPa.")
                        if key == "UV Index" and not (0 <= value <= 13):
                            raise ValueError("Chỉ số UV phải nằm trong khoảng 0 đến 13.")
                        if key == "Visibility (km)" and not (0 <= value <= 20):
                            raise ValueError("Tầm nhìn phải nằm trong khoảng 0 đến 20 km.")
                        # Lưu giá trị đã chuyển đổi
                        data_input[key] = value
                return data_input
            except ValueError as e:
                messagebox.showerror("Lỗi dữ liệu", str(e))
                return None
            

        def on_update(data_window, tree):  
            selected_item = tree.selection()
            if selected_item:  
                # Lấy chỉ số dòng từ Treeview  
                selected_row = tree.index(selected_item[0])

                def save_updated_data():
                    data_input = {
                        "Cloud Cover": self.cloud_cover_combobox.get(),
                        "Season": self.season_combobox.get(),
                        "Location": self.location_combobox.get(),
                        "Weather Type": self.weather_type_combobox.get(),
                        "Temperature (°C)": self.temperature_entry.get(),
                        "Humidity (%)": self.humidity_entry.get(),
                        "Wind Speed (mph)": self.wind_speed_entry.get(),
                        "Precipitation (%)": self.precipitation_entry.get(),
                        "Atmospheric Pressure (hPa)": self.atmospheric_pressure_entry.get(),
                        "UV Index": self.uv_index_entry.get(),
                        "Visibility (km)": self.visibility_entry.get(),
                    }

                    valid_data = validate_and_convert(data_input)
                    if valid_data is None:
                        return  # Dừng lại nếu dữ liệu không hợp lệ
                    
                    # Cập nhật dữ liệu trong DataFrame
                    for column, value in data_input.items():
                        self.data.at[selected_row, column] = value
                    
                    messagebox.showinfo("Thông báo","Cập nhật thành công!")

                    # Cập nhật Treeview
                    tree.item(tree.get_children()[selected_row], values=list(self.data.iloc[selected_row]))
                    self.update_window.destroy()  # Đóng cửa sổ cập nhật

                # Tạo cửa sổ cập nhật
                self.update_window = tk.Toplevel(self.root)
                self.update_window.title("Cập nhật dữ liệu")
                # self.update_window.geometry("500x400")

                update_frame = ttk.Frame(self.update_window)
                update_frame.pack(padx=20, pady=20)

                self.error_label = ttk.Label(update_frame, text="", foreground="red")
                self.error_label.grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")

                ttk.Label(update_frame, text="Cloud Cover:").grid(row=0, column=0, padx=5, pady=5)
                self.cloud_cover_combobox = ttk.Combobox(update_frame, values=["Partly cloudy", "Clear", "Overcast", "Cloudy"])
                self.cloud_cover_combobox.grid(row=0, column=1, padx=5, pady=5)
                self.cloud_cover_combobox.insert(0, self.data.iloc[selected_row]["Cloud Cover"])

                ttk.Label(update_frame, text="Season:").grid(row=1, column=0, padx=5, pady=5)
                self.season_combobox = ttk.Combobox(update_frame, values=["Spring", "Summer", "Fall", "Winter"])
                self.season_combobox.grid(row=1, column=1, padx=5, pady=5)
                self.season_combobox.set(self.data.iloc[selected_row]["Season"])

                ttk.Label(update_frame, text="Location:").grid(row=2, column=0, padx=5, pady=5)
                self.location_combobox = ttk.Combobox(update_frame, values=["Inland", "Mountain", "Coastal"])
                self.location_combobox.grid(row=2, column=1, padx=5, pady=5)
                self.location_combobox.set(self.data.iloc[selected_row]["Location"])

                ttk.Label(update_frame, text="Weather Type:").grid(row=3, column=0, padx=5, pady=5)
                self.weather_type_combobox = ttk.Combobox(update_frame, values=["Rainy", "Cloudy", "Sunny", "Snowy"])
                self.weather_type_combobox.grid(row=3, column=1, padx=5, pady=5)
                self.weather_type_combobox.set(self.data.iloc[selected_row]["Weather Type"])

                ttk.Label(update_frame, text="Temperature (°C):").grid(row=4, column=0, padx=5, pady=5)
                self.temperature_entry = ttk.Entry(update_frame)
                self.temperature_entry.grid(row=4, column=1, padx=5, pady=5)
                self.temperature_entry.insert(0, str(self.data.iloc[selected_row]["Temperature (°C)"]))

                ttk.Label(update_frame, text="Humidity (%):").grid(row=5, column=0, padx=5, pady=5)
                self.humidity_entry = ttk.Entry(update_frame)
                self.humidity_entry.grid(row=5, column=1, padx=5, pady=5)
                self.humidity_entry.insert(0, str(self.data.iloc[selected_row]["Humidity (%)"]))

                ttk.Label(update_frame, text="Wind Speed (mph):").grid(row=6, column=0, padx=5, pady=5)
                self.wind_speed_entry = ttk.Entry(update_frame)
                self.wind_speed_entry.grid(row=6, column=1, padx=5, pady=5)
                self.wind_speed_entry.insert(0, str(self.data.iloc[selected_row]["Wind Speed (mph)"]))

                ttk.Label(update_frame, text="Precipitation (%):").grid(row=7, column=0, padx=5, pady=5)
                self.precipitation_entry = ttk.Entry(update_frame)
                self.precipitation_entry.grid(row=7, column=1, padx=5, pady=5)
                self.precipitation_entry.insert(0, str(self.data.iloc[selected_row]["Precipitation (%)"]))

                ttk.Label(update_frame, text="Atmospheric Pressure (hPa):").grid(row=8, column=0, padx=5, pady=5)
                self.atmospheric_pressure_entry = ttk.Entry(update_frame)
                self.atmospheric_pressure_entry.grid(row=8, column=1, padx=5, pady=5)
                self.atmospheric_pressure_entry.insert(0, str(self.data.iloc[selected_row]["Atmospheric Pressure (hPa)"]))

                ttk.Label(update_frame, text="UV Index:").grid(row=9, column=0, padx=5, pady=5)
                self.uv_index_entry = ttk.Entry(update_frame)
                self.uv_index_entry.grid(row=9, column=1, padx=5, pady=5)
                self.uv_index_entry.insert(0, str(self.data.iloc[selected_row]["UV Index"]))

                ttk.Label(update_frame, text="Visibility (km):").grid(row=10, column=0, padx=5, pady=5)
                self.visibility_entry = ttk.Entry(update_frame)
                self.visibility_entry.grid(row=10, column=1, padx=5, pady=5)
                self.visibility_entry.insert(0, str(self.data.iloc[selected_row]["Visibility (km)"]))


                 # Tạo khung cho các nút
                button_frame = ttk.Frame(update_frame)
                button_frame.grid(row=11, column=0, columnspan=2, pady=10)
                # Nút lưu và đóng cửa sổ  
                tk.Button(button_frame, text="Save", command=save_updated_data).pack(side=tk.LEFT, padx=5)
                ttk.Button(button_frame, text="Cancel", command=self.update_window.destroy).pack(side=tk.LEFT, padx=5)
            else:  
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dòng để cập nhật.")

        def add_update_button(data_window, tree, nav_frame):
            ttk.Button(nav_frame, text="Update", command=lambda: on_update(data_window, tree)).pack(side=tk.LEFT, padx=2, pady=2)
            
        # Hiển thị cửa sổ dữ liệu và thêm nút "Cập nhật"
        self.show_data_window(additional_button=add_update_button)

    def sort_data(self):
        """Hàm tạo cửa sổ sắp xếp và hiển thị kết quả sắp xếp trên GUI"""
        sort_window = tk.Toplevel(self.root)
        sort_window.title("Sắp xếp dữ liệu")
        sort_window.geometry("400x300")
        
        # Tạo menu chọn cột
        column_label = tk.Label(sort_window, text="Chọn cột cần sắp xếp:")
        column_label.pack(pady=10)
        
        columns = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (mph)', 'Precipitation (%)',
                   'Atmospheric Pressure (hPa)', 'UV Index', 'Visibility (km)']
        
        column_combo = ttk.Combobox(sort_window, values=columns)
        column_combo.set(columns[0])  # Mặc định chọn cột đầu tiên
        column_combo.pack(pady=5)

        # Lựa chọn kiểu sắp xếp (tăng dần hoặc giảm dần)
        sort_order_label = tk.Label(sort_window, text="Chọn kiểu sắp xếp:")
        sort_order_label.pack(pady=5)
        sort_order = ttk.Combobox(sort_window, values=["Tăng dần", "Giảm dần"])
        sort_order.set("Tăng dần")  # Mặc định là tăng dần
        sort_order.pack(pady=5)

        # Hàm để thực hiện sắp xếp khi người dùng nhấn nút "Sắp xếp"
        def apply_sort():
            column_name = column_combo.get()  # Lấy tên cột người dùng chọn
            order = sort_order.get()  # Lấy kiểu sắp xếp (tăng hoặc giảm dần)
            
            # Chọn kiểu sắp xếp: True cho Tăng dần, False cho Giảm dần
            ascending = True if order == "Tăng dần" else False
            
            try:
                # Gọi hàm sapXep từ sorting.py để sắp xếp dữ liệu
                self.data = sapXep(self.original_data, column_name, ascending=ascending)
                
                # Hiển thị dữ liệu đã sắp xếp lên GUI
                self.show_data_window()  # Hàm hiển thị dữ liệu lên GUI

            except ValueError as e:
                # Nếu có lỗi (ví dụ cột không tồn tại), hiển thị thông báo lỗi
                messagebox.showerror("Lỗi", str(e))

        # Nút để thực hiện sắp xếp
        sort_button = tk.Button(sort_window, text="Sắp xếp", command=apply_sort)
        sort_button.pack(pady=20)

        # Nút khôi phục dữ liệu gốc (nếu muốn)
        def reset_data():
            self.data = self.original_data.copy()  # Khôi phục dữ liệu gốc
            self.show_data_window()  # Hiển thị lại dữ liệu gốc
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