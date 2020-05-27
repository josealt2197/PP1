'''
****Guía de Código Fuente***

 -- Funciones Adicionales...........................~ln:20
 -- Algoritmos de Cirado
    -- Cifrado/Descifrado César....................~ln:124
    -- Cifrado/Descifrado por llave................~ln:175
    -- Cifrado/Descifrado Sustitución Vigenére.....~ln:250
    -- Cifrado/Descifrado RSA......................~ln:316
    -- Cifrado/Descifrado Palabra inversa..........~ln:432
    -- Cifrado/Descifrado Mensaje inverso..........~ln:457
    -- Cifrado/Descifrado Telefonico...............~ln:475
    -- Cifrado/Descifrado Binario..................~ln:624
-- Validacion de Entradas..........................~ln:705
-- Menús de Navegación
    -- Menu Cifrado................................~ln:787
    -- Menu Descifrado.............................~ln:873
    -- Menu Principal..............................~ln:962
'''
# --------------------------------------------Funciones Adicionales----------------------------------------------------------------------------

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
    divisor = 2

    while (divisor < num):
        if (num % divisor == 0):
            return False
        divisor = divisor + 1

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
    divisor = min(a, b)

    while (divisor > 1):
        if (a % divisor == 0 and b % divisor == 0):
            break
        divisor -= 1

    return divisor


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

    while (indice != len(cadena)):
        if (esEntero(cadena[indice]) == True):
            return True
        indice += 1

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

    while (indice != len(cadena)):
        if (cadena[indice] == caracter):
            return indice
        indice += 1

    return -1


# --------------------------------------------Cifrado/Descifrado Cesar----------------------------------------------------------------------------

'''
    Entradas:
        - Un parametro "opcion", el cual determina si se debe realizar un procesos de "cifrado" o "descrifrado"
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada o descifrada con el algoritmo de cifrado César
    Restricciones:
        - No hay.

'''
def cifrarDescifrar_CodigoCesar(operacion, cadena):
    cadena = cadena.upper()
    cadenaResultante = ""
    indice = 0

    while (indice != len(cadena)):
        cadenaResultante = cadenaResultante + cifrarDescifrarLetra_CodigoCesar(cadena[indice], operacion)
        indice += 1

    if (operacion == "descifrado"):
        cadenaResultante = cadenaResultante.lower()

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

    if (buscarCaracter(letras, letra) != -1):
        if (operacion == "cifrado"):
            letraCifrada_Descifrada = letrasDesplazadas[buscarCaracter(letras, letra)]
        else:
            letraCifrada_Descifrada = letras[buscarCaracter(letrasDesplazadas, letra)]
        return letraCifrada_Descifrada
    else:
        return letra


# --------------------------------------------Cifrado/Descifrado Por Llave----------------------------------------------------------------------------
'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado por Llave
    Restricciones:
        - No hay.

'''
def cifrarDescifrar_CodigoPorLlave(operacion, cadena):
    clave = input("Digite la clave requerida para cifrar la palabra/frase: ")
    if (len(clave) <= 1):
        print("Se ha producido un ERROR: La clave debe estar compuesta por al menos dos caracteres")
    else:
        cadena = cadena.lower()
        cadenaResultante = ""
        letraResultante = ""
        indice = 0
        indiceClave = 0

        while (indice != len(cadena)):
            if (cadena[indice].isalpha() == True):
                letraResultante = cifrarDescifrarLetra_CodigoPorLlave(cadena[indice], operacion, clave[indiceClave])
                indiceClave += 1
            elif (cadena[indice] == " "):
                letraResultante = cadena[indice]
            else:
                letraResultante = " "

            if (indiceClave == (len(clave))):
                indiceClave = 0

            cadenaResultante = cadenaResultante + letraResultante
            indice += 1

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

    if (buscarCaracter(letras, letra) != -1 and buscarCaracter(letras, clave) != -1):

        if (operacion == "cifrado"):
            posLetraCifrada_Descifrada = (buscarCaracter(letras, letra) + 1) + (buscarCaracter(letras, clave) + 1)

            if (posLetraCifrada_Descifrada > 26):
                posLetraCifrada_Descifrada = posLetraCifrada_Descifrada - 26
        else:
            posLetraCifrada_Descifrada = (buscarCaracter(letras, letra) + 1) - (buscarCaracter(letras, clave) + 1)

            if (posLetraCifrada_Descifrada < 0):
                posLetraCifrada_Descifrada = posLetraCifrada_Descifrada + 26

            letraCifrada_Descifrada = letras[posLetraCifrada_Descifrada - 1]

        letraCifrada_Descifrada = letras[posLetraCifrada_Descifrada - 1]

        return letraCifrada_Descifrada
    else:
        return letra


# --------------------------------------------Cifrado/Descifrado por Sustitucion Vigenére------------------------------------------------------------
'''
    Entradas:
        - Una cadena de carateres 
        - Un parametro "opcion", el cual determina si se debe realizar un procesos de "cifrado" o "descrifrado"
    Salida:
        - El valor de la cadena cifrada o descifrada con el algoritmo de cifrado por Sustitución Vigenére
    Restricciones:
        - No hay.

