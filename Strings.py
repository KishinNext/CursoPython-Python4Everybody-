# palabra = input("Ingrese cualquier palabra")
# longitud = len(palabra) - 1
#
# for lon in palabra:
#     letra = palabra[longitud]
#     longitud -= 1
#     print(letra)
# #########################################
# def contador(palabra, letra):
#     word = palabra
#     count = 0
#     for letter in word:
#         if letter == letra:
#             count = count + 1
#     return  count
#
# palabra = input("Ingrese cualquier palabra: ")
# letra = input("Que letra desea contar?: ")
#
# try:
#     cuenta = contador(palabra,letra)
#     print(str(cuenta))
# except:
#     print("Porfavor solo ingrese palabras.")
#

###########################################

str = 'X-DSPAM-Confidence:0.8475'

position = str.find(':')
numero = float(str[position + 1:])
print(numero)
