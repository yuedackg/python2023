#filename: 10-18-2-22000-name.py
# 事前準備：
# Ctrl+a：　全選択
# Ctrl+c：　コピー
# Ctrl+N：　新規作成
# Ctrl+v：　貼り付け
# Ctrl＋S： 保存
# 課題２：
# 　プログラムを実行時に、フォルダに格納されている
# 「10-18-1-22000-name.py」を読み込み、ファイル「output2.txt」に
# 書き込む
# 読み込むファイル→myfile
# 書き込むファイル→myOutput

folder = "c://users//admin//Desktop//python2023//10-18"
filename = "10-18-1-22000-name.py"
path = folder + "//" + filename             # ファイルのパスを作る
myfile = open( path, "r", encoding="utf-8") # ファイルを開く
path = folder + "//" + "output2.txt"        # 書き出しファイル
myoutput = open( path, "w", encoding="utf-8" ) # 書き出しで開く
# print( myfile.read())                       # ファイルを開いて、表示
myoutput.write( myfile.read())
myfile.close()                              # ファイルを閉じる
myoutput.close()

