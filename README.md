## Nguồn gốc Dữ liệu

- **Nguồn**: Bộ dữ liệu này được cung cấp trên Kaggle, được tạo ra bởi người dùng Nikhil7280 với mục tiêu phục vụ các bài toán phân loại thời tiết. Link tham khảo: [Kaggle Weather Type Classification](https://www.kaggle.com/datasets/nikhil7280/weather-type-classification/data).
- **Dữ liệu tổng hợp (Synthetic)**: Dữ liệu được tạo ngẫu nhiên và không thu thập từ nguồn thực tế, mà được mô phỏng để có thể phản ánh các yếu tố thời tiết đa dạng nhằm phục vụ cho các bài toán phân loại trong học máy.

## Mô tả Dữ liệu 

Bộ dữ liệu bao gồm các thông số thời tiết, chẳng hạn như nhiệt độ, độ ẩm, tốc độ gió, lượng mưa, áp suất, và loại thời tiết. Cụ thể:

1. **Temperature (°F)**: Nhiệt độ tại địa điểm đo, biểu thị theo độ Fahrenheit.
2. **Humidity (%)**: Độ ẩm không khí.
3. **Wind Speed (mph)**: Tốc độ gió.
4. **Precipitation (%)**: Khả năng có mưa tại thời điểm đo.
5. **Cloud Cover**: Mức độ che phủ của mây, gồm các giá trị như "partly cloudy," "clear," hoặc "overcast."
6. **Atmospheric Pressure (hPa)**: Áp suất khí quyển.
7. **UV Index**: Chỉ số tia cực tím.
8. **Season**: Mùa trong năm (Winter, Spring, Summer, Autumn).
9. **Visibility (km)**: Tầm nhìn tính bằng km.
10. **Location**: Khu vực địa lý đo đạc (inland, mountain, coastal).
11. **Weather Type**: Loại thời tiết gồm các giá trị "Rainy," "Sunny," "Cloudy," và "Snowy."

## Chức năng của Dữ liệu

Bộ dữ liệu được thiết kế để:   

1. **Thực hành các thuật toán phân loại**: Phân loại thời tiết dựa trên các đặc điểm đầu vào, rất hữu ích cho các bài toán học máy trong lĩnh vực phân loại (classification).
2. **Xử lý dữ liệu và tiền xử lý**: Dữ liệu bao gồm nhiều kiểu biến khác nhau (liên tục, phân loại), tạo điều kiện cho việc áp dụng các kỹ thuật tiền xử lý, chuyển đổi, và xử lý dữ liệu.
3. **Phát hiện ngoại lệ**: Các giá trị bất thường (outliers) trong dữ liệu thời tiết có thể được phát hiện để cải thiện độ chính xác của mô hình.
4. **Thực hành phân tích dữ liệu**: Bộ dữ liệu cho phép phân tích và trực quan hóa các mối quan hệ giữa các yếu tố thời tiết, ví dụ, mối quan hệ giữa nhiệt độ và độ ẩm theo từng mùa, hoặc phân tích theo vị trí địa lý.
