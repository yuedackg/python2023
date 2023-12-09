
class Customer:
    bmi = 22
    def __init__(self, number, name , height=0):
        self.__number = number
        self.__name = name 
        self.__height = height
        print( __name__)
    
    def get_name ( self):
        return self.__name
    
    def get_number( self):
        return self.__number
    
    def set_number( self, number):
        self.__number = number
    
    
    def get_height( self):
        return self.__height
    
    def  set_height( self, value):
        self.__height= value
        
    def std_weight( self):
        return Customer.bmi * (self.height / 100 )** 2
    
    name = property( get_name)
    number = property( get_number , set_number)
    height = property( get_height)

if __name__ == "__main__":
    taro= Customer( 101, "斎藤太郎",180)
    print( "{} 標準体重{:2f}kg".format( taro.name , taro.std_weight()))

    