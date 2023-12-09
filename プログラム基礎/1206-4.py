#ここから下に関数tyouhen()を作成してください
import math
def tyouhen( a, b):
    ans = math.sqrt( a**2 + b**2 )
    return ans
#ここまでに関数を書いておくこと

sa = input( "短辺１の長さを入力してください：")
sb = input( "短辺２の長さを入力してください：")
a = int( sa)
b = int( sb)

kotae = tyouhen( a , b )
print( "長辺の長さは" + str(kotae) + "です")
