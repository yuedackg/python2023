# filename : 11-16-1-22000-name.py
import numpy as np
# 上の行のnumpyで黄色の線が出る人は、numpyのinstall
# ①　「スタート」⇒cmdと入力
# ③　pip  install  numpy

# もとになる二次元配列
point = [   [500, 200],
            [100, 300],
            [50,  100]]

# numpyの配列にする
matp = np.array( point)
print( 'Shape:', matp.shape)
print( 'Rank:', matp.ndim)
print(  'matrix:\n' , matp)
print( 'matp[1][1]:' , matp[1][1])

#2次元配列の拡大・縮小を行う
scale = 2.0
matp2 = matp * scale
print( matp2)

# point配列の縦・横を入れ替える
matp3 = matp.T
print( "縦横の入れ替え\n", matp3)

# 90度回転する
rot = [ [ 0, -1],
        [ 1,  0]]
# numpyの配列にする
rotp = np.array( rot)
# 回転計算をする
matp4 = np.dot( rotp, matp3)
print( matp4 )

# 回転前
#  [[500 100  50]
#  [200 300 100]]

# 回転の式　※行列を使った計算
# | 0  -1 | | 500 100  50 |
# | 1   0 | | 200 300 100 |

# 回転後
# [[-200 -300 -100]
#  [ 500  100   50]]