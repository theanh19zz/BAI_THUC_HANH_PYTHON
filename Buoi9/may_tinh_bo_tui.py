import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x420")
cua_so.resizable(False, False)


bieu_thuc = ""
bien_hien_thi = tk.StringVar()


entry_hien_thi = tk.Entry(
    cua_so,
    textvariable=bien_hien_thi,
    font=("Arial", 20),
    justify="right",
    bd=5,
    relief=tk.SUNKEN
)
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)



def nhap_nut(gia_tri):
    global bieu_thuc
    bieu_thuc += str(gia_tri)
    bien_hien_thi.set(bieu_thuc)



def xoa_man_hinh():
    global bieu_thuc
    bieu_thuc = ""
    bien_hien_thi.set("")



def tinh_ket_qua():
    global bieu_thuc
    try:

        ket_qua = str(eval(bieu_thuc))
        bien_hien_thi.set(ket_qua)
        bieu_thuc = ket_qua 
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho số 0!")
        xoa_man_hinh()
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
        xoa_man_hinh()



nut_bam = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
]


for (text, r, c) in nut_bam:
    if text == "C":
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, bg="#ff9999", command=xoa_man_hinh)
    else:
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, command=lambda t=text: nhap_nut(t))
    btn.grid(row=r+1, column=c, padx=5, pady=5)


btn_bang = tk.Button(cua_so, text="=", font=("Arial", 14), bg="#99ccff", width=23, height=2, command=tinh_ket_qua)
btn_bang.grid(row=6, column=0, columnspan=4, padx=5, pady=5)


cua_so.mainloop()