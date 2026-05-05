datos = bytearray(b"Hola, mundo!")
vista = memoryview(datos)
vista[0] = 104 # Modifica 'H' por 'h' (ASCII 104)
print(datos)