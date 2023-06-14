# Ctrl + N
# Ctrl + S
# filename : 06-08-3-22xxx-youruname.py

# 値を並べて、[]で囲ったものをリストという
# for分のinの後ろにはリストを書くことが出来る
# range()を使わない書き方
for item in ["hello", "world"]:
	print( item  )

#問題： 2,3,5,7,11,13,17,19,23,29 をrange()でかけますか？
# 不規則な数字を使う時は、リストを使用する
for item in [2,3,5,7,11,13,17,19,23,29 ]:
	print( item)

# for分をコンパクトにするために、[]を一旦別の名前を付けることもある
mylist = [48, "nakashima", 89, "inoue"]
for item in mylist:
	print( item)
#