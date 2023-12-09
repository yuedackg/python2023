with open( "20000-02-07-02.py", "r", encoding="UTF-8") as f:
    # ここでファイルを1行読み飛ばす
    next(f)
    # 1行読み込み
    buff = f.readline()
    # 表示
    print( buff)
    