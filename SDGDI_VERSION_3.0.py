lista_productos=[]
#producto={"nombre":nombre,
#          "cantidad":stock,
#          "precio":1500,
#          "codigo":codigo}

#trabajar con cadenas de caracteres para hacer validaciones.
#el codigo debe tener una mayuscula, debe tener 5 caracteres minimos y debe tener al menos un numero.

opcion="0"

"""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
""" 

#cuenta la cantidad de mayuscuas en el argumento/parametro solicitado.
def contarMayusculas(codigo):
    contador_mayusculas=0
    for letra in str(codigo):
        if letra.isupper()==True:
            contador_mayusculas+=1 #contador_mayusculas=contador_mayusculas+1

    return contador_mayusculas


def contarNumeros(codigo):
    contador_numeros=0
    for letra in str(codigo):
        if letra.isnumeric()==True:
            contador_numeros+=1

    return contador_numeros


def validarCantidadCaracteres(codigo):
    if len(codigo)>=5:
        return True
    else:
        return False
    

def validarCodigo(codigo):
    if contarMayusculas(codigo) <2:
        print("El código debe tener al menos dos mayusculas.")
        return False
    
    elif contarNumeros(codigo)==0:
        print("El código debe tener al menos un número.")
        return False
    
    elif validarCantidadCaracteres(codigo)==False:
        print("El código debe tener un largo de al menos 5 caracteres.")
        return False
    
    else:
        return True


def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ").lower()
    while True:
        codigo=input("Ingrese el código del producto: ")
        if validarCodigo(codigo)==True:
            print("El código es correcto.")
            break
        else:
            print("El código es incorrecto.")

    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
            
        else:
            producto=[nombre,precio,stock]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")
        
    
def buscarProducto(nombre):
    for producto in lista_productos:
        if producto["nombre"]==nombre:
            return producto
    return
        #print("-"*60)
        #print(f"Nombre: {nombre} \t Precio: ${precio} \t Stock: {stock} unidades")
        #print("-"*60)
        #return [nombre,precio,stock]


def guardarProducto(nombre,precio,stock):

    if buscarProducto==None:
        producto={"nombre":nombre,"cantidad":stock,"precio":precio}
        lista_productos.append(producto)
        return "Se guardado correctamente el producto"
    else:
        return "Un producto con ese nombre ya se encuentra guardado."


    producto={"nombre":nombre,"cantidad":stock,"precio":precio}
    lista_productos.append(producto)
    print("Se guardado correctamente el producto")
    #print("Se guardado correctamente el producto")
    #print("No se puede guardar un producto con el mismo nombre que uno ya creado")


def actualizarProducto(nombre,nuevoPrecio,nuevoStock):
    productoEncontrado=buscarProducto(nombre)
    if productoEncontrado!=None:
        indice=lista_productos.index(productoEncontrado)
        productoEncontrado["cantidad"]=nuevoStock
        productoEncontrado["precio"]=nuevoPrecio
        lista_productos[indice]=productoEncontrado
        print("Producto actualizado con éxito")
    else:
        print("No existe un producto con ese nombre")


def mostarInventarioCompleto():
    print("-"*60)
    if(len(lista_productos)==0):
        print("Aún no hay productos agregados")
        return
    else:

        for producto in lista_productos:
            
            print(f"Nombre: {producto["nombre"]} \t Precio: ${producto["precio"]} \t Stock: {producto["cantidad"]} unidades")
        
        print("-"*60)


def eliminarProducto(nombre):
    productoEncontrado=buscarProducto(nombre)
    if productoEncontrado!=None:
        lista_productos.remove(productoEncontrado)
        return True
    else:
        return False


while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    match opcion:

        case "1":
            
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                #guardarProducto(*nuevoProducto)
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        
        case "2":
            
            nombreProducto=input("Ingrese el nombre del producto a buscar: ").lower()
            productoEncontrado=buscarProducto(nombreProducto)
            if productoEncontrado!=None:
                print(f"Nombre: {productoEncontrado["nombre"]} \t Precio: ${productoEncontrado["precio"]} \t Stock: {productoEncontrado["cantidad"]} unidades")
        
        case "3":
            
            print("*Ingrese los datos del producto a actualizar*")
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                actualizarProducto(*nuevoProducto)
        
        case "4":
            
            mostarInventarioCompleto()
        
        case "5":
            
            nombreProducto=input("Ingrese el nombre del producto a eliminar: ").lower()
            eliminarProducto(nombreProducto)
            if eliminarProducto(nombreProducto)==True:
                print("Producto eliminado correctamente.")
            else:
                print("No se ha podido eliminar el producto.")
        
        case "6":
            
            print("Saliendo...")
            break        