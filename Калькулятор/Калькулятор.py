import tkinter as tk
from tkinter import ttk, messagebox
from tokenize import Double

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operator_var.get()

        match op:
            case '+':
                result = a + b
            case '-':
                result = a - b
            case '*':
                result = a * b
            case '/':
                if b == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль!")
                    return
                result = a / b
            case _:
                messagebox.showerror("Ошибка", "Неизвестный оператор")
                return

        label_result.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")

root = tk.Tk()
root.title("Калькулятор (match-case)")
root.geometry("300x250")


tk.Label(root, text="Первое число:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Второе число:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Операция:").pack(pady=5)
operator_var = tk.StringVar(value='+')
tk.OptionMenu(root, operator_var, '+', '-', '*', '/').pack()

tk.Button(root, text="Вычислить", command=calculate).pack(pady=10)
label_result = tk.Label(root, text="", fg="blue")
label_result.pack(pady=5)

root.mainloop() 







