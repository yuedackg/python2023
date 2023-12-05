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
def key(n):
    global current_number
    current_number = current_number * 10 + n 
    show_number( current_number)
    
def show_number(num):           # 電卓の表示部分を書きかえる
    e.delete(0, tk.END)
    e.insert( 0, str( num))
    
def key1():
    print( "hit 1")
    key(1)
def key2():
    print( "hit 2")
    key(2)
def key3():
    key(3)
    print( "hit 3")
def key4():
    key(4)
    print( "hit 4")
def key5():
    key(5)
    print( "hit 5")
def key6():
    key(6)
    print( "hit 6")
def key7():
    key(7)
    print( "hit 7")
def key8():
    key(8)
    print( "hit 8")
def key9():
    key(9)
    print( "hit 9")
def key0():
    key(0)
    print( "hit 0")

def clear ():
    global current_number
    current_number=0            # 0にして
    show_number(current_number) # 再表示
    print( "hit clear")

# +ボタンが押された時は、現在表示されている値がメモリされ、
# その後に０が表示される（消されなくてもいいが、次に押した数になる
def plus():
    global current_number
    global first_term
    
    first_term = current_number # 数字をメモリーする
    current_number = 0          # 表示している数字を消す
    show_number(current_number)
    print( "hit plus")
    
def eq():
    print( "hit eq")
    global secound_term
    global result
    global current_number
    secound_term = current_number
    result = first_term + secound_term
    current_number = 0
    show_number(result)


root = tk.Tk()              # Windowを作る
root.geometry( "200x200")   # 画面のサイズ設定　
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
b0 = tk.Button( f, text='0', command=key0)
bc = tk.Button( f, text='C', command=clear)
bp = tk.Button( f, text='+', command=plus)
be = tk.Button( f, text='=', command=eq)

b1.grid(row=3, column=0)    # 3行目の0桁に表示する
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)    
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)    
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid( row=4, column=0)
bc.grid ( row=1,column=3)
be.grid( row=4,column=3)
bp.grid( row=2,column=3)

e = tk.Entry( f)
e.grid(row=0, column=0, columnspan=4)
clear()
root.mainloop()             #　イベントをまつ
