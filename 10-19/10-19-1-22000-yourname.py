# filename: 10-19-1-22000-name.py

# 別のファイルmodule.pyを使う
import module

# module.pyの中のcalc()を使いたい
#モジュール名．関数名（）を使う
print( module.calc( 4, 6))
print( module.calc( 8, 3))

# 違うファイルの中の関数を使用するときは、モジュール名を書くのが面倒