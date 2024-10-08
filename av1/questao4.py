#questao 4
popA = 80000
popB = 200000
anos = 0

while popA < popB:
  popA += popA * 3/100 #aumento de 3% na popA
  popB += popB * 1.5/100 #aumento de 1,5% na popA
  anos += 1 #os aumentos acontecem por ano

print(anos, "anos serão necessários para a população A ultrapassar a população B")
