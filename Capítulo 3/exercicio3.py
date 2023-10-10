nome = input("Entre com o nome: ") 
media = input("Entre com a média: ")

aluno = {"Nome" : nome, "Média" : media}

if int(media) >= 60:
    aluno["Situação"] = "AP"
else:
    aluno["Situação"] = "RP"

print(aluno)