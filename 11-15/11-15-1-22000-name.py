# filename: 11-15-1-22000-name.py
# 2次元配列などを便利に扱うnumpyパッケージを使えるようにする
# numpy を　npという名前で使えるようにする
# import numpy as np

# 絵を描くライブラリ
import sys
import tkinter as tk

root = tk.Tk()
root.geometry( "600x400")
canvas = tk.Canvas( root, bg="white")
# canvasの配置
canvas.pack( fill=tk.BOTH, expand=True)
# (50,50)-(100,100)-(50,100)の三角形を描く
canvas.create_line( 50, 50, 100, 100, fill="Orange", width=3)

#座標を2次元配列にする
point = [[50, 200],
         [100, 100],
         [50, 100]]
# 座標の配列を使って線を引く
canvas.create_line( point[1][0], point[1][1],  
                   point[2][0], point[2][1], fill="Blue", width=3 )
canvas.create_line( point[2][0], point[2][1], 
                    point[0][0], point[0][1], fill="Green", width=3)
# 16行目の命令を、2次元配列pointを使って書き直す。色はRed
canvas.create_line( point[0][0], point[0][1],
                   point[1][0],point[1][1], fill="Red", width=3  )

root.mainloop()
