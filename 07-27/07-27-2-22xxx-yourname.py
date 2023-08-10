# filename: 07-27-2-22xxx-yourname.py
# 関数の定義では、引数の個数は決まっている
# def  関数名（仮引数1、仮引数2）：
# 　　本文

# 関数の定義では、引数の数を変えて定義できる
# def 関数名（仮引数１, *仮引数２）：
# 上記の形は、仮引数の個数はわからない　
# *をつけた部分は、0個以上の仮引数を表す。
def  myFunc( num1, *tupple):
    print( tupple)
    
myFunc( 10, "ueda")
myFunc( 20 , "ueda", "ohishi")
myFunc( 30 , "ueda", "ohishi", "harada")
myFunc( 40)

# 可変長引数を扱う
#  Japan,...,HongKongは、kuni2に格納される
def myFunc2( kuni, *kuni2):
    count = 1
    
    # kuni　は1つ目、"country"
    print ( kuni)
    
    # 2つ目以降の引数kuni2からひとつづつ取り出す　
    for val in  kuni2 :
        print( val )
        count += 1

myFunc2( "country", "Japan", "America", "Canada", "Hong Kong")