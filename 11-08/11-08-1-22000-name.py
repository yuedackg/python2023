# filename: 11-08-1-22000-name.py
# 正規表現（Regular Expression）
# 　　　　　⇒RE
# ライブラリのインポート（事前作業）
import re

# 目的
# 正規表現の目的は、文字列の柔軟な検索
# 検索語「ueda」だと。
# 「ueda」　OK
# 「Ueda」　NG
# 「UEDA」　NG
# 「Ueda」と「ueda」を探す
# ⇒ワイルドカードを利用する　＊　？
#　[uU]eda　を使って探す
# 「ueda」　OK
# 「Ueda」　OK
# 「UEDA」　NG
# ①正規表現を使た文字列を作る
m = "[uU]eda"
# ②探す対象を作る
ss = "ueda Ueda UEDA uEdA"
# ③検索処理をする(最初に見つかるのは？)
ans = re.search( m , ss )
print( ans)
# ③全部探す
ans2 = re.findall( m, ss)
# 結果があるかチェック
if ans2 :
    # 結果があれば、表示
    print( ans2)
    