import pandas as pd
import numpy as np

paises = pd.read_csv('Capítulo 5/paises.csv', delimiter=';')

# Exercício 1 - Mostre quais os países da OCEANIA e quantos países são da OCEANIA
print("==== Exercício 1 ====")
paises_oceania = paises[paises.Region.str.contains("OCEANIA")]
print("Países pertencentes a Ocenia: \n", paises_oceania['Country'])
print("Quantidade de países na Oceania: ", len(paises_oceania))

# Exercício 2 - Mostre a média da taxa de alfabetização (Literaçy (%)) do planeta
print("==== Exercício 2 ====")
media = paises['Literacy (%)'].mean()
print(f"Média da taxa de alfabetização: {media:.2f}")

# Exercício 3 - Encontre o nome e a região do país que possui a maior população
print("==== Exercício 3 ====")
linha_pais = paises.loc[paises['Population'].idxmax()]
print("País com a maior população:", linha_pais['Country'])
print("Região:", linha_pais['Region'])
print("Número de habitantes:", linha_pais['Population'])

# Exercício 4 - Busque o nome de todos os países do dataset que não possuem costa marítima (Coastline (coast/area radio) == 0) e guarde-os em um novo arquivo chamado noCoast.csv
print("==== Exercício 4 ====")
paises_no_coast = paises[paises['Coastline (coast/area ratio)'] == 0]
print("Salvando arquivo .csv...")
paises_no_coast.to_csv('Capítulo 5/Exercicios/noCoast.csv', sep=';')
print("Arquivo salvo em \'Capítulo 5/Exercicios/noCoast.csv\'.")