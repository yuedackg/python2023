A = input( "A:")
print( "A:" , A)

B = input( "B:")
C = input( "C:")
#文字列を数字に変換する
A = int( A)
B = int( B)
C = int( C)
import math

Z = B * B
Y = - B
X = 4 * A * C
W = 2 * A
V = math.sqrt( Z - X )
X1 = ( Y + V ) / W
X2 = ( Y - V ) / W

print( "X1=", X1, ", X2=", X2)

