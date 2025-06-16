"""
Acciones del menú:

Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
opcion=0
nombreProductos=[]
precioProductos=[]
stockProductos=[]


def solicitarProducto():

    nombre=input("Ingrese el nombre del producto: ")
    try:
        precio=int(input("Ingrese el precio del producto: "))
        stock=int(input("Ingrese el stock del producto: "))
        if precio <0 or stock<0:
            raise ValueError
        else:
            producto=[nombre,precio,stock]
            return producto
    except ValueError:
        print("Debe ingresar valores númericos")
    

def agregarProducto(nombre,stock,precio):
    nombreProductos.append(nombre)
    stockProductos.append(stock)
    precioProductos.append(precio)
    #return None

def buscarProducto(nombre):
    try:
        indiceProducto=nombreProductos.index(nombre)

        nompreProd=nombreProductos[indiceProducto]
        stockProd=stockProductos[indiceProducto]
        precioProd=precioProductos[indiceProducto]

        producto=[nompreProd,precioProd,stockProd]
        return producto
    except ValueError:
        print("No se ha encontrado el próducto")
   




while opcion!=5:
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE INVENTARIO")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea (1-6): ")

    match opcion:
        case "1":
            producto=solicitarProducto()
            if producto!= None:
                #nompreProd=producto[0]
                #stockProd=producto[2]
                #precioProd=producto[1]
                agregarProducto(producto[0],producto[2],producto[1])
        case "2":
            nombreProducto= input("Ingrese el nombre del producto a buscar: ")
            producto=buscarProducto(nombreProducto)
            if producto!=None:
                print(f"Nombre: {producto[0]} \t\t\t Precio: ${producto[1]} \t\t\t Stock: {producto[2]}")

        case "3":
            pass #el pass es para evitar un error. Se debe remover al colocar el código correspondiente