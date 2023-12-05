# filename: 11-29-1-22000-name.py
# 課題
# 四角形（１０，１０）ー（１００，１００）を描く
# 任意の角度回転させる
# 座標の配列を作る
# (10,10), (10,100), (100,100), (100,10)
point = [[ 100, 100],
         [ 100, 150],
         [ 150, 150],
         [ 150, 100]]
# ライブラリを使えるようにする
import sys
import tkinter as tk
# 四角形を描く
root = tk.Tk()
root.geometry( "600x400")
canvas = tk.Canvas( root, bg="white")
canvas.pack( fill=tk.BOTH, expand=True)
for x in range(4):
    canvas.create_line( point[x][0],
                        point[x][1],
                        point[(x+1)%4][0],
                        point[(x+1)%4][1], fill="Red", width=3)
kakudo = input( "回転?")
import math
# 文字列kakudoを数字に直す
kakudo = float( kakudo )
# CGの単位に変換[deg] -> [rad]
rad = 2.0 * math.pi / 360.0 * kakudo
print( rad)
# 11-16-2-22000-name.pyと同じもの
mat = [ [ math.cos(kakudo), - math.sin( kakudo)],
        [ math.sin( kakudo), math.cos( kakudo)]]
# パッケージを使う
import numpy as np
# 変換 （2次元配列の計算を行得るように変換）
point2 = np.array( point)
mat2 = np.array( mat)
ans = np.dot( mat2, point2.T)
print( ans)
root.mainloop()


