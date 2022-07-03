from Inventory import Products

class Product:
    def __init__(self,producto):
        self.id = producto['id']
        self.name = producto['name']
        self.price = producto['price']
        self.inventory = producto['inventory']

    def AddProduct(self):
        Products[self.id] = [self.name, self.price, self.inventory] #productos[12] = ["Algo", 1000 , 25] Add new item 
        return "Add new product"

    def UpdateProduct(self):
        Products[self.id] = [self.name, self.price, self.inventory] #productos[1] = ["Algo", 1000 , 25] Update item with index
        return "Editing product"

    def DeleteProduct(self):
        Products.pop(self.id) #productos.pop(n) remove item with index
        return "Deleting producto"

    def SearchForId(self):
        if self.id in Products:
            return True
        return False 

    def GetMaxPrice(self):
        PoolPrice = 0
        Product = ''
        for key in Products.keys():
            if(Products[key][1] > PoolPrice):
                PoolPrice = Products[key][1]
                Product = Products[key][0]
        return Product

    def GetMinPrice(self):
        PoolPrice = 0
        Product = ''
        for key in Products.keys():
            if(Products[key][1] > PoolPrice and PoolPrice == 0):
                PoolPrice = Products[key][1]
            elif(Products[key][1] < PoolPrice):
                PoolPrice = Products[key][1]  
                Product = Products[key][0]
        return Product

    def GetAvarage(self):
        Suma = 0
        for key in Products.keys():
            Suma += Products[key][1]
        return round(Suma/len(Products), 1)

    def GetTotalPrice(self):
        Suma = 0
        for key in Products.keys():
            Suma += Products[key][1] * Products[key][2]
        return Suma    