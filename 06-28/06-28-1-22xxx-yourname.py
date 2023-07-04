# Ctrl+N 	新規ファイルの作成
# Ctrl+S	保存
#  filenmae: 06-28-1-22xxx-yourname.py

# 問題１
# 　リストabcを作成しなさい
# 	abc[0]	"suzuki"
# 	abc[1]	"sasaki"
# 	abc[2]	"ueda"
# 	abc[3]	"ohishi"
# 	abc[4]	"harada"

abc = [ "suzuki", "sasaki", "ueda", "ohishi", "harada"]
print(  abc)
# 0番目の要素を表示したい
print( abc[0])

# ※注意
# リストは、値（文字列）を並べて書く（左辺）
# リストの名前は左辺、リストの要素は右辺

# 問題２　
# リストabcの要素数を表示してください
kosu = len( abc)
print( "個数：", kosu)

# ーーー まとめて書くと下のようになる
print( "個数：",len(abc))
# ※注意
# 個数は
# 　len(リストの名前)
# 要素の個数が得られる
