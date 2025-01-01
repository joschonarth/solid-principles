"""
L - Liskov Substitution Principle (LSP) - Princípio da Substituição de Liskov

Objetos podem ser substituídos por seus subtipos sem que isso afete a execução correta do programa.

"O LSP pode e deve ser estendido ao nível da arquitetura. Uma simples violação de substituição, pode fazer com que a arquitetura de um sistema seja poluída com uma significativa quantidade de mecanismos extras." 
"""

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

def testar_forma(forma):
    print(f"Área: {forma.calcular_area()}")

ret = Retangulo(5, 10)
testar_forma(ret)

quad = Quadrado(4)
testar_forma(quad)
