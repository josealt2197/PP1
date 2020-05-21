'''
    Entradas:
        - Una cadena de carateres 
    Salida:
        - El valor de la cadena cifrada con los carateres de sus palabras
          en una posicion inversa
    Restricciones:
        - No hay.

'''
def cifrar_PalabraInversa():
    cadena=input("\nIngrese la frase/palabra que desea cifrar: ")
    palabra=""
    cadenaCifrada=""
    indice = 0

    while(indice != len(cadena)):
        if(cadena[indice]==" "):
            cadenaCifrada = cadenaCifrada + " "
        else:
            palabra=cadena[indice]+palabra
        indice+=1

    print(palabra)
    print(cadenaCifrada)


'''
    Entradas:
        - Una cadena de carateres cifrada con los carateres de sus palabras
          en una posicion inversa
    Salida:
        - El valor de la cadena de carateres descifrada con sus caracteres
          en posiciones correctas.
    Restricciones:
        - No hay.

'''
def descifrar_PalabraInversa():
    cadena=input("\nIngrese la frase/palabra que desea descifrar: ")
    palabra=""
    cadenaDescifrada=""
    indice = 0

    while(indice != len(cadena)):
        if(cadena[indice]==" "):
            cadenaDescifrada = cadenaDescifrada + palabra + " "
        else:
            palabra=cadena[indice]+palabra
        indice+=1

    print(palabra)
    print(cadenaDescifrada)


#Menu
def menuCifradoPalabInv():    

    print("\n\t----------------------")
    print("\t  Cifrado Palabra Inversa")
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
        menuCifradoPalabInv()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrar_PalabraInversa())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoPalabInv()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + descifrar_PalabraInversa())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoPalabInv()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoPalabInv()
        
#menuCifradoPalabInv() 
