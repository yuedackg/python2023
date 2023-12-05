# filename : 10-12-2-22000-yourname.py
# ※一つ目のファイル「file1.txt」
# file1.txt
# my name is 植田
# ※二つ目のファイル「file2.txt」
# file2.txt
# my name is 吉祥
f1out = open( "C://Users//admin//Desktop//file1.txt" , "w", encoding="utf-8")
f1out.write( "file1.txt\n")
f1out.write( "my name is 植田")
f1out.close()

f2out = open( "C://Users//admin//Desktop//file2.txt", "w", encoding="utf-8")
f2out.write("file2.txt\n")
f2out.write("my name is 吉祥")
f2out.close()

f3in =open( "C://Users//admin//Desktop//file1.txt" , "r", encoding="utf-8")
txt = f3in.read()
print( txt)
f3in.close()

f4in =open( "C://Users//admin//Desktop//file2.txt" , "r", encoding="utf-8")
txt2 = f4in.read()
print( txt2)
f4in.close()

f5out=open( "C://Users//admin//Desktop//file3.txt" , "w", encoding="utf-8")
f5out.write( txt)
f5out.write( txt2)
f5out.close()