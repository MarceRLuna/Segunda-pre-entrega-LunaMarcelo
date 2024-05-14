
from package.cliente import Cliente

Base_de_usuarios = []

def mostrar_datos():
    
    longitud = len(Base_de_usuarios)

    if longitud == 0:
        print("No hay usuarios cargados en el sitema")
        print("Volviendo al menú !!!")
    else:    
        for clientes in Base_de_usuarios:
            print(clientes)
 

def registro():

    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    mail = input("Ingrese dirección de mail del cliente: ")
    dni = input("Ingrese el nro. de documento: ")
    telefono = input("Ingrese teléfono del cliente: ")

    nuevo_cliente = Cliente(nombre,apellido,dni, mail, telefono)
    Base_de_usuarios.append(nuevo_cliente)
    
    mensaje = str(input("Quiere registrar el producto que compró el cliente? SI / NO ").upper())

    if mensaje.upper() == "SI":
        nuevo_cliente.guardar_productosComprados(producto = input("Ingrese el nombre del producto comprado: "))
        nuevo_cliente.guardar_fecha_compra(fecha = input("Ingrese la fecha en la que se realizó la compra: "))
    else:
        print("Volviendo al menú")
            
    return nuevo_cliente
    
    
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