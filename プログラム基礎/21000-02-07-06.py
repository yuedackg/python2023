# iter　イテレータが使えるかの実験

a = [1, 2, 3]
print( a )
print( a[1])

# 変数aから順番に取り出す -> イテレータがある
for item in a:
    # リストaはイテレータ（繰り返し取り出し）に対応していない
    #　TypeError が出ることを確認する
    next( a)    
    print( item)

    