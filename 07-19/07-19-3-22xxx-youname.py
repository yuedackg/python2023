# 数字の集合を作る
# 例）
# 　3の倍数の集合
# 　5の倍数の集合　⇒等間隔で用意される数字
#  　　　　　　　　　等差数列
# 【書き方】
# 集合名 = { 値 for i in range(N) }  <- i: 0, 1,2,3,...,N-1
baisu3 = { 3*i for i in range( 5)} 
#        i:0  1  2  3  4
#          0  3  6  9 12
print( baisu3)

# 例２  集合{ 3, 6, 9, 12, 15}を作る。
baisu3= { 3*i for i in range( 1, 6)}
print( baisu3)
baisu3= { i for i in range( 3, 16, 3)}
print( baisu3)
