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
def key3():
    print( "hit 3")
def key4():
    print( "hit 4")
def key5():
    print( "hit 5")
def key6():
    print( "hit 6")
def key7():
    print( "hit 7")
def key8():
    print( "hit 8")
def key9():
    print( "hit 9")
    
root = tk.Tk()              # Windowを作る
f = tk.Frame( root)         # フレームを作る
f.grid()                    # グリッドレイアウトにする
b1 = tk.Button( f, text='1', command=key1)
b2 = tk.Button( f, text='2', command=key2)
b3 = tk.Button( f, text='3', command=key3)
b4 = tk.Button( f, text='4', command=key4)
b5 = tk.Button( f, text='5', command=key5)
b6 = tk.Button( f, text='6', command=key6)
b7 = tk.Button( f, text='7', command=key7)
b8 = tk.Button( f, text='8', command=key8)
b9 = tk.Button( f, text='9', command=key9)

b1.grid(row=3, column=0)    # 3行目の0桁に表示する
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)    
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)    
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

root.mainloop()             #　イベントをまつ
