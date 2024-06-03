# Criando a classe Restaurante
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# Criando instâncias da classe Restaurante
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# 1)
restaurante_praca.categoria = 'Italiana'

# 2) 
nome_restaurante_praca = restaurante_praca.nome

# 3)
if restaurante_praca.ativo:
    mensagem_ativo = "O restaurante está ativo."
else:
    mensagem_ativo = "O restaurante está inativo."

# 4)
categoria = Restaurante.categoria

# 5)
restaurante_praca.nome = 'Bistrô'

# 6)
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7)
if restaurante_pizza.categoria == 'Fast Food':
    mensagem_categoria_pizza = "A categoria da instância é 'Fast Food'."

# 8)
restaurante_pizza.ativo = True

# 9)
print("Nome do restaurante:", restaurante_praca.nome)
print("Categoria do restaurante:", restaurante_praca.categoria)

# Imprimindo as mensagens
print(mensagem_ativo)
print("A categoria da classe Restaurante é:", categoria)
print(mensagem_categoria_pizza)

