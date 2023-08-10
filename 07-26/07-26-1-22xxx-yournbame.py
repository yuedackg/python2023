# filename : 07-26-1-22xxx-yourname.py
# 【演習】
# 入力された文字をリストに格納する
# 最後に「end」の文字が入力されたら、リストの追加を終了し、リスト全体を表示する
# 1.からの集合を作る
# 2．文字を入力する
# 3．endの文字が入るまで繰り返す＝endが入らなければ、続ける
# ４．集合に追加
# ５．集合の内容を出力する
# listname = set()
# keyword = input( "Enter name:") 
# while keyword != "end" :
#     listname.add( keyword)
#     keyword = input( "Enter name:") 
# print( listname )
# ---ここから下は完成品
lista = set()
strKey = input( "Enter Name:")
while strKey != "end":
    lista.add( strKey)
    strKey=input( "Enter Name:")
print( lista)

# 名前を入力して、集合にあるかないかを判断する
inputName = input( "Your Name:")

# 名前inputNameが集合listaに存在するか判断する
if inputName in lista :
    
    print( "include")
else:
    print( "not include")
    