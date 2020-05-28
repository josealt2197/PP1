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
    llavePublica=""
    llavePrivada=""
    p=randint(0,1000)
    q=randint(0,1000)
    n=0
    fiDeN=0
    e=0
    d=0

    #Paso 1
    while(esPrimo(p)!=True and esPrimo(p)!=True):
        p=randint(0,1000)
        q=randint(0,1000)

    # print("p= "+str(p))
    # print("q= "+str(q))
    
    #Paso 2
    n=p*q
    # print("n= "+str(n))
    
    #Paso 3
    fiDeN=(p-1)*(q-1)
    # print("fiDeN= "+str(fiDeN))
    
    #Paso 4
    e=randint(0,fiDeN)
    while(calcularMCD(fiDeN,e)!=1):
        e=randint(0,fiDeN)
    # print("e= "+str(e))
    
    #Paso 5
    d=1
    while(((e*d) + (fiDeN * -1))!=1): 
        d+=1

    # print("d= "+str(d))

    claves= "Llaves generadas:" "Publica: ("+str(n)+", "+str(e)+") y Privada: ("+str(n)+", "+str(d)+")" 
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
    print("Digite la clave publica requerida para cifrar la frase/palabra")
    n=int(input("-->Ingrese el primer valor de la clave: "))
    e=int(input("-->Ingrese el segundo valor de la clave: "))
    cadenaResultante = ""
    letraResultante = ""
    indice = 0
    
    while(indice != len(cadena)):
        if(cadena[indice].isascii()==True):
            letraResultante=str((ord(cadena[indice])**e)%n)
        else:
            letraResultante=cadena[indice]

        cadenaResultante = cadenaResultante + "*"+ letraResultante
        indice+=1
        
    return cadenaResultante[1:]

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
    
    while(indice != len(letrasSeparadas)):
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
    divisor = min(a,b)

    while(divisor>1):
        if(a%divisor==0 and b%divisor==0):
            break
        divisor-=1

    return divisor

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
        
#menuCifradoRSA()
