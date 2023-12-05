# filename: 09-27-1-22000-yourname.py

from turtle import *

# ｂが押された時の処理
def changeBlue():
    print( "press b")

# →が押された時の処理
def changeRight():
    print( "Right key press")

# イベント処理の登録
onkey( changeBlue, "b")
onkeypress( changeRight, "Right")

# イベントを読む
listen()
done()
