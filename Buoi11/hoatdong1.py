import numpy as np

diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]      # list Python thuần
diem_array = np.array(diem_list)           # chuyển sang mảng NumPy (ndarray)

print(type(diem_list), type(diem_array))

# Phép toán vector hóa: cộng trực tiếp 0.5 vào TOÀN BỘ mảng, không cần vòng lặp
diem_cong_them = diem_array + 0.5
print(diem_cong_them)

# So sánh với cách làm bằng list thuần (Buổi 3) - cần dùng list comprehension/vòng lặp
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print(diem_cong_them_list)

print("Trung bình:", np.mean(diem_array))
print("Lớn nhất:", np.max(diem_array))
print("Nhỏ nhất:", np.min(diem_array))
print("Độ lệch chuẩn:", round(np.std(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma trận:\n", ma_tran)
print("Kích thước (shape):", ma_tran.shape)
print("Ma trận nhân 2:\n", ma_tran * 2)
#Đối với diem_array + 0.5: Biểu thức này thực hiện được là nhờ cơ chế tính toán vector hóa của NumPy. Mảng NumPy (ndarray) cho phép áp dụng các phép toán số học trực tiếp lên toàn bộ các phần tử cùng một lúc ở tầng mã nguồn tối ưu mà không cần dùng vòng lặp tường minh.

#Đối với diem_list + 0.5: Sẽ bị lỗi (gây ra TypeError) vì trong Python thuần, toán tử + khi thao tác với kiểu dữ liệu list có ý nghĩa là nối các danh sách lại với nhau (ví dụ: list1 + list2), chứ không hỗ trợ cộng một giá trị số (float/int) vào từng phần tử bên trong danh sách[cite: 4]. Do đó, nếu dùng list thuần, bạn bắt buộc phải dùng vòng lặp hoặc list comprehension (như [diem + 0.5 for diem in diem_list])