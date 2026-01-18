#MAIS UM PROGRAMA EM PYTHON, PARA MANUSEAR INFORMAÇÕES DE UM SUPERMERCADO

print("Escolha um tipo de carne, dentre as opções disponíveis!\n")
print("1->FILÉ DUPLO (R$ 4,90 por kg , para até 5kg)<-->(R$5,80 por kg, para mais do que 5kg)!\n")
print("2->ALCATRA (R$ 5,90 por kg , para até 5kg)<-->(R$6,80 por kg, para mais do que 5kg)!\n")
print("3->PICANHA (R$ 6,90 por kg , para até 5kg)<-->(R$7,80 por kg, para mais do que 5kg)!\n")

escolha = int(input())

if(escolha == 1):
    print("Ok, digite a quantidade(em kg) de filé duplo, que pretende levar:\n")
    qtdefile = int(input())
    if(qtdefile <= 5):
        preco = 4.90 * qtdefile
        print("Possui cartão de desconto promocional:\n")
        print("1 --> SIM\n")
        print("0 --> NÃO\n")
        NovaEscolha = int(input())
        if(NovaEscolha == 1):
            Desconto = preco * 0.05
            NovoPreco = preco - Desconto
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 5%\n")
            print(f"O valor a pagar é R$%.2f\n" % NovoPreco)
            print(f"Valor do desconto: R$%.2f\n" % Desconto)
            print("Tipo de carne: FILÉ DUPLO.\n")
            print(f"Quantidade de FILÉ DUPLO(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")

        elif(NovaEscolha == 0):
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 0%\n")
            print(f"O valor a pagar é R$%.2f\n" % preco)
            print(f"Valor do desconto é de R$0,00\n")
            print("Tipo de carne: FILÉ DUPLO.\n")
            print(f"Quantidade de FILÉ DUPLO(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")
        else:
            print("Dado inválido, tente novamente!\n")
            exit(1)

    else:
        preco = 5.80 * qtdefile
        print("Possui cartão de desconto promocional:\n")
        print("1 --> SIM\n")
        print("0 --> NÃO\n")
        NovaEscolha = int(input())
        if(NovaEscolha == 1):
            Desconto = preco * 0.05
            NovoPreco = preco - Desconto
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 5%\n")
            print(f"O valor a pagar é R$%.2f\n" % NovoPreco)
            print(f"Valor do desconto: R$%.2f\n" % Desconto)
            print("Tipo de carne: FILÉ DUPLO.\n")
            print(f"Quantidade de FILÉ DUPLO(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")

        elif(NovaEscolha == 0):
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 0%\n")
            print(f"O valor a pagar é R$%.2f\n" % preco)
            print(f"Valor do desconto é de R$0,00\n")
            print("Tipo de carne: FILÉ DUPLO.\n")
            print(f"Quantidade de FILÉ DUPLO(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")
        else:
            print("Dado inválido, tente novamente!\n")
            exit(1)

elif(escolha == 2):
    print("Ok, digite a quantidade(em kg) de alcatra, que pretende levar:\n")
    qtdefile = int(input())
    if(qtdefile <= 5):
        preco = 5.90 * qtdefile
        print("Possui cartão de desconto promocional:\n")
        print("1 --> SIM\n")
        print("0 --> NÃO\n")
        NovaEscolha = int(input())
        if(NovaEscolha == 1):
            Desconto = preco * 0.05
            NovoPreco = preco - Desconto
            
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 5%\n")
            print(f"O valor a pagar é R$%.2f\n" % NovoPreco)
            print(f"Valor do desconto: R$%.2f\n" % Desconto)
            print("Tipo de carne: ALCATRA.\n")
            print(f"Quantidade de alcatra(em kg): %d" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")


        elif(NovaEscolha == 0):
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 0%\n")
            print(f"O valor a pagar é R$%.2f\n" % preco)
            print(f"Valor do desconto é de R$0,00\n")
            print("Tipo de carne: ALCATRA.\n")
            print(f"Quantidade de alcatra(em kg): %d" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")
        else:
            print("Dado inválido, tente novamente!\n")
            exit(1)

    else:
        preco = 6.80 * qtdefile
        print("Possui cartão de desconto promocional:\n")
        print("1 --> SIM\n")
        print("0 --> NÃO\n")
        NovaEscolha = int(input())
        if(NovaEscolha == 1):
            Desconto = preco * 0.05
            NovoPreco = preco - Desconto
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 5%\n")
            print(f"O valor a pagar é R$%.2f\n" % NovoPreco)
            print(f"Valor do desconto: R$%.2f\n" % Desconto)
            print("Tipo de carne: ALCATRA.\n")
            print(f"Quantidade de alcatra(em kg): %d" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")
           

        elif(NovaEscolha == 0):
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 0%\n")
            print(f"O valor a pagar é R$%.2f\n" % preco)
            print(f"Valor do desconto é de R$0,00\n")
            print("Tipo de carne: ALCATRA.\n")
            print(f"Quantidade de alcatra(em kg): %d" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")
        else:
            print("Dado inválido, tente novamente!\n")
            exit(1)


elif(escolha == 3):
    print("Ok, digite a quantidade(em kg) de picanha, que pretende levar:\n")
    qtdefile = int(input())
    if(qtdefile <= 5):
        preco = 6.90 * qtdefile
        print("Possui cartão de desconto promocional:\n")
        print("1 --> SIM\n")
        print("0 --> NÃO\n")
        NovaEscolha = int(input())
        if(NovaEscolha == 1):
            Desconto = preco * 0.05
            NovoPreco = preco - Desconto
            
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 5%\n")
            print(f"O valor a pagar é R$%.2f\n" % NovoPreco)
            print(f"Valor do desconto: R$%.2f\n" % Desconto)
            print("Tipo de carne: PICANHA.\n")
            print(f"Quantidade de picanha(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")

        elif(NovaEscolha == 0):
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 0%\n")
            print(f"O valor a pagar é R$%.2f\n" % preco)
            print(f"Valor do desconto é de R$0,00\n")
            print("Tipo de carne: PICANHA.\n")
            print(f"Quantidade de picanha(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")
        else:
            print("Dado inválido, tente novamente!\n")
            exit(1)

    else:
        preco = 7.80 * qtdefile
        print("Possui cartão de desconto promocional:\n")
        print("1 --> SIM\n")
        print("0 --> NÃO\n")
        NovaEscolha = int(input())
        if(NovaEscolha == 1):
            Desconto = preco * 0.05
            NovoPreco = preco - Desconto
            
            
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 5%\n")
            print(f"O valor a pagar é R$%.2f\n" % NovoPreco)
            print(f"Valor do desconto: R$%.2f\n" % Desconto)
            print("Tipo de carne: PICANHA.\n")
            print(f"Quantidade de picanha(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")

        elif(NovaEscolha == 0):
            print("CUPOM FISCAL GERADO:\n")
            print("Desconto: 0%\n")
            print(f"O valor a pagar é R$%.2f\n" % preco)
            print(f"Valor do desconto é de R$0,00\n")
            print("Tipo de carne: PICANHA.\n")
            print(f"Quantidade de picanha(em kg): %d\n" % qtdefile)
            print("Forma de pagamento: Cartão de débito.\n")
        else:
            print("Dado inválido, tente novamente!\n")
            exit(1)
else:
    print("Dado inválido, tente novamente!\n")
    exit(1)