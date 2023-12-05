#filename: 10-18-2-22000-name.py 
# 課題３：
# このプログラムの内容をファイル「output3.txt」に3回書き出して下さい。

folder = "c://users//admin//Desktop//python2023//10-18"
filename = "10-18-1-22000-name.py"
path = folder + "//" + filename             # ファイルのパスを作る
myfile = open( path, "r", encoding="utf-8") # ファイルを開く
path = folder + "//" + "output3.txt"        # 書き出しファイル
myoutput = open( path, "a", encoding="utf-8" ) # 書き出しで開く
buff = myfile.read()
myoutput.write( buff )
myoutput.write( buff )
myoutput.write( buff )

myfile.close()                              # ファイルを閉じる
myoutput.close()

