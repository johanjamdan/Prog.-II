def main():
    n = input("Dime un número para el factorial: ")
    
    try:
        n = int(n)
        if n < 0:
            print("No se puede con negativos.")
            return
            
        res = 1
        for i in range(1, n + 1):
            res *= i
            
        print(f"El factorial es: {res}")
    except:
        print("Eso no es un número válido.")

if __name__ == "__main__":
    main()