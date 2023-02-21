import random 
import tkinter as tk
root = tk.Tk()
root.title("Тест")
root.geometry("400x400")

def create_rectangle():
    canvas.delete("all")
    canvas.create_rectangle(random.randint(0,400),random.randint(0,250),random.randint(0,400),random.randint(0,250),
    fill = "red",)
def create_oval():   
    canvas.delete("all")
    canvas.create_oval(random.randint(0,400),random.randint(0,250),random.randint(0,400),random.randint(0,250),
    fill = "yellow",)
def create_polygon():
    canvas.delete("all")
    canvas.create_polygon(random.randint(0,400),random.randint(0,250),random.randint(0,400),random.randint(0,250),random.randint(0,400),random.randint(0,250))
    fill = "blue" #хотел чтобы треугольник был синим, но он все равно черный:)
button = tk.Button(
text = "rect",
width = 7,
height = 3,
bg = "white",
fg = "black",
command = create_rectangle
)
button_oval = tk.Button(
text = "oval",
width = 7,
height = 3,
bg = "white",
fg = "black",
command = create_oval
)
button_polygon = tk.Button(
text = "poly",
width = 7,
height = 3,
bg = "white",
fg = "black",
command = create_polygon
)
canvas = tk.Canvas(
width=400,
height=250,
)

button_oval.pack()
canvas.pack()
button.pack(side="bottom")
button_polygon.pack()
root.mainloop()
root.resizable(False)