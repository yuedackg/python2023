# Ctrl+N
# Ctrl+S
# filename : 06-15-2-22xxx-yourname.py

# 関数をつくる
# 準備
# 	関数名　Nijou
# 	引数　　　x
# 	戻り値  ans
#   c = Nijou(2)  ; cが４	（２ｘ２）
#   c = Nijou(3)  ; cが９　　（３ｘ３）

# def  kansu-mei (  hikisu):
# 	meirei
# 	meirei
# 	return  modori-ti

# 関数の定義(用意)
def Nijou( x ):
	ans = x * x
	return ans

# 関数使う
c = Nijou(10)
print(c)

# 三乗を計算する関数を定義してください
# 関数名：Sanjo
def Sanjo( x):
	ans = x*x*x
	return ans
# 関数を使います。
d = Sanjo( 4)
print( d)    # 64 (4x4x4)の結果
e = Sanjo( 11)
print( e)
