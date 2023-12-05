# filename: 11-02-1-22000-name.py
# calc220001102.pyを使えるようにする
import calc220001102 as calc

# test code.
print( calc.add( 3, 4))
print( calc.sub( 5, 2))
calc.credit()

# import命令でモジュールを取り込んでも、その中に入っている関数を使用するときは、
# モジュール名.関数名（）
# と書かなければならない。
# このモジュール名が長い時には、短縮した文字を使いたいときに、as命令で短くする。

# モジュール名を書きたくないときは、from~import命令で省略
# 記法もあるが、積極的には使わない