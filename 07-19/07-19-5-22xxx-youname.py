# 100以下の2の倍数の集合
baisu2 = { i for i in range( 2, 101, 2)}
# 100以下の3の倍数の集合
baisu3 = { i for i in range( 3, 101, 3)}
# 100以下の1から100までの集合
zentai = { i for i in range( 1, 101, 1)}

print( "zentai:", zentai)

zentai = zentai - baisu2
print( "zentai:", zentai)

zentai = zentai - baisu3
print( "zentai:", zentai)

# ２＊Nから始まるNの倍数を集合から引く　Ｎ：2,3,...,99
# -> 素数集まり
