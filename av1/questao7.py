valorDivida = float(input("Digite o valor da dívida: R$ "))

#valores q a questao deu
parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

#pra cada quantidade de parcelas calcula os juros e o v das parcelas
for i in range(len(parcelas)): #range para a sequencia e len para return a qtd de parcelas
    vJuros = valorDivida * (juros[i] / 100) #multiplica a divida pelo juros de cada parcela
    vTotal = valorDivida + vJuros #calculo do montante
    vParcela = vTotal / parcelas[i] #parcelas após o juros
    
    #resultados na sequencia e valores arredondados pra 2 casas
    print(f"Dívida: R$ {vTotal:.2f} / Juros: {juros[i]}% / Parcelas: {parcelas[i]} / Valor da Parcela: R$ {vParcela:.2f}")
