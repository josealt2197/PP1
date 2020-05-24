
'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado Binario
    Restricciones:
        - No hay.

'''
def cifrar_CodigoBinario():
    cadena=input("Ingrese la frase/palabra que desea cifrar: ")
    if(buscarNumero(cadena)==True):
        print("Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos o símbolos")
        #Falta validar que no contenga simbolos
    else:       
        cadena=cadena.lower()
        cadenaResultante = ""
        letraResultante = ""
        indice = 0
        indiceClave = 0
        
        while(indice != len(cadena)):
            if(cadena[indice].isalpha()==True):
                letraResultante=" "+cifrarLetra_CodigoBinario(cadena[indice])
            elif(cadena[indice]==" "):
                letraResultante=" *"
            else:
                letraResultante=cadena[indice]

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
def cifrarLetra_CodigoBinario(letra):
    letraCifrada= ""
    letras = "abcdefghijklmnopqrstuvwxyz"    

    if(buscarCaracter(letras, letra)!=-1):

        letraCifrada = format(buscarCaracter(letras, letra), '05b')
                                                                         
        return letraCifrada
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

'''
    Entradas:
         - pNum: Un número entero positivo mayor a 0.
    Salidas:
         - El valor de pNum convertido a número entero positivo.
    Restricciones:
         - Ninguna. La función NO debe validar restricciones.

'''

def convertirBinario(pNum):

    exponente=0
    resultado=0

    while(pNum>0):
        resultado=resultado+(pNum%10*(2**exponente))
        exponente=exponente+1
        pNum=pNum//10

    return resultado
    
#Menu
def menuCifradoBinario():    

    print("\n\t----------------------")
    print("\t  Cifrado Binario")
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
        menuCifradoBinario()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrar_CodigoBinario())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoBinario()
    elif(opcion==2):
        #print("La cadena descifrada es la siguiente: " + descifrar_CodigoBinario())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoBinario()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoBinario()
        
menuCifradoBinario() 
