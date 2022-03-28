from tkinter import *
from tkinter import messagebox
def Cal_bmi(e):
    bmi = weight.get() / (height.get() / 100) ** 2
    tt_bmi.set(f'BMI = {bmi:.2f}')
    color_zone = ""
    if bmi > 30:
        color_zone = "#ff0a00"
        data["text"] = "โรคอ้วนอันตราย"
    elif bmi >= 25:
        color_zone = "#FF9933"
        data["text"] = "โรคอ้วน"
    elif bmi >= 23:
        color_zone = "#FFFF33"
        data["text"] = "อ้วน"
    elif bmi >= 18.5:
        color_zone = "#63d12e"
        data["text"] = "สมส่วน"
    else:
        color_zone = "#000080"
        data["text"] = "น้ำหนักต่ำกว่าเกณฑ์"
    lbl_bmi["bg"] = color_zone
def SS():
    Thank = StringVar()
    Thank.set("ขอบคุณครับ \n"
              "กลุ่มBMI")
    Thankyou = Thank.get()
    messagebox.showinfo("ค่า BMIgit initและสีต่างๆ", Thankyou)
root = Tk()
root.option_add("*Font", "consolas 20")

tt_bmi = StringVar()

Label(root, text="น้ำหนัก (Kg.)" ,fg="#628e9d").grid(row=0, column=0, sticky="sw", padx=10)
Label(root, text="ส่วนสูง (Cm.)",fg="#628e9d").grid(row=1, column=0, sticky="sw", padx=10)


weight = Scale(root, from_=1, to=100, orient=HORIZONTAL, length=200, width=30 ,fg="#edfdff" , bg="#4a99b5")
weight.set(40)
weight.grid(row=0, column=1)
weight.bind('<B1-Motion>', Cal_bmi)
weight.bind('<Button-1>', Cal_bmi)
height = Scale(root, from_=1, to=200, orient=HORIZONTAL, length=200, width=30,fg="#edfdff" , bg="#4a99b5")
height.set(100)
height.bind('<B1-Motion>', Cal_bmi)
height.bind('<Button-1>', Cal_bmi)
height.grid(row=1, column=1)
lbl_bmi = Label(root, textvariable=tt_bmi,fg="White")
lbl_bmi.grid(row=3, columnspan=2, sticky="news")
data = Label(root,text = "")
data.grid(row=2, columnspan=2, sticky="news")
Button(root, text='เสร็จสิ้น', bg='#4a99b5', fg='#edfdff', width=5,command=SS).grid(row=4, column=1, sticky='SE')
root.mainloop()

