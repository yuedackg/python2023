# filename: 09-27-2-22000-yourname.py
# Ctrl＋N　（新規作成）
# CTRL＋S　（保存）
# filename: 09-27-1-22000-yourname.py
# 【課題2】
# マウスをクリックした場所まで、
# 線を引クプログラムに修正しなさい

from turtle import *
# （ｘ、ｙ）はクリックした場所
# （ｘｘ、ｙｙ）は最後に引いた線の終点
# newxyが現在線を引こうとしているところ
def come( x, y):
    (xx, yy) = pos()
    # newxy = ( (xx+x)/2 , (yy+y)/2 )
    newxy = ( x, y)
    print( x,y)
    goto ( newxy)

onscreenclick(come)
done()
