
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