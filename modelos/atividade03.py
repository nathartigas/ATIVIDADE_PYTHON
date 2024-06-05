class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor 
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

# Questão 1
class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao == 'medico':
            return f'Olá Dr. {self.nome}'
        elif self.profissao == 'advogado':
            return f'Olá Dr. {self.nome}'
        else:
            return f'Olá {self.nome}'

# Questão 2 e 3
class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Conta de {self._titular} - Saldo: {self._saldo}'

    @classmethod
    def ativar_conta(cls):
        cls._ativo = True
        return cls._ativo

# Questão 5 e 6
class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Conta de {self._titular} - Saldo: {self._saldo}'

    @classmethod
    def ativar_conta(cls):
        cls._ativo = True
        return cls._ativo

    @property
    def titular(self):
        return self._titular

# Questão 4
class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Conta de {self._titular} - Saldo: {self._saldo}'

    @classmethod
    def ativar_conta(cls):
        cls._ativo = True
        return cls._ativo

# Questão 7 e 8
class ClienteBanco:
    def __init__(self, nome='', idade=0, profissao='', endereco='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def conta(cls):
        return ContaBancaria()

# Exemplo de uso
pessoa1 = Pessoa('João', 30, 'medico')
print(pessoa1.saudacao)

conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Maria', 500)
print(conta1)
print(conta2)

ContaBancaria.ativar_conta()
print(ContaBancaria._ativo)

cliente1 = ClienteBanco('Fulano', 25, 'estudante', 'Rua A, 123', '123456789')
cliente2 = ClienteBanco('Ciclano', 35, 'engenheiro', 'Rua B, 456', '987654321')
cliente3 = ClienteBanco('Beltrano', 40, 'advogado', 'Rua C, 789', '123789456')
