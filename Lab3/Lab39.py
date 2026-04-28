texto = "bienvenido al laboratorio de ciberseguridad"

# 1. Ponemos la primera letra en mayúscula
print(texto.capitalize())

# 2. Contamos cuántas veces aparece la letra "a"
cantidad_a = texto.count("a")
print(f"La letra 'a' aparece {cantidad_a} veces")

# 3. Verificamos si termina en una palabra específica
print(texto.endswith("ciberseguridad")) # Devuelve True