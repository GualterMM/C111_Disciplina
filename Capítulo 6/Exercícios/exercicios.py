import matplotlib.pyplot as plt
import pandas as pd

# Carregando os datasets
dfPaises = pd.read_csv("../../Capítulo 5/paises.csv", delimiter=";")
dfEspaco = pd.read_csv("../../Capítulo 4/Exercícios/space.csv", delimiter=";")

# Exercício 1 - Trace um gráfico em barras mostrando quantas empresas espaciais os EUA e a CHINA possuem
empresas_us = dfEspaco["Location"].str.contains("USA").sum()
empresas_ch = dfEspaco["Location"].str.contains("China").sum()

plt.title("Quantidade de empresas espaciais por país")
plt.bar(["USA", "China"], [empresas_us, empresas_ch])
plt.show()

# Exercício 2 - Trace dois gráficos de linhas em um mesmo plano cartesiano, um mostrando a taxa de mortalidade e outro a taxa de natalidade dos países da América do Norte.
paises_na = dfPaises[dfPaises["Region"].str.contains("NORTHERN AMERICA")]
taxa_nat = paises_na["Birthrate"]
taxa_mor = paises_na["Deathrate"]

plt.title("Comparação de taxas de natalidade e mortalidade na América do Norte")
plt.plot(paises_na["Country"], taxa_nat, 'r-', paises_na["Country"], taxa_mor)
plt.show()

