#FRUTEIRA!


qtdemorango = int(input("Escreva a quantidade total de morangos(em kg) que pretende levar:\n"))

qtdemaca = int(input("Agora, escreva a quantidade total de maçãs(em kg) que pretende levar:\n"))

def CalculaPrecoMorango(qtdemorango):
    if(qtdemorango > 5):
        precoMorango = 2.20 * qtdemorango

    else:
        precoMorango = 2.50 * qtdemorango
    return precoMorango

def CalculaPrecoMaca(qtdemaca):
    if(qtdemaca > 5):
        precoMaca = 1.50 * qtdemaca
    else:
        precoMaca = 1.80 * qtdemaca

    return precoMaca

resultadoPreco = float(CalculaPrecoMorango(qtdemorango) + CalculaPrecoMaca(qtdemaca))

if(qtdemorango + qtdemorango > 8 or resultadoPreco > 25):
    desconto = resultadoPreco * 0.10
    NovoPreco = resultadoPreco - desconto
    print(f"Parabéns, você ganhou um desconto de 10% , sobre o valor final da compra!\n")
    print(f"Você cumpriu ao menos um dos seguintes critérios:\n")
    print(f"Você levou mais de 8kg em frutas.\n")
    print(f"Ou então, o valor total da compra deu mais que R$25,00.\n")   
    print(f"Nesse caso o preço final a ser pago é de R$%.2f\n" % NovoPreco)
else:
    print(f"O valor final a ser pago é de R$%.2f\n" % resultadoPreco) 

