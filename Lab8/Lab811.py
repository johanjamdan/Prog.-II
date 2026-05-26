class Persona:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario

p1 = Persona("Johan", 2000)
print(p1.nombre)
print(p1._salario)