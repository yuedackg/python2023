# filename: 11-09-1-22000-name.py

# 本日の演習
# 文字列の検索を正規表現で行い、そのマッチした文字列を取り出す。

# 探す対象
target = "Python python PYTHON pytHON pYtHoN"

# 今回探すパターン　Python , python
restr = "[pP]ython"

import re
ans = re.search( restr , target )

print( ans.group())     # <- マッチした文字列を表示する
