# 問題２
# 1.新規ファイルを作成　Ctrl＋N
# 2．保存してください　Ctrl＋ｓ
# 　場所：デスクトップ　
# 　filename：05-31-2-22xxx-youname.py

# ・変数aに数字を入力してください。「Enter Number:」
# ・変数ｂに数字を入力してください。「Enter Number:」
# ・変数aに、変数aを数字に変換した値を入れてください
# ・変数bに、変数bを数字に変換した値を入れてください
# ・もし（if）変数aと変数bが同じなら、
# 	・「同じ値です」と表示してください
# ・違うなら（else）
# 	・「異なる値です」と表示してください
# ・「プログラム終了」と表示して下さい。※同じでも違っても同じメッセージを出す
a = input ( "Enter Number:")
b= input( "Enter Number:")
a = int( a )
b = int( b)
if  a == b :
	print( "同じ", end="")
else:
	print( "異なる", end="")
print("値です。\nプログラム終了")

# 比較演算子　※比べるときに通記号
# 	==	等しい
# 	!=	等しくない
# 	>	より大きい
# 	<	より小さい
# 	>=	以上　≧
# 	<=	以下　≦


