from typing import final

@final
class Base:
    pass

# NOTA: Un linter (como MyPy) marcará esto como ERROR en tu editor, 
# pero Python en ejecución lo procesará siguiendo su filosofía.
class Derivada(Base):
    pass

print("Código ejecutado. (Recuerda que Python permite la herencia "
      "en runtime; el bloqueo es solo a nivel de linter/MyPy).")