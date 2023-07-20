# XOR 排他的論理和
# 片側にしか含まれないもの
# 集合Aと集合Bであらわすと、A^B
s = { 1, 2, 3, 4}
b = { 4, 5, 6, 7}
print( "or:",   s | b)
print( "and:",  s & b)
print( "xor",   s ^ b)

# 部分集合
# 全部が含まれていればTrue、含まれていなければFalse
b = { 1, 2, 3, 4, 5 }
print( s.issubset( b ))

# 互いに素（共通ではない）
s = { 1,2 }
b = { 3, 4}
print( s.isdisjoint( b))
