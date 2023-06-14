# Ctrl + N   [File] -> [New Text File]  新規にファイルを作成する
# Ctrl + s   [File] -> [Save]　　　　　　　　　名前を付けて保存する
# filename : 0531-1-22xxxx-ueda.py　　　　場所、名前、ファイルの種類
# 問題
# 　　・「画面に数字を入れて下さい」と表示し、入力された数を変数ataiに格納する　　input()
# 　　・変数ataiの内容（文字列）を数字に変換してください。変換した値を変数ataiに入れる　int()
# 　　・ifで、変数ataiの内容が10より大きければ、　　　　if
# 　　　「10より大きい」と表示する　　　　　　　　　　　　　　　print()
# 　　・そうでなければ　　　　						else:　　　　　　　　　　　　　　　　　　
# 　　　「10以下です」と表示
atai = input( "画面に数字を入れてください")
atai = int( atai)
if atai > 10 :
	print( "10より大きい")
else:
	print( "10以下")
	print( "プログラム終了")

# 出来た人
# 10の時はどのような結果
# 11の時はどのような結果になりますか