'''
def cifrarDescifrar_SustitucionVigenere(operacion, cadena):
    clave = input("Digite la clave requerida para cifrar/descifrar la palabra/frase: ")
    if (clave == "" or len(clave) != 2):
        print("Se ha producido un ERROR: La clave debe estar compuesta por dos dígitos")
    else:
        if (esEntero(clave) == True):
            cadena = cadena.lower()
            clave1 = int(clave[0])
            clave2 = int(clave[1])
            cadenaResultante = ""
            letraResultante = ""
            indice = 0

            while (indice != len(cadena)):
                if (cadena[indice] == " "):
                    letraResultante = " "
                elif ((indice + 1) % 2 != 0):
                    letraResultante = cifrarDescifrarLetra_CodigoVigenere(cadena[indice], operacion, clave1)
                else:
                    letraResultante = cifrarDescifrarLetra_CodigoVigenere(cadena[indice], operacion, clave2)

                cadenaResultante = cadenaResultante + letraResultante
                indice += 1

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

    if (buscarCaracter(letras, letra) != -1):
        if (operacion == "cifrado"):
            letraCifrada_Descifrada = letras[(buscarCaracter(letras, letra) + clave)]
        else:
            letraCifrada_Descifrada = letras[(buscarCaracter(letras, letra) - clave)]

        return letraCifrada_Descifrada
    else:
        return letra


# --------------------------------------------Cifrado/Descifrado RSA----------------------------------------------------------------------------
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
    llavePublica = ""
    llavePrivada = ""
    p = randint(1000, 10000)
    q = randint(1000, 10000)
    n = 0
    fiDeN = 0
    e = 0
    d = 0

    # Paso 1
    while (esPrimo(p) == False and esPrimo(p) == False):
        p = randint(1000, 10000)
        q = randint(1000, 10000)

    print("p= " + str(p))
    print("q= " + str(q))

    # Paso 2
    n = p * q
    print("n= " + str(n))

    # Paso 3
    fiDeN = (p - 1) * (q - 1)
    print("fiDeN= " + str(fiDeN))

    # Paso 4
    e = randint(0, fiDeN)
    while (calcularMCD(fiDeN, e) != 1):
        e = randint(0, fiDeN)
    print("e= " + str(e))

    # Paso 5
    d = randint(0, 1000)
    while (((d * e) - 1) % fiDeN != 0):
        d = randint(0, 1000)
    print("d= " + str(d))

    print("Llaves generadas: ")
    print("Publica: (" + str(n) + ", " + str(e) + ")")
    print("Privada: (" + str(n) + ", " + str(d) + ")")


'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado RSA
    Restricciones:
        - No hay.

'''
def cifrar_CodigoRSA(cadena):
    print("Digite la clave publica requerida para cifrar la frase/palabra")
    n = int(input("-->Ingrese el primer valor de la clave: "))
    e = int(input("-->Ingrese el segundo valor de la clave: "))
    d = 2753
    cadenaResultante = ""
    letraResultante = ""
    indice = 0

    while (indice != len(cadena)):
        if (cadena[indice].isascii() == True):
            letraResultante = str((ord(cadena[indice]) ** e) % n)
        else:
            letraResultante = cadena[indice]

        cadenaResultante = cadenaResultante + "*" + letraResultante
        indice += 1

    return cadenaResultante[1:] 
        #+ "\nLlave Pública: ("+str(n)+","+str(e)+")" + "\nLlave Privada: ("+str(n)+","+str(d)+")")


'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado RSA
    Restricciones:
        - No hay.

'''
def descifrar_CodigoRSA(cadena):
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


# --------------------------------------------Cifrado/Descifrado Palabra Inversa----------------------------------------------------------------------
'''
    Entradas:
        - Una cadena de carateres 
    Salida:
        - El valor de la cadena con los carateres de sus palabras
          en una posicion inversa
    Restricciones:
        - No hay.

'''
def cifrar_descifrar_PalabraInversa(cadena):
    palabras = cadena.split()
    palabra = ""
    cadenaCifrada = ""
    contador = 0

    while (contador < len(palabras)):
        palabra = palabras[contador]
        cadenaCifrada = cadenaCifrada + palabra[::-1] + " "
        contador += 1

    return cadenaCifrada


# --------------------------------------------Cifrado/Descifrado Mensaje Inverso----------------------------------------------------------------------------
'''
    Entradas:
        - Una cadena de carateres 
    Salida:
        - El valor de la cadena de carateres con sus caracteres
          en posiciones inversas a las originales.
    Restricciones:
        - No hay.

'''
def cifrarDescifrar_MensajeInverso(cadena):
    cadenaDescifrada = cadena[::-1]
    indice = 0

    return cadenaDescifrada


# --------------------------------------------Cifrado/Descifrado Código Telefónico----------------------------------------------------------------------------
'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado telefónico.
    Restricciones:
        - No hay.

'''
def cifrar_CodigoTelefonico(cadena):
    cadena = cadena.lower()
    cadenaCifrada = ""
    indice = 0

    while (indice != len(cadena)):
        cadenaCifrada = cadenaCifrada + cifrarLetra_CodigoTelefonico(cadena[indice])
        indice += 1

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

    if (buscarCaracter(letras, letra) != -1):
        while (inicio < 25):

            bloque = letras[inicio:fin]

            if (buscarCaracter(bloque, letra) == -1):
                if (numeroAsignado == 5 or numeroAsignado == 7):
                    inicio += 3
                    fin += 4
                elif (numeroAsignado == 6):
                    inicio += 4
                    fin += 3
                else:
                    inicio += 3
                    fin += 3

                numeroAsignado += 1
            else:
                return str(numeroAsignado + 1) + str(buscarCaracter(bloque, letra) + 1)

    elif (letra == " "):
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
def descifrar_CodigoTelefonico(cadena):
    cadena = cadena.lower()
    cadenaDescifrada = ""
    letraCifrada = ""
    indice = 0

    while (indice != len(cadena)):

        if (cadena[indice] == "*"):
            cadenaDescifrada = cadenaDescifrada + " "

        elif (esEntero(cadena[indice]) == True):
            letraCifrada = letraCifrada + cadena[indice]
            if (len(letraCifrada) == 2):
                cadenaDescifrada = cadenaDescifrada + descifrarLetra_CodigoTelefonico(letraCifrada)
                letraCifrada = ""
        else:
            cadenaDescifrada = cadenaDescifrada + cadena[indice]

        indice += 1

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
    # numeros = "23456789"

    # Recuperar Numero Asignado
    numeroAsignado = letraCifrada[0]
    # Recuperar Numero de Letra
    codigoLetra = letraCifrada[1]

    if (numeroAsignado == "2"):
        bloque = letras[0:3]

    elif (numeroAsignado == "3"):
        bloque = letras[3:6]

    elif (numeroAsignado == "4"):
        bloque = letras[6:9]

    elif (numeroAsignado == "5"):
        bloque = letras[9:12]

    elif (numeroAsignado == "6"):
        bloque = letras[12:15]

    elif (numeroAsignado == "7"):
        bloque = letras[15:19]

    elif (numeroAsignado == "8"):
        bloque = letras[19:22]

    else:
        bloque = letras[22:25]

    return bloque[int(codigoLetra) - 1]


