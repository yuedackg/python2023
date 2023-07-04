# Ctrl＋N	新規ファイル
# Ctrl＋S	保存
# filename：06-21-1-22xxx-yourname.py
#  用意されたフォルダに保存

# 【復習】
# 関数名：printName
# 引数：xxxx
# 戻り値：strMessage
# 処理：
# 　①引数xxxxの前に文字列「私の名前は」を付け、後ろに「です」を付けた文字列をつくり変数strMessageに格納する
# 　②変数strMessageを表示する
# 　③文字列を呼び出し側に返す（戻り値）

# 呼び出し側では、関数printName()をパラメータ'ueda'を付けて呼び出す
# 戻り値を次のprint（）で表示する

def  printName( xxxx ):
	strMessage = '私の名前は' + xxxx + "です"
	print( strMessage)
	return strMessage

ret = printName( 'ueda')
print( "戻り値：" + ret)


