# 1. CTRL+N　新規にファイルを作って
# 2. CTRL+S　保存
# filename: 09-06-01-22000-yourname.py
# 文字列の長さを知る
# 文字列の位置を探す
# 文字列の分解はsplit()メソッドを使用する

# 文字列を入力し、変数retに受け取る
ret = input( "Enter:")
print( "Enter string:" , ret )

# 文字列「,」　の場所を探す
# 文字の場所を探すときはindex()を使う
# 文字列.index( 探す文字)　の形で記述する
print( "index:", ret.index(","))

# 文字列を切り出す
# 部分的に文字列を取りだす方法
# 文字列[開始：長さ]
# 入力された文字列の中の「,」より左側を取り出し、変数retlに格納する
key = ret.index(",")
        # 文字列の0番目からkey-1番目
print( ret[0:key])

# 入力された文字列の中の「,」より右側を取り出し、変数retrに格納する
key = ret.index(",")
nagasa = len( ret)
print( ret[key+1:nagasa])
