#questao 6
sal = 1000.00
aumento = 1.5/100

for y in range(1996, 2026): #vai de 96 a 25 (o ultimo n conta)
  sal += sal * aumento #salario vzs o aumento de cada ano
  aumento *= 2 #aumento dobra a cada ano

print("Salário de ", y, "-", "R$", sal)