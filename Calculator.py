from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")

# Логика Калькулятора
def calc(key):
  global memory
  if key == "=":
    # исключаем написание букв
    str1 = "-+123456789.*/"
    if calc_entry.get () [0] not in str1:
      calc_entry.insert(END, "Первый символ не число!")
      messagebox.showerror("Ошибка!", "Вы ввели не число!")
      
    # счет
    try:
      result = eval(calc_entry.get())
      calc_entry.insert(END, "=" + str(result))
    except:
      calc_entry.insert(END, "Ошибка!")
      messagebox.showerror("Ошибка!", "Проверь правильность данных")
      
    # Очистить поле
  elif key == "c":
    calc_entry.delete(0, END)
# Создаем все кнопки
bttn_list = [
  "7", "8", "9", "+", "-",
  "4", "5", "6", "*", "/",
  "1", "2", "3", "-/+", "=",
  "0", ".", "c", "", ""
]
r = 1
c = 0

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)

for i in bttn_list:
  rel = ""
  # cmd=lambda x=i:_#calc(x) 
  ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
  c += 1
  if c>4:
    c=0
    r += 1
    
root.mainloop()