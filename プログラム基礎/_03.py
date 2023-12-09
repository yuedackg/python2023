# プログラム名：210xx-03.py
# 入力ファイル：210xx-2023-01-31.txt
# 入力ファイル：210xx-2023-01-31-02.txt
# 出力ファイル：210xx-merge.txt

# ファイルを読み込みモード”r”で開く

with open("21000-merge.txt", "w") as fw:
    with open( "210xx-2023-01-31-02.txt", "r") as fr: 
        ret = fr.read()
        print( ret, file=fw)

    with open( "210xx-2023-01-31.txt", "r") as fr:
        ret = fr.read()
        print( ret, file=fw)




    