def update_data(self):  
        """Hiển thị cửa sổ để người dùng chọn dòng cần cập nhật."""  
        if self.data.empty:  
            messagebox.showerror("Lỗi", "Không có dữ liệu để cập nhật.")  
            return  

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
                        "Temperature (°C)": float(self.temperature_entry.get()) if self.temperature_entry.get() else None,
                        "Humidity (%)": float(self.humidity_entry.get()) if self.humidity_entry.get() else None,
                        "Wind Speed (km/h)": float(self.wind_speed_entry.get()) if self.wind_speed_entry.get() else None,
                        "Precipitation (%)": float(self.precipitation_entry.get()) if self.precipitation_entry.get() else None,
                        "Atmospheric Pressure (hPa)": float(self.atmospheric_pressure_entry.get()) if self.atmospheric_pressure_entry.get() else None,
                        "UV Index": int(self.uv_index_entry.get()) if self.uv_index_entry.get() else None,
                        "Visibility (km)": float(self.visibility_entry.get()) if self.visibility_entry.get() else None,
                    }

                    # Cập nhật dữ liệu trong DataFrame
                    for column, value in data_input.items():
                        self.data.at[selected_row, column] = value

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

                ttk.Label(update_frame, text="Wind Speed (km/h):").grid(row=6, column=0, padx=5, pady=5)
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