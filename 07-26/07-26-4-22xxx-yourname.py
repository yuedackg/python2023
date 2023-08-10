# filename: 07-26-4-22xxx-yourname.py
import math

def kai( a, b, c):
    bunbo = 2 * a
    D=b * b - 4 * a * c
    
    x1 = - b + math.sqrt( D)
    x2 = - b - math.sqrt( D)
    
    print( "x1 = ", x1, "; x2 = ", x2)

#　2次方程式の解
kai ( 1, 5, 6)
kai ( b=5, c=6, a = 1)
