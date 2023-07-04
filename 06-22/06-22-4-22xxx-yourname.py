# filename: 06-22-4-22xxx-yourname.py
# リストをつくる
arr = [10, 20, 30, 40, 50]

# リストの中に値があるかの判断は「in」を使う
# 「値　in　リスト」　　で、値がリストに含まれるかのテスト
# 結果はTrue（あるばあい）/False（ないばあい）

result = 30 in arr
print( result)

result = 31 in arr
print( result)

# リストから数字を消すときは、最初に含まれている（True）であることを確認して削除
# リストの中に数字がふくまれている＊ならば＊　＝　if
# 例１）　30を消す
if  30 in arr :
	arr.remove(30)

# 例２　31を消す
if 31 in arr:
	arr.remove(31)

# 例３　変数Nの値を消す
N = 11
if N in arr :
	arr.remove(N)

