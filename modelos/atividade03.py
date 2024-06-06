# class Livro:
#     def __init__(self, titulo='', autor='', paginas=0):
#         self.titulo = titulo
#         self.autor = autor 
#         self.paginas = paginas

#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'

#     def aumentar_paginas(self, quantidade):
#         self.paginas += quantidade

# # Questão 1
# class Pessoa:
#     def __init__(self, nome='', idade=0, profissao=''):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao

#     def __str__(self):
#         return f'{self.nome}, {self.idade} anos, {self.profissao}'

#     def aniversario(self):
#         self.idade += 1

#     @property
#     def saudacao(self):
#         if self.profissao == 'medico':
#             return f'Olá Dr. {self.nome}'
#         elif self.profissao == 'advogado':
#             return f'Olá Dr. {self.nome}'
#         else:
#             return f'Olá {self.nome}'

# # Questão 2 e 3
# class ContaBancaria:
#     def __init__(self, titular='', saldo=0):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False

#     def __str__(self):
#         return f'Conta de {self._titular} - Saldo: {self._saldo}'

#     @classmethod
#     def ativar_conta(cls):
#         cls._ativo = True
#         return cls._ativo

# # Questão 5 e 6
# class ContaBancaria:
#     def __init__(self, titular='', saldo=0):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False

#     def __str__(self):
#         return f'Conta de {self._titular} - Saldo: {self._saldo}'

#     @classmethod
#     def ativar_conta(cls):
#         cls._ativo = True
#         return cls._ativo

#     @property
#     def titular(self):
#         return self._titular

# # Questão 4
# class ContaBancaria:
#     def __init__(self, titular='', saldo=0):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False

#     def __str__(self):
#         return f'Conta de {self._titular} - Saldo: {self._saldo}'

#     @classmethod
#     def ativar_conta(cls):
#         cls._ativo = True
#         return cls._ativo

# # Questão 7 e 8
# class ClienteBanco:
#     def __init__(self, nome='', idade=0, profissao='', endereco='', telefone=''):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao
#         self.endereco = endereco
#         self.telefone = telefone

#     @classmethod
#     def conta(cls):
#         return ContaBancaria()

# # Exemplo de uso
# pessoa1 = Pessoa('João', 30, 'medico')
# print(pessoa1.saudacao)

# conta1 = ContaBancaria('João', 1000)
# conta2 = ContaBancaria('Maria', 500)
# print(conta1)
# print(conta2)

# ContaBancaria.ativar_conta()
# print(ContaBancaria._ativo)

# cliente1 = ClienteBanco('Fulano', 25, 'estudante', 'Rua A, 123', '123456789')
# cliente2 = ClienteBanco('Ciclano', 35, 'engenheiro', 'Rua B, 456', '987654321')
# cliente3 = ClienteBanco('Beltrano', 40, 'advogado', 'Rua C, 789', '123789456')



















# class Livro:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo
#         self.autor = autor 
#         self.paginas = paginas

#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'

#     def aumentar_paginas(self, quantidade):
#         self.paginas += quantidade

# livro1=Livro('Tanto Faz','Jão',50)
# print(livro1)

# livro1.aumentar_paginas(90)
# print(livro1)
# print('')

# # Questão 1
# class Pessoa:
#     def __init__(self, nome, idade, profissao):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao

#     def __str__(self):
#         return f'{self.nome}, {self.idade} anos, {self.profissao}'

#     def aniversario(self):
#         self.idade += 1

#     @property
#     def saudacao(self):
#         if self.profissao:
#             print (f'Olá sou {self.nome}! trabalho com {self.profissao}')
#         else:
#             print( f'Olá sou {self.nome}')

# pessoa1=Pessoa('Aparicio',90,'Programador')
# print(pessoa1)
# print('')
# pessoa1.aniversario
# print(pessoa1)
# print('')
# pessoa1.saudacao
# print(pessoa1)
# print('')

# Questão 2 e 3
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Conta de {self._titular} - Saldo: R${self._saldo}'

# conta1=ContaBancaria('Nathan',3000.00)
# conta2=ContaBancaria('Joe',2.00)

# print(conta1)
# print('')
# print(conta2)


# Questão 4
#     @classmethod
#     def ativar_conta(cls):
#         cls._ativo = True
#         # return cls._ativo

# conta3=ContaBancaria('Arina',3.58)
# print(f'Antes de ativas: Conta ativa? {conta3._ativo}')
# ContaBancaria.ativar_conta(conta3)
# print(f'Depois de ativas: Conta ativa? {conta3._ativo}')

# Questão 5 e 6
# class ContaBancariaPythonica:
#     def __init__(self, titular, saldo):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False

#     @property
#     def titular(self):
#         return self._titular

#     @property
#     def titular(self):
#         return self._titular

#     @property
#     def titular(self):
#         return self._titular

# conta4=ContaBancariaPythonica('Josefino',1500.03)
# print(f'Titular da conta 4 é: {conta4.titular}' )



# Questão 7 e 8
class ClienteBanco:
    def __init__(self, nome, idade, profissao, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.endereco = endereco
        self.telefone = telefone


cliente1 = ClienteBanco('Fulano', 25, 'medico', 'Rua A, 123', '123456789')
cliente2 = ClienteBanco('Ciclano', 35, 'engenheiro', 'Rua B, 456', '987654321')
cliente3 = ClienteBanco('Beltrano', 40, 'advogado', 'Rua C, 789', '123789456')


@classmethod
def criar_conta(cls,titular,saldo_inicial):
        conta=ClienteBanco(titular,saldo_inicial)
        return conta

conta_cliente1=ClienteBanco.criar_conta('Tertulia',999.99)
print(f'Conta de {conta_cliente1.titular} Com saldo de R${conta_cliente1.saldo_inicial}')

