def contar_hasta(n):
    cuenta = 1
    while cuenta <= n:
        yield cuenta
        cuenta += 1
    
for numero in contar_hasta(5):
    print(numero)