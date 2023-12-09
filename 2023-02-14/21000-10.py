# ファイル名：    C21000_10.py
# 関数名：        sumTo( n)
# 内容：
# １からｎまでの足し算を行う結果を作る

# 上記のモジュールを作成しなさい

def sumTo( n):
    ans = 0
    for i in range( 1, n+1):
        ans = ans + i
    return ans

print( sumTo(6))