import sys
import random

'''
                Tecnologico de Costa Rica 

            TI 1401 - Taller de Programación   

                Primer Proyecto Programado 

            Técnicas de Cifrado de Mensajes

    Estudiantes:
           José Altamirano Salazar - 2020426159
              Josué Brenes Alfaro - 2020054427

'''
# --------------------------------------------Funciones Adicionales----------------------------------------------------------------------------

'''
Determinar si un numero es primo 
    Entradas:
        - Un valor de tipo entero 
    Salidas:
        - True si el valor recibido es primo
        - False si el valor recibido no es primo
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
        - Dos números enteros mayores a cero.
    Salida:
        - El valor del Máximo Común Divisor entre ambos numeros.
    Restricciones:
        - No hay.
'''
def calcularMCD(a, b):
    divisor = 1
    while(divisor <= a and divisor <= b):
        if(a % divisor == 0 and b % divisor == 0):
            mcd = divisor
        divisor += 1
    return mcd


'''
Buscar un valor numerico dentro de una cadena
    Entradas:
        - Una cadena de caracteres
    Salida:
        - True si alguno de los caracteres de la cadena corresponde a un valor numérico
        - False si ninguno de los caracteres de la cadena corresponde a un valor numérico 
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
Determinar si una cadena o caracter interpretarse como un entero
    Entradas:
        - Un valor de tipo cadena o caracter a ser validado.
    Salidas:
        - True: si el valor recibido puede convertirse a entero
        - False: si no es posible convertir el valor recibido a entero
    Restricciones:
        - No hay
'''
def esEntero(pNum):
    try:
        resultado = int(pNum)
        return True
    except:
        return False


'''
Buscar un caracter especifico dentro de una cadena de caracteres
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


def invertirOrden(cadena):
    indice=0
    resultado=""
    while( indice<len(cadena)):
        letra=cadena[indice]
        resultado=letra+resultado
        indice+=1
    return resultado

# --------------------------------------------Cifrado/Descifrado Cesar----------------------------------------------------------------------------

'''
Cifrar o Descifrar una frase con el algoritmo de cifrado Cesar
    Entradas:
        - Un parametro "operacion" de tipo cadena de caracteres, el cual determina si se 
          debe realizar un procesos de "cifrado" o "descifrado"
        - Una cadena de carateres 
    Salida:
        - El valor de la cadena recibida como parametro cifrada o descifrada con el 
          algoritmo de cifrado César
    Restricciones:
        - No hay.
'''
def cifrarDescifrarCesar(operacion, cadena):
    cadena = cadena.upper()
    cadenaResultante = ""
    indice = 0

    while (indice != len(cadena)):
        cadenaResultante = cadenaResultante + cifrarDescifrarLetraCesar(cadena[indice], operacion)
        indice += 1

    if (operacion == "descifrado"):
        cadenaResultante = cadenaResultante.lower()

    return cadenaResultante


'''
Sustituir una letra según el proceso de cifrado o descifrado del algoritmo de cifrado Cesar
    Entradas:
        - Un valor unico de tipo caracter
        - Un parametro "operacion" de tipo cadena de caracteres, el cual determina si se 
          debe realizar un procesos de "cifrado" o "descifrado"
    Salida:
        - El valor del caracter cifrado o descifrado con el algoritmo de cifrado César
    Restricciones:
        - No hay.
'''
def cifrarDescifrarLetraCesar(letra, operacion):
    letraCifradaDescifrada = ""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letrasDesplazadas = "DEFGHIJKLMNOPQRSTUVWXYZABC"

    if (buscarCaracter(letras, letra) != -1):
        if (operacion == "cifrado"):
            letraCifradaDescifrada = letrasDesplazadas[buscarCaracter(letras, letra)]
        else:
            letraCifradaDescifrada = letras[buscarCaracter(letrasDesplazadas, letra)]
        return letraCifradaDescifrada
    else:
        return letra


# --------------------------------------------Cifrado/Descifrado Por Llave----------------------------------------------------------------------------
'''
Cifrar o Descifrar una frase con el algoritmo de cifrado Por Llave
    Entradas:
        - Un parametro "operacion" de tipo cadena de caracteres, el cual determina si se 
          debe realizar un procesos de "cifrado" o "descifrado"
        - Una cadena de carateres con la frase a ser cifrada o descifrada
        - Una cadena de caracteres con el valor de la clave requerida por el algoritmo
          de cifrado Por Llave
    Salida:
        - El valor de la cadena cifrada o descifrada con el algoritmo de cifrado Por Llave
    Restricciones:
        - No hay.
'''
def cifrarDescifrarPorLlave(operacion, cadena, clave):
    cadena = cadena.lower()
    cadenaResultante = ""
    letraResultante = ""
    indice = 0
    indiceClave = 0

    while (indice != len(cadena)):
        if (cadena[indice].isalpha() == True):
            letraResultante = cifrarDescifrarLetraPorLlave(cadena[indice], operacion, clave[indiceClave])
            indiceClave += 1
        elif (cadena[indice] == " "):
            letraResultante = cadena[indice]
        else:
            letraResultante = letraResultante
        if (indiceClave == (len(clave))):
            indiceClave = 0

        cadenaResultante = cadenaResultante + letraResultante
        indice += 1

    if (operacion == "descifrado"):
        cadenaResultante = cadenaResultante.lower()

    return cadenaResultante


'''
Sustituir una letra según el proceso de cifrado o descifrado del algoritmo de cifrado Por Llave
    Entradas:
        - Un valor unico de tipo caracter a ser cifrado o descifrado
        - Un parametro "operacion" de tipo cadena de caracteres, el cual determina si se 
          debe realizar un procesos de "cifrado" o "descifrado"
        - Un valor unico de tipo caracter a ser utilizado como la clave por el algoritmo 
          de cifrado
    Salida:
        - El valor del caracter cifrado o descifrado con el algoritmo de cifrado Por Llave
    Restricciones:
        - No hay.
'''
def cifrarDescifrarLetraPorLlave(letra, operacion, clave):
    posLetraCifradaDescifrada = 0
    letraCifradaDescifrada = ""
    letras = "abcdefghijklmnopqrstuvwxyz"

    if (buscarCaracter(letras, letra) != -1 and buscarCaracter(letras, clave) != -1):

        if (operacion == "cifrado"):
            posLetraCifradaDescifrada = (buscarCaracter(letras, letra) + 1) + (buscarCaracter(letras, clave) + 1)

            if (posLetraCifradaDescifrada > 26):
                posLetraCifradaDescifrada = posLetraCifradaDescifrada - 26
        else:
            posLetraCifradaDescifrada = (buscarCaracter(letras, letra) + 1) - (buscarCaracter(letras, clave) + 1)

            if (posLetraCifradaDescifrada < 0):
                posLetraCifradaDescifrada = posLetraCifradaDescifrada + 26

            letraCifradaDescifrada = letras[posLetraCifradaDescifrada - 1]

        letraCifradaDescifrada = letras[posLetraCifradaDescifrada - 1]

        return letraCifradaDescifrada
    else:
        return letra


# --------------------------------------------Cifrado/Descifrado por Sustitucion Vigenére------------------------------------------------------------
'''
Cifrar o Descifrar una frase con el algoritmo de cifrado por Sustitucion Vigenére
    Entradas:
        - Un parametro "operacion" de tipo cadena de caracteres, el cual determina si se 
          debe realizar un procesos de "cifrado" o "descifrado"
        - Una cadena de carateres con la frase a ser cifrada o descifrada
        - Una cadena de caracteres con el valor de la clave requerida por el algoritmo
          de cifrado por Sustitucion Vigenére
    Salida:
        - El valor de la cadena cifrada o descifrada con el algoritmo de cifrado por Sustitución Vigenére
    Restricciones:
        - No hay.
'''
def cifrarDescifrarSustitucionVigenere(operacion, cadena, clave):
    cadena = cadena.lower()
    clave1 = int(clave[0])
    clave2 = int(clave[1])
    cadenaResultante = ""
    letraResultante = ""
    indice = 0
    posicion = 1

    while (indice != len(cadena)):
        if (cadena[indice] == " "):
            letraResultante = " "
            posicion=1
        elif (posicion % 2 != 0):
            letraResultante = cifrarDescifrarLetraSustitucionVigenere(cadena[indice], operacion, clave1)
            posicion += 1
        else:
            letraResultante = cifrarDescifrarLetraSustitucionVigenere(cadena[indice], operacion, clave2)
            posicion += 1

        cadenaResultante = cadenaResultante + letraResultante
        indice += 1
        

    return cadenaResultante


'''
Sustituir una letra según el proceso de cifrado o descifrado del algoritmo de cifrado por Sustitucion Vigenére
    Entradas:
        - Un valor unico de tipo caracter a ser cifrado o descifrado
        - Un parametro "operacion" de tipo cadena de caracteres, el cual determina si se 
          debe realizar un procesos de "cifrado" o "descifrado"
        - Un valor unico de tipo entero a ser utilizado como la clave por el algoritmo 
          de cifrado
    Salida:
        - El valor del caracter cifrado o descifrado con el algoritmo de cifrado por Sustitucion Vigenére
    Restricciones:
        - No hay.
'''
def cifrarDescifrarLetraSustitucionVigenere(letra, operacion, clave):
    letraCifrada_Descifrada = ""
    letrasCifrado = "abcdefghijklmnopqrstuvwxyzabcdefghi"
    letrasDescifrado = "abcdefghijklmnopqrstuvwxyz"

    if (buscarCaracter(letrasDescifrado, letra) != -1):
        if (operacion == "cifrado"):
            letraCifrada_Descifrada = letrasCifrado[(buscarCaracter(letrasCifrado, letra) + clave)]
        else:
            letraCifrada_Descifrada = letrasDescifrado[(buscarCaracter(letrasDescifrado, letra) - clave)]

        return letraCifrada_Descifrada
    else:
        return letra


# --------------------------------------------Cifrado/Descifrado RSA----------------------------------------------------------------------------
'''
Obtener las llaves publica y privada para el cifrado RSA, llamar a la funcion de cifrado y retornar la cadena cifrada
    Entradas:
        - Una cadena de carateres con la frase a ser cifrada
    Salidas:
        - El valor de la cadena cifrada con el algoritmo de cifrado RSA
        - Una Cadena de caracteres compuesta por los valores de las llaves 
          publica (n,e ) y privada (n,d) 
    Restricciones:
        - Ninguna
'''
def cifrarRSA(cadena):
    p=random.randint(1,1000)
    q=random.randint(1,1000)
    n=0
    fiDeN=0
    e=0
    d=0

    #Paso 1
    while(esPrimo(p)!=True and esPrimo(q)!=True):
        p=random.randint(1,1000)
        q=random.randint(1,1000)
    
    #Paso 2
    n=p*q
    
    #Paso 3
    fiDeN=(p-1)*(q-1)
    
    #Paso 4
    e=random.randint(3,fiDeN-2)
    while(calcularMCD(fiDeN,e)!=1):
        e=random.randint(0,fiDeN)
    
    #Paso 5
    d=1
    x=((d*e)-1)%fiDeN
    while(x!=0): 
        d+=1
        x=((d*e)-1)%fiDeN

    cadenaDeRetorno = cifrarFraseRSA(cadena, n, e)

    cadenaDeRetorno =  cadenaDeRetorno + "\n-->Las llaves generadas son: Publica: ("+str(n)+", "+str(e)+") y Privada: ("+str(n)+", "+str(d)+")" 

    return cadenaDeRetorno

'''
Cifrar una frase con el algoritmo de cifrado RSA
    Entradas:
        - Una cadena de carateres con la frase a ser cifrada
        - Valores de la Clave Publica (n y e)
    Salida:
        - El valor de la cadena cifrada  con el algoritmo de cifrado RSA
    Restricciones:
        - No hay.
'''
def cifrarFraseRSA(cadena, n, e):
    cadenaResultante = ""
    letraResultante = ""
    indice = 0
    
    while(indice != len(cadena)):
        if(cadena[indice].isascii()==True):
            letraResultante=(ord(cadena[indice])**e)%n
        else:
            letraResultante=cadena[indice]

        cadenaResultante = cadenaResultante + "*"+ str(letraResultante)
        indice+=1

    return cadenaResultante[1:]

'''
Desifrar una frase con el algoritmo de cifrado RSA
    Entradas:
        - Una cadena de carateres con la frase a ser descifrada
    Salida:
        - El valor de la cadena descifrada con el algoritmo de cifrado RSA
    Restricciones:
        - No hay.
'''
def descifrarRSA(cadena, n, d):
    n=int(n)
    d=int(d)
    cadenaResultante = ""
    letrasSeparadas = cadena.split("*")
    letraResultante = ""
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
Cifrar o Descifrar una frase con el algoritmo de cifrado Palabra Inversa
    Entradas:
        - Una cadena de carateres con la frase a ser cifrada o descifrada
    Salida:
        - El valor de la cadena cifrada o descifrada con los carateres de sus palabras
          en una posicion inversa
    Restricciones:
        - No hay.
'''
def cifrarDescifrarPalabraInversa(cadena):
    cadena=cadena+" "
    palabra=""
    cadNueva=""
    while(cadena!=""):
        if(cadena[0]!=" "):
            palabra=palabra+cadena[0]
        else:
            cadNueva=cadNueva+" "+invertirOrden(palabra)
            palabra=""
        cadena=cadena[1:]
    
    return cadNueva[1:]



# --------------------------------------------Cifrado/Descifrado Mensaje Inverso----------------------------------------------------------------------------
'''
Cifrar o Descifrar una frase con el algoritmo de cifrado Mensaje Inverso
    Entradas:
        - Una cadena de carateres con la frase a ser cifrada o descifrada
    Salida:
        - El valor de la cadena cifrada o descifrada con sus carateres 
          en una posicion inversa a la original
    Restricciones:
        - No hay.
'''
def cifrarDescifrarMensajeInverso(cadena):
    cadenaDescifrada = invertirOrden(cadena)

    return cadenaDescifrada


# --------------------------------------------Cifrado/Descifrado por Código Telefónico----------------------------------------------------------------------------
'''
Cifrar una frase con el algoritmo de cifrado por Código Telefónico
    Entradas:
        - Una cadena de carateres con la frase a ser cifrada 
    Salida:
        - El valor de la cadena cifrada con el algoritmo de 
          cifrado por Código Telefónico 
    Restricciones:
        - No hay.
'''
def cifrarCodigoTelefonico(cadena):
    cadena = cadena.lower()
    cadenaCifrada = ""
    indice = 0

    while (indice != len(cadena)):
        cadenaCifrada = cadenaCifrada + cifrarLetraCodigoTelefonico(cadena[indice])
        indice += 1

    return cadenaCifrada


'''
Sustituir un caracter según el proceso de cifrado del algoritmo de cifrado por Código Telefónico
    Entradas:
        - Un caracter en minuscula
    Salida:
        - Dos caracteres numéricos en el caso de que corresponda a una letra
        - Un carácter con el símbolo “*” en caso de sea un espacio
        - El mismo carácter en caso de que no aplique uno de los casos anteriores
    Restricciones:
        - No hay.
'''
def cifrarLetraCodigoTelefonico(letra):
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
Descifrar una frase con el algoritmo de cifrado por Código Telefónico
    Entradas:
        - Una cadena de carateres con la frase a ser descifrada
    Salida:
        - El valor de la cadena descifrada con el algoritmo de 
          cifrado por Código Telefónico 
    Restricciones:
        - No hay.
'''
def descifrarCodigoTelefonico(cadena):
    cadena=str(cadena)
    cadenaDescifrada = ""
    letraCifrada = ""
    indice = 0

    while (indice != len(cadena)):

        if (cadena[indice] == "*"):
            cadenaDescifrada = cadenaDescifrada + " "

        elif (esEntero(cadena[indice]) == True):
            letraCifrada = letraCifrada + cadena[indice]
            if (len(letraCifrada) == 2):
                cadenaDescifrada = cadenaDescifrada + descifrarLetraCodigoTelefonico(letraCifrada)
                letraCifrada = ""
        else:
            cadenaDescifrada = cadenaDescifrada + cadena[indice]

        indice += 1

    return cadenaDescifrada

'''
Sustituir un caracter según el proceso de cifrado del algoritmo de cifrado por Código Telefónico
    Entradas:
        - Una cadena de 2 caracteres numericos
    Salida:
        - Un caracter del alfabeto al cual corresponden los valores recibidos
        segun el algoritmo de cifrado telefónico
    Restricciones:
        - No hay.
'''
def descifrarLetraCodigoTelefonico(letraCifrada):
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


# --------------------------------------------Cifrado/Descifrado Binario----------------------------------------------------------------------------
'''
Cifrar una frase con el algoritmo de cifrado Binario
    Entradas:
        - Una cadena de carateres con la frase a ser cifrada 
    Salida:
        - El valor de la cadena cifrada con el algoritmo de cifrado Binario
    Restricciones:
        - No hay.
'''
def cifrarBinario(cadena):
    cadena = cadena.lower()
    cadenaResultante = ""
    letraResultante = ""
    indice = 0
    indiceClave = 0

    while (indice != len(cadena)):
        if (cadena[indice].isalpha() == True):
            letraResultante = " " + cifrarLetraBinario(cadena[indice])
        elif (cadena[indice] == " "):
            letraResultante = " *"
        else:
            letraResultante = cadena[indice]

        cadenaResultante = cadenaResultante + letraResultante
        indice += 1

    return cadenaResultante


'''
Sustituir un caracter según el proceso de cifrado del algoritmo de cifrado Binario
    Entradas:
        - Un caracter en minuscula
    Salida:
        - El valor en binario al cual corresponde la posicion de la letra 
          en el alfabeto según el algoritmo de cifrado Binario
    Restricciones:
        - No hay.
'''
def cifrarLetraBinario(letra):
    letraCifrada = ""
    letras = "abcdefghijklmnopqrstuvwxyz"

    if (buscarCaracter(letras, letra) != -1):

        letraCifrada = format(buscarCaracter(letras, letra), '05b')

        return letraCifrada
    else:
        return letra

'''
Descifrar una frase con el algoritmo de cifrado Binario
    Entradas:
        - Una cadena de carateres con la frase a ser descifrada 
    Salida:
        - El valor de la cadena en lenguaje natural descifrada 
          con el algoritmo de cifrado Binario
    Restricciones:
        - No hay.
'''
def descifrarBinario(cadena):
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

'''
Sustituir un numero binario por un caracter según el proceso de descifrado del algoritmo de cifrado Binario
    Entradas:
        - Un cadena de cinco valores en formato binario
    Salida:
        - El valor del caracter al cual corresponde la posicion de la letra 
          en el alfabeto expresada por el valor binario recibido, según el 
          algoritmo de cifrado binario
    Restricciones:
        - No hay.
'''
def sacarLetra(binario):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    binario = str(binario)
    letra = abecedario[int(binario, 2)]
    return letra


# --------------------------------------------Validacion de Entradas----------------------------------------------------------------------------
'''
Validar que la frase a ser cifrada cumpla con las caracteristicas de la entrada de cada algoritmo
    Entradas:
        - Un cadena de caracteres 
        - El numero de opción de cifrado seleccionado segun el Menú de opciones de Cifrado
    Salida:
        - El número de error que corresponda cada restriccion validada por la función
        - El valor de la cadena de caracteres recibida como la frase a ser cifrada
    Restricciones:
        - No hay.
'''
def validarEntradaAscii(cadena):
    
    entradaValida = False 

    if (cadena==""):
        return "-1"
    else:
        if(cadena.isascii()==True):
            entradaValida = True
        else:
            return "-2"
        
    if(entradaValida == True):
        return cadena   

def validarEntradaABC(cadena):

    entradaValida = False 

    abecedario = "abcdefghijklmnopqrstuvwxyz "

    if (cadena==""):
        return "-1"
    else:
        indice=0
        while (indice != len(cadena)):
            if(buscarCaracter(abecedario, cadena[indice].lower())==-1):
                return "-2"
            indice+=1
        entradaValida = True
    
    if(entradaValida == True):
        return cadena   

def validarEntradaBinario(cadena):

    entradaValida = False 

    charBin = "01* "

    if (cadena==""):
        return "-1"
    else:
        indice=0
        while (indice != len(cadena)):
            if(buscarCaracter(charBin, cadena[indice])==-1):
                return "-2"
            indice+=1
        
        entradaValida = True
        
    if(entradaValida == True):
        return cadena  

def validarEntradaNumAst(cadena):

    entradaValida = False 

    abcAst = "0123456789*"

    if (cadena==""):
        return "-1"
    else:
        indice=0
        while (indice != len(cadena)):
            if(buscarCaracter(abcAst, cadena[indice])==-1):
                return "-2"
            indice+=1

        entradaValida = True
        
    if(entradaValida == True):
        return cadena  

def validarEntradaCifradoTelefonico(cadena):

    abcAst = "123456789*"

    if (cadena==""):
        return "-1"
    else:
        indice=0
        while (indice != len(cadena)):
            if(buscarCaracter(abcAst, cadena[indice])==-1):
                return "-2"
            indice+=1

    if(validarParesCifradoTelefonico(cadena)!="-1"):              
        return cadena  
    else:
        return "-3"

def validarParesCifradoTelefonico(cadena):
    parNumeros=""
    cadena=cadena.replace("*","")

    if(len(cadena)%2!=0):
        return "-1"
    else:
        while (cadena != ""):

            parNumeros = cadena[:2]

            if(buscarCaracter("10", parNumeros[0])!=-1 or parNumeros[1] == "0"):
                return "-1"
            elif(buscarCaracter("234568", parNumeros[0])!=-1):
                if(buscarCaracter("123", parNumeros[1])!=-1):
                    cadena=cadena[2:]
                else:
                    return "-1"
            elif(buscarCaracter("79", parNumeros[0])!=-1):
                if(buscarCaracter("1234", parNumeros[1])!=-1):
                    cadena=cadena[2:]
                else:
                    return "-1"
        return "1"


def validarClavePorLlave(clave):
    
    entradaValida = False 

    abecedario = "abcdefghijklmnopqrstuvwxyz"

    if (clave==""):
        return "-1"
    else:
        indice=0
        while (indice != len(clave)):
            if(buscarCaracter(abecedario, clave[indice].lower())==-1):
                return "-2"
            indice+=1
        entradaValida = True
    
    if(entradaValida == True):
        return clave   

def validarClaveVigenere(clave):

    entradaValida = False 

    numeros = "0123456789"

    if (clave==""):
        return "-1"
    else:
        if(len(clave)!=2):
            return "-2" 
        else:     
            indice=0
            while (indice != len(clave)):
                if(buscarCaracter(numeros, clave[indice]) == -1):
                    return "-2"
                indice+=1

        entradaValida = True
        
    if(entradaValida == True):
        return clave 

def validarClaveRSA(n, d):

    if(n=="" or d==""):
        return "-1"
    elif (esEntero(n)==False or esEntero(d)==False):
        return "-2"
    else:
        return "1"
    

# --------------------------------------------Menu Cifrado----------------------------------------------------------------------------
'''
Desplegar y seleccionar entre las opciones de cifrado disponibles
    Entradas:
        - Un caracter en de tipo numérico con un valor entre 1 y 9
    Salida:
        - La explicación de las restricciones validadas sobre las 
          entradas y claves para los algoritmos de cifrado.
        - El resultado de alguno de las opciones de cifrado disponibles
    Restricciones:
        - El valor ingresado debe ser un entero entre 1 y 9 incluso
'''
def menuCifrado():
    opcionMenu=""

    while(opcionMenu!="9"):
        resultadoEntrada=""
        resultadoClave=""
        cadena=""

        print("\t-----------------------")
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

        opcionMenu = input("\n<--Opcion: ")

        if(esEntero(opcionMenu)==True):

            opcion=int(opcionMenu)

            if (opcion == 9):
                print("\n\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
                print("\t»Regresando al Menu Principal»")
                print("\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»\n")
                break
            elif(opcion>=1 and opcion<=8):
                cadena = input("\n<--Ingrese la frase o palabra que desea cifrar: ")

                if (opcion == 1):
                    print("\n\t---------------------")
                    print("\t    Cifrado Cesar")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"):       
                        print("\n\t*************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese un valor para la palabra o frase*")
                        print("\t*************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t************************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t************************************************************************************************\n")  
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarDescifrarCesar("cifrado", resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")

                elif (opcion == 2):
                    print("\n\t---------------------")
                    print("\t  Cifrado Por Llave")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"):       
                        print("\n\t*************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese un valor para la palabra o frase*")
                        print("\t*************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):       
                        print("\n\t**********************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t**********************************************************************************************\n")  
                    else:
                        clave = input("<--Digite la clave requerida para cifrar la palabra/frase: ")
                        resultadoClave = validarClavePorLlave(clave)
                        if(resultadoClave=="-1"):       
                            print("\n\t**************************************************************************")
                            print("\t*Se ha producido un ERROR: Es necesario que ingrese un valor para la clave*")
                            print("\t***************************************************************************\n")
                        elif(resultadoClave=="-2"):
                            print("\n\t**********************************************************************************************")
                            print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                            print("\t************************************************************************************************\n")
                        else:
                            print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarDescifrarPorLlave("cifrado", resultadoEntrada, resultadoClave))
                            input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 3):
                    print("\n\t---------------------")
                    print("\tSustitucion Vigenére")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"):       
                        print("\n\t*************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese un valor para la palabra o frase*")
                        print("\t*************************************************************************************\n")

                    elif(resultadoEntrada=="-2"):
                        print("\n\t***********************************************************************************************")       
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t************************************************************************************************\n") 
                    else:
                        clave = input("<--Digite la clave requerida para cifrar la palabra/frase: ")
                        resultadoClave = validarClaveVigenere(clave)
                        if(resultadoClave=="-1"):       
                            print("\n\t***************************************************************************")
                            print("\t*Se ha producido un ERROR: Es necesario que ingrese un valor para la clave*")
                            print("\t***************************************************************************\n")
                        elif(resultadoClave=="-2"):       
                            print("\n\t***************************************************************************************") 
                            print("\t*Se ha producido un ERROR: La clave SOLO debe contener DOS numeros enteros entre 0 y 9*")
                            print("\t***************************************************************************************\n") 
                        else:
                            print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarDescifrarSustitucionVigenere("cifrado", resultadoEntrada, resultadoClave))
                            input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 4):
                    print("\n\t---------------------")
                    print("\t     Cifrado RSA")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaAscii(cadena)
                    if(resultadoEntrada=="-1"):  
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):  
                        print("\n\t********************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra/frase solo debe contener caracteres ASCII*")
                        print("\t********************************************************************************\n")     
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarRSA(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 5):
                    print("\n\t---------------------")
                    print("\t   Palabra Inversa")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaAscii(cadena)
                    if(resultadoEntrada=="-1"):       
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"): 
                        print("\n\t********************************************************************************")      
                        print("\t*Se ha producido un ERROR: La palabra/frase solo debe contener caracteres ASCII*")
                        print("\t********************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarDescifrarPalabraInversa(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 6):
                    print("\n\t---------------------")
                    print("\t   Mensaje Inverso")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaAscii(cadena)
                    if(resultadoEntrada=="-1"): 
                        print("\n\t**************************************************************************************")      
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):       
                        print("\n\t********************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra/frase solo debe contener caracteres ASCII*")
                        print("\t********************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarDescifrarMensajeInverso(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 7):
                    print("\n\t---------------------")
                    print("\t  Cifrado Telefónico")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"):   
                        print("\n\t**************************************************************************************")    
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):  
                        print("\n\t************************************************************************************************")     
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t************************************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarCodigoTelefonico(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 8):
                    print("\n\t---------------------")
                    print("\t   Cifrado Binario")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"): 
                        print("\n\t**************************************************************************************")       
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n") 
                    elif(resultadoEntrada=="-2"): 
                        print("\n\t************************************************************************************************")       
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t************************************************************************************************\n") 
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarBinario(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")       
            else:            
                print("\n\t***************************************")
                print("\t*Opcion no valida, vuelva a intentarlo*")
                print("\t***************************************\n")
        else:
            print("\n\t***************************************")
            print("\t*Opcion no valida, vuelva a intentarlo*")
            print("\t***************************************\n")


# --------------------------------------------Menu Descifrado----------------------------------------------------------------------------
'''
Desplegar y seleccionar entre las opciones de descifrado disponibles
    Entradas:
        - Un caracter en de tipo numérico con un valor entre 1 y 9
    Salida:
        - La explicación de las restricciones validadas sobre las 
          entradas y claves para los algoritmos de descifrado.
        - El resultado de alguno de las opciones de descifrado disponibles
    Restricciones:
        - El valor ingresado debe ser un entero entre 1 y 9 incluso
