"""
I - Interface Segregation Principle (ISP) - Princípio da Segregação de Interfaces

Uma classe não deve ser forçada a implementar interfaces que ela não utiliza

Em vez disso, interfaces devem ser segregadas com conjuntos menores e mais específicos de métodos.
"""

from abc import ABC, abstractmethod

# Interfaces segregadas
class Impressora(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Digitalizadora(ABC):
    @abstractmethod
    def digitalizar(self):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass

# Impressora a laser que só imprime
class ImpressoraLaser(Impressora):
    def imprimir(self):
        print("Imprimindo com Impressora a Laser")

# Impressora multifuncional que implementa todos os métodos
class ImpressoraMultifuncional(Impressora, Digitalizadora, Fax):
    def imprimir(self):
        print("Imprimindo com Impressora Multifuncional")

    def digitalizar(self):
        print("Digitalizando com Impressora Multifuncional")

    def fax(self):
        print("Enviando fax com Impressora Multifuncional")

def testar_impressora(impressora):
    impressora.imprimir()

def testar_digitalizadora(digitalizadora):
    digitalizadora.digitalizar()

def testar_faxineira(faxineira):
    faxineira.fax()

laser = ImpressoraLaser()
testar_impressora(laser)  # Funciona corretamente, pois a ImpressoraLaser só implementa o  método imprimir

multifuncional = ImpressoraMultifuncional()
testar_impressora(multifuncional)
testar_digitalizadora(multifuncional)
testar_faxineira(multifuncional)
