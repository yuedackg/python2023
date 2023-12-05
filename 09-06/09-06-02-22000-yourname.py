# 1. CTRL+N　新規にファイルを作って
# 2. CTRL+S　保存
# filename: 09-06-02-22000-yourname.py
# 課題
# 　URLを入力し、ホスト名だけを取り出してください
#  　例）
#   　入力：http://www.yahoo.co.jp/travel/index.html
#     出力：www.yahoo.co.jp
    
# 文字列を入力して、変数URLに入れる
url = input( "enter url:")

# 変数URLの中から、「//」の右側を取り出して、変数URL1に入れる
key = url.index( "//")
# nagasa= len(url)
url1 = url[key+2:-1]
print( url1)

# 変数URL1の中から、「/」の左側を取り出して、変数URL2
key = url1.index( "/")
url2 = url1[ 0: key]

# ホスト名が入っている変数URL2の内容を表示する
print( "host : ", url2)

# split()を使った簡単な方法
ret2 = url.split("/")
#    http: /   /   wwww.yahoo.co.jp  / hello
#     0      1      2                     3
print( ret2[2])