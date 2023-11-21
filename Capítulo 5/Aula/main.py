import numpy as np
import pandas as pd

# 1D - Series
# Exige chave e valor como parâmetro (dicionário)
dic = {'a': 10, 'b': 20, 'c': 30}
series1 = pd.Series(dic)
print(series1)
print(type(series1))

# Modo de criação alternativo
labels = ['a', 'b', 'c']
dados = [10, 20, 30]
series2 = pd.Series(data=dados, index=labels)

# Acessando o valor de uma chave
print(series1['a'])

# Acessando múltiplos valores
print(series1[['a', 'b']])

# Fazendo operações em array com NumPy
print(np.mean(series1))

# Usando notação númerica no Pandas (alfabético)
print(series1[1:])

# 2D+ - Dataframe
np.random.seed(10)
df = pd.DataFrame(index=['A', 'B', 'C', 'D', 'E',], columns=['W', 'X', 'Y', 'Z'], data=np.random.randint(1, 50, [5,4]))
print(df)

# Acessnado um valor do Dataframe (1° parâmetro - linha, 2° parâmetro - coluna)
print(df['Y']['C'])

# Pegando apenas uma coluna
print(df['X'])

# Importando dataset
dataset = pd.read_csv('Capítulo 5/paises.csv', delimiter=';')

# Mostrar os primeiros 4 elementos
print(dataset.head(4))

# Mostrar os últimos 4 elementos
print(dataset.tail(4))

# Mostrar as colunas do dataset
print(dataset.columns)