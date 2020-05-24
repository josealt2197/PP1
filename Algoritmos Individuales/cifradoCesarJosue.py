'''CIFRADO CESAR'''
'''ENTRADA: Se debe ingresar una cadena de caracteres a cifrar'''
'''SALIDA:La cadena de caracteres cifrada segun el CIFRADO CESAR'''
'''RESTRICCIONES: lo ingresado debe ser unicamente una cadena de caracteres'''
def cifradoCesar():
    contandor = 0
    resultado=""
    cadena = input("ingrese la oración que desea decifrar: ")
    if (esNumeroEntero(cadena) and esNumeroEntero(cadena)):
        print("Debe ingresar palabras")
        return cifradoCesar()
    cadena = cadena.lower()

    while (contandor<len(cadena)):
        if(cadena[contandor]== " " ):
            resultado=resultado+" "
        else:
            resultado=resultado+cifrarLetra(cadena[contandor])
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
    if (esNumeroEntero(cadena) and esNumeroEntero(cadena)):
        print("Debe ingresar palabras")
        return cifradoCesar()
    cadena = cadena.lower()

    while (contandor<len(cadena)):
        if(cadena[contandor]== " " ):
            resultado=resultado+" "
        else:
            resultado=resultado+descifrarLetra(cadena[contandor])
        contandor+=1
    print("su secreto es: "+ str(resultado))



'''******************************************************************************************************************'''


def cifrarLetra(letra):
    abecedario = "abcdefghijklmnopqrstuwxyz"
    i = 0
    tamano = len(abecedario)
    while (i < tamano):
        if (abecedario[i] == letra and
                abecedario[i] != 'x' and
                abecedario[i] != 'y' and
                abecedario[i] != 'z'):
            return abecedario[i + 3]
        elif (abecedario[i] == 'x'):
            return 'a'
        elif (abecedario[i] == 'y'):
            return 'b'
        elif (abecedario[i] == 'z'):
            return 'c'
        i += 1



def descifrarLetra(letra):
    abecedario = "abcdefghijklmnopqrstuwxyz"
    i = 0
    tamano = len(abecedario)
    while (i < tamano):
        if (abecedario[i] == letra and
                abecedario[i] != 'x' and
                abecedario[i] != 'y' and
                abecedario[i] != 'z'):
            return abecedario[i - 3]
        elif (abecedario[i] == 'x'):
            return 'a'
        elif (abecedario[i] == 'y'):
            return 'b'
        elif (abecedario[i] == 'z'):
            return 'c'
        i += 1

def esNumeroEntero(pNumero):
    try:
        numero = int(pNumero)
        return True
    except:
        return False

'''******************************************************************************************************************'''


