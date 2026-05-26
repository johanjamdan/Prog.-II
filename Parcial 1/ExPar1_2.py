def convertir_moneda():
    tasa_euro = 0.92 
    
    while True:
        entrada = input("¿Cuántos dólares (USD) quieres convertir?: ") 
        
        try:
            dolares = float(entrada)
            
            if dolares < 0:
                print("El monto no puede ser negativo. Intenta de nuevo.")
                continue 
                
            euros = dolares * tasa_euro
            
            print(f"Resultado: {dolares} USD equivalen a {euros:.2f} EUR")
            break 
            
        except ValueError:
            print("Error: Por favor, ingresa un número válido (ejemplo: 10.50).")

convertir_moneda()

#6. ¿Cómo lo haría? ¿Qué debe tomar en cuenta?
#Para crear un conversor de USD a Euros, se debe considerar:

#Tasa de cambio: Es un valor volátil, por lo que debe definirse como una variable (preferiblemente una constante al inicio o mediante una API).

#Validacion de entrada: Asegurarse de que el usuario ingrese valores numéricos positivos.

#Formato de salida: Redondear a dos decimales para representar centavos correctamente.

#Aplicación: Se solicita el monto en USD, se multiplica por el factor de conversión (ej. 0.92) y se muestra el resultado.