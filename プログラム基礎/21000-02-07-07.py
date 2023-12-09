# filename: 21000-02-07-07.py
# イテレータに対応していない変数をイテレータで扱えるようにする

abc =  [ 21000, 22000 , 23000 ,20000]
abcd = iter( abc)

for line in abcd:
    # 要素を飛ばして読み込みたいときはイテレータ型に変換
    next( abcd)
    print( line)
    
