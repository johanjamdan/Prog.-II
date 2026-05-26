def transformar (valores):
    for i in range(len(valores)):
        valores[i] = valores[i] + i
lista = [10, 20, 30, 40]
transformar(lista)
print(lista)

#1. ¿Qué hace este programa? ¿Cuál es la salida?
#El programa define una función que recorre una lista y le suma a cada elemento su propio índice de posición.
#Salida: [10, 21, 32, 43]

#2. Explique cómo cambia la lista en cada iteración.
#La lista original es [10, 20, 30, 40]. En cada paso del ciclo for:
#Iteración 0: valores[0] (10) + 0 = 10
#Iteración 1: valores[1] (20) + 1 = 21
#Iteración 2: valores[2] (30) + 2 = 32
#Iteración 3: valores[3] (40) + 3 = 43

#3. ¿Por qué no se necesita return para modificar la lista?
#En Python, las listas son objetos mutables. Cuando pasas una lista a una función, 
#se pasa una referencia al objeto original en la memoria. Cualquier cambio realizado 
#mediante el acceso por índice (valores[i] = ...) afecta directamente a la lista original, lo devolverá.


#4. ¿Qué pasaría si dentro de la función se hace: valores = [0, 0, 0]?
#La lista original no cambiaría. Al asignar esos valores, estás reasignando 
#el nombre del parámetro local a un nuevo objeto en memoria. La referencia a la lista 
#original lista se pierde dentro del ámbito de la función, pero el objeto original 
#fuera de ella permanece intacto.

#5. Reescriba la función para crear y retornar una nueva lista sin modificar la original.

#def transformar_nueva(valores):
    #nueva_lista = []
    #for i in range(len(valores)):

        #nueva_lista.append(valores[i] + i)
    #return nueva_lista