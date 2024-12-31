"""
O - Open-Closed Principle (OCP) - Princípio Aberto-Fechado

"Um artefato de software deve ester aberto para extensão, mas fechado para modificação."

"Em outras palavras, o comportamento de um artefato de software deve ser extensível, sem ter que modificar esse artefato."
"""

from abc import ABC, abstractmethod

# Interface para os exames
class Exame(ABC):
    @abstractmethod
    def verificar_condicoes(self):
        pass

# Implementação para exame de sangue
class ExameSangue(Exame):
    def verificar_condicoes(self):
        # Condições específicas para exame de sangue
        print("Verificando condições do exame de sangue...")
        return True

# Implementação para exame de raio-x
class ExameRaioX(Exame):
    def verificar_condicoes(self):
        # Condições específicas para exame de raio-x
        print("Verificando condições do exame de raio-x...")
        return True

# Classe para aprovação de exames
class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        if exame.verificar_condicoes():
            print(f"{exame.__class__.__name__} aprovado!")
        else:
            print(f"{exame.__class__.__name__} não aprovado!")

# Exemplo de uso:
if __name__ == "__main__":
    exame_sangue = ExameSangue()
    exame_raio_x = ExameRaioX()

    aprovador = AprovaExame()
    aprovador.aprovar_solicitacao_exame(exame_sangue)
    aprovador.aprovar_solicitacao_exame(exame_raio_x)
