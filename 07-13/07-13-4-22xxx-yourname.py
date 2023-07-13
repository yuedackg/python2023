import math 
print( math.pi)
# 球の体積を求める
# 4/3 πｒ^3
#【仕様】
# 関数名：　VolumeBall
# 引数：　  hankei
# 戻値：    ret

# 【関数：呼び出され側】
def VolumeBall( hankei ):
    ans = 4 / 3 * math.pi * hankei * hankei *hankei
    return ans

# 【呼び出し側】
kotae = VolumeBall( 20 )
print( "半径20の体積は", kotae)
