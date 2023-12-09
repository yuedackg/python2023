# デスクトップにあるファイルをすべて表示しなさい。
# ファイル・ディレクトリ操作を行う場合に使用する
import os

# デスクトップのファイル・フォルダ一覧を表示する
files = os.listdir( "/Users/admin/Desktop")

# 読みだしたリストをすべて表示する ⇒フォルダだけ表示
for item in files:
    print( item)