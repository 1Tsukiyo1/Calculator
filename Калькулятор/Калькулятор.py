import tkinter as tk
from tkinter import ttk, messagebox
import math

def calculate():
    try:
        a = float(entry_a.get())
        op = operator_var.get()

        match op:
            case '+':
                b = float(entry_b.get())
                result = a + b
            case '-':
                b = float(entry_b.get())
                result = a - b
            case '*':
                b = float(entry_b.get())
                result = a * b
            case '/':
                b = float(entry_b.get())
                if b == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль!")
                    return
                result = a / b
            case 'sin':
                result = math.sin(math.radians(a))
            case 'cos':
                result = math.cos(math.radians(a))
            case 'tan':
                if (a % 180) == 90:
                    messagebox.showerror("Ошибка", "Тангенс не определён для этого угла!")
                    return
                result = math.tan(math.radians(a))
            case 'cot':
                tan_val = math.tan(math.radians(a))
                if tan_val == 0:
                    messagebox.showerror("Ошибка", "Котангенс не определён для этого угла!")
                    return
                result = 1 / tan_val
            case '√':
                if a < 0:
                    messagebox.showerror("Ошибка", "Корень из отрицательного числа не определён!")
                    return
                result = math.sqrt(a)
            case _:
                messagebox.showerror("Ошибка", "Неизвестный оператор")
                return

        label_result.config(text=f"Результат: {result:.6f}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

root = tk.Tk()
root.title("Калькулятор (match-case)")
root.geometry("300x280")

tk.Label(root, text="Число/Угол (для тригонометрии):").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Второе число (для +, -, *, /):").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Операция:").pack(pady=5)
operator_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/', 'sin', 'cos', 'tan', 'cot', '√']
tk.OptionMenu(root, operator_var, *operations).pack()

tk.Button(root, text="Вычислить", command=calculate).pack(pady=10)
label_result = tk.Label(root, text="", fg="blue")
label_result.pack(pady=5)

root.mainloop() 







