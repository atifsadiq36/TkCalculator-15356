import tkinter as tk
from tkinter import messagebox


def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_var.set(f"Result: {result}")
    except ValueError:
        show_error()

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_var.set(f"Result: {result}")
    except ValueError:
        show_error()

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_var.set(f"Result: {result}")
    except ValueError:
        show_error()

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        result = float(entry1.get()) / num2
        result_var.set(f"Result: {result}")
    except ValueError:
        show_error()

def show_error():
    messagebox.showerror("Input Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.resizable(False, False)

# --- Input Fields ---

tk.Label(root, text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()


frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=add).grid(row=0, column=0, padx=5)
tk.Button(frame, text="-", width=5, command=subtract).grid(row=0, column=1, padx=5)
tk.Button(frame, text="*", width=5, command=multiply).grid(row=0, column=2, padx=5)
tk.Button(frame, text="/", width=5, command=divide).grid(row=0, column=3, padx=5)


result_var = tk.StringVar()
result_var.set("Result: ")

tk.Label(root, textvariable=result_var, font=("Arial", 12)).pack(pady=20)


root.mainloop()