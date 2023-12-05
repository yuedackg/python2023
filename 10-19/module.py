# filename :module.py       ⇐ ファイル名が違います！

def calc( x, y):            # 関数calc()を作る。パラメータは二つ
    ans = x - y             # 二つの引数で、x-yを計算
    print( "x:",x )         # 画面にxを表示
    print( "y:",y)          # 画面にyを表示
    print( "x - y : ", ans) # 計算結果ansを表示
    return ans              # 戻り値

print( calc(  4, 5) )       # 関数を使ってみた　４－５で、-1が表示される

# ここまで、関数を覚えた人は、何も新しいことはありません。
# ファイル名がmodule.pyになっているのがいつもと違うことです。
# このファイルで定義された関数calc()は、このファイルの中で使える
