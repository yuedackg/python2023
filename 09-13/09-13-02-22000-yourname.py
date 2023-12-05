# filename: 09-13-02-22000-yourname.py
#ライブラリの読み込み
from turtle import *

N = input( "正N角形のNを入力してください：")

# 角度を求める
kakudo = 180 * (int(N)-2)/ int(N)
print( kakudo)

# ペンを上げる(線を書かない)
penup()

# 90度左に回転する（＝上方向）
left(90)
forward(150)

# ペンを下す（書き始め）
pendown()
for i in range( int(N) ):
    # 1本目 1辺の長さは200
    left( 180- kakudo )
    forward( 20)
done()