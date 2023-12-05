# filename: 11-09-2-22000-name.py


target = "Python python PYTHON pytHON pYtHoN"
restr = "(p|P)ython"
import re
ans = re.search( restr , target )
print( ans.group())   
print( ans.group(1))  
keyword = "Excel"
ans2 = re.search( keyword, target)
print( ans2)
if  ans2 :
    print( "値があります")
else:
    print( "値がない")
