# n!を計算する
def  fact(n ):
    ans = 1 
    for i in range(1, n + 1):
        ans = ans * i
    return ans 

# ファイル名=module名：21000-05.py
# print( fact( 4))

# モジュール化をする準備
# １．ファイル名は、先頭は英字
# 　　英字（A-Z,a-z,_）と数字で構成する

# 元：    20000-05.py
# 変更後：C2000005.py
