# リストをもらって、そのイテレータを作り、
# 最初の要素だけ取り出した後、 
# そのイテレータを返す関数but_first(ls) を定義してください。
def but_first( ls):
    it = iter( ls )
    next( it)
    return it

abc = [ 1,2,3,4,5]
print( abc)
abc2 = but_first( abc)
for e in abc2:
    print( line)
    