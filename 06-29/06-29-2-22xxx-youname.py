# filename: 06-29-2-22xxx-yourname.py
mylist = list( "nagahama")
print( mylist)
# 関数：list(文字列)を使うと、文字列をばらしたリストをつくる。
replist = list( "123")
print(replist)
# 4文字目から、6文字目の前の文字までを指定
print( mylist[4:6])
# 問題　[ 'g', 'a', 'h']と表示してください
print( mylist[2:5])
# :の前を省略すると0 、後ろを省略すると最後
print( mylist[:3])
print( mylist[4:])
# mylistの3文字目から、replistの文字列を入れる
mylist[3:7] = replist
print(mylist)