# filename: 07-26-1-22xxx-yourname.py
# デフォルト引数
def printName( strName):
    print( "私の名前は", strName, "です。")

printName( "西村")

# 上記の例では、必ず引数を書く必要がある
# （書かないと、エラー）
# printName() はエラー
# デフォルト引数は、引数を書かないときに、指定される値を決めること
# def  関数名（ 変数名＝値, ...):
#     処理

# printName2()と書いたときに、「私の名前は樋口です」のように、
# 省略されたら「樋口」を使う
def printName2( strName = "樋口"):
    print( "私の名前は", strName, "です。")

printName2()
printName2( "植田")