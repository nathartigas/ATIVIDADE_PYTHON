# Questão 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro("Fusca", "Azul", 1972)


# Questão 2
class Restaurante:
    def __init__(self, nome, categoria, ativo, capacidade, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.localizacao = localizacao

meu_restaurante = Restaurante("Restaurante do João", "Brasileiro", True, 50, "Rua Principal")


# Questão 3
class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=50, localizacao=""):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.localizacao = localizacao

restaurante_padrao = Restaurante("Restaurante Padrão", "Internacional")


# Questão 4
class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=50, localizacao=""):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.localizacao = localizacao

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}"

    @property
    def ativo(self):
        return "Ativado" if self.ativo else "Desativado"

restaurante_exemplo = Restaurante("Restaurante Exemplo", "Italiano")
print(restaurante_exemplo)  


# Questão 5
class Cliente:
    def __init__(self, nome, idade, genero, endereco):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.endereco = endereco

cliente1 = Cliente("João", 30, "Masculino", "Rua A")
cliente2 = Cliente("Maria", 25, "Feminino", "Rua B")
cliente3 = Cliente("Pedro", 35, "Masculino", "Rua C")



