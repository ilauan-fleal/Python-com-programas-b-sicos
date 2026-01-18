

dia = int(input("Digite um dia do mês:\n"))

if(dia > 31):
    print("Valor inválido o dia de um mês não tem mais do que 31 dias\n")
    exit(1)


elif(dia == 31):
        print("Se o dia escolhido for o dia 31  , então no caso as possibilidades para os meses são:\n")
        print("1 --> Janeiro.\n")
        print("3 --> Março.\n")
        print("5 --> Maio.\n")
        print("7 --> julho.\n")
        print("9 --> Setembro.\n")
        print("11 --> Novembro.\n")
        print("Escolha um valor para o mês correspondente:\n")
        mes = int(input())
        if(mes % 2 == 0):
            print("Mês inválido, perante o dia escolhido!\n")
            exit(1)
        else:

            ano = int(input("Escolha o ano:\n"))
            if(ano % 4 == 0 and ano % 100 != 0):
                print("Trata-se de um ano bissexto:\n")
                print(f"A data inserida é: %d/%d/%d\n" % (dia, mes, ano))
            else:

                print(f"A data inserida é: %d/%d/%d\n" % (dia, mes, ano))
else:

    mes = int(input("Escolha o mês:\n"))
    if(dia > 29 and mes == 2):
        print("Erro fevereiro tem apenas 28 ou 29 dias!\n")
        exit(1)
    elif(mes > 12 or mes == 0):
        print("Valor inválido!\n")
        exit(1)
    else:

        ano = int(input("Escolha o ano:\n"))
        if(dia == 29 and mes == 2 and ano % 4 == 0 and ano % 100 != 0):
            print("Erro, nos anos bissextos, fevereiro tem apenas 28 dias!\n")
            exit(1)
        else:

            print(f"A data inserida é: %d/%d/%d\n" % (dia, mes, ano))


    

