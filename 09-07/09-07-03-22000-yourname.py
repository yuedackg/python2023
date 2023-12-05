# 辺の長さが300の正六角形を作成してください
from turtle import *

left(90)
forward(300)
left(120)
for i in range( 6):
    forward(300)
    left( 60)

i=0
while i<6 :
    forward(300)
    left( 60)
    i = i+ 1

done()

# 同じことが繰り返される部分をforを使って書き直しなさい

