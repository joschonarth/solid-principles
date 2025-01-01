from abc import ABC, abstractmethod

class Impressora(ABC):
    @abstractmethod
    def imprimir(self):
        pass
    
    @abstractmethod
    def digitalizar(self):
        pass
    
    @abstractmethod
    def fax(self):
        pass

# Impressora a laser que só imprime
class ImpressoraLaser(Impressora):
    def imprimir(self):
        print("Imprimindo com Impressora a Laser")
    
    def digitalizar(self):
        pass  # Não implementa digitalização

    def fax(self):
        pass  # Não implementa fax

# Impressora multifuncional que implementa todos os métodos
class ImpressoraMultifuncional(Impressora):
    def imprimir(self):
        print("Imprimindo com Impressora Multifuncional")

    def digitalizar(self):
        print("Digitalizando com Impressora Multifuncional")

    def fax(self):
        print("Enviando fax com Impressora Multifuncional")

def testar_impressora(impressora):
    impressora.imprimir()
    impressora.digitalizar()
    impressora.fax()

# A impressora laser não pode implementar corretamente os métodos de digitalização e fax
laser = ImpressoraLaser()
testar_impressora(laser)  # Isso é um problema porque a ImpressoraLaser não pode digitalizar ou enviar fax
