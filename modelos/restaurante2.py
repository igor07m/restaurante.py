# 1 criar uma classe Restaurante
class Restaurante:
    
    restaurantes= []
    
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
        
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# 2 criação de objetos
restaurante_praca=Restaurante('Praça','Gourmet')

restaurante_pizza=Restaurante('Pizza Express','Italiana')

# restaurante=[restaurante_praca,restaurante_pizza]

# 3 contribuindo os objetos
print(vars(restaurante_praca))
print(vars(restaurante_pizza))
print('')

print(restaurante_praca)
print(restaurante_pizza)
print('')

Restaurante.listar_restaurantes()