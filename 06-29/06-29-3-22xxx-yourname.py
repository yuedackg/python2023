# filename: 06-29-3-22xxx-yourname.py
# 番号のリストをつくる
mylist = list( range( 10))
print( mylist)
# 数字Nを指定したら、０，１，２，・・・・、N-1までの並びをつくる
# range( N )  ・・・　０からN-1まで
# range( S, N)・・・　SからN-1まで
m = list( range( 3, 8))
print(m)
# range( S, N, STEP)・・・S,S+STEP,・・・＜N
# 次の数字を表示しなさい 11, 14, 17, 20, ...41
n = list( range( 11, 42, 3))
print(n)