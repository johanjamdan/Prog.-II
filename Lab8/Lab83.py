class Persona:
    def __init__(self, nom, ed):
        self.nombre = nom
        self.edad = ed

    def saludar(self):
        print("Hola, mi nombre es: " + self.nombre)

p1 = Persona("Johan", 19)
p1.saludar()