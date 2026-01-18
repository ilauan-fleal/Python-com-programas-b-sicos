contagem = 1

v = float(input("Insira o valor inicial investido na poupança:\n"))

t = int(input("Insira o tempo de aplicação em meses:\n"))

i = float(input("Insira o valor da taxa de juros:\n"))

i = i/100

print("Insira os valores de depósito adicionais que houveram durante o período em questão:\n")
while contagem < t:
    print(f"Insira o valor adicional %d:\n" % contagem)
    a = float(input())
    contagem += 1
    v += a

def CalculaJuros(v, t, i):
    m = v*(i + 1)**t
    j = m - v
    print(f"O valor total do montante é de R$%.2f \n" % m)
    print(f"Os juros recebidos no período em questão são iguais a R$%.2f" % j)

CalculaJuros(v, t, i)




