#filename: 11-30-1-22000-name.py
# でたらめな数を作る
import numpy as np

# 乱数＝でたらめな数を作る
# rand() : 0~1未満のでたらめな数を作る。　かっこの中は、作る個数
ans10 = np.random.rand(10)
print( "ans10:",  ans10)

# かっこの中の数字を書かないと1つだけ
ans = np.random.rand()
print( "ans:" , ans)

# さいころ（１~６）を作る　ーーーーーーーーーーーーーーーーーーー
ans = np.random.rand()      # 0.0    -  0.9999

# 6倍する：　0から6未満
ans6 = ans * 6              # 0.0   - 5.9999

# +1 する
ans6 = ans6 + 1             # 1.0   - 6.9999

# 小数点以下を切り捨て
answer = int( ans6)         # 1    -  6 

print( "answer:", answer)

