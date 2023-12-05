# filename : 09-28-1-22000-yourname.py
# GUIを作る
# 電卓の画面を作る

# GUIを作るには、tkinterを使用する。
                            # 短縮形tkを使用する 
import tkinter as tk
                            # 電卓に表示される値
current_number = 0 
                            # 最初の項目
first_term = 0
                            # 二つ目の項目
secound_term = 0 
                            # 計算結果
result = 0

                            
                            #   画面を作る
def key1():
    print( "hit 1")
def key2():
    print( "hit 2")

root = tk.Tk()              # Windowを作る
f = tk.Frame( root)         # フレームを作る
f.grid()                    # グリッドレイアウトにする
b1 = tk.Button( f, text='1', command=key1)
b2 = tk.Button( f, text='2', command=key2)

b1.grid(row=3, column=0)    # 3行目の0桁に表示する
b2.grid(row=3, column=1)

root.mainloop()             #　イベントをまつ
