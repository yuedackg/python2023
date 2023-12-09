mojiretu = "私の名前は中野です"

with open( "2023-01-31-05+.txt", "w", encoding="shift_jis") as f:
    print( mojiretu, file=f)
    
# Windowsは基本的にShift-JISを使うため、
# 他の形式のファイルは文字化けしやすい

# メモ帳などで読むためには,
# 文字コードの指定が必要

print( "program terminated.")