# filename: 06-15-4-22xxx-yourname.py
# 関数をつくる
# 関数名：　sumN
# 戻り値：sum
# sumN(5):1+2+...+5
# sumN(8):1+2+...+8

def sumN( hyusei):
	sum = 0
	for cnt in range(  hyusei + 1 ):
		sum = sum + cnt
	return sum	

print( "0,1,...10 の合計は、",sumN(10), "です")

print( "0,1,...14 の合計は、",sumN(14), "です")
print( "0,1,...15 の合計は、",sumN(15), "です")
