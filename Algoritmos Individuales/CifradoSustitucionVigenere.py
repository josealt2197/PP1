
'''
    Entradas:
        - Una cadena de carateres 
        - Un parametro "opcion", el cual determina si se debe realizar un procesos de "cifrado" o "descrifrado"
    Salida:
        - El valor de la cadena cifrada o descifrada con el algoritmo de cifrado por Sustitución Vigenére
    Restricciones:
        - No hay.

'''
def cifrarDescifrar_SustitucionVigenere(operacion):
    cadena=input("Ingrese la frase/palabra que desea cifrar/descifrar: ")
    clave=input("Digite la clave requerida para cifrar/descifrar la palabra/frase: ")
    if(clave=="" or len(clave)!=2):
        print("Se ha producido un ERROR: La clave debe estar compuesta por dos dígitos")
    else:
        if(esEntero(clave)==True):
            cadena=cadena.lower()
            clave1=int(clave[0])
            clave2=int(clave[1])
            cadenaResultante = ""
            letraResultante = ""
            indice = 0

            while(indice != len(cadena)):
                if(cadena[indice]==" "):
                    letraResultante = " "
                elif((indice+1)%2!=0):
                    letraResultante=cifrarDescifrarLetra_CodigoVigenere(cadena[indice],operacion,clave1)
                else:
                    letraResultante=cifrarDescifrarLetra_CodigoVigenere(cadena[indice],operacion,clave2)
                    
                cadenaResultante = cadenaResultante + letraResultante
                indice+=1

            return cadenaResultante
        else:
            print("Se ha producido un ERROR: Los digitos de la clave deben ser valores enteros")

'''
    Entradas:
        - Un caracter
        - Un parametro "opcion", el cual determina si se debe realizar un procesos de "cifrado" o "descrifrado"
    Salida:
        - El valor del caracter cifrado o descrifrado, segun la operacion, requerida con el algoritmo de cifrado
        por Sustitución Vigenére
    Restricciones:
        - No hay.

'''
def cifrarDescifrarLetra_CodigoVigenere(letra, operacion, clave):
    letraCifrada_Descifrada = ""
    letras = "abcdefghijklmnopqrstuvwxyzabcdefghi"


    if(buscarCaracter(letras, letra)!=-1):
        if(operacion=="cifrado"):
            letraCifrada_Descifrada = letras[(buscarCaracter(letras, letra)+clave)]
        else:
            letraCifrada_Descifrada = letras[(buscarCaracter(letras, letra)-clave)]
        
        return letraCifrada_Descifrada
    else:
        return letra

'''
    Entradas:
        - Un caracter y una cadena de caracteres
    Salida:
        - El numero que corresponde a la posicion en la cadena en la cual se encuentra
          el caracter
        - -1 si el caracter no se encuentra entre los que conforman la cadena
    Restricciones:
        - No hay.

'''
def buscarCaracter(cadena, caracter):
    indice = 0
    
    while(indice != len(cadena)):
       if(cadena[indice]==caracter):
           return indice
       indice+=1

    return -1

'''
    Entradas:
        - El valor a ser validado(pnum)
    Salidas:
        - True: si el valor recibido puede convertirse a entero
        - False: si no es posible convertirlo a entero
    Restricciones:
        - El formato del valor recibido deber ser una cadena/str

'''
def esEntero(pNum):
    try:
        resultado = int(pNum)
        return True
    except:
        return False

#Menu
def menuCifradoVigenere():    

    print("\n\t----------------------------------")
    print("\t  Cifrado por Sustitución Vigenére")
    print("\t------------------------------------")
    print("\nSeleccione una de las opciones.")
    print("Digite el numero correspondiente.")
    print("\n1. Cifrar frase o palabra")
    print("2. Descifrar frase o palabra")
    print("3. Finalizar Programa")
    
    try:
        opcion = int(input("\nOpcion: "))
    except:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoVigenere()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrarDescifrar_SustitucionVigenere("cifrado"))
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoVigenere()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + cifrarDescifrar_SustitucionVigenere("descifrado"))
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoVigenere()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoVigenere()
        
menuCifradoVigenere() 
