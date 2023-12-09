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
import math
class MyPoints:
    # ここから下がコンストラクタ
    def __init__(self, x1,y1,x2,y2):
        self.xstart = x1
        self.ystart = y1
        self.xend = x2
        self.yend = y2
    # ここから下に、printNorm()メソッドを追加する
    def printNorm(self):
        takasa = self.yend - self.xstart
        haba = self.xend - self.xstart
        kekka = math.sqrt( takasa**2 + haba**2)
        print( "長さは", kekka)
    def getNorm(self):
        takasa = self.yend - self.xstart
        haba = self.xend - self.xstart
        kekka = math.sqrt( takasa**2 + haba**2)
        # print( "長さは", kekka)
        return kekka 
        
    # 対角線の座標を指定した時の面積
    def printRect( self):
        # 高さ
        takasa= self.yend - self.ystart
        # 横幅
        haba= self.xend - self.xstart
        space = takasa * haba 
        print("S = ", space)
        
a = MyPoints( 2, 2, 4, 4) 
# 数字のチェック
print( a.xstart)
print( a.ystart)
print( a.xend)
print( a.yend)

a.printNorm()   
ret = a.getNorm()
print( "ret=", ret)
        
a.printRect()
