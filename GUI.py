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
        ttk.Button(self.control_frame, text="Sort", command=self.sort_data).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Filter", command=self.filter_data).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.control_frame, text="Update", command=self.update_data).pack(fill=tk.X, padx=5, pady=5)
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
        # Tạo các trường nhập liệu
        labels = [
            "Temperature (°C)", "Humidity (%)", "Wind Speed (mph)", "Precipitation (%)", 
            "Cloud Cover", "Atmospheric Pressure (hPa)", "UV Index", "Season", 
            "Visibility (km)", "Location", "Weather Type"
        ]
        
        entries = {}
    
        # Tạo nhãn và trường nhập liệu theo bố cục lưới
        for i, label in enumerate(labels):
            ttk.Label(main_frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entry = ttk.Entry(main_frame, width=30)
            entry.grid(row=i, column=1, pady=5, padx=10)
            entries[label] = entry

        error_label = ttk.Label(main_frame, text="", foreground="red")
        error_label.grid(row=len(labels)+1, column=0, columnspan=2, pady=5, sticky="ew")
        def on_add():
                # Lấy dữ liệu từ các trường nhập liệu
                data_input = {label: entries[label].get() for label in labels}

                # Thêm hàng mới vào DataFrame thông qua hàm Create
                updated_data = Create(self.data, data_input , error_label)  # Sử dụng hàm Create của bạn

                #if isinstance(updated_data, pd.DataFrame):  # Kiểm tra dữ liệu trả về
                if updated_data is not None:
                    self.data = updated_data  # Cập nhật dữ liệu mới
                    self.original_data = self.data.copy()  # Cập nhật bản sao dữ liệu gốc nếu cần
                    messagebox.showinfo("Thông báo", "Thêm dữ liệu thành công!")  # Hiển thị thông báo thành công
                    self.save_csv()  # Lưu lại CSV nếu cần
                    input_window.destroy()  # Đóng cửa sổ nhập liệu
                else:
                    # Nếu dữ liệu không hợp lệ, hiển thị thông báo lỗi
                    #messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")                   
                    messagebox.showerror("Lỗi", f"Dữ liệu nhập vào không hợp lệ, vui lòng kiểm tra lại!")
                    return
        #Nút thêm dữ liệu
        ttk.Button(main_frame, text="Thêm", command=on_add).grid(row=len(labels), column=0, columnspan=2, pady=20)
   
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
                """Kiểm tra xem giá trị có phải là số hay không."""
                try:
                    float(value)  # Kiểm tra nếu có thể chuyển sang kiểu float
                    return True
                except ValueError:
                    return False

            def on_update(data_window, tree):  
                selected_item = tree.selection()
                if selected_item:  
                    # Lấy chỉ số dòng từ Treeview  
                    selected_row = tree.index(selected_item[0])

                    def save_updated_data():
                        # Lấy các giá trị nhập vào
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

                        # Kiểm tra các ô nhập liệu số có hợp lệ không
                        for key, value in data_input.items():
                            if key not in ["Cloud Cover", "Season", "Location", "Weather Type"]:  # Những trường không phải số
                                if not is_number(value):
                                    messagebox.showerror("Lỗi dữ liệu", f"Vui lòng nhập một giá trị hợp lệ cho '{key}'.")
                                    return  # Dừng lại và không lưu nếu có lỗi


                        # Nếu tất cả đều hợp lệ, thực hiện lưu dữ liệu
                        for key, value in data_input.items():
                            if key not in ["Cloud Cover", "Season", "Location", "Weather Type"]:
                                # Chuyển đổi các giá trị số thành float hoặc int khi cần
                                if '.' in value:
                                    value = float(value)
                                else:
                                    value = int(value)

                            self.data.at[selected_row, key] = value

                        # Cập nhật Treeview
                        tree.item(tree.get_children()[selected_row], values=list(self.data.iloc[selected_row]))
                        self.update_window.destroy()  # Đóng cửa sổ cập nhật

                    # Tạo cửa sổ cập nhật
                    self.update_window = tk.Toplevel(self.root)
                    self.update_window.title("Cập nhật dữ liệu")

                    update_frame = ttk.Frame(self.update_window)
                    update_frame.pack(padx=20, pady=20)

                    self.error_label = ttk.Label(update_frame, text="", foreground="red")
                    self.error_label.grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")

                    # Các trường nhập liệu
                    ttk.Label(update_frame, text="Cloud Cover:").grid(row=0, column=0, padx=5, pady=5)
                    self.cloud_cover_combobox = ttk.Combobox(update_frame, values=["Partly cloudy", "Clear", "Overcast", "Cloudy"])
                    self.cloud_cover_combobox.grid(row=0, column=1, padx=5, pady=5)
                    self.cloud_cover_combobox.set(self.data.iloc[selected_row]["Cloud Cover"])

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