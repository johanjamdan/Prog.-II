import string

def contar_unicas(texto):
    limpio = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    return len(set(limpio.split()))

def la_mas_larga(texto):
    palabras = texto.split()
    return max(palabras, key=len) if palabras else ""

def sacar_frecuencia(texto):
    txt = texto.replace(" ", "").lower()
    total = len(txt)
    conteo = {}

    for letra in txt:
        if letra.isalpha():
            conteo[letra] = conteo.get(letra, 0) + 1
    
    print("\nFrecuencias:")
    for letra, num in conteo.items():
        porcentaje = (num / total) * 100
        print(f"'{letra}': {num} veces ({porcentaje:.1f}%)")

def main():
    txt = input("Pega tu texto aquí: ")
    
    if not txt.strip():
        print("Escribe algo primero.")
        return

    print("-" * 20)
    print(f"Palabras únicas: {contar_unicas(txt)}")
    print(f"Palabra más larga: {la_mas_larga(txt)}")
    sacar_frecuencia(txt)

if __name__ == "__main__":
    main()