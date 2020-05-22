from random import randint, uniform,random

def generarLlavesRSA():
    llavePublica=""
    llavePrivada=""
    p=randint(1000,10000)
    q=randint(1000,10000)
    n=0
    fiDeN=0
    e=0
    d=0

    #Paso 1
    while(esPrimo(p)!=True and esPrimo(p)!=True):
        p=randint(1000,10000)
        q=randint(1000,10000)

    print("p= "+str(p))
    print("q= "+str(q))
    
    #Paso 2
    n=p*q
    print("n= "+str(n))
    
    #Paso 3
    fiDeN=(p-1)*(q-1)
    print("fiDeN= "+str(fiDeN))
    
    #Paso 4
    e=randint(0,fiDeN)
    while(calcularMCD(fiDeN,e)!=1):
        e=randint(0,fiDeN)
    print("e= "+str(e))
    
    #Paso 5
    d=randint(0,1000)   
    while(((d*e)-1)%fiDeN!=0):
        d=randint(0,1000)
    print("d= "+str(d))

    print("Llaves generadas: ")
    print("Publica: ("+str(n)+", "+str(e)+")")
    print("Privada: ("+str(n)+", "+str(d)+")")

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
