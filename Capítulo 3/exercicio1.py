times = ['Real Madrid', 'Bayern de Munique', 'Milan', 'Barcelona', 'Boca Juniors']

print("Primeiros três colocados: ")
print(times[:3])

print("Últimos dois colocados: ")
print(times[3:])

print("Ordem alfabética dos times: ")
print(sorted(times))

print("Colocação do Barcelona: ")
print(times.index("Barcelona") + 1)