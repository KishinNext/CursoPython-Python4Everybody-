Horas = input('Introduzca laas horas trabajadas: ')
Tarifa = input('Introduzca la tarifa por hora: ')
try:
    Hour = float(Horas)
    Tar = float(Tarifa)

    if Hour >= 40:
        Newhour = Hour - 40
        Salario = (Hour * Tar) + (Newhour * (Tar * 0.5))
    else:
        Salario = Hour * Tar
    print('Su salario es: '+ str(Salario))
except:
    print('Por favor, introduzca un número')



Puntuacion = input("Introduzca su puntuación: ")

try:
    Puntuacion=float(Puntuacion)
except:
    print("Porfavor, introduzca un número válido")
    quit()

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
