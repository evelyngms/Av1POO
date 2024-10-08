gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

totalAlunos = 0
notas = [] #armazena os acertos
continuar = 'SIM'

while continuar.upper() == 'SIM': #continua o looping enquanto mais alunos forem utilizar
    acertos = 0
    totalAlunos += 1 #incrementa mais 1 aluno

    print(f"Aluno {totalAlunos}") #numeração do aluno q estiver utilizando o sistema
    for q in range(10): #estrutura de repetição q pede as respostas das questoes
        resposta = input(f"Digite a resposta da questão {q+1}: ").upper() #soma 1 para cada questao e deixa em capslock
        if resposta == gabarito[q]: 
            acertos += 1 #se a resposta corresponder ao gabarito, add 1ponto

    notas.append(acertos)
    print(f"Você teve {acertos} acertos | Nota: {acertos}/10.") #contagem de acertos

    continuar = input("Outro aluno irá conferir o gabarito? (SIM/NÃO): ")

if totalAlunos > 0:
    maiorNota = max(notas) #maior nota da turma
    menorNota = min(notas) #menor nota da turma
    mediaNotas = sum(notas) / totalAlunos  #soma das notas dividido pela qtd de alunos

    print("\nResultados finais:") #\n para quebra de linha
    print(f"a. Maior nota: {maiorNota}")
    print(f"b. Menor nota: {menorNota}")
    print(f"c. Total de alunos: {totalAlunos}")
    print(f"d. Média das notas da turma: {mediaNotas:.2f}")
else:
    print("Nenhum aluno utilizou o sistema")
