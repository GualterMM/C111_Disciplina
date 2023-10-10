import numpy as np

# Exercicio 1 - Crie um array de floats com 10 elementos positivos e negativos entre 0 e 1. Em seguida, multiplique seus valores por 100 e crie um novo vetor apenas com a parte inteira destes números (use seed(5)).
print("==== Exercicio 1 ====")

np.random.seed(5)
arr = np.random.randn(10)
arr = arr * 100
integer_array = arr.astype(int)
print(integer_array)

# Exercicio 2 - Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros entre 1 e 50 (use seed(10)).
print("\n==== Exercicio 2 ====")

np.random.seed(10)
mtz = np.random.randint(1, 50, 16).reshape([4,4])
print(mtz)

# Exercicio 3 - Mostre o resultado da média de cada linha e cada coluna da matriz gerada pela questão 2, e em seguida, apresente o maior valor das médias para as linhas e também para as colunas.
print("\n==== Exercicio 3 ====")

print("Medias por linha: ", mtz.mean(axis=1))
print("Medias por coluna: ", mtz.mean(axis=0))
print("Maior media por linha: ", max(mtz.mean(axis=1)))
print("Maior media por coluna: ", max(mtz.mean(axis=0)))

# Exercicio 4 - Baseado na matriz gerada na questão 2, mostre a quantidade de aparições de cada um dos números na mesma. Em seguida, mostre apenas os números que aparecem 2 vezes.
print("\n==== Exercicio 4 ====")

print("Quantidade de aparicao por numero: ", np.unique(mtz, return_counts=True))
mtz_cond = np.unique(mtz, return_counts=True)[0]
print("Numeros que aparecem 2 vezes: ", mtz_cond[np.unique(mtz, return_counts=True)[1] == 2])
