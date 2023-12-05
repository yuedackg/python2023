#filename 11-16-2-22000-name.py
import numpy as np

# 回転行列を作る
# | cos(Θ)    -sin(Θ) |
# | sin(Θ) 　　cos(Θ) |

# sin , cos を使いたいときは、次の行を書く
import math
# 360[度]＝２PI　[rad]
kakudo = math.pi / 2.0  # rad を使った単位に変換
# sin(kakudo)は、math.sin(kakudo)とかく。
mat = [ [ math.cos(kakudo), - math.sin( kakudo)],
        [ math.sin( kakudo), math.cos( kakudo)]]

# 二次元配列をnumpyにする
mat2 = np.array( mat)
# 回転の行列完成

print( mat2)