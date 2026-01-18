#ALTERANDO UM POUCO O SCRIPT!


contagem = 1

m = float(input("Insira o valor do montante pretendido na poupança:\n"))

t = int(input("Insira o tempo de aplicação em meses:\n"))

i = float(input("Insira o valor da taxa de juros:\n"))

i = i/100



def CalculaJuros(m, t, i):
    v = m/((1 + i)**t)
    j = m - v
    print(f"O valor da aplicação inicial, nesse caso, deve ser de R$%.2f \n" % v)
    print(f"Os juros recebidos no período em questão são iguais a R$%.2f" % j)

CalculaJuros(m, t, i)





