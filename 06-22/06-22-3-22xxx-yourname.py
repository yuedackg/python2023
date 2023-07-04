# filename: 06-22-3-22xxx-yourname.py

arr = [ 1, 2, 4, 8, 16, 32]
print(arr)

# リストに値を追加する
# リストに「.append()」を使用する ；リストの最後に追加
arr.append(64)
print(arr)

# リストに「.insert()」を使用する　；リストの引数1番目の前に、引数2番目の値を挿入
arr.insert( 0, 100)
print( arr)

arr.insert( 0, 200)
print(arr)

# リストから,リストの中にある値を削除する
arr.remove( 4)
print( arr)
# リストの中に値がないときにはエラー
arr.remove( 101)
print( arr)