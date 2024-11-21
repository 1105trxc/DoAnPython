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
            CRUD.data = CRUD.Create(CRUD.data)
        elif choice == '2':
            CRUD.data = CRUD.Delete(CRUD.data)
        elif choice == '3':
            CRUD.Read(CRUD.data)
        elif choice == '4':
            CRUD.data = CRUD.Update(CRUD.data)
        elif choice == '5':
            CRUD.saveData(CRUD.data)
        elif choice == '6':
            locDuLieu.output_file = locDuLieu.xuatLocDuLieu()
        elif choice == '7':
             sapXepGiam.output_file = sapXepGiam.sapXepGiam()
        elif choice == '8':
            sapXepTang.output_file = sapXepTang.sapXepTang()
        elif choice == '9':
            bieuDoKhuVuc.data = bieuDoKhuVuc.Draw()
        elif choice == '10':
            bieuDoMua.data = bieuDoMua.Draw()
        elif choice == '11':
            heatMap.data = heatMap.Draw()
        elif choice == '12':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình, chỉ thực thi nếu chạy trực tiếp tệp
if __name__ == "__main__":
    main()
