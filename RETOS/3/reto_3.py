def  eliminar_espacios(entrada):
    entrada_sin_espacios = ""
    for contador in range(len(entrada)):
        if entrada[contador] != " ":
            entrada_sin_espacios += entrada[contador]
    return entrada_sin_espacios

def contar_letras(entrada_p):
    letras = ""
    numeros = ""
    accountant = 0
    while accountant  < len(entrada_p):
        print(accountant)
        letras += " " + entrada_p[accountant]
        contador_letra = 1
        for j in range(accountant,len(entrada_p)):
            print(f"j: {j}")
            accountant += 1
            print(f"j + 1: {j + 1} len: {len(entrada_p)}")
            if j + 1 < len(entrada_p):
                if entrada_p[j] != entrada_p[j + 1]:
                    numeros += " "  + str(contador_letra )
                    break
                else:
                    contador_letra += 1
            else:
                numeros += " "  + str(contador_letra )
         


    return  letras.strip() + "\n" + numeros.strip()

entrada_procesada = eliminar_espacios(input())
print(entrada_procesada)
salida = contar_letras(entrada_procesada)
print(salida)