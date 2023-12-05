# CTRL + N
# CTRL + S
# filename : 09-07-1-22000-yourname.py

# 昨日の問題を関数にする

# 以上のプログラムを関数getHostname（）という関数にする
# 引数：なし　　戻り値：ホスト名
def getHostname():
    # URL文字列を入力
    ret = input( "Enter URL:")
    # 最初のプロトコルの部分の開始場所を出している
    separatePos = ret.index("//")
    # プロトロコルの後ろの部分から、最後までを取り出す。
    urls = ret[separatePos+2:-1]
    # ホスト名の後ろの「/」の位置を求めている
    separatePos = urls.index( "/")
    # 後のフォルダの位置の前までを取り出している
    hostname = urls[0:separatePos]
    return hostname

print( "hostname: " , getHostname())