# --------------------------------------------Cifrado Binario----------------------------------------------------------------------------
'''
    Entradas:
        - Una cadena de carateres en lenguaje natural
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado Binario
    Restricciones:
        - No hay.

'''
def cifrar_CodigoBinario(cadena):
    cadena = cadena.lower()
    cadenaResultante = ""
    letraResultante = ""
    indice = 0
    indiceClave = 0

    while (indice != len(cadena)):
        if (cadena[indice].isalpha() == True):
            letraResultante = " " + cifrarLetra_CodigoBinario(cadena[indice])
        elif (cadena[indice] == " "):
            letraResultante = " *"
        else:
            letraResultante = cadena[indice]

        cadenaResultante = cadenaResultante + letraResultante
        indice += 1

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
    letraCifrada = ""
    letras = "abcdefghijklmnopqrstuvwxyz"

    if (buscarCaracter(letras, letra) != -1):

        letraCifrada = format(buscarCaracter(letras, letra), '05b')

        return letraCifrada
    else:
        return letra


def descifrar_CodigoBinario(cadena):
    binario = ""
    resultado = ""
    while (cadena != ""):

        if (cadena[0] == "*"):
            resultado = resultado + " "
            cadena = cadena[2:]
        else:
            binario = cadena[0:5]
            resultado = resultado + sacarLetra(binario)
            cadena = cadena[6:]

    return resultado


def sacarLetra(binario):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    binario = str(binario)
    letra = abecedario[int(binario, 2)]
    return letra


# --------------------------------------------Validacion de Entradas----------------------------------------------------------------------------

def validarEntradaCifrado(numCifrado):
    
    fraseSoloABC = "12378"
    fraseSoloAscii = "456"

    entradaValida = False 

    abecedario = "abcdefghijklmnopqrstuvwxyz "
    abecedarioAst = "abcdefghijklmnopqrstuvwxyz*"

    cadena = input("Ingrese la frase o palabra que desea cifrar: ")
    if (cadena==""):
        return "-1"
    else:
        if (buscarCaracter(fraseSoloABC, str(numCifrado)) != -1):
            indice=0
            while (indice != len(cadena)):
                if(buscarCaracter(abecedario, cadena[indice].lower())==-1):
                    return "-2"
                indice+=1
            entradaValida = True
        else:
            if (buscarCaracter(fraseSoloAscii, str(numCifrado)) != -1):
                if(cadena.isascii()==True):
                    entradaValida = True
                else:
                    return "-3"
        
        if(entradaValida == True):
            return cadena        

def validarEntradaDescifrado(numCifrado):
    
    fraseSoloABC = "123"
    fraseSoloAscii = "456"
    fraseABCyAst = "7"
    fraseSoloBin = "8"

    entradaValida = False 

    abecedario = "abcdefghijklmnopqrstuvwxyz "
    abecedarioAst = "abcdefghijklmnopqrstuvwxyz*"
    charBin = "01* "

    cadena = input("Ingrese la frase o palabra que desea cifrar: ")
    if (cadena==""):
        return -1
    else:

        if (buscarCaracter(fraseSoloABC, numCifrado) != -1):
            indice=0
            while (indice != len(cadena)):
                if(buscarCaracter(abecedario, cadena[indice].lower())==-1):
                    return "-2"
                indice+=1
            entradaValida = True
        else:
            if (buscarCaracter(fraseSoloAscii, str(numCifrado)) != -1):
                if(cadena.isascii()==True):
                    entradaValida = True
                else:
                    return "-3" 
            else:
                if (buscarCaracter(fraseABCyAst, numCifrado) != -1):
                    indice=0
                    while (indice != len(cadena)):
                        if(buscarCaracter(abecedarioAst, cadena[indice].lower())==-1):
                            return -4
                        indice+=1
                    entradaValida = True

                else:
                    if (buscarCaracter(fraseSoloBin, numCifrado) != -1):
                        indice=0
                        while (indice != len(cadena)):
                            if(buscarCaracter(charBin, cadena[indice].lower())==-1):
                                return -5
                            indice+=1
                    entradaValida = True
        
        if(entradaValida == True):
            return cadena       

