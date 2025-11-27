import tkinter as tk
import random

root = tk.Tk()
root.title("Цветная панель")

frame = tk.Frame(root, width=200, height=150, bg="gray")
frame.pack(pady=20)

def change_color():
    color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    frame.config(bg=color)

btn = tk.Button(root, text="Сменить цвет", command=change_color)
btn.pack()

root.mainloop()
