import Product as P

Action = input()
id , name , price , inventory = input().split()

tmpProducto = { 'id': int(id), 'name': name, 'price': float(price), 'inventory': int(inventory) }
Product = P.Product(tmpProducto)

if (Product.SearchForId() and Action == 'AGREGAR') or (not Product.SearchForId() and (Action == 'ACTUALIZAR' or Action == 'BORRAR')):
    print('ERROR')
else:
    if(Action == 'AGREGAR'):
        Response = Product.AddProduct()
    elif(Action == 'ACTUALIZAR'):
        Response = Product.UpdateProduct()
    elif(Action == 'BORRAR'):
        Response = Product.DeleteProduct()

    print(Product.GetMaxPrice(), Product.GetMinPrice(), Product.GetAvarage() , Product.GetTotalPrice())