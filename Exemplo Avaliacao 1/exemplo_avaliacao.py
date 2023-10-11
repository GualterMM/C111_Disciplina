import numpy as np

# Carregando o dataset
dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8')

# Questão 1 - Faça um slicing no dataset para mostrar apenas o País (Country), Região (Region), População (Population) e Area (Area (sq. mi.)) dos países contidos nele
sliced_array = dataset[:,0:4].copy()
print("================= Questão 1 =================")
print(sliced_array)
print('\n')

# Questão 2 - Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset
print("================= Questão 2 =================")
unique_regions = np.unique(dataset[1:, 1])
print(unique_regions)
print('\n')

# Questão 3 - Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset
print("================= Questão 3 =================")
literacy_mean = np.mean(dataset[1:,9].astype(float))
print("Taxa média de alfabetização mundial: ", literacy_mean, "%")
print('\n')

# Questão 4 - Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset
print("================= Questão 4 =================")
regions = dataset[1:,1]
na_regions = np.char.find(regions, 'NORTHERN AMERICA')
na_countries = len(regions[na_regions >= 0])
print("Quantidade de países na América do Norte: ", na_countries)
print('\n')

# Questão 5 - Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui a maior renda per capita (GDP ($ per capita));
print("================= Questão 5 =================")
regions = dataset[1:, 1]
gdp = dataset[1:, 8].astype(float)

result = np.char.find(regions, 'LATIN AMER. & CARIB')
gdp_la = gdp[result>=0]
indice = np.where(gdp==np.max(gdp_la))[0][0]

print("Pais: ", dataset[indice+1, 0])
print("Renda per capita: ", np.max(gdp_la))