from typing import final

class Padre:
    @final
    def metodo_sagrado(self):
        print("No me cambies.")

class Hijo(Padre):
    # NOTA: Un linter (como MyPy) marcará esto como ERROR por intentar sobreescribir.
    def metodo_sagrado(self):
        print("Intentando cambiarlo.")

# Uso del código
objeto_hijo = Hijo()
objeto_hijo.metodo_sagrado()