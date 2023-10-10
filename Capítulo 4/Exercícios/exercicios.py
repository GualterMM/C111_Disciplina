import numpy as np
import random

# Exercício 1 - Crie um Array de tamanho 21 com valores linearmente espaçados entre 0 e 1
print("==== Exercicio 1 ====")
arr_ex1 = np.linspace(0, 1, 21)
print(arr_ex1)
print()

# Exercício 2 - Crie dois Arrays: um de número pares de 0 até 51 e outro também de número pares de 100 até 50. Em seguida, os concatene e mostre os resultados ordenados
print("\n==== Exercicio 2 ====")
arr_pares_1 = np.arange(0, 51, 2)
arr_pares_2 = np.arange(100, 49, -2)

arr_resultante = np.sort(np.concatenate((arr_pares_1, arr_pares_2)))
print(arr_resultante)
print()

# Exercício 3 - Ordene os resultados do array resultante da questão anterior em ordem decrescente
print("\n==== Exercicio 3 ====")

arr_dec = np.sort(arr_resultante)[::-1]

print(arr_dec)

# Exercício 4 - Crie uma matriz formada somente por uns de tamanho 3x4. Em seguida, transforme-a em um Array 1-D
print("\n==== Exercicio 4 ====")

arr_uns = np.ones((3, 4))

arr_1d = arr_uns.flatten()

print("Matriz 3x4:")
print(arr_uns)

print("\nArray 1-D:")
print(arr_1d)

# Exercício 5 - Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor com número par ou ímpar de elementos
print("\n==== Exercicio 5 ====")

arr_rand = np.zeros((random.randint(1,10),random.randint(1,10)))

print("Formato:", arr_rand.shape)

x = arr_rand.shape[0]
y = arr_rand.shape[1]

z = x*y

if z%2 == 0:
    print("A matriz poderia ser um vetor com numero par de elementos")
else:
    print("A matriz poderia ser um vetor com numero impar de elementos")