# Ctrl+N, Ctrl+s
# filename: 10-12-1-220000-yourname.py
# 【課題】
# ファイルの読み書きを行う
fout = open( "C://Users//admin//Desktop//22000.txt", "w", encoding="utf-8")    # ファイルを開く
# fout = open( "C://Users//22123//Desktop//22123.txt",)
fout.write( "hello vscode\n")                         # 文字を書く
fout.write( "My name is UEDA")                      # 文字を書く
fout.close()                                        # ファイルを閉じる
# ファイルがどこに出されるか？
#　→　下の画面でプロンプトに「PS C:\Users\admin>」と表示されてる
#   　dirコマンドで確認できる
