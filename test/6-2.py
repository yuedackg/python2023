for myCount in range( 1, 5, 1):
	print( "[", myCount, "]", end="")
	for mySubCount in range( myCount):
		print( "*", end="")
	print( "")
for myCount in range( 5, 0, -1):
	print( "[", myCount, "]", end="")
	for mySubCount in range( myCount):
		print( "*", end="")
	print( "")

