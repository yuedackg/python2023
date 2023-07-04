# Ctrl＋N	新規ファイル
# Ctrl＋S	保存
# filename：06-21-3-22xxx-yourname.py
#  用意されたフォルダに保存

# 【問題３】
# 関数名：　PlusMinusN
# 引数：　base , sabun 
# 戻り値：　iPlus, iMinus     		->  return  ans1, ans2 
# 処理：
# 　１：　変数base＋変数sabun　を行い、変数iPlusに入れる
# 　２：　変数baseー変数sabun を行い、変数iMinusに入れる
# 　３：　戻り値として、変数iPlusと変数iMinusを返す
# ーーーーここから書く
def PlusMinusN( base, sabun):
	iPlus  = base + sabun
	iMinus = base - sabun
	return iPlus, iMinus

# ーーーーここまで書く
ret1 , ret2 = PlusMinusN( 10, 2)
print( "大きい数は", ret1)
print( "小さい数は", ret2)
