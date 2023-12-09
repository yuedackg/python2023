# classの定義
class TestClass:
    # classの中のメソッドの定義
    # __init__()を「コンストラクタ」（最初に実行される）
    def __init__( self, code , name):
        # classの中で使う変数は「self.」をつける
        self.code=code
        self.name=name
            
# 使用する⇒　classを生成（値をセットする）する
a = TestClass( 1, "テスト１")
a = TestClass( 2, "てすと２")
# セットされた値を表示してみる
print( "code=", a.code)
print( "name=", a.name)


