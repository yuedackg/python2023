# 文字列を入力して、変数ｘに格納
x = input( "Enter String:")

# ファイルをオープンする　「gorira」はファイル名に対するエイリアス
gorira = open( "210xx-2023-01-31.txt", "w")

# ファイルに書き込む
print( x, file=gorira)
# 注意
# 　file=は出力先をfileで示される場所に変更する
 
# ファイルを閉じる
gorira.close()















