'''
    Entradas:
        - Una cadena de carateres 
    Salida:
        - El valor de la cadena con los carateres de sus palabras
          en una posicion inversa
    Restricciones:
        - No hay.

'''
def cifrar_descifrar_PalabraInversa():
    cadena=input("\nIngrese la frase/palabra que desea cifrar: ")
    palabras=cadena.split()
    palabra=""
    cadenaCifrada=""
    contador = 0

    while(contador<len(palabras)):
        palabra=palabras[contador]
        cadenaCifrada=cadenaCifrada+palabra[::-1]+" "
        contador+=1
        
    return cadenaCifrada


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
        print("La cadena cifrada es la siguiente: " + cifrar_descifrar_PalabraInversa())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoPalabInv()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + cifrar_descifrar_PalabraInversa())
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
        
menuCifradoPalabInv() 
