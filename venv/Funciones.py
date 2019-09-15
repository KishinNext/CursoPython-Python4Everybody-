import math
import random

for i in range(10):
    x = random.randint(5,10)
    print(x)

t = [1,2,3]
random.choice(t)

def repite():
    muestra_estribillo()
    muestra_estribillo()

def muestra_estribillo():
    print('Soy un leñador, que alegría.')

def muestra_dos_veces(bruce):
    print(bruce)
    print(bruce)
muestra_dos_veces("Hola "*4)

def sumados(a,b):
    suma = a + b
    return suma

print(sumados(10,12))

############## ejercicios

Horas = input('Introduzca laas horas trabajadas: ')
Tarifa = input('Introduzca la tarifa por hora: ')

def calcula_slario(H,T):
    if H >= 40:
        Newhour = H - 40
        Salario = (H * T) + (Newhour * (T * 0.5))
    else:
        Salario = H * T
    return Salario

try:
    Hour = float(Horas)
    Tar = float(Tarifa)
    sal = calcula_slario(Hour,Tar)
    print('Su salario es: '+ str(sal))
except:
    print('Por favor, introduzca un número')

Puntuacion = input("Introduzca su puntuación: ")

def calcula_calificacion(Puntuacion):
    if Puntuacion >= 0.9:
        print("Sobresaliente")
    elif Puntuacion >= 0.8:
        print("Notable")
    elif Puntuacion >= 0.7:
        print("Bien")
    elif Puntuacion >= 0.6:
        print("Suficiente")
    else:
        print("Insuficiente")


try:
    Puntuacion=float(Puntuacion)
    calcula_calificacion(Puntuacion)
except:
    print("Porfavor, introduzca un número válido")
    quit()


