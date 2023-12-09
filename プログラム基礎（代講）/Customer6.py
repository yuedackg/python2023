class Customer:
    bmi = 22
    def __init__(self, number,name,height=0):
        self.number=number
        self.name = name
        self.height=height

    def std_weight( self):
        return Customer.bmi * (self.weight / 100 )**2 
    def show_info( self):
        return 0
    
#  クラスの定義終わり

def my_info(self):
    print("{}:{}".format( self.number, self.name))
    
Customer.show_info = my_info

taro = Customer( 101, "斎藤太郎",180)

taro.show_info()

