
# def hacer_lista(cadena_input):
#   cadena = ''
#   for i in range(len(cadena_input)):
#     # print(entrada_clases[i])
#     if cadena_input[i] == '[' or cadena_input[i] == ']' or cadena_input[i] == ',' or cadena_input[i] == ' ':
#       continue
#     cadena += cadena_input[i] + " "
    
#   cadena = cadena.strip()

#   return cadena.split(' ')


# # #######################################

# def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
#   resultado = []
#   # Algoritmo
#   for item in indices:
#     for i in range(len(clases)):
#         if clases[i] == clase_a_verificar and item==i:
#             resultado.append(item)

#   return resultado


# indices = hacer_lista('[1,3,6,8] ')

# clases = hacer_lista('[3,2,1,1,1,3,2,1,1,1]')

# clase_a_verificar = int('1')


# print(laminas_faltantes_por_clase(indices, clases, clase_a_verificar))









# #




















# # from collections import OrderedDict
# # def clases(clases):
# #   resultado=OrderedDict.fromkeys(clases).keys()
# #   return (list(resultado ))

# # def mefaltandelaclase(indices, clases, clase_a_verificar):
# #   resultado = []
# #   for item in indices:
# #     for i in range(len(clases)):
# #       if(clases[i]==clase_a_verificar and item==i):
# #         resultado.append(item)
# #   return resultado


# # # indices = input()
# # # clases_in = input()
# # # clase_a_verificar = int(input())

# # # print(mefaltandelaclase(indices, clases_in, clase_a_verificar))


# A = "Durante la altura"

# if "al" in A:
#     print("yes")
# else:
#     print("no")

# def valide_jugada(A:tuple, B: tuple)->bool:
#    return A[0] in B or A[1] in B

# print(valide_jugada((3,4),(0,1)))



# tupla =(1, -2, 3)
# a, b, c = tupla

# print ("a = ", a)
# print ("b =", b)
# print("c =",c)


# def unir_listas(lista1, lista2):

#       lista1.extend(lista2)

# avengers = ['Tony', 'Natalia', 'Steve']

# nuevos_avengers = ['Thor', 'Peter']

# unir_listas(avengers, nuevos_avengers)

# print(avengers)



# import numpy as np

# x = np.array([[1,2,5], [3,4,6]], dtype=np.float128)

# y = np.array([[5,6,-1], [7,8,-5]], dtype=np.float128)

# print("Suma:")

# # print(x + y)
# puertos = {22:"SSH", 23:"Telnet40", 80:"HTTP", 3306:"40MySQL"}

# protocolo = puertos[40]

# print(protocolo)

# print(np.add(x, y))





puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}

puertos[23] = "Telnet"

puertos[110] = "POP"

print(puertos)


# # def notengo(laminas_persona_1, laminas_persona_2):
# #   resultado = []
# #   for lamina in laminas_persona_1:
# #     if(laminas_persona_2.count(lamina)==0):
# #       resultado.append(lamina)
# #   return resultado
# # def puedocambiar(laminas_persona_1, laminas_persona_2):
# #   resultado = 0
# #   if(len(laminas_persona_1)>len(laminas_persona_2)):
# #     for l in laminas_persona_2:
# #       if(laminas_persona_1.count(l)==0):
# #         resultado+=1
# #   else:
# #      for l in laminas_persona_1:
# #       if(laminas_persona_2.count(l)==0):
# #         resultado+=1
#   return resultado