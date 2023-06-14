# New file :	Ctrl+N
# Save 	:	Ctrl+S
# filename : 	06-07-1-22xxx-yourname.py  
# 				（保存場所：デスクトップ）
# 				（ファイルの種類：Python）

# 課題１
# 　繰返し（loop）を学ぶ　　⇨　回数が決まっている：for
						# 回数が決まっていないとき：while

for i in range( 5) :
	print ( "iの値は：", i )
	
for u in range( 6):
	print( "uの値は：",u)

for k in range( 2, 6 ):
	print( "kの値は：", k)

# j を　７から１３まで出してください
# jの値は：　7
# jの値は：　8
# jの値は：　9
#　　...
# jの値は：　13
for j in range( 7,14 ):
	print( "jの値は：",j)

for m in range( 3, 10, 3):
	print( "mの値は：", m)


# 次のように表示するプログラムを作りなさい
# nの値は：5
# nの値は：10
# nの値は：15
# nの値は：20　　　　　⇨最初の値：5　終わりの値は20、　増える値は５
for n in range( 5, 21, 5):
	print( "nの値は：", n)
