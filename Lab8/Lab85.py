class Persona:
    def __init__(self, nom, ed):
        self.nombre = nom
        self.edad = ed

    def obtener_informacion(self):
        return f"{self.nombre}, tiene {self.edad} años."
    
p1 = Persona("Johan", 19)
print(p1.obtener_informacion())