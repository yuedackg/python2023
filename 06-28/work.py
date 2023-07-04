# filename: 06-28-3-22xxx-yourname.py
# リストnameListの定義
namelist = [
		"Ken", "Bob", "Alice", "Guil", "Chun"]
#キーボードから名前を入力する
inName = input ( "Search Name :")
print ( inName)

# 問題６
if inName in namelist:
	print( "名前が登録されています")
else:
	print( "名前の登録がありません")