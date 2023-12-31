# 郵便番号を正規表現で表す。

# 例）
# 　815-0035　…　数字が3桁。間にマイナス、最後に数字が4桁
#  [0123456789] ・・・数字の1桁
#  [0123456789][0123456789] ・・・・数字の二けた
 
#  [0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]
 
#  [0-9]　・・・数字の1桁を表す短縮法
 
#  [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]
 
#  [0-9]+-[0-9]+
 
ans = input (  "郵便番号を入れてください:")
m = "^[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$" 
import re
ret = re.findall( m , ans )
if ret :
    print( "あなたの入力した郵便番号は正しい")
    print( ret )
else : 
    print( "あなたの入力した郵便番号は間違い")

# 815-0030  ⇒　あなたの入力した郵便番号は正しい
# 0030-815　⇒　あなたの入力した郵便番号は間違い
 
ans = input ( "メールアドレスの@の前を入れてください")
m = "[Cc][kK][gG]22[0-9]*"
ret = re.findall(  m , ans)
if ret :
    print( "メールの正しいIDが入力されました。")