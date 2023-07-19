# 集合の演算
# 　and    &   intersection()
# 　or　　　|   union()
# 100以下の2の倍数の集合
baisu2 = { i for i in range( 2, 101, 2)}
# 100以下の3の倍数の集合
baisu3 = { i for i in range( 3, 101, 3)}
print( "baisu2:", baisu2)
print( "baisu3:", baisu3)

# 2と3の公倍数：　2の倍数でかつ、3の倍数
baisu6 = baisu2 & baisu3
print( "baisu6:", baisu6)
