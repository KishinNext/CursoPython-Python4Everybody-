while True:
    archivo = input('Ingrese el nombre del archivo: ')
    guardar = input('Ingrese el nombre del archivo en donde va guardar: ')
    try:
        file = open(archivo+'.txt')
        save = open(guardar+'.xlsx','w')
        break
    except:
        print('El archivo no fue encontrado...')
        print('Recuerde: No es necesario agregar la extensión del archvo (.txt)')
        continue
count = 0
for line in file:
    line = line.rstrip()
    if line.startswith('Subject:'):
        print(line)
        save.write(line+'\n')
save.close()