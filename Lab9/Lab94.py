class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b # No usa 'self' ni 'cls'

# Se llama directamente sin instanciar la clase
resultado = Calculadora.sumar(5, 3)
print(f"Resultado de la suma estática (5 + 3): {resultado}")