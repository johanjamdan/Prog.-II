class Persona:
    def __init__(self, nom, edad):
        self.nombre = nom
        self.__edad = edad

    def obtener_edad(self):
        return self.__edad

    def asignar_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo")

p1 = Persona("Johan", 19)
print(p1.obtener_edad())
p1.asignar_edad(19)
print(p1.obtener_edad())