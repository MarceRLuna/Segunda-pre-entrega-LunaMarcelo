
from package.cliente import Cliente

# Creamos una lista vacía en donde guardaremos la información que creemos de cada "Cliente"
Base_de_usuarios = []

# Función que me permite mostrar por consola todos los clientes que tenemos guardados en la lista Base_de_usuarios
def mostrar_datos():
    
    longitud = len(Base_de_usuarios)

    if longitud == 0:
        print("No hay usuarios cargados en el sitema")
        print("Volviendo al menú !!!")
    else:    
        for clientes in Base_de_usuarios:
            print(clientes) # invocación al método __srt__ de la clase Cliente
 
# Función que me permite instanciar un cliente utilizando el método constructor de la clase Cliente
def registro():

    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    mail = input("Ingrese dirección de mail del cliente: ")
    dni = input("Ingrese el nro. de documento: ")
    telefono = input("Ingrese teléfono del cliente: ")

    nuevo_cliente = Cliente(nombre,apellido,dni, mail, telefono) # Instancia del objeto cliente
    Base_de_usuarios.append(nuevo_cliente) # guardamos dicha instancia dentro de la lista
    
    mensaje = str(input("Quiere registrar el producto que compró el cliente? SI / NO ").upper())

    # Utilización de los dos métodos definidos en la clase Cliente.
    if mensaje.upper() == "SI":
        nuevo_cliente.guardar_productosComprados(producto = input("Ingrese el nombre del producto comprado: "))
        nuevo_cliente.guardar_fecha_compra(fecha = input("Ingrese la fecha en la que se realizó la compra: "))
    else:
        print("Volviendo al menú")
            
    return nuevo_cliente
    
# Función que me permite manejar desde un sencillo menú toda la lógica del programa.    
def menu ():

    print(""" 
    ***** MENU DE OPCIONES ***** """)

    choice = input("""
    - Opción 1 - Registrar cliente.    
    - Opción 2 - Ver clientes registrados.
    - Opción 3 - Salir. 
          
    Elija una opción: """)

    while choice > "0" and choice <= "3" :
        if choice == "1":
            registro()                                  
        elif choice == "2":
            mostrar_datos()                        
        elif choice == "3":
            print("Saliendo del programa.")
            break
        return menu()                      
    else:
        print ("No ha elegido una opción correcta, vuelva a intentarlo.")
        return menu()