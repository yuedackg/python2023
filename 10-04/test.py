ary = [1,6,2,7,3,8,4,9,5]
print(len(ary))

ary = [1,6,2,7,3]
print(ary[0])

ary = [ 2, 4, 6, 8]
print( len( ary))

ary = [ 1, 3, 5, 7, 9]
print( ary[-1])


MaxDay = (0,31,28,31,30,31,30,31,31,30,31,30,31)
print( '2月の最後は', MaxDay[2],'日です')

myDic = { "first":"satou",
		  "secound":"suzuki",
		  "third":"tanaka"}
print( myDic["secound"])

mySet = { 1, 2, 2, 3, 3, 3, 4}
print( len( mySet))

baisu2 = { 2 * i + 2 for i in range( 5)}
print( baisu2)

baisu2 = { 2 * i + 2 for i in range( 15)}
baisu3 = { 3 * i + 3 for i in range( 10)}

baisu6 = baisu3 & baisu2

print(baisu6)
