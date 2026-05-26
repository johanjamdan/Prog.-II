def transformar (valores):
    for i in range(len(valores)):
        valores[i] = valores[i] + i
lista = [10, 20, 30, 40]
transformar(lista)
print(lista)