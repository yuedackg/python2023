# filename: 11-30-1-22000-name.py
# matplotlibは通常モードで使えません。
# ターミナルを表示して、
# 「pip  install   matplotlib」を入力する必要があります。
import matplotlib 
# グラフを書くライブラリの短縮文字列はp
import matplotlib.pyplot as p

# tkinterを使ってグラフを描く
matplotlib.use( "tkagg")

# 表示を行うグラフを用意する
data = [1, 10, 2, 8, 3]

# グラフを内部の表示領域に描く
p.plot( data)

# タイトルの設定
p.title( "サンプルデータ")

# jiku label
p.xlabel( "yoko")
p.ylabel( "tate")

# 見えるようにする
p.show()