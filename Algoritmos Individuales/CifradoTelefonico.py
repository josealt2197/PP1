'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado telefónico.
    Restricciones:
        - No hay.

'''
def cifrar_CodigoTelefonico():
    cadena=input("Ingrese la frase/palabra que desea cifrar: ")
    cadena=cadena.lower()
    cadenaCifrada = ""
    indice = 0

    while(indice != len(cadena)):
        cadenaCifrada = cadenaCifrada + cifrarLetra_CodigoTelefonico(cadena[indice])
        indice+=1

    return cadenaCifrada

'''
    Entradas:
        - Un caracter en lenguaje natural en minuscula
    Salida:
        - Dos caracteres numéricos en el caso de que corresponda a una letra
        - Un carácter con el símbolo “*” en caso de sea un espacio
        - El mismo carácter en caso de que no aplique uno de los casos anteriores
    Restricciones:
        - No hay.

'''
def cifrarLetra_CodigoTelefonico(letra):
    letraCifrada = ""
    numeroAsignado = 1
    bloque = ""
    inicio = 0
    fin = 3
    letras = "abcdefghijklmnopqrstuvwxyz"

    if(buscarCaracter(letras, letra)!=-1):
        while(inicio < 25):

            bloque=letras[inicio:fin]

            if(buscarCaracter(bloque, letra)==-1):
                if(numeroAsignado==5 or numeroAsignado==7):
                    inicio+=3
                    fin+=4
                elif(numeroAsignado==6):
                    inicio+=4
                    fin+=3
                else:
                    inicio+=3
                    fin+=3

                numeroAsignado+=1
            else:
                return str(numeroAsignado+1)+str(buscarCaracter(bloque, letra)+1)

    elif(letra==" "):
        return "*"
    else:
        return letra

'''
    Entradas:
        - Una cadena de carateres cifrada con el algoritmo de cifrado telefónico
    Salida:
        - El valor de la cadena de carateres en lenguaje natural .
    Restricciones:
        - No hay.

'''
def descifrar_CodigoTelefonico():
    cadena=input("Ingrese la frase/palabra que desea descifrar: ")
    cadena=cadena.lower()
    cadenaDescifrada = ""
    letraCifrada=""
    indice = 0

    while(indice != len(cadena)):

        if(cadena[indice]=="*"):
            cadenaDescifrada = cadenaDescifrada + " "
            
        elif(esEntero(cadena[indice])==True):
            letraCifrada=letraCifrada+cadena[indice]
            if(len(letraCifrada)==2):
                cadenaDescifrada = cadenaDescifrada + descifrarLetra_CodigoTelefonico(letraCifrada)
                letraCifrada=""
        else:
            cadenaDescifrada = cadenaDescifrada + cadena[indice]
        
        indice+=1

    return cadenaDescifrada

'''
    Entradas:
        - Una cadena de 2 caracteres numericos
    Salida:
        - Un caracter del alfabeto al cual corresponden los valores recibidos
        segun el algoritmo de cifrado telefónico
    Restricciones:
        - No hay.

'''
def descifrarLetra_CodigoTelefonico(letraCifrada):
    codigoLetra = ""
    numeroAsignado = ""
    bloque = ""
    letras = "abcdefghijklmnopqrstuvwxyz"
    #numeros = "23456789"

    #Recuperar Numero Asignado
    numeroAsignado = letraCifrada[0]
    #Recuperar Numero de Letra 
    codigoLetra = letraCifrada[1]
    
    if(numeroAsignado=="2"):
        bloque=letras[0:3]
        
    elif(numeroAsignado=="3"):
        bloque=letras[3:6]

    elif(numeroAsignado=="4"):
        bloque=letras[6:9]

    elif(numeroAsignado=="5"):
        bloque=letras[9:12]

    elif(numeroAsignado=="6"):
        bloque=letras[12:15]

    elif(numeroAsignado=="7"):
        bloque=letras[15:19]

    elif(numeroAsignado=="8"):
        bloque=letras[19:22]

    else:
        bloque=letras[22:25]
    
    return bloque[int(codigoLetra)-1]
    

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
    resultado = -1
    
    while(indice != len(cadena)):
       if(cadena[indice]==caracter):
           resultado=indice
       indice+=1

    return resultado

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
def menuCifradoTelefonico():    

    print("\n\t----------------------")
    print("\t  Cifrado Telefónico")
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
        menuCifradoTelefonico()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrar_CodigoTelefonico())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoTelefonico()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + descifrar_CodigoTelefonico())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoTelefonico()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoTelefonico()
        
menuCifradoTelefonico() 