'''
def menuDescifrado():
    opcionMenu=""
    while(opcionMenu!="9"):
        resultadoEntrada=""
        resultadoClave=""

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

        opcionMenu = input("\n<--Opcion: ")

        if(esEntero(opcionMenu)==True):

            opcion=int(opcionMenu)

            if (opcion == 9):
                print("\n\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
                print("\t»Regresando al Menu Principal»")
                print("\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»\n")
                break
            elif(opcion>=1 and opcion<=8):
                cadena = input("\n<--Ingrese la frase o palabra que desea descifrar: ")

                if (opcion == 1):

                    print("\n\t---------------------")
                    print("\t    Descifrado Cesar")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")

                    elif(resultadoEntrada=="-2"):
                        print("\n\t************************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t************************************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra descifrada es la siguiente: " + cifrarDescifrarCesar("descifrado", resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 2):
                    print("\n\t---------------------")
                    print("\t  Descifrado Por Llave")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t************************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t************************************************************************************************\n")
                    else:
                        clave = input("<--Digite la clave requerida para descifrar la palabra/frase: ")
                        resultadoClave = validarClavePorLlave(clave)
                        if(resultadoClave=="-1"):
                            print("\n\t****************************************************************************")
                            print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la clave*")
                            print("\t****************************************************************************\n")
                        elif(resultadoClave=="-2"):
                            print("\n\t**************************************************************************************")
                            print("\t*Se ha producido un ERROR: La clave NO debe contener caracteres numéricos ni símbolos*")
                            print("\t**************************************************************************************\n")
                        else:
                            print("\n-->La frase o palabra descifrada es la siguiente: " + cifrarDescifrarPorLlave("descifrado", resultadoEntrada, resultadoClave))
                            input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 3):
                    print("\n\t---------------------")
                    print("\tSustitucion Vigenére")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaABC(cadena)
                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t************************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase NO debe contener caracteres numéricos ni símbolos*")
                        print("\t************************************************************************************************\n")
                    else:
                        clave = input("<--Digite la clave requerida para descifrar la palabra/frase: ")
                        resultadoClave = validarClaveVigenere(clave)
                        if(resultadoClave=="-1"):
                            print("\n\t****************************************************************************")
                            print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la clave*")
                            print("\t****************************************************************************\n")

                        elif(resultadoClave=="-2"):
                            print("\n\t************************************************************************")
                            print("\t*Se ha producido un ERROR: La clave NO debe contener letras ni símbolos*")
                            print("\t************************************************************************\n")

                        else:
                            print("\n-->La frase o palabra descifrada es la siguiente: " + cifrarDescifrarSustitucionVigenere("descifrado", resultadoEntrada, resultadoClave))
                            input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 4):
                    print("\n\t---------------------")
                    print("\t     Descifrado RSA")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaNumAst(cadena)
                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase SOLO debe contener caracteres numéricos*") 
                        print("\t*entre 2 y 9 (incluso) y el simbolo \"*\"                                            *")
                        print("\t**************************************************************************************\n")
                    else:
                        print("Digite la clave requerida para cifrar la palabra/frase")
                        n = input("-->Ingrese el primer valor de la clave privada: ")
                        d = input("-->Ingrese el segundo valor de la clave privada: ")
                        resultadoClave = validarClaveRSA(n, d)
                        if(resultadoClave=="-1"):
                            print("\n\t*************************************************************************")
                            print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para n y d*")
                            print("\t*************************************************************************\n")
                        elif(resultadoClave=="-2"):
                            print("\n\t*******************************************************************************")
                            print("\t* Se ha producido un ERROR: los valores de n y d deben ser dos valores enteros*")
                            print("\t*******************************************************************************\n")
                        else:
                            print("\n-->La frase o palabra descifrada es la siguiente: " + descifrarRSA(cadena, n, d))
                            input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 5):
                    print("\n\t---------------------")
                    print("\t   Palabra Inversa")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaAscii(cadena)

                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t********************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra/frase solo debe contener caracteres ASCII*")
                        print("\t********************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarDescifrarPalabraInversa(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 6):
                    print("\n\t---------------------")
                    print("\t   Mensaje Inverso")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaAscii(cadena)
                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t********************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra/frase solo debe contener caracteres ASCII*")
                        print("\t********************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra cifrada es la siguiente: " + cifrarDescifrarMensajeInverso(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 7):
                    print("\n\t---------------------")
                    print("\t  Descifrado Telefónico")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaCifradoTelefonico(cadena)

                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase SOLO debe contener caracteres numéricos*") 
                        print("\t*entre 2 y 9 (incluso) y el simbolo \"*\"                                            *")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-3"):
                        print("\n\t***********************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase SOLO debe contener caracteres numéricos en pares*")
                        print("\t***********************************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra descifrada es la siguiente: " + descifrarCodigoTelefonico(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
                elif (opcion == 8):
                    print("\n\t---------------------")
                    print("\t   Descifrado Binario")
                    print("\t-----------------------")

                    resultadoEntrada = validarEntradaBinario(cadena)

                    if(resultadoEntrada=="-1"):
                        print("\n\t**************************************************************************************")
                        print("\t*Se ha producido un ERROR: Es necesario que ingrese una valor para la palabra o frase*")
                        print("\t**************************************************************************************\n")
                    elif(resultadoEntrada=="-2"):
                        print("\n\t****************************************************************************************")
                        print("\t*Se ha producido un ERROR: La palabra o frase SOLO debe contener los caracteres numéricos*") 
                        print("\t*1 o 0, o el simbolo \"*\"                                                               *")
                        print("\t******************************************************************************************\n")
                    else:
                        print("\n-->La frase o palabra descifrada es la siguiente: " + descifrarBinario(resultadoEntrada))
                        input("\n<--Presione la tecla \"Enter\" para continuar...\n")
            else:            
                print("\n\t***************************************")
                print("\t*Opcion no valida, vuelva a intentarlo*")
                print("\t***************************************\n")
        else:
            print("\n\t***************************************")
            print("\t*Opcion no valida, vuelva a intentarlo*")
            print("\t***************************************\n")



# --------------------------------------------Menu Principal----------------------------------------------------------------------------
'''
Desplegar y seleccionar entre las opciones de programa
    Entradas:
        - Un caracter en de tipo numérico con un valor entre 1 y 3
    Salida:
        - Ninguna
    Restricciones:
        - El valor ingresado debe ser un entero entre 1 y 3 incluso
'''
def menuPrincipal():
    opcion=0
    print("\n\t≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    print("\t Cifrado de Mensajes")
    print("\t≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")

    while(opcion!=3):
        print("\n\t--------------------")
        print("\t   Menú Principal")
        print("\t--------------------")
        print("\nSeleccione una de las opciones.")
        print("Digite el numero correspondiente.")
        print("\n1. Cifrar una frase o palabra")
        print("2. Descifrar una frase o palabra")
        print("3. Finalizar Programa")

        try:
            opcion = int(input("\n<--Opcion: "))
        except:
            print("\t***************************************")
            print("\t*Opcion no valida, vuelva a intentarlo*")
            print("\t***************************************")
            menuPrincipal()

        if (opcion == 1):
            print("\n\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
            print("\t»Cargado Opciones de Cifrado»")
            print("\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»\n")
            menuCifrado()
        elif (opcion == 2):
            print("\n\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
            print("\t»Cargado Opciones de Descifrado»")
            print("\t»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»\n")
            menuDescifrado()
        elif (opcion == 3):
            print("\n\t»»»»»»»»»»»»»»»»»»»»»")
            print("\t»Programa Finalizado»")
            print("\t»»»»»»»»»»»»»»»»»»»»»")
            #sys.exit(0)
        else:
            print("\t***************************************")
            print("\t*Opcion no valida, vuelva a intentarlo*")
            print("\t***************************************")
            menuPrincipal()

menuPrincipal()
