from abc import ABC, abstractmethod

class Encriptador(ABC): # Actúa como interfaz pura (todos sus métodos son abstractos)
    @abstractmethod
    def encriptar(self, datos: str) -> str:
        pass

    @abstractmethod
    def desencriptar(self, datos: str) -> str:
        pass

class EncriptadorAES(Encriptador):
    def encriptar(self, datos: str) -> str:
        return f"AES({datos})"

    def desencriptar(self, datos: str) -> str:
        return datos.replace("AES(", "").replace(")", "")

# Uso del código
encriptador = EncriptadorAES()
texto_oculto = encriptador.encriptar("HolaClase")
print(f"Encriptado: {texto_oculto}")

texto_original = encriptador.desencriptar(texto_oculto)
print(f"Desencriptado: {texto_original}")