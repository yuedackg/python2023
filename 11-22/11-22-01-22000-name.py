# filename: 11-22-01-22000-name.py
kakudo = input( "回転角度を入力して下さい：")
kakudo = float( kakudo )    # 小数点数に変換(kakudo を計算できるように)

print( "入力された角度は", kakudo)  # 確認のための表示

import math

ans = 2 * math.pi / 360 * kakudo    # 単位ラジアンに変更

print( "変換後の角度は", ans)       # 変換後の単位で表示

# 90度は、π/２  ≒　1.57
# 180度は、π    ≒　3.14
# 270度は、3π/2 ≒　4.71
# 360度は、2π   ≒　6.28



