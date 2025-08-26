from abc import ABC, abstractmethod

RAÇAS = ["humano", "elfo", "anão", "halfling", "gnomo", "meioelfo"]

class Raça(ABC):
    def __init__(self, movimento, infravisao, alinhamento):
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento

    @abstractmethod
    def habilidades(self):
        pass

class humano(Raça):
    def __init__(self):
        super().__init__(movimento = 9, infravisao = 0, alinhamento = "Qualquer")

    def habilidades(self):
        Habilidades = ["APRENDIZADO", "ADAPTIBILIDADE"]

class elfo(Raça):
    def __init__(self):
        super().__init__(movimento = 9, infravisao = 18, alinhamento = "Neutro")

    def habilidades(self):
        Habilidades = ["APRENDIZADO", "ADAPTIBILIDADE"]
    
class anão(Raça):
    def __init__(self):
        super().__init__(movimento = 9, infravisao = 18, alinhamento = "Ordem")

    def habilidades(self):
        Habilidades = ["APRENDIZADO", "ADAPTIBILIDADE"]

class halfling(Raça):
    def __init__(self):
        super().__init__(movimento = 9, infravisao = 0, alinhamento = "Neutro")

    def habilidades(self):
        Habilidades = ["APRENDIZADO", "ADAPTIBILIDADE"]

class gnomo(Raça):
    def __init__(self):
        super().__init__(movimento = 9, infravisao = 18, alinhamento = "Neutro")

    def habilidades(self):
        Habilidades = ["APRENDIZADO", "ADAPTIBILIDADE"]

class meioelfo(Raça):
    def __init__(self):
        super().__init__(movimento = 9, infravisao = 9, alinhamento = "Caos")

    def habilidades(self):
        Habilidades = ["APRENDIZADO", "ADAPTIBILIDADE"]