# filename: 11-15-2-22000-name.py
# import numpy as np

import sys
import tkinter as tk
root = tk.Tk()
root.geometry( "600x400")
canvas = tk.Canvas( root, bg="white")
canvas.pack( fill=tk.BOTH, expand=True)

point = [[500, 200],
         [100, 300],
         [50, 100]]
for x in range(3):
    canvas.create_line( point[x][0], point[x][1],
                    point[(x+1) % 3 ][0],point[(x+1) % 3 ][1], fill="Red", width=3  )
    
# 図形の回転　角度Θ
# アフィン変換をすることで、回転が行える。
# ①座標を2次元配列にする
# ②アフィン変換の2次元配列を作る
# ③2次元配列の掛け算（Numpy）
root.mainloop()
