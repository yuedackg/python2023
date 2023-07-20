# filename: 07-20-3-22xxx-yourname.py

S = { 2, 4, 8, 16 }
print( S)

#集合に値を追加する
#　集合名.add( 追加する値 )
S.add( 32)
print( S)

# 集合から値を削除する
# 　集合名.remove( 削除する値 )
S.remove( 2 )
print( S) 
# ないものをremove()削除するとエラー
# S.remove( 2)
# print( S)
# ないものをdiscard()削除するとエラーにはならない
S.discard(2 )
# POP()
# 集合の中から一つだけ取り出す。
# 取り出した値は集合から削除される
print(  S.pop() )
print( S)

# 空集合（なにもない）を作る
S.clear()
print( S)



