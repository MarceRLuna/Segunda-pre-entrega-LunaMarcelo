
# FUNCIONES QUE UTILIZA EL PROGRAMA

def mostrar_datos():
    
    if Base_de_usuarios == {}:
        print("No se ha cargado ningún dato, la base de datos está vacía.")
    else:
        print("Estos son los datos almacenados:")
        n = 1
        for user, password in Base_de_usuarios.items(): # recorremos la base de datos para cada usario y contraseña almacenados.            
            print (f'{n} - Usuario: {user}, Contraseña: {password}')
            n += 1


def registro():
    #pedimos al usuario que ingrese un nombre de usuario
    user = str(input("Ingrese el nombre de usuario: ").upper())
    
    #Evaluamos si el nombre de usuario se encuentra repetido en la base de datos, si está repetido le solicitamos que ingrese otro.
    while user.upper() in Base_de_usuarios.keys():
        print("El nombre elegido ya se encuentra registrado")
        user = str(input("Ingrese otro nombre de usuario: ").upper())
    else: # Si no está repetido continuamos con la carga de datos
        if user.upper() not in Base_de_usuarios.keys():
            pass

    #pedimos al usuario que ingrese una contraseña
    password = str(input("Ingrese la contraseña: ").upper())

    #Evaluamos si la contraseña se encuentra repetida en la base de datos, si está repetida le solicitamos que ingrese otra.
    while password.upper() in Base_de_usuarios.values():
        print("La contraseña elegida ya se encuentra registrada")
        password = str(input("Ingrese otra contraseña: ").upper())
    else:# Si no está repetida continuamos con la ejecución del programa
        if password.upper() not in Base_de_usuarios.values():
            pass

    #Evaluamos si el usuario a completado con los datos solicitados, mientras no los complete de manera correcta se repetirá la petición.
    if user == "" or password == "":
        chance = 1
        while chance <= 3: 

            print("Debe completar con los datos solicitados")
            
            if user == "": #si el usuario vuelve a dejar el dato en blanco, se repite la petición hasta que la cantidad de intentos cumple condición del bucle while
                
                user = str(input(f"Intento nro. {chance} - Ingrese nuevamente el nombre de usuario: ").upper())
                
                # Evaluamos nuevamente si el usuario ingresado se encuentra ya registrado.
                
                i = 1

                while i<= 3:
                    if user.upper() in Base_de_usuarios.keys():
                        print("El nombre elegido ya se encuentra registrado")
                        user = str(input(f"Intento nro. {i} - Ingrese otro nombre de usuario: ").upper())
                        break
                    i += 1    
                else:
                    print("Continuando con la carga de datos .....")

                
                       
            elif password == "":
                
                password = str(input(f"Intento nro. {chance} - Ingrese nuevamente la contraseña: ").upper())

                j = 1

                while j <= 3:
                    if password.upper() in Base_de_usuarios.values():
                        print("La contraseña elegida ya se encuentra registrada")
                        password = str(input(f"Intento nro. {j} - Ingrese otra contraseña: ").upper())
                        break
                    j += 1    
                else:
                    print("Continuando con la carga de datos .....")
                
                
            chance += 1             
              
            
            #si el usuario completa con los datos que se solicitan, los almacenamos en la base de datos.
            if user.upper() != "" and password.upper() != "":
                Base_de_usuarios[user.upper()] = password.upper()
                # una vez almacenado el dato, volvemos a preguntar si se quiere registrar otro usuario y contraseña
                print("Desea registrar otro usuario?")
                resp = input("SI/NO: ")
                
                # Evaluamos la respuesta del usuario.
                while resp.upper() != "SI" and resp.upper() != "NO":
                    print("Elija una opción válida")
                    resp = input("SI/NO: ")
                else:
                    if resp.upper() == "NO":
                       print("Redirigiendo al menú.")
                    else:
                        registro()
                break
        else:
            print("Intentos agotados, usuario no registrado, volviendo al menú !!!.")
               
    else: # Si el usuario completa con los datos al primer intento, almacenamos dichos datos en nuestra base Base de datos.
        Base_de_usuarios[user] = password               

        # Consultamos nuevamente si se quiere registrar otro usuario y contraseña.                             
        print("Desea registrar otro usuario?")
        resp = input("SI/NO: ")

        # Evaluamos la respuesta del usuario.
        while resp.upper() != "SI" and resp.upper() != "NO":
            print("Elija una opción válida")
            resp = input("SI/NO: ")
        else:
            if resp.upper() == "NO":
               print("Volviendo al menú.")
            else:
                registro() 


def login():

    if Base_de_usuarios == {}:
        
        print("La Base de datos está vacía, primero debe registrar un usuario y contraseña")

    elif Base_de_usuarios != {}:

        key = str(input("Ingrese su nombre de usuario: ").upper())
            
        if key.upper() in Base_de_usuarios.keys():   
            value = str(input("Ingrese su contraseña: ").upper()) 

            if value.upper() == Base_de_usuarios[key]:
                print("Inicio de sesión exitoso !!!")
                                                                           
            else:
                chance = 1
                while chance <=2:
                    print("Contraseña incorrecta")
                    value = str(input("Ingrese nuevamente su contraseña: ").upper())
                    if value.upper() == Base_de_usuarios[key]:
                        print("Inicio de sesión exitoso!")                            
                        break
                    chance += 1                        
                else:
                    print("Intentos agotados, no se puede iniciar sesión, volviendo al menú")
                                
        else: # si el nombre de usuario no coincide con alguno guardado en la base de datos, ejecutamos el siguiente código.       
            print("EL nombre de usuario no se encuentra registrado")
            print("Desea intentar logearse nuevamente?")
            resp = input("SI/NO: ")
            # Evaluamos la respuesta del usuario.
            while resp.upper() != "SI" and resp.upper() != "NO":
                print("Elija una opción válida")
                resp = input("SI/NO: ")
            else:
                if resp.upper() == "NO":
                    print("Volviendo al menú.")
                else:
                    login()                    
    

def menu ():

    print(""" 
    ***** MENU DE OPCIONES ***** """)

    choice = input("""
    - Opción 1 - Registrar usuario.
    - Opción 2 - Login.
    - Opción 3 - Ver usuarios registrados.
    - Opción 4 - Salir. 
          
    Elija una opción: """)

    while choice > "0" and choice <= "4" :
        if choice == "1":
            registro()                                  
        elif choice == "2":
            login()                      
        elif choice == "3":
            mostrar_datos()            
        elif choice == "4":
            print("Saliendo del programa.")
            break
        return menu()                      
    else:
        print ("No ha elegido una opción correcta, vuelva a intentarlo.")
        return menu()
    

# LOGICA DEL PROGRAMA

Base_de_usuarios = { }

menu()
           

