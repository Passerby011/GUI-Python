# GUI-calculator.py

from tkinter import *
from tkinter import ttk, messagebox



GUI = Tk() #ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณราคาปลา')
GUI.geometry('700x600')

bg = PhotoImage(file = "icons8-doge.png")
# bg = PhotoImage(file= r'C:\Users\Uncle Engineer\Desktop\Basic Python\car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา(กิโลกรัม)',font=(None,15))
L.pack(pady=30)

v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack(ipadx= 10,)
L = Label(GUI,text='กรุณากรอกราคา(กิโลกรัมล่ะ)',font=(None,15))
L.pack(pady=15)
v_quantity2 = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E2 = ttk.Entry(GUI, textvariable=v_quantity2, font=(None,20))
E2.pack(ipadx= 10,pady=5)

def Cal():
        try:
            quan = float(v_quantity.get())
            NNN = float(v_quantity2.get())
            calc = quan * NNN  # 39 บาทต่อกิโล * จำนวนปลาที่กรอกมา
            messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc) )
            v_quantity.set('')
            E1.focus()
          

            
        except:
            messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น'.format(calc) )
            v_quantity2.set('')
            E2.focus()
        
B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=40,ipady=20,pady=20) #ipadx ขยายความกว้าง x/y


GUI.mainloop()