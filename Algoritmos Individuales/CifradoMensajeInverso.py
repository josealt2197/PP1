'''
    Entradas:
        - Una cadena de carateres 
    Salida:
        - El valor de la cadena de carateres con sus caracteres
          en posiciones inversas a las originales.
    Restricciones:
        - No hay.

'''
def cifrar_descifrar_PalabraInversa():
    cadena=input("\nIngrese la frase/palabra que desea descifrar: ")
    cadenaDescifrada=cadena[::-1]
    indice = 0

    return cadenaDescifrada


#Menu
def menuCifradoMsjInv():    

    print("\n\t----------------------")
    print("\t  Cifrado Mensaje Inverso")
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
        menuCifradoMsjInv()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrar_descifrar_PalabraInversa())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoMsjInv()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + cifrar_descifrar_PalabraInversa())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoMsjInv()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoMsjInv()
        
menuCifradoMsjInv() 
