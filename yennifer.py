productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],}

print("MENU PRINCIPAL")
print("1 stock marca")
print("2 busqueda por precio")
print("3 actualizar precio")
print("4 salir")

def stock_marca(stock):
    marca = int(input("ingresar marca:" )).lower()
    if marca in stock:
        print(f"esta es la marca: {marca}")
    else:
        print("marca no encontrada intente nuevamente")

def busqueda_porprecio(productos):
    precio = int(input("ingrese precio: "))
    marca = input("ingrese una marca")
    modelo = int(input("ingrese un modelo"))
    if precio >= 0:
        
        for precio in productos:
            print(f"productos: {marca} , {modelo}")
    else:
        print("no hay noteboocks en ese rango de precio")

def actualizar_precio(stock):
    modelo = int(input("ingrese un modelo"))
    precio = int(input("ingrese precio: "))
    if modelo in stock:
        print(f"modelo: {modelo}")
    elif precio in stock:
        print("ingresar un precio nuevo")
    else:
        ("opcion no valida")

while True:
    opcion = int("ingresa un numero del 1 al 4: ")

    if opcion == stock_marca(stock):
        print("")
    elif opcion == busqueda_porprecio(productos):
        print("")
    elif opcion == actualizar_precio(stock):
        print("")
    elif opcion == 4:
        print("programa finalizado")
    else:
        print("opcion no valida intente nuevamente")
    
    break

 




   

    



