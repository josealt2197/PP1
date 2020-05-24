
'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado por Llave
    Restricciones:
        - No hay.

'''
def cifrar_CodigoPorLlave(operacion):
    cadena=input("Ingrese la frase/palabra que desea cifrar: ")
    clave=input("Digite la clave requerida para cifrar la palabra/frase: ")
    if(len(clave)<= 1):
        print("Se ha producido un ERROR: La clave debe estar compuesta por al menos dos caracteres")
    elif(buscarNumero(cadena)==True):
        print("Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos o enteros")
    else:       
        cadena=cadena.lower()
        cadenaResultante = ""
        letraResultante = ""
        indice = 0
        indiceClave = 0
        
        while(indice != len(cadena)):
            if(cadena[indice].isalpha()==True):
                letraResultante=cifrarDescifrarLetra_CodigoPorLlave(cadena[indice],operacion,clave[indiceClave])
                indiceClave+=1
            elif(cadena[indice]==" "):
                letraResultante=cadena[indice]
            else:
                letraResultante=" "

            if(indiceClave==(len(clave))):
                indiceClave=0
                
            cadenaResultante = cadenaResultante + letraResultante
            indice+=1
            
        return cadenaResultante

'''
    Entradas:
        - Un caracter
    Salida:
        - El valor del caracter cifrado con el algoritmo de cifrado César
    Restricciones:
        - No hay.

'''
def cifrarDescifrarLetra_CodigoPorLlave(letra, operacion, clave):
    posLetraCifrada_Descifrada = 0
    letraCifrada_Descifrada = ""
    letras = "abcdefghijklmnopqrstuvwxyz"    

    if(buscarCaracter(letras, letra)!=-1 and buscarCaracter(letras, clave)!=-1):

        if(operacion=="cifrado"):
            posLetraCifrada_Descifrada = (buscarCaracter(letras, letra)+1)+(buscarCaracter(letras, clave)+1)

            if(posLetraCifrada_Descifrada>26):
                posLetraCifrada_Descifrada=posLetraCifrada_Descifrada-26
        else:
            posLetraCifrada_Descifrada = (buscarCaracter(letras, letra)+1)-(buscarCaracter(letras, clave)+1)
            
            if(posLetraCifrada_Descifrada<0):
                posLetraCifrada_Descifrada=posLetraCifrada_Descifrada+26

            letraCifrada_Descifrada = letras[posLetraCifrada_Descifrada-1]


        letraCifrada_Descifrada = letras[posLetraCifrada_Descifrada-1]
                                                                         
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
        - Una cadena de caracteres
    Salida:
        - True si alguno de los caracteres de la cadena corresponde a un valor numerico
        - False si ninguno de los caracteres de la cadena corresponde a un valor numerico 
    Restricciones:
        - No hay.

'''
def buscarNumero(cadena):
    indice = 0
    
    while(indice != len(cadena)):
       if(esEntero(cadena[indice])==True):
           return True
       indice+=1

    return False
    

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
def menuCifradoPorLlave():    

    print("\n\t----------------------")
    print("\t  Cifrado por Llave")
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
        menuCifradoPorLlave()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrar_CodigoPorLlave("cifrado"))
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoPorLlave()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + cifrar_CodigoPorLlave("descifrado"))
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoPorLlave()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoPorLlave()
        
menuCifradoPorLlave() 
