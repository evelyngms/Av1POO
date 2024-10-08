#questao 3
num = int(input("Digite um número inteiro"))

if num < 2:
  primo = False #um num só pode ser primo a partir do 2
else:
  for n in range(2, num): #seleciona todos os divisores de 2 ate o num
    if num % n == 0: #resto da divisão por todos os num até ele
      primo = False #se o num tiver outro divisor alem de 1 e ele mesmo, nao é primo
      break #quebra de contagem

if primo:
  print(num, "é primo")
else:
  print(num, "não é primo")

"""
num = int(input("Digite um número inteiro: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
        else:
        print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
"""