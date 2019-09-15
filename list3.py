while True:
    Archivo = input('Introduzca el nombre del archivo: ')

    try:
        File = open(Archivo+'.txt')
        break
    except:
        print('Archivo no encontrado porfavor intente denuevo.')
        continue
for line in File:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[1])