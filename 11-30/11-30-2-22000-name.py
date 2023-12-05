# filename: 11-30-2-22000-name.py
import numpy as np

# 3x3 の二次元配列に、乱数を作る
ans33 = np.random.randn( 3, 3 )

print( "ans33: \n",  ans33)

# 3行5列の表の乱数表を作る
ans35 = np.random.randn( 3, 5)
print( "ans35: \n",  ans35)

# 再現可能な乱数を作る。
# 乱数はある数字をもとにして作る。元になる数字を決めることをSeedを決めるという
# np.random.seed( 10000)

# 乱数を作る
ans0 = np.random.rand()

print( "ans0:", ans0)

# 整数の乱数を作る --------------------------------------------------
ansint = np.random.randint(7, size=10)

print( "ansint:", ansint)

# 配列の中身をシャッフルする　----------------------------------------
series = [ 1, 2, 3, 4, 5, 6]    # 整列されている（昇順）
shuffle = np.random.permutation( series)

print( "shuffle:", shuffle)     # 並べられていない

# 別の方法
shuffle = np.random.permutation(  [ 1, 2, 3, 4, 5, 6]  )
print( "shuffle:", shuffle)     # 並べられていない