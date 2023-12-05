point = [[ 100, 100],
         [ 100,150],
         [150,150],
         [150, 100],
         ]
# ライブラリを使えるようにする
import sys
import tkinter as tk
# 四角形を描く
root = tk.Tk()
root.geometry( "600x400")
canvas = tk.Canvas( root, bg="white")
canvas.pack( fill=tk.BOTH, expand=True)
for x in range(len(point)):
    print(point[x][0], point[x][1],
                    point[(x+1) % 4 ][0],point[(x+1) % 4 ][1])
    canvas.create_line( point[x][0], point[x][1],
                    point[(x+1) % 4 ][0],point[(x+1) % 4 ][1], fill="Red", width=3  )
kakudo = input( "回転?")
import math
# 文字列kakudoを数字に直す
kakudo = float( kakudo )
# CGの単位に変換[deg] -> [rad]
rad = 2.0 * math.pi / 360.0 * kakudo
print( rad) 
mat = [ [ math.cos(kakudo), - math.sin( kakudo)],
        [ math.sin( kakudo), math.cos( kakudo)]]
print( mat)     
import numpy as np
mat2 = np.array(mat)
point2 = np.array( point)
point4 = np.dot( mat2, point2.T).T

# point3 = point2.T
# point4 = np.dot( mat2, point3).T
# print( point4)
for x in range(len(point4)):
    canvas.create_line( point4[x][0],
                        point4[x][1],
                        point4[(x+1) % 4 ][0],
                        point4[(x+1) % 4 ][1], 
                        fill="Blue", width=3  )
root.mainloop()
