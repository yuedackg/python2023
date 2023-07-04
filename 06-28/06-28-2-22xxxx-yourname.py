# filename : 06-28-2-22xxx-yourname.py
# 問題１のリストabcをコピーする
abc = [ "suzuki", "sasaki", "ueda", "ohishi", "harada"]

# 問題３
# リストの要素をすべて表示しなさい　for文
# 変数itemの文字は使わない事（変数名を書き換えて作ること）
for item in abc:
	print( item)

# 注意　for文は　取り出す変数名とリスト名を書く
# リストの中から、一つずつ取り出して、変数の中に格納し繰返しを行う

# 問題４　whileを使ったリストの表示
# whileで取り出す場合には、要素指定が必要
# 0,1,2,3...4＜　５　←この数字を出すときにlen()
lp = 0
while lp < len(abc):
	print( abc[lp])
	lp = lp + 1
print( "Q4 end.")

# 問題５　奇数番目（1,3,5・・・）の要素だけを表示
lpodd = 1
while lpodd < len(abc):
	print( abc[lpodd])
	lpodd = lpodd + 2
	# lpodd += 2
print( "Q5 end.")


