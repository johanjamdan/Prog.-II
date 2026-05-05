def main():
    # Definimos las provincias y comarcas en una tupla
    # Al ser una 'tuple', el orden es inmutable y no permite cambios en tiempo de ejecución.
    provincias_y_comarcas = (
        "Bocas del Toro", 
        "Coclé", 
        "Colón", 
        "Chiriquí", 
        "Darién", 
        "Herrera", 
        "Los Santos", 
        "Panamá", 
        "Veraguas", 
        "Panamá Oeste", 
        "Guna Yala", 
        "Emberá-Wounaan", 
        "Ngäbe-Buglé", 
        "Naso Tjër Di", 
        "Madugandí", 
        "Wargandí"
    )

    print("--- Listado de Provincias y Comarcas de Panamá ---")
    # Iteramos sobre la secuencia para mostrar el orden fijo
    for i, lugar in enumerate(provincias_y_comarcas, 1):
        print(f"{i}. {lugar}")

    print("\n[INFO] La estructura es de tipo 'tuple', por lo tanto es INMUTABLE.")
    
    # Nota técnica: 
    # Si intentáramos hacer: provincias_y_comarcas[0] = "Nueva Provincia"
    # El intérprete de Python generaría un TypeError porque las tuplas no permiten reasignación.

if __name__ == "__main__":
    main()