# filename : 07027-3-22xxx-ouname.py
# print()のオプション

print( "hello")

print( 100)

print( "blue", "red", "green")

# 文字列の区切りを変更
print( "blue", "red", "green", sep="+++")

# 文字列の区切り文字をなくす
print( "blue", "red", "green", sep="")

# 改行あり   次の行は「end='\n'」が省略されている
print( "hello")
print( "world")

# 改行なし
print( "hello", end='')
print( "world")