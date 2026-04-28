# 1. Literal de bytes (forma más común)
# \xFF representa el valor 255 en hexadecimal
mi_byte = b"\xFF"

# 2. Constructor bytes a partir de un entero
mi_byte_dos = bytes([255])

# Verificación
print(type(mi_byte))    # Muestra <class 'bytes'>
print(mi_byte[0])       # Imprime el valor decimal: 255