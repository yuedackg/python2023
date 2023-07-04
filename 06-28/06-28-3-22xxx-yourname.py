# filename: 06-28-3-22xxx-yourname.py
# リストnameListの定義
namelist = ["Ken", "Bob", "Alice", "Guil", "Chun"]
inName = input ( "Search Name :")
print ( inName)

if inName in namelist:
	print( "名前が登録されています")
else:
	print( "名前の登録がありません")
print( "Q6 end.")
