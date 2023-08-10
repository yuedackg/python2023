# filename : 07-26-22xxx-yourname.py
# program は　-1-からコピーして使う
# 関数の定義　複雑な部分を1つの命令に纏める
def isCheck():
    # 名前を入力して、集合にあるかないかを判断する
    inputName = input( "Your Name:")
    # 名前inputNameが集合listaに存在するか判断する
    if inputName in lista :
        print( "include")
    else:
        print( "not include")
# 関数はここまで

lista = set()
strKey = input( "Enter Name:")
while strKey != "end":
    lista.add( strKey)
    strKey=input( "Enter Name:")
print( lista)

# 関数を使う
isCheck()

