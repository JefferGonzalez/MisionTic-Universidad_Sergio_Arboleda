Action = input()
id , name , price , inventory = input().split()

Products = {
    1: ["Manzanas", 5000.0, 25],
    2: ["Limones", 2300.0, 15],
    3: ["Peras", 2700.0, 33],
    4: ["Arandanos", 9300.0, 5],
    5: ["Tomates", 2100.0, 42],
    6: ["Fresas", 4100.0, 3],
    7: ["Helado", 4500.0, 41],
    8: ["Galletas", 500.0, 8],
    9: ["Chocolates", 3500.0, 80],
    10: ["Jamon", 15000.0, 10],
}

def AddProduct(Product):
    Products[Product['id']] = [Product['name'], Product['price'], Product['inventory']] #productos[12] = ["Algo", 1000 , 25] Add new item 
    return "Add new product"

def UpdateProduct(Product):
    Products[Product['id']] = [Product['name'], Product['price'], Product['inventory']] #productos[1] = ["Algo", 1000 , 25] Update item with index
    return "Editing product"

def DeleteProduct(Product):
    Products.pop(Product['id']) #productos.pop(n) remove item with index
    return "Deleting producto"

def GetMaxPrice():
    PoolPrice = 0
    Product = ''
    for key in Products.keys():
        if(Products[key][1] > PoolPrice):
            PoolPrice = Products[key][1]
            Product = Products[key][0]
    return Product

def GetMinPrice():
    PoolPrice = 0
    Product = ''
    for key in Products.keys():
        if(Products[key][1] > PoolPrice and PoolPrice == 0):
            PoolPrice = Products[key][1]
        elif(Products[key][1] < PoolPrice):
            PoolPrice = Products[key][1]  
            Product = Products[key][0]
    return Product

def GetAvarage():
    Suma = 0
    for key in Products.keys():
        Suma += Products[key][1]
    return round(Suma/len(Products), 1)

def GetTotalPrice():
    Suma = 0
    for key in Products.keys():
        Suma += Products[key][1] * Products[key][2]
    return Suma


if (int(id) in Products and Action == 'AGREGAR') or (int(id) not in Products and (Action == 'ACTUALIZAR' or Action == 'BORRAR')):
    print('ERROR')
else:
    Product = { 'id': int(id), 'name': name, 'price': float(price), 'inventory': int(inventory) }
    if(Action == 'AGREGAR'):
        Response = AddProduct(Product)
    elif(Action == 'ACTUALIZAR'):
        Response = UpdateProduct(Product)
    elif(Action == 'BORRAR'):
        Response = DeleteProduct(Product)

    print(GetMaxPrice(), GetMinPrice(), GetAvarage() , GetTotalPrice())