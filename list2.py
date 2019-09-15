Archivo =  input('Escriba el nombre del archivo: ')
try:
    File = open(Archivo+'.txt')
except:
    print('Error al abrir el archivo, intentelo de nuevo.')
word = list()
count = 0
for line in File:
    words = line.split()
    anterior = None
    for wo in words:
        word.append(wo)
word.sort()
anterior = None
final = list()
for new in word:
    if anterior is None or anterior != new:
        final.append(new)
        anterior = new

print(final)