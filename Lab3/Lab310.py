# Ejemplo de validación de datos
usuario = "CiberAlumno2026"
pin = "1234"
mensaje_vacio = "   "

# 1. isalnum(): Verifica si es alfanumérico (letras y números, sin espacios ni símbolos)
print(f"¿El usuario es válido? {usuario.isalnum()}")

# 2. isdigit(): Verifica si el texto contiene solo números (útil para IDs o PINs)
print(f"¿El PIN es numérico? {pin.isdigit()}")

# 3. isspace(): Verifica si la cadena solo tiene espacios en blanco
print(f"¿El mensaje está vacío? {mensaje_vacio.isspace()}")