def matriz():
    n = input("Tamaño de la matriz (que sea par): ")
    
    try:
        n = int(n)
        if n % 2 != 0:
            print("Te dije que fuera par.")
            return

        print("\nGenerando matriz...")
        for i in range(n):
            for j in range(n):
                if i == j:
                    print("1", end="  ")
                else:
                    print("0", end="  ")
            print()
            
    except:
        print("Entrada inválida.")

if __name__ == "__main__":
    matriz()