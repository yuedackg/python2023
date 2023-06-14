# Ctrl+n
# Ctrl+s
# filename : 06-01-2-22xxx-younamme.py   [desktop]

import random
# print( random.random())
#　でたらめな数字が出てくればOK　隣の席の人と違えばOK

saikoro = random.random()
if  saikoro < 1.0/6  :
	print( 1)
elif saikoro < 2.0 /6 :
	print(2)
elif saikoro < 3.0 / 6 :
	print( 3)
elif saikoro < 4.0 / 6 :
	print( 4)
elif saikoro < 5.0 / 6:
	print( 5)
elif saikoro < 6.0 / 6:
	print( 6)