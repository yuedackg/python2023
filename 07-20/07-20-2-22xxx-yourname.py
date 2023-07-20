# filename: 07-20-2-22xxx-yourname.py
# 2から100までの素数を求める

s = { i for i in range( 2, 101)}
print( s)

for lp in range ( 2, 101):
    # print( lp)
    # lpの倍数の集合を作る
    M = { k for k in range( 2*lp, 101, lp )}
    s = s - M
print( s)

# 2から10000までの素数を求めて下さい　（4分）
s = { i for i in range( 2, 10001)}
print( s)

for lp in range ( 2, 10001):
    M = { k for k in range( 2*lp, 10001, lp )}
    s = s - M
print( s)