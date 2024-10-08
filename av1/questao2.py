#questao 2
par = 0
impar = 0

#estrutura para rodar o input 10vzs e solicitar 10 num
for _ in range(10):
    num = int(input("Digite um número inteiro: "))  #entrada de um num de cada vez

    if num % 2 == 0:  #se o resto da divisão for 0, é par
        par += 1  #conta 1 a mais nos pares
    else:
        impar += 1  #conta 1 a mais nos ímpares

print("Qtd de números pares: ", par)
print("Qtd de números ímpares: ", impar)