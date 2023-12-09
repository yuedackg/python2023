# 文字列 name をファイル名とするファイルの最後の行を文字列として返す関数 last_line(name) を、 ファイルオブジェクトに対する for 文を用いて定義してください。

def last_line( name ):
    # ここに関数を作成する
    # ファイルを開く、ファイルオブジェクトをｆにする
    with open( name , "r", encoding="UTF-8") as f:
        # ファイルオブジェクトを使って、文字列を取り出す
        for line in f:
            ans = line    
        # この時点で、残っている文字をansに入れる
    return ans

buff = last_line( "21000-02-07-05.py")
print( buff)
# 緒方は、遊び続けている。が、勉強もできる。ここはチェックのための文字