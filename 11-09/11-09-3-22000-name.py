# filename: 11-09-3-22000-name.py

# 一次元配列＝数字・文字列の並び
ary1 = [ 11, 12, 13 ]
ary2 = [ "Oct", "Nov", "Dec"]

print( ary1)
print( ary2)

# 二次元配列　
ary3 = [ [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]]
print( ary3)
print( ary3[1][1] )    # "5"を取り出す
print( ary3[0][0] )    # "1"を取り出す
print( ary3[1][2] )    # "6"を取り出す

ary4 = [ [ "A", "B", "C", "D"],
         [ "E", "F", "G", "H"],
         [ "I", "J", "K", "L"],
         [ "M", "N", "O", "P"],
         [ "Q", "R", "S", "T"],
         [ "U", "V", "W", "X"],
         [ "Y", "Z","",""],  ]

#自分の名前を出力してください
print( ary4[3][1])  # N
print( ary4[0][0])  # A
print( ary4[2][2])  # K
print( ary4[0][0])  # A
print( ary4[2][1])  # J
print( ary4[2][0])  # I
print( ary4[3][0])  # M 
print( ary4[0][0])  # A

# 2次元配列の高速化
# できないわけではないけれど、Pythonの2次元配列、3次元配列は遅い。

import numpy
hsary = numpy.array( ary4)

# もしくは、

import numpy as np
hsary2 = np.array( ary4)