# def validarClaveCifrado(numCifrado):
    
#     fraseSoloNum = "3"
#     fraseSoloABC = "2"

#     entradaValida = False 

#     numeros = "0123456789"
#     abecedario = "abcdefghijklmnopqrstuvwxyz"

#     clave = input("Digite la clave requerida para cifrar la palabra/frase: ")
#     if (cadena==""):
#         return "-1"
#     else:
#         if (buscarCaracter(fraseSoloNum, str(numCifrado)) != -1):
#             indice=0
#             while (indice != len(cadena)):
#                 if(buscarCaracter(numeros, cadena[indice].lower())==-1):
#                     return "-2"
#                 indice+=1
#             entradaValida = True
#         else:
#             if (buscarCaracter(fraseSoloAscii, str(numCifrado)) != -1):
#                 if(cadena.isascii()==True):
#                     entradaValida = True
#                 else:
#                     return "-3"
        
#         if(entradaValida == True):
#             return cadena        


# --------------------------------------------Menu Cifrado----------------------------------------------------------------------------
def menuCifrado():
    opcionesValidas = "12345678"

    print("\t---------------------")
    print("\t  Opciones de Cifrado")
    print("\t-----------------------")
    print("\nSeleccione una de las opciones.")
    print("Digite el numero correspondiente.")
    print("\n1. Cifrado Cesar")
    print("2. Cifrado Por Llave")
    print("3. Cifrado por Sustitucion Vigenére")
    print("4. Cifrado RSA")
    print("5. Cifrado Palabra Inversa")
    print("6. Cifrado Mensaje Inverso")
    print("7. Cifrado Telefónico")
    print("8. Cifrado Binario")
    print("9. Regresar al Menú Principal")

    try:
        opcion = int(input("\nOpcion: "))
    except:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuCifrado()

    print("\n")

    if (buscarCaracter(opcionesValidas, str(opcion)) != -1):
        resultadoEntrada = validarEntradaCifrado(opcion)
        if(resultadoEntrada=="-1"):       
            print("*** Se ha producido un ERROR: Es necesario que ingrese una valor para palabra o frase ***")
            menuDescifrado()
        elif(resultadoEntrada=="-2"):       
            print("*** Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos ***")
            menuDescifrado()
        elif(resultadoEntrada=="-3"):
            print("*** Se ha producido un ERROR: La palabra o frase SOLO debe contener caracteres ASCII ***")
            menuDescifrado()
        elif(resultadoEntrada=="-4"):
            print("*** Se ha producido un ERROR: La palabra o frase SOLO debe contener caracteres del alfabeto o el símbolo \"*\" ***")
            menuDescifrado()
        else:
            if (opcion == 1):
                print("La frase o palabra cifrada es la siguiente: " + cifrarDescifrar_CodigoCesar("cifrado", resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
            elif (opcion == 2):
                print("La frase o palabra cifrada es la siguiente: " + cifrarDescifrar_CodigoPorLlave("cifrado", resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
            elif (opcion == 3):
                print("La frase o palabra cifrada es la siguiente: " + cifrarDescifrar_SustitucionVigenere("cifrado", resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
            elif (opcion == 4):
                print("La frase o palabra cifrada es la siguiente: " + cifrar_CodigoRSA(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
            elif (opcion == 5):
                print("La frase o palabra cifrada es la siguiente: " + cifrar_descifrar_PalabraInversa(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
            elif (opcion == 6):
                print("La frase o palabra cifrada es la siguiente: " + cifrarDescifrar_MensajeInverso(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
            elif (opcion == 7):
                print("La frase o palabra cifrada es la siguiente: " + cifrar_CodigoTelefonico(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
            elif (opcion == 8):
                print("La frase o palabra cifrada es la siguiente: " + cifrar_CodigoBinario(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuCifrado()
    else:
        if (opcion == 9):
            menuPrincipal()
        else:
            print("\t*************************************")
            print("\tOpcion no valida, vuelva a intentarlo")
            print("\t*************************************")
            menuCifrado()


# --------------------------------------------Menu Descifrado----------------------------------------------------------------------------
def menuDescifrado():
    opcionesValidas = "12345678"

    print("\t------------------------")
    print("\t  Opciones de Descifrado")
    print("\t--------------------------")
    print("\nSeleccione una de las opciones.")
    print("Digite el numero correspondiente.")
    print("\n1. Descifrado Cesar")
    print("2. Descifrado Por Llave")
    print("3. Descifrado por Sustitucion Vigenére")
    print("4. Descifrado RSA")
    print("5. Descifrado Palabra Inversa")
    print("6. Descifrado Mensaje Inverso")
    print("7. Descifrado Telefónico")
    print("8. Descifrado Binario")
    print("9. Regresar al Menú Principal")

    try:
        opcion = int(input("\nOpcion: "))
    except:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuDescifrado()

    print("\n")

    if (buscarCaracter(opcionesValidas, str(opcion)) != -1):
        resultadoEntrada = validarEntradaDescifrado(opcion)
        if(resultadoEntrada=="-1"):       
            print("*** Se ha producido un ERROR: Es necesario que ingrese una valor para palabra o frase ***")
            menuDescifrado()
        elif(resultadoEntrada=="-2"):       
            print("*** Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos ***")
            menuDescifrado()
        elif(resultadoEntrada=="-3"):
            print("*** Se ha producido un ERROR: La palabra o frase SOLO debe contener caracteres ASCII ***")
            menuDescifrado()
        elif(resultadoEntrada=="-4"):
            print("*** Se ha producido un ERROR: La palabra o frase SOLO debe contener caracteres del alfabeto o el símbolo \"*\" ***")
            menuDescifrado()
        elif(resultadoEntrada=="-5"):
            print("*** Se ha producido un ERROR: La palabra o frase SOLO puede contener los caracteres 1, 0, el símbolo * o espacios en blanco ***")
            menuDescifrado()
        else:
            if (opcion == 1):
                print("La frase o palabra descifrada es la siguiente: " + cifrarDescifrar_CodigoCesar("descifrado", resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
            elif (opcion == 2):
                print("La frase o palabra descifrada es la siguiente: " + cifrarDescifrar_CodigoPorLlave("descifrado", resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
            elif (opcion == 3):
                print("La frase o palabra descifrada es la siguiente: " + cifrarDescifrar_SustitucionVigenere("descifrado", resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
            elif (opcion == 4):
                print("La frase o palabra descifrada es la siguiente: " + descifrar_CodigoRSA(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
            elif (opcion == 5):
                print("La frase o palabra descifrada es la siguiente: " + cifrar_descifrar_PalabraInversa(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
            elif (opcion == 6):
                print("La frase o palabra descifrada es la siguiente: " + cifrarDescifrar_MensajeInverso(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
            elif (opcion == 7):
                print("La frase o palabra descifrada es la siguiente: " + descifrar_CodigoTelefonico(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
            elif (opcion == 8):
                print("La frase o palabra descifrada es la siguiente: " + descifrar_CodigoBinario(resultadoEntrada))
                input("\n-->Presione la tecla enter para continuar...")
                menuDescifrado()
    else:    
        if (opcion == 9):
            menuPrincipal()
        else:
            print("\t*************************************")
            print("\tOpcion no valida, vuelva a intentarlo")
            print("\t*************************************")
            menuDescifrado()


# --------------------------------------------Menu Principal----------------------------------------------------------------------------
def menuPrincipal():
    opcion = 0

    print("\n\t------------------")
    print("\t  Menu Principal")
    print("\t--------------------")
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
        menuPrincipal()

    print("\n")

    if (opcion == 1):
        menuCifrado()
        input("\n-->Presione la tecla Enter para continuar...")
        menuPrincipal()
    elif (opcion == 2):
        menuDescifrado()
        input("\n-->Presione la tecla Enter para continuar...")
        menuPrincipal()
    elif (opcion == 3):
        print("\t----------------------")
        print("\tPrograma Finalizado")
        print("\t----------------------")
    else:
        print("\t*************************************")
        print("\tOpcion no valida, vuelva a intentarlo")
        print("\t*************************************")
        menuPrincipal()


menuPrincipal()
