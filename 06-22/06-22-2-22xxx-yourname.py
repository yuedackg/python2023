# 値を複数個格納できる特殊な変数がある
# ・リスト　※ここから
# ・タプル
# ・辞書
# ・集合

# リストは、値を入れる変数をいくつか並べたもの
# 名前はすべて同じ

# 例）空のリスト
lName = []
print( lName)

# 例）1,2,3,4が格納されている
lValue = [ 1, 2, 3, 4]
print(lValue)

# 複数の値を一つの変数で扱うことが出来る

# 例）変数lValueの3を取り出したい
print( lValue[2])

# Pythonは０から数え始める
	# BASICは１，２，３，・・・
	# C、Javaは０，１，２，・・・

# リストに格納するのは同じタイプの値だが
# 混在することもできる
arr = [ 22000, "Y.UEDA", 169.5]
print( "学籍番号：", arr[0])
print( "名　　　前：", arr[1])
print( "身　　　長：", arr[2])
