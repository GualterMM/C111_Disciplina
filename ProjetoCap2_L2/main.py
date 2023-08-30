# Capítulo 3 - Coleções

# 1. Tuplas
# Declarada por parênteses ()
# Imutável
# Melhor usada para armazenar dado que não necessitam de alteração (ex: Datasets)
nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print(nomes)

# Slicing - "Fatiamento" dos dados dentro das coleções
print(nomes[0]) # Primeiro elemento
print(nomes[2:]) # Do terceiro elemento pra frente
print(nomes[-1]) # Último elemento

# 2. Listas
# Declarada por colchetes []
# Alterável
nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
print(nomes[1:3])

# Inserção
nomes.append('Kuririn') # ou nomes.insert pra inserir antes de um dado índice

# Atualização
nomes[0] = 'Bulma'

# Remoção (por índice, padrão é o último elemento)
nomes.pop()

# Remoção (por conteúdo)
nomes.remove('Bulma') # ou del nomes[index]

# 3. Conjuntos
# Declarado por chaves {}
# Posição dos elementos é aleatória
# Valores são cópias (hash)
# Não são guardados elementos repetidos 
# Melhor usado para remover dados duplicados
nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Goku'}

# Inserção
nomes.add('Kuririn')

# Remoção
nomes.remove('Goku') # ou nomes.discard()

# Atualização

print(nomes)

# Casting
lista = [1, 1, 1, 2, 3, 4, 5, 5]
print("Lista: ", lista, "\nLista como conjunto", set(lista))

# 4. Dicionários
# Declarado por chaves {}, e populado por chave : valor
# Essencialmente um map
dados = {'nome' : 'Goku', 'idade' : 42, 'sexo': 'M'}

# Inserção
dados['cabelo'] = 'Castanho'

# Remoção
del dados['cabelo']

# Atualização
dados['idade'] = 43

print(dados)
print(dados['idade'])