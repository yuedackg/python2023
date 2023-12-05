#filename: 10-18-1-22000-name.py
# 課題：
# 　プログラムを実行時に、フォルダに格納されている
# 「10-18-1-22000-name.py」を読み込み、コンソールに出力する。

folder = "c://users//admin//Desktop//python2023//10-19"
filename = "10-18-1-22000-name.py"
path = folder + "//" + filename             # ファイルのパスを作る
myfile = open( path, "r", encoding="utf-8") # ファイルを開く
print( myfile.read())                       # ファイルを開いて、表示
myfile.close()                              # ファイルを閉じる

# 課題２：　        Hint：write()を使います
#  このプログラムの内容をファイル「output2.txt」に書き出してください
# 課題３：
# このプログラムの内容をファイル「output3.txt」に3回書き出して下さい。