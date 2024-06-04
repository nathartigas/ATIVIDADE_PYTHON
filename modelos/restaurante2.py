# #1 criar uma classe Restaurante usando construtor
# class Restaurante:
#     def __init__(self,nome,categoria):
#     self.nome=nome
#     self.categoria=categoria
#     self.ativo=False

# def __str__(self):
#     return self.nome

# # 2 criação de objetos
# restaurante_praca=Restaurante('Praça','Gourmet')

# restaurante_pizza=Restaurante('Pizza Express','Italiana')


# restaurantes=[restaurante_praca,restaurante_pizza]

# #print(dir(restaurante_pizza.ativo))

# #3 consumindo os objetos
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print('')

# print(restaurante_praca)
# print(restaurante_pizza)
# print('')



class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}"

    # Criar um método para listar restaurantes
    @staticmethod
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f" {restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}")

# Criando objetos
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# Consumindo os objetos
for restaurante in Restaurante.restaurantes:
    print(restaurante)

# Listando os restaurantes
print("\nListagem de restaurantes:")
Restaurante.listar_restaurantes()

