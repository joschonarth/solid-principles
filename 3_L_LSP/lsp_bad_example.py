class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Subclasse Quadrado que quebra o LSP
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def set_largura(self, largura):
        self.largura = largura
        self.altura = largura  # Isso quebra a lógica do Retângulo

    def set_altura(self, altura):
        self.altura = altura
        self.largura = altura  # Isso também quebra a lógica do Retângulo

def testar_forma(retangulo):
    retangulo.set_largura(5)
    retangulo.set_altura(10)
    print(f"Área: {retangulo.calcular_area()}")

ret = Retangulo(2, 3)
testar_forma(ret)

quad = Quadrado(4)
testar_forma(quad)  # Resultado inesperado, pois altera ambos os lados