contador = 0
media = 0
mas = None
mes = None
while True:
    Numeros = input('Ingrese solo números: ')
    try:
        if Numeros == 'fin':
            break
        else:
            Num = float(Numeros)
            contador += 1
            media = media + Num
            if mas is None or Num > mas:
                mas = Num
            if mes is None or Num < mes:
                mes = Num
    except:
        print('Error, Ingreso un caracter no válido.')
        continue
print('El número total de numeros es: ', str(contador))
print('el total es: ', str(media))
print('El mínimo es: ', str(mes))
print('El máximo es: ', str(mas))