# filename: 09-14-01-22000-yourname.py
from turtle import *

# Turtle Graphics の様々な関数
# 1.最初の位置を知る
x,y = pos()
d=heading()
print( "x=", x, "y=", y, "d=", d )

forward(100)
x,y = pos()
print( "x=", x, "y=", y)

left(90)
x,y = pos()
print( "x=", x, "y=", y)

forward(100)
x,y = pos()
print( "x=", x, "y=", y)

done()
