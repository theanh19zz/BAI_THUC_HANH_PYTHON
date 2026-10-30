import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")
print(df.head())          
print(df.shape)           
print(df.columns.tolist()) 

diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)

print("Điểm trung bình toàn bộ:", df["diem"].mean())
print("Điểm cao nhất:", df["diem"].max())
print("Điểm thấp nhất:", df["diem"].min())

diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh viên đạt:")
print(sinh_vien_dat)
print("\nSinh viên không đạt:")
print(sinh_vien_khong_dat)