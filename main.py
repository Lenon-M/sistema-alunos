alunos = []

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

alunos.append({
    "nome": nome,
    "media": media
})

print("\nAluno cadastrado:")
print("Nome:", nome)
print("Média:", media)

