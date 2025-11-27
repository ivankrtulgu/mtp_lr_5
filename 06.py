import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Прогрессбар")

pb = ttk.Progressbar(root, length=300, mode="determinate")
pb.pack(pady=20)

def run():
    pb["value"] = 0
    for i in range(101):
        pb["value"] = i
        root.update()
        time.sleep(0.01)

btn = tk.Button(root, text="Старт", command=run)
btn.pack()

root.mainloop()
