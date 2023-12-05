# filename: 11-22-02-22000-name.py
import math

def convertKakudo( kakudo):             # 関数converKakudo
    ans = 2 * math.pi / 360 * kakudo    # 単位ラジアンに変更
    return ans                          # 計算結果はans

kakudo = input( "回転角度を入力して下さい：")
kakudo = float( kakudo )    # 小数点数に変換(kakudo を計算できるように)
print( "入力された角度は", kakudo)  # 確認のための表示

ans = convertKakudo( kakudo)        # 角度の変換を行う

print( "変換後の角度は", ans)       # 変換後の単位で表示

# 回転変換の2次元配列を作る
# | cos Θ   -sin Θ ｜ = ｜ m00  m01 ｜
# | sin Θ    cos Θ ｜   ｜ m10  m11 ｜
# cos Θ  -> math.cos(Θ)
# sin Θ　-> math.sin(Θ)
m00 = math.cos(     ans )   # 各要素をバラバラに書いた
m01 = - math.sin(   ans )
m10 = math.sin(     ans )
m11 = math.cos(     ans )

rot = [ [ m00, m01],        # 回転の2次元配列を作る
        [ m10, m11]]

print( rot)
# 座標（ 10, 0）,(0,0),(10,10),(0,10)
point = [ [10, 0, 10, 0], 
          [0, 0, 10, 10]]

# 90度回転すると（ 10,0） -> ( 0, 10)
import numpy as np                  # 計算用のライブラリ
rot2 = np.array( rot)               # 2次元配列をnumpy形式
point2 = np.array( point)           # 座標の配列もnumpy形式
newpoint = np.dot( rot2, point2)    # 回転計算
print( newpoint)                    # 結果の出力

    # （ 10, 0）⇒ ( 6.123234e-16, 1.000000e+01)
    #           ≒（ 0, 10）
