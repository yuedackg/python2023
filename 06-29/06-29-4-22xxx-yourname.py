# filename : 06-29-4-22xxx-yourname.py
# 多次元リスト
matrix = [  [1,2,3]  ,  [4,5,6]  ,  [7,8,9] ]
print( matrix)
print( matrix[0])
print(matrix[0][1])
# 問題　matrixの中の数字6を表示してください
print(matrix[1][2])
# 問題　matrixの中の数字7を表示してください
print(matrix[2][0])
# 問題　次の2次元リストを作ります
# 　　 [0] [1][2][3][4] 
# [0] 	1   2  3  4  5
# [1]	6   7  8  9 10
# [2]	11 12 13 14 15
l = list( range(1,6))
m = list( range(6,11))
n = list( range( 11,16))
o = [ l, m, n]
print( o)