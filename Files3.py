while True:
    Archivo = input('Ingrese el nombre del archivo: ')
    try:
        if Archivo == 'na na boo boo':
            print('NA NA BOO BOO TO YOU')
            File = open(Archivo + '.txt')
        else:
            File = open(Archivo+'.txt')
            break
    except:
        print('Porfavor ingrese un nomber válido.')
        continue
contador = 0;
sumaa = 0;
for line in File:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        espacio = line.find(': ')
        numero = line[espacio + 1:]
        contador = contador + 1
        sumaa = sumaa + float(numero)


print(sumaa/contador)