# filename : 07-13-3-22xxx-yourname.py
# 高さｈ、幅ｗ、奥行ｘの立方体の体積を求めなさい
# 関数名：      Volume
# 引数：        h,w,x :すべて正の値
# 体積（答え）： ans
def Volume ( h, w, x ):
    ans = h * w * x
    return  ans

kotae = Volume( 3, 3, 10 )
print( "w:", 3, ", h:", 3 , ", x:", 10 , ", ans=", kotae)
