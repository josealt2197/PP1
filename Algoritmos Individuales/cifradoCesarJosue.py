'''CIFRADO CESAR'''
'''ENTRADA: Se debe ingresar una cadena de caracteres a cifrar'''
'''SALIDA:La cadena de caracteres cifrada segun el CIFRADO CESAR'''
'''RESTRICCIONES: lo ingresado debe ser unicamente una cadena de caracteres'''
def cifradoCesar():
    contandor = 0
    resultado=""
    cadena = input("ingrese la oración que desea decifrar: ")
    if (esNumeroEntero(cadena) ):
        return "Debe ingresar palabras"
       
    cadena = cadena.upper()

    while (contandor<len(cadena)):
        if(cadena[contandor]== " " ):
            resultado=resultado+" "
        else:
            resultado=resultado+cifrarLetra(cadena[contandor])
            print ( resultado)
        contandor+=1
    print("su secreto es: "+ str(resultado))


'''DESCIFRADO CESAR'''
'''ENTRADA: Se debe ingresar una cadena de caracteres a decifrar'''
'''SALIDA:La cadena de caracteres descifrada segun el CIFRADO CESAR'''
'''RESTRICCIONES: lo ingresado debe ser unicamente una cadena de caracteres'''
def desCifradoCesar():
    contandor = 0
    resultado=""
    cadena = input("ingrese la oración que desea decifrar: ")
    if (esNumeroEntero(cadena)):
        print("Debe ingresar palabras")
        
    cadena = cadena.upper()

    while (contandor<len(cadena)):
        if(cadena[contandor]== " " ):
            resultado=resultado+" "
        else:
            resultado=resultado+descifrarLetra(cadena[contandor])
        contandor+=1
    print("su secreto es: "+ str(resultado))



'''******************************************************************************************************************'''


def cifrarLetra(letra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    tamano = len(abecedario)
    while (i < tamano):
        if (abecedario[i] == letra and
                abecedario[i] != 'X' and
                abecedario[i] != 'Y' and
                abecedario[i] != 'Z'):
            return abecedario[i + 3]
        elif (letra == 'X'):
            return 'A'
        elif (letra == 'Y'):
            return 'B'
        elif (letra == 'Z'):
            return 'C'
        i += 1



def descifrarLetra(letra):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    tamano = len(abecedario)
    while (i < tamano):
        if (abecedario[i] == letra and
                abecedario[i] != 'A' and
                abecedario[i] != 'B' and
                abecedario[i] != 'C'):
            return abecedario[i - 3]
        elif (letra == 'A'):
            return 'X'
        elif (letra == 'B'):
            return 'Y'
        elif (letra == 'C'):
            return 'Z'
        i += 1

def esNumeroEntero(pNumero):
    try:
        numero = int(pNumero)
        return True
    except:
        return False

'''******************************************************************************************************************'''


