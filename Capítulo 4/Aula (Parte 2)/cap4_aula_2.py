import numpy as np

# GERANDO NÚMEROS ALEATÓRIOS
np.random.seed(10)
arr = np.random.randint(1, 50, 25)

# Pegar valores únicos
print(np.unique(arr, return_counts=True))

# 4.6 Operações básicas co Arrays
mtz = np.random.randint(1, 10, 12).reshape(3, 4)
print(mtz)
print(mtz.sum(axis=0)) # Soma dos elementos da matriz, 0 = Coluna, 1 = Linha
print(mtz.sum(axis=1))
print(mtz.mean(axis=0)) # Média dos elementos da matriz, 0 = Coluna, 1 = Linha

# Broadcasting: Operações diretas nos elementos do array
print(mtz/5)
print(mtz*5)

# Operações condicionais no array
print(mtz%2==0) # Aplica operação de resto nos elementos do array, retornando em booleano quais elementos são pares
print(mtz[mtz%2==0]) # Aplica a "máscara" de booleanos, e retorna os elementos pares
print(mtz[mtz>5])

# Array de nomes
arr_nomes = np.array(['Sarah', 'Isabela', 'Lucas', 'Fernanda', 'Gualter'])
result = np.char.find(arr_nomes, "F") # Busca nomes contendo G, retorna índice da posição se houver
print(arr_nomes[result>=0])
