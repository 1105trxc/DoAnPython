import pandas as pd
file_name = r"dataDaLamSach.csv"  # File nguồn
def sapXep(df, column_name, ascending=True):
    """
    Hàm sắp xếp DataFrame theo cột `column_name` theo thứ tự tăng dần hoặc giảm dần.
    
    Parameters:
        df (pd.DataFrame): DataFrame cần sắp xếp.
        column_name (str): Tên cột cần sắp xếp.
        ascending (bool): Nếu True, sắp xếp tăng dần. Nếu False, sắp xếp giảm dần.
        
    Returns:
        pd.DataFrame: DataFrame sau khi sắp xếp.
    """
    try:
        # Sắp xếp dữ liệu theo cột
        sorted_df = df.sort_values(by=column_name, ascending=ascending)
        return sorted_df
    except KeyError:
        # Trường hợp cột không tồn tại trong DataFrame
        raise ValueError(f"Cột '{column_name}' không tồn tại trong dữ liệu.")

