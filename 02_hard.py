import tkinter as tk

root = tk.Tk()
root.title("Рисование")

canvas = tk.Canvas(root, width=1280, height=720, bg="white")
canvas.pack()

def draw(event):
    r = 4
    canvas.create_rectangle(event.x, event.y, event.x+r, event.y+r, fill="black", outline="")

canvas.bind("<B1-Motion>", draw)

root.mainloop()
