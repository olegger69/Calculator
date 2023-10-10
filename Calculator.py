from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")
# Создаем все кнопки
bttn_list = [
  "7", "8", "9", "+", "-",
  "4", "5", "6", "*", "/",
  "1", "2", "3", "-/+", "=",
  "0", ".", "c", "", ""
]
r = 1
c = 0

for i in bttn_list:
  rel = ""
  # cmd=lambda x=i:_#calc(x) 
  ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
  c += 1
  if c>4:
    c=0
    r += 1
    
root.mainloop()