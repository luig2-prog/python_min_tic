# def par_number(numbers):
#     result = []
#     for i in numbers:
#         print(int(i))
#         if int(i) != 0 and int(i) % 2 == 0:
#             result += [int(i)]

#     return result



# entrada = "1, 2, 5, 6, 7, 8, 9, -6, 3"
# variable = entrada.split(", ")
# print(variable)
# result = par_number(variable) == "2, 6, 8, -6"
# print(result)



def repeat(lista_elemt):
    for i in range(len(lista_elemt)):
        print()        

    return ""


entrada = "PHP, PHP, Python, PHP, Python, JS, Python, Python, PHP, Python"

lista = entrada.split(", ")

test_one = repeat(lista)

salida = "Python"

print(test_one == salida)