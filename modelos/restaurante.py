# 1 criar uma classe Restaurante
class Restaurante:
    nome=''
    categoria=''
    ativo=False

 # 2 criação de objetos
 restaurante_praca=Restaurante()
 restaurante_praca.nome='praça'
 restaurante_praca.categoria='Gourmet' 


# questão 1
restaurante_praca.categoria='italiana'
print(restaurante_praca.categoria)
print('')

# questão 2
nome_restaurante=restaurante_praca.nome
print(nome_restaurante)
print('')

# questão 3
if restaurante_praca.ativo:
    print('O restaurant esta ativo')
    else:
        print('O restaurante esta inativo')
        print('')

# questão 4
categoria=Restaurante.categoria
print(categoria)
print('')

#  questão 5
restaurante_praca.nome='Bistro'
print(restaurante_praca.nome)
print('')

#  questão 6
restaurante_pizza.nome='Pizza place'
restaurante_pizza='Fast Food'
print(vars(restaurante_pizza))
print('')

# questão 7
if restaurante_pizza.categoria='Fast Food'
print('A categoria é fast food')
else:
    print('A categoria não fast food')
print('')

# questão 8
restaurante_pizza.ativo=False
print(restaurante_pizza.ativo)
print('')

# questão 9
print(f_'Nome: '(restaurante_praca.nome), 'categoria:')