# 問題３　03.py
# クラス「MyPoints」を定義してください。
# コンストラクタ（__init__()）の引数はx1,y1, x2, y2とします。
# コンストラクタの処理では、クラス内変数xstartにx1を、
#                         クラス内変数ystartにy1を、
#                         クラス内変数xendにx2を、
#                         クラス内変数yendにy2を代入してください。
# 追加するメソッドは、printNorm()を追加してください。
# メソッドprintNorm()の処理では、
# 　　　　(xstart, ystart)から（xend, yend）の長さを計算してください
#         計算の手順は、
#         ①yend-ystart　を変数takasaに計算する
#         ②xend-xstart　を変数habaに計算する
#         ③長さを計算し、平方根を計算する
#             math.sqrt(　takasa / haba )
#           ※行頭で「import math」を書くこと
a = MyPoints( 2, 2, 4, 4) 
a.printNorm()           
