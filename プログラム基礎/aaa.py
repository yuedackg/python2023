# 文字列を入力し、変数ｘに格納する
x=input("Enter name:")

# ファイルを開き、ファイルセレクタｆを使用する
with open( "2023-01-31-02.txt", "w") as f:
    
    # インデントしている部分は、ファイルが開かれている
    print( x , file=f)

# インデントが戻されているので、ファイルが閉じられている
print( "program terminated.")

    
    