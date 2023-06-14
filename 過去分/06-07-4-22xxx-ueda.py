# 2,4,6,8,10,・・・12・・・,14の合計を計算しなさい　⇨56が正解
sum = 0
for i in range( 2, 15, 2):
	sum = sum + i
	print( "sum=", sum)
