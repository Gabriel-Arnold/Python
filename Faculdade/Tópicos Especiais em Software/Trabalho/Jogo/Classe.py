from abc import ABC, abstractmethod

CLASSES = ["guerreiro", "mago", "ladrão"]

class Classe(ABC):
    def __init__(self, vida, nivel):
        self.vida = vida
        self.nivel = nivel

    @abstractmethod
    def habilidades(self):
        pass

class Guerreiro(Classe):
    def __init__(self, vida = 10, nivel = 1):
        super().__init__(vida, nivel)

    def habilidades(self):
        return super().habilidades()

class Ladrão(Classe):
    def __init__(self, vida = 6, nivel = 1):
        super().__init__(vida, nivel)

    def habilidades(self):
        return super().habilidades()

class Mago(Classe):
    def __init__(self, vida = 4, nivel = 1):
        super().__init__(vida, nivel)

    def habilidades(self):
        return super().habilidades()