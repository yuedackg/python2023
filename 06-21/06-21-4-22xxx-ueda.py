# Ctrl＋N	新規ファイル
# Ctrl＋S	保存
# filename：06-21-4-22xxx-yourname.py
#  用意されたフォルダに保存

# return 文の個数が決まらない
# 　⇨リスト（数字の塊）で数字を返す

def amari ( v ):
	while( v > 0):
		m = v % 2
		print( v, m)
		v = v // 2

amari( 5)

