# 11-02-2-22000-name.py
# 日付を扱うモジュール
import datetime

# コンストラクタ（変数の初期化）
bn = datetime.date( 2003, 1, 2 )
bx = datetime.date( 2005, 1, 2 )

# datetime型からそれぞれを取り出す
print( bx.year)
print( bx.year, bx.month, bx.day)

# 今日の日付
print( bx.today())

# 二人の生まれた日付の差は？
ans = bx - bn
print( ans.days)

# あなたの誕生日から、何日が立ちましたか？
birth = datetime.date(2000, 4, 1 )
today = birth.today()
delta = today - birth
print( "誕生日から", delta.days,
       "日たちました")

# 時間の計算
start = datetime.time( "10:55")
end = datetime.time( "12:25")
delta = end -start 
print( delta)
