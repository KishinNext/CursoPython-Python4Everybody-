Archivo = input('Escriba el nombre del archivo sin extensión: ')

try:
    File = open(Archivo+'.txt')
except:
    print('Porfavor, ingrese un nombre válido (mbox)')

for line in File:
    line = line.rstrip()
    line = line.upper()
    print(line)