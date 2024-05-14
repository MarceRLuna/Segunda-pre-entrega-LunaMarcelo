
class Cliente:
    
    def __init__(self, nombre,apellido, dni, mail, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail
        self.telefono = telefono
        self.fecha_compra = []
        self.producto_comprado = []       
                
    def __str__(self):
        return f'''
        Datos del cliente:  
                          Nombre: {self.nombre}
                          Apellido: {self.apellido}
                          D.N.I.: {self.dni}
                          Dirección de correo: {self.mail}
                          Teléfono: {self.telefono}
                          Producto comprado: {self.producto_comprado}
                          Fecha en que se realizó la compra: {self.fecha_compra}'''    
   
          
    def guardar_productosComprados(self, producto):        
        
        self.producto_comprado.append(producto)

        print(f"El producto: {producto},  fue agregado a la lista de productos comprados por el cliente {self.nombre}")
        
        respuesta = str(input("Cargar otro producto?").upper())
                
        while respuesta.upper() == "SI":
            
            producto = input("Ingrese el nombre del producto comprado: ")
            
            self.producto_comprado.append(producto)
            
            respuesta = str(input("Cargar más productos ?").upper())
        else:
            print("Regresando al menú.")
           
        

    def guardar_fecha_compra(self, fecha):
        self.fecha_compra.append(fecha)
        print(f"La fecha {fecha} fue agregada a las fechas de compra del cliente {self.nombre}")    
          


