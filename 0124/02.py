# ファイル名：02.py
# 
# 問題
# クラス名：　myPoint
# 引数：　x,y
# 初期化：　class内変数Xにxを設定する
#           class内変数Yにｙを設定する
# メソッドprintMenseki()を追加する
class MyPoint:
    def __init__( self, x, y):
        self.X = x
        self.Y = y
    def printMenseki(self):
        print( self.X * self.Y)
        
b = MyPoint( 2,4)
print( "b.X = ", b.X)
print( "b.Y = ", b.Y)
b.printMenseki()
