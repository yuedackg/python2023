# filename : 07-13-2-22xxx-yourname.py
# 縦の長さｈ、横の長さｗの長方形の面積を計算しなさい
# ｈがマイナスの時は面積を-1にしなさい
# ｗがマイナスの時は面積を-1にしなさい

# 関数名：area
# 引数：w, h
# 戻り値：ans

def area ( w, h ):
    ans = w * h 
    if w < 0 :
        ans = -1
    if h < 0 :
        ans = -1 
    return ans

S = area ( 3, 3 )
print( "S=", S)

S = area ( 3, 0 )
print( "S=", S)

S = area ( -3, -3 )
print( "S=", S)

    
# def area( w, h ):
#     if w >= 0 or h >= 0 :
#         ans = w * h
#     if w < 0 :
#         ans = -1
#     if h < 0 :
#         ans = -1 
#     return ans 
        
