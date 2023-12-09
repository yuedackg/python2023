# 数字を入力し、その数字の平方根を計算する
# 例）√４　⇒ ２
#     √９　⇒　３

myValue=input("enter value:")
print(float(myValue)+1 )

#ルートの計算
#    # 数学系の関数を使用するときは、
#    # mathモジュールをインポート
import math
myAnswer = math.sqrt( float( myValue))
print( "√", myValue, "=", myAnswer)

