# filename: 07-13-1-22xxx-yourname.py
# 関数を作る
#  絶対値：　-1　   ⇒　１
#   　　　　 数字がマイナスなら、-1をかける
#           数字がプラスなら、そのまま
# 関数名：             myAbs
# 引数：　             x
# 戻り値（計算結果）：　ans  
# 書き方
# def   functionname ( parameter ):
#       statement
#       statement
#       return  value
# 
def myAbs( x ):
    if x < 0 :
        ans = x * -1
    else:
        ans = x
    return ans
# 使い方
#  value = functionname( 123)
kotae = myAbs( -4 )
print( "kotae : ", kotae)
kotae = myAbs( 4 )
print( "kotae : ", kotae)
