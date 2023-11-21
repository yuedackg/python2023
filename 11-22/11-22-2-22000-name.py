import math
import numpy as np

kakudo = input( "回転する角度:")
kakudo = float( kakudo)

# 単位を変換
rad = kakudo * math.pi * 2.0 / 360

# 回転角行列の作成
a11 = math.cos( rad)
a12 = - math.sin( rad)
a21 = math.sin( rad)
a22 = math.cos(rad)

# 回転行列のもと
rotate = [
	[ a11, a12],
	[ a21, a22]
]

# 回転行列 （Numpyを使って便利）
rotateMat = np.array( rotate)

# 途中経過
print( rotateMat)

# 確認用の座標
xy=[ 1, 0]

point = np.array( xy)
point = point.T

print( "point:\n", point)
point2 = np.dot( rotateMat, point)

print( "point2\n", point2)