# Ctrl+N
# Ctrl+S
# filename: 06-29-1-22xxx-yourname.py
# Thema:　リストの要素の入れ替え
mylist = [ "ueda", "ohishi", "harada", "mino","nagahama"]
print( mylist)
# 順番通りに表示されていることを確認
# 問題１　要素１と要素３を入れ替えて、表示
tmp=mylist[1]
mylist[1]=mylist[3]
mylist[3]=tmp
print( mylist)

# 問題２：1番目から3番目を”suzuki”に変える
mylist[1] = "suzuki"
mylist[2] = "suzuki"
mylist[3] = "suzuki"
# 別解
mylist[1] = mylist[2] = mylist[3] = "suzuki"
print(mylist)
