import Cleaning.Clean as Clean
import CRUD.CRUD as CRUD
import HamTienIch.locDuLieu as locDuLieu
import HamTienIch.sapXepGiam as sapXepGiam
import HamTienIch.sapXepTang as sapXepTang
import VeBieuDo.bieuDoTheoKhuVuc as bieuDoKhuVuc
import VeBieuDo.bieuDoTheoMua as bieuDoMua
import VeBieuDo.heatMap as heatMap

def main():
    while True:
        print("\n=== QUẢN LÝ DỮ LIỆU THỜI TIẾT ===")
        print("1. Thêm dữ liệu")
        print("2. Xóa dữ liệu")
        print("3. Đọc dữ liệu")
        print("4. Cập nhật dữ liệu")
        print("5. Lưu dữ liệu")
        print("6. Lọc dữ liệu")
        print("7. Sắp xếp dữ liệu tăng dần")
        print("8. Sắp xếp dữ liệu giảm dần")
        print("9. Vẽ biểu đồ theo khu vực")
        print("10. Vẽ biểu đồ theo mùa")
        print("11. Vẽ biểu đồ heat map")
        print("12. Thoát chương trình")

        # Yêu cầu người dùng chọn chức năng
        choice = input("Chọn chức năng (1-12): ").strip()

        # Thực hiện chức năng tương ứng
        if choice == '1':
            CRUD.data = CRUD.addData(CRUD.data)
        elif choice == '2':
            CRUD.data = CRUD.deleteData(CRUD.data)
        elif choice == '3':
            CRUD.read_data(CRUD.data)
        elif choice == '4':
            CRUD.data = CRUD.update_data(CRUD.data)
        elif choice == '5':
            CRUD.save_data(CRUD.data)
        elif choice == '6':
             locDuLieu.file_name = locDuLieu.xuatLocDuLieu()
        elif choice == '7':
             sapXepGiam.file_name = sapXepGiam.sapXepGiam()
        elif choice == '8':
            sapXepTang.file_name = sapXepTang.sapXepTang()
        elif choice == '9':
            bieuDoKhuVuc.data = bieuDoKhuVuc.draw()
        elif choice == '10':
            bieuDoMua.data = bieuDoMua.draw()
        elif choice == '11':
            heatMap.data = heatMap.draw()
        elif choice == '12':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình, chỉ thực thi nếu chạy trực tiếp tệp
if __name__ == "__main__":
    main()
