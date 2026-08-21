#hoat dong 3.1: soi loi dat ten
# 1diem: Sai - Bat dau bang chu so (sua: diem1)
# gia-tri: Sai - Chua dau gach ngang (sua: gia_tri)
# _tam_thoi: Dung - Bat dau bang dau _ hop le
# Diem_TB: Dung - Dat ten kieu Snake_case hop le
# class: Sai - Trung tu khoa keyword cua Python
# so luong: Sai - Chua khoang trang
# MAX_SPEED: Dung - Viet hoa hang so hop le
# diemTB: Dung - Dat ten kieu camelCase hop le
# 2024_data: Sai - Bat dau bang chu so (sua: data_2024)
# tong$: Sai - Chua ky tu dac biet $
# sinhVien1: Dung - Chu so dung o cuoi hop le
# Hoat dong 3.2: Ap dung PEP8
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  # Hang so (UPPER_CASE)

print("Ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUC_LUONG_TOI_THIEU)
import keyword

# Liệt kê từ khóa
print("Danh sách từ khóa:", keyword.kwlist)
print("Số lượng từ khóa:", len(keyword.kwlist))
# --- Bài tập 5.1: Toán tử số học ---
a = 17
b = 5
print("=== Bài 5.1 ===")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# --- Bài tập 5.2: Toán tử so sánh & logic ---
diem = 6.5
tuoi = 20
print("\n=== Bài 5.2 ===")
is_kha = (diem >= 6.5) and (diem < 8.0)
is_chua_du_tuoi_hoac_gia = (tuoi < 18) or (tuoi > 60)
not_is_kha = not is_kha

print("Đạt loại Khá:", is_kha)
print("Chưa đủ 18 hoặc trên 60 tuổi:", is_chua_du_tuoi_hoac_gia)
print("Phủ định đạt loại Khá:", not_is_kha)

# --- Bài tập 5.3: Toán tử gán & toán tử đặc biệt ---
print("\n=== Bài 5.3 ===")
x = 10
x += 5
print("Sau x += 5:", x)
x -= 3
print("Sau x -= 3:", x)
x *= 2
print("Sau x *= 2:", x)
x /= 4
print("Sau x /= 4:", x)
x //= 2
print("Sau x //= 2:", x)
x **= 3
print("Sau x **= 3:", x)

danh_sach = [1, 2, 3, "python"]
danh_sach_2 = danh_sach
danh_sach_3 = [1, 2, 3, "python"]

print("3 có trong danh_sach:", 3 in danh_sach)
print("danh_sach_2 is danh_sach:", danh_sach_2 is danh_sach)
print("danh_sach_3 is danh_sach:", danh_sach_3 is danh_sach)

# --- Bài tập 5.4: Độ ưu tiên toán tử ---
print("\n=== Bài 5.4 ===")
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)
print("10 > 5 and 3 < 1 or not False =", 10 > 5 and 3 < 1 or not False)
# 6.1 - Kiểu dữ liệu của biến

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

# 6.2 - Tính điểm trung bình và xếp loại

ho_ten = "Do Dong Minh"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

loai_gioi = dtb >= 8.0
loai_kha = dtb >= 6.5 and dtb < 8.0
loai_trung_binh = dtb >= 5.0 and dtb < 6.5
loai_yeu = dtb < 5.0

print(ho_ten, "- Điểm trung bình:", round(dtb, 2))
print("Đạt loại giỏi", loai_gioi)
print("Đạt loại khá", loai_kha)
print("Đạt loại trung bình", loai_trung_binh)
print("Đạt loại yếu", loai_yeu)
print("Kiểu dữ liệu của loại giỏi:", type(loai_gioi))
