import tkinter as tk

def say_hello():
    print("Привет!")

root = tk.Tk()
root.title("Кнопка")

btn = tk.Button(root, text="Привет", command=say_hello)
btn.pack(padx=20, pady=20)

root.mainloop()
