# Princípios SOLID

Este repositório contém estudos e exemplos práticos sobre os cinco princípios de design SOLID, que ajudam a criar software mais robusto, manutenível e flexível. Os princípios SOLID são uma combinação de boas práticas de design de software orientado a objetos, que podem ser aplicados para melhorar a qualidade do código.

## Índice

- [Responsabilidade Única - Single Responsibility Principle (SRP)](#responsabilidade-única---single-responsibility-principle-srp)
- [Aberto-Fechado - Open/Closed Principle (OCP)](#aberto-fechado---open-closed-principle-ocp)
- [Substituição de Liskov - Liskov Substitution Principle (LSP)](#substituição-de-liskov---liskov-substitution-principle-lsp)
- [Segregação de Interface - Interface Segregation Principle (ISP)](#segregação-de-interface---interface-segregation-principle-isp)
- [Inversão de Dependência - Dependency Inversion Principle (DIP)](#inversão-de-dependência---dependency-inversion-principle-dip)

---

## Responsabilidade Única - Single Responsibility Principle (SRP)

O **Princípio da Responsabilidade Única (SRP)** afirma que **uma classe deve ter apenas uma razão para mudar**, ou seja, ela deve ser responsável por uma única tarefa.

### Exemplo:

```python
# Violando SRP
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def salvar_funcionario(self):
        # lógica para salvar o funcionário no banco de dados
        pass

# Correção: Aplicando SRP
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self):
        return self.salario

class RepositorioFuncionario:
    def salvar_funcionario(self, funcionario):
        # lógica para salvar o funcionário no banco de dados
        pass
```

## Aberto-Fechado - Open-Closed Principle (OCP)

O **Princípio do Aberto-Fechado (OCP)** afirma que **uma classe deve ser aberta para extensão, mas fechada para modificação**. Ou seja, devemos ser capazes de estender o comportamento de uma classe sem modificar seu código original.

### Exemplo:

```python
# Violando OCP
class Calculadora:
    def calcular(self, tipo, a, b):
        if tipo == "soma":
            return a + b
        elif tipo == "subtracao":
            return a - b
        # Se precisarmos de uma nova operação, a classe precisa ser modificada

# Correção: Aplicando OCP
from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def executar(self, a, b):
        pass

class Soma(Operacao):
    def executar(self, a, b):
        return a + b

class Subtracao(Operacao):
    def executar(self, a, b):
        return a - b

class Calculadora:
    def calcular(self, operacao: Operacao, a, b):
        return operacao.executar(a, b)
```

## Substituição de Liskov - Liskov Substitution Principle (LSP)

O **Princípio da Substituição de Liskov (LSP)** afirma que **os objetos de uma classe derivada devem poder ser substituídos por objetos da classe base sem alterar o comportamento correto do sistema**.

### Exemplo:

```python
# Violando LSP
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Quadrado(Retangulo):  # Quadrado é um tipo de retângulo
    def __init__(self, lado):
        super().__init__(lado, lado)

# A substituição de Retangulo por Quadrado pode quebrar a lógica de cálculo da área
```

```python
# Correção: Aplicando LSP
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Figura):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Quadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
```

## Segregação de Interface - Interface Segregation Principle (ISP)

O **Princípio da Segregação de Interface (ISP)** afirma que **os clientes não devem ser forçados a depender de interfaces que não utilizam**.

### Exemplo:

```python
# Violando ISP
class Impressora:
    def imprimir(self):
        pass
    
    def digitalizar(self):
        pass

class ImpressoraLaser(Impressora):
    def imprimir(self):
        print("Imprimindo com Laser")

    def digitalizar(self):
        pass  # Não implementa digitalização

# Correção: Aplicando ISP
class Impressora(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Digitalizadora(ABC):
    @abstractmethod
    def digitalizar(self):
        pass

class ImpressoraLaser(Impressora):
    def imprimir(self):
        print("Imprimindo com Laser")

class Multifuncional(Impressora, Digitalizadora):
    def imprimir(self):
        print("Imprimindo com Multifuncional")

    def digitalizar(self):
        print("Digitalizando com Multifuncional")
```

## Inversão de Dependência - Dependency Inversion Principle (DIP)

O **Princípio da Inversão de Dependência (DIP)** afirma que **módulos de alto nível não devem depender de módulos de baixo nível, ambos devem depender de abstrações**. Além disso, **abstrações não devem depender de detalhes, detalhes devem depender de abstrações**.

### Exemplo:

```python
# Violando DIP
class Notificador:
    def __init__(self):
        self.email_service = EmailService()  # Dependência direta de EmailService

    def enviar_notificacao(self, mensagem):
        self.email_service.enviar_email(mensagem)

class EmailService:
    def enviar_email(self, mensagem):
        print(f"Enviando e-mail com a mensagem: {mensagem}")

# Correção: Aplicando DIP
from abc import ABC, abstractmethod

class NotificacaoService(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class EmailService(NotificacaoService):
    def enviar(self, mensagem):
        print(f"Enviando e-mail com a mensagem: {mensagem}")

class Notificador:
    def __init__(self, notificacao_service: NotificacaoService):
        self.notificacao_service = notificacao_service  # Injeção de dependência

    def enviar_notificacao(self, mensagem):
        self.notificacao_service.enviar(mensagem)
```
