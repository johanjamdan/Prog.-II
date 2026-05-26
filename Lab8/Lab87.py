class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def imprimir_nombre(self):
        print(self.nombre, self.apellido)

p1 = Persona("Hanna", "Licona")
p1.imprimir_nombre()

class Estudiante(Persona):
    pass

x = Estudiante("Johan", "Jamdan")
x.imprimir_nombre()