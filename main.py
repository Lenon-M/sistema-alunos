print("=== SISTEMA DE CADASTRO DE ALUNOS ===")

alunos = []

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "APROVADO"
else:
    print('\nBurrão! KAKAKAKA')
    situacao = "REPROVADO"
    

alunos.append({
    "nome": nome,
    "media": media,
    "situacao": situacao
})

print("\nAluno cadastrado:")
print("Nome:", nome)
print("Média:", media)
print("Situação:", situacao)

