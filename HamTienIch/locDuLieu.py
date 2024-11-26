import pandas as pd  

def locKieuSo(df, column, min_val, max_val):
    try:
        # Kiểm tra nếu cột không tồn tại trong DataFrame
        if column not in df.columns:
            print(f"Cột '{column}' không tồn tại trong dữ liệu.")
            return None
        
        # Kiểm tra nếu cột có kiểu dữ liệu số
        if not pd.api.types.is_numeric_dtype(df[column]):
            print(f"Cột '{column}' không phải là kiểu số.")
            return None

        # Lọc dữ liệu
        df_filtered = df[(df[column] >= min_val) & (df[column] <= max_val)]
        
        # Kiểm tra nếu không có dòng nào thỏa mãn
        if df_filtered.empty:
            print(f"Không có dữ liệu thỏa mãn điều kiện lọc: {min_val} <= {column} <= {max_val}")
            return None
        return df_filtered
    except ValueError:
        print("Lỗi: Giá trị nhập vào không hợp lệ.")
        return None
    except Exception as e:
        print(f"Lỗi trong quá trình lọc dữ liệu: {e}")
        return None
    
def locKieuString(df, column, condition):
    """
    Lọc dữ liệu kiểu chuỗi từ file CSV dựa trên một điều kiện và một cột cụ thể.
    """
    try:
        # Lọc dữ liệu theo điều kiện
        df_filtered = df[df[column].str.contains(condition, na=False)]

        # Kiểm tra nếu không có dữ liệu sau khi lọc
        if df_filtered.empty:
            print("Không có dữ liệu thỏa mãn điều kiện lọc.")
            return None
        return df_filtered
    except Exception as e:
        print(f"Lỗi trong quá trình lọc dữ liệu: {e}")
        return None

