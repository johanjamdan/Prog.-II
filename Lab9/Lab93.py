class Persona:
    # Atributo estático (compartido por todas las instancias)
    contador = 0

    def __init__(self):
        Persona.contador += 1 # Se accede con el nombre de la clase

# Uso del código
p1 = Persona()
p2 = Persona()
p3 = Persona()

print(f"Total de personas creadas (contador): {Persona.contador}")