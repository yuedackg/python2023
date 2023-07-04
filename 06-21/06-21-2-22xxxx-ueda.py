# Ctrl＋N	新規ファイル
# Ctrl＋S	保存
# filename：06-21-2-22xxx-yourname.py
#  用意されたフォルダに保存
#
# 関数名:myConcatenate
# 引数：sei, mei 
# 戻り値：ans
# 処理：
# 　①変数sei と変数meiの間に空白を入れて結合し、戻り値ansに入れる
#    ans = sei + ' ' + mei 
# 　②print()文を使用し、画面に戻り値ansの内容を表示する
# 　③戻り値として値を返す
# ――――ここから関数をつくる
def  myConcatenate( sei , mei ):
	ans = sei + ' ' + mei 
	print( ans)
	return ans
# ――――ここまで
ret = myConcatenate ( 'Ueda' , 'Yoshihiro')
print('戻り値：', ret )
