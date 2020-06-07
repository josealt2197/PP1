
'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
        - Un parametro "opcion", el cual determina si se debe realizar un procesos de "cifrado" o "descrifrado"
    Salida:
        - El valor de la cadena cifrada o descifrada con el algoritmo de cifrado César
    Restricciones:
        - No hay.

'''
def cifrarDescifrar_CodigoCesar(operacion):
    cadena=input("Ingrese la frase/palabra que desea cifrar: ")
    cadena=cadena.upper()
    cadenaResultante = ""
    indice = 0

    while(indice != len(cadena)):
        cadenaResultante = cadenaResultante + cifrarDescifrarLetra_CodigoCesar(cadena[indice],operacion)
        indice+=1

    if(operacion=="descifrado"):
        cadenaResultante=cadenaResultante.lower()

    return cadenaResultante

'''
    Entradas:
        - Un caracter
    Salida:
        - El valor del caracter cifrado con el algoritmo de cifrado César
    Restricciones:
        - No hay.

'''
def cifrarDescifrarLetra_CodigoCesar(letra, operacion):
    letraCifrada_Descifrada = ""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letrasDesplazadas = "DEFGHIJKLMNOPQRSTUVWXYZABC"

    if(buscarCaracter(letras, letra)!=-1):           
        if(operacion=="cifrado"):
            letraCifrada_Descifrada = letrasDesplazadas[buscarCaracter(letras, letra)]
        else:
            letraCifrada_Descifrada = letras[buscarCaracter(letrasDesplazadas, letra)]
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

#Menu
def menuCifradoCesar():    

    print("\n\t----------------------")
    print("\t  Cifrado Cesar")
    print("\t----------------------")
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
        menuCifradoCesar()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrarDescifrar_CodigoCesar("cifrado"))
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoCesar()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + cifrarDescifrar_CodigoCesar("descifrado"))
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoCesar()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoCesar()
        
menuCifradoCesar() 
