print( "----------------------- first step.")
with open( "20000-02-07-01.py", "r") as f:
    buff = f.readline()
    print( buff)
print( "------------------------ secound step.")
with open( "20000-02-07-01.py", "r") as f:
    buff = f.read()
    print( buff)
    
    