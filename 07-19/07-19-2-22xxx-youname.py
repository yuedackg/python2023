# 集合の並びはない
myList = { 4, 3, 2, 1}
print( myList)

# 空集合＝何もない集まり
myList = {} 
print( myList)
print( len( myList))

# リストから集合を作る
    # リスト　※下の例は8個
myList = [1,2,3,4,1,2,3,4]
print ( myList)
    # リストmyListを集合に変換するには、set()メソッドを使う
mySet = set( myList)
print( mySet)
print( len( mySet))
