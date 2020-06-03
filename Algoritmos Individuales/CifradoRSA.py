from random import randint 

'''
Obtener las llaves publica y privada para el cifrado RSA
    Entradas:
        - Ninguna
    Salidas:
        - Una Cadena de caracteres compuesta por los valores de las llaves publica y privada concatenados
    Restricciones:
        - Ninguna
'''
def generarLlavesRSA():
     #Paso 1
    p=randint(1,999)
    while(esPrimo(p)==False):
        p=randint(1,999)

    q=randint(1,999)
    while(esPrimo(q)==False):
        q=randint(1,999)

    #Paso 2
    n=p*q
    print("n= "+str(n))
    
    #Paso 3
    fiDeN=(p-1)*(q-1)
    
    #Paso 4
    e=randint(3,fiDeN-2)
    x=calcularMCD(fiDeN,e)
    while(x!=1):
        e=randint(3,fiDeN-2)
        x=calcularMCD(fiDeN,e)

    print("e= "+str(e))
    
    #Paso 5
    d=1
    y=((d*e)-1)%fiDeN
    while(y!=0): 
        d+=1
        y=((d*e)-1)%fiDeN

    claves= [n, e, d] 
    return claves
    # print("Llaves generadas: ")
    # print("Publica: ("+str(n)+", "+str(e)+")")
    # print("Privada: ("+str(n)+", "+str(d)+")")

'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado RSA
    Restricciones:
        - No hay.

'''
def cifrar_CodigoRSA():
    cadena=input("Ingrese la frase/palabra que desea cifrar: ")
##    print("Digite la clave publica requerida para cifrar la frase/palabra")
##    n=int(input("-->Ingrese el primer valor de la clave: "))
##    e=int(input("-->Ingrese el segundo valor de la clave: "))
    claves = generarLlavesRSA()
    n = int(claves[0])
    e = int(claves[1])
    d = int(claves[2])
    cadenaResultante = ""
    letraResultante = ""
    cadenaDeRetorno = ""
    indice = 0
    
    while(indice != len(cadena)):
        if(cadena[indice].isascii()==True):
            letraResultante=(ord(cadena[indice])**e)%n
        else:
            letraResultante=cadena[indice]

        cadenaResultante = cadenaResultante + "*"+ str(letraResultante)
        indice+=1

    cadenaDeRetorno = cadenaResultante[1:] + "\n-->Llaves generadas: Publica: ("+str(n)+", "+str(e)+") y Privada: ("+str(n)+", "+str(d)+")" 

    return cadenaDeRetorno    

'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado RSA
    Restricciones:
        - No hay.

'''
def descifrar_CodigoRSA():
    cadena=input("Ingrese la frase/palabra que desea descifrar: ")
    print("Digite la clave privada requerida para descifrar la frase/palabra")
    n=int(input("-->Ingrese el primer valor de la clave: "))
    d=int(input("-->Ingrese el segundo valor de la clave: "))
    cadenaResultante = ""
    letrasSeparadas = cadena.split("*")
    letraCifrada = ""
    indice = 0
    print(len(letrasSeparadas))
    while(indice != len(letrasSeparadas)):
        print(letrasSeparadas[indice])
        if(esEntero(letrasSeparadas[indice])==True):
            letraResultante=chr( ( int(letrasSeparadas[indice])**d )%n )
        else:
            letraResultante=cadena[indice]

        cadenaResultante = cadenaResultante + letraResultante
        indice+=1
        
    return cadenaResultante


'''
Determinar si un numero es primo 
    Entradas:
        - Un numero entero 
    Salidas:
        - True si el numero ingresado es primo
        - False si el numero ingresado no es primo
    Restricciones:
        - El numero debe ser un entero positivo mayor a 1
'''
def esPrimo(num):
    divisor=2

    while(divisor<num):
        if(num%divisor==0):
            return False
        divisor= divisor + 1

    return True

'''
Calcular el Maximo Común Divisor de dos numeros.
    Entradas:
        - Dos números enteros mayores a cero
    Salida:
        - El valor del Máximo Común Divisor entre ambos numeros
    Restricciones:
        - No hay.
'''
def calcularMCD(a, b):
    i = 1
    while(i <= a and i <= b):
        if(a % i == 0 and b % i == 0):
            mcd = i
        i += 1
    return mcd

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
def menuCifradoRSA():    
    print("\n" * 100)
    print("\n\t----------------------")
    print("\t  Cifrado RSA")
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
        menuCifradoRSA()

    print("\n")
    
    if(opcion==1):
        print("La cadena cifrada es la siguiente: " + cifrar_CodigoRSA())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoRSA()
    elif(opcion==2):
        print("La cadena descifrada es la siguiente: " + descifrar_CodigoRSA())
        input("\n-->Presione la tecla enter para continuar...")
        menuCifradoRSA()
    elif(opcion==3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifradoRSA()
        
menuCifradoRSA()
