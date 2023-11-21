import numpy as np
import math

kakudo = input( "回転する角度を入力してください：")

# 角度の単位を[度]→[rad]に変換
rad = 2 * math.pi / 360.0 *float( kakudo)

print( "角度：", kakudo , "[度]は、", rad, "[rad]です")

