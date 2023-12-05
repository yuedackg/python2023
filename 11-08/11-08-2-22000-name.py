# filename:11-08-2-22000-name.py

# 課題
# 　画面に「文字列を入れてください」と表示し文字列を入力する
#  文字列End、endを入れたときに終了する
#  それ以外の文字が入力された時は、「文字列を入れてください」と表示

#  正規表現を作る
m = "[Ee]nd"
# メッセージを変数に入れておく（2か所で使うため）
msg = "文字列を入れてください"

                    # 正規表現を使えるようにする
import re
                    # 文字列の入力を受け付ける
ans = input( msg)   
                    # 文字の検索をする
ans2 = re.findall( m, ans)
                    # 文字が含まれているときはTrue（終了）なので、
                    # 継続であれば、TrueとFalseが逆になる
while not  ans2:
    ans = input( msg)
    ans2 = re.findall( m, ans)
    