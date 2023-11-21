import numpy as np

# Carregando o dataset
dataset = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')
dataset_no_header = dataset[1:, :]

# Questão 1
# Mostre qual a média de idade dos clientes presentes neste dataset;
print('\n================== Questão 1 ==================')
avg_age = np.mean(dataset[1:, 1:2].astype(int))
print(f'Idade média dos clientes: {avg_age}')

# Questão 2
# Mostre quantos clientes gastaram mais que a média de gastos das compras deste dataset
print('\n================== Questão 2 ==================')
costs = dataset[1:, 5:6].astype(float)
avg_cost = np.mean(costs)
amount_above_avg = len(costs[costs > avg_cost])
print(f'{amount_above_avg} gastaram mais dinheiro do que a média de gastos, que foi igual a {avg_cost}')

# Questão 3
# Mostre qual é a porcentagem de vendas do item menos vendido da loja
print('\n================== Questão 3 ==================')
sold_items = np.unique(dataset[1:, 3:4], return_counts=True)
total_sold = np.sum(sold_items[1])
less_sold_item = sold_items[0][sold_items[1].argmin()]
less_sold_percent = (sold_items[1].min() / total_sold) * 100
print(f'O item menos vendido foi {less_sold_item}, totalizando apenas {less_sold_percent}% de todas as vendas')

# Questão 4
# Mostre qual a porcentagem de vendas que tiveram algum tipo de desconto
print('\n================== Questão 4 ==================')
disc_applied = dataset[1:, 13:14]
total_disc_applied = len(disc_applied[np.char.find(disc_applied, "Yes") >= 0])
disc_percent = (total_disc_applied / len(disc_applied)) * 100
print(f'Porcentagem de vendas com desconto aplicado: {disc_percent}%')

# Questão 5
# Mostre qual a cor de roupa mais popular no verão segundo este dataset
print('\n================== Questão 5 ==================')
colors = dataset[1:, 8:9]
category = dataset[1:, 4:5]
seasons = dataset[1:, 9:10]

summer_colors = colors[(np.char.find(seasons, "Summer") >= 0) & (np.char.find(category, "Clothing") >= 0)]
colors_counts = np.unique(summer_colors, return_counts=True)
most_popular_summer_clothes = colors_counts[0][colors_counts[1].argmax()]
print(f'A cor mais popular durante o verão foi {most_popular_summer_clothes}')