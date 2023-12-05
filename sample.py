import sys
import tkinter as tk

root = tk.Tk()
root.geometry( "600x400")
canvas = tk.Canvas(root, bg = "gray")
canvas.pack(fill = tk.BOTH, expand = True)

point = [
    [10, 10],
    [200, 200],
    [10, 200]
]
canvas.create_line( point[0][0], point[0][1], point[1][0], point[1][1], fill = "Blue", width = 5)
canvas.create_line( point[1][0], point[1][1], point[2][0], point[2][1], fill = "Blue", width = 5)
canvas.create_line( point[2][0], point[2][1], point[0][0], point[0][1], fill = "Blue", width = 5)

root.mainloop()

