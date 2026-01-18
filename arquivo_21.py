#PROGRAMA PARA CÁLCULO DE FOLHA DE PAGAMENTO!

x = int(input("Diga o valor de sua hora de trabalho:\n"))

y = int(input("Informe o total de horas trabalhadas no mês:\n"))

salario = x * y

if(salario <= 900):
    print("Você está isento de imposto de renda!\n")
elif(salario > 900 and salario <= 1500):
    #5 % de desconto no IMPOSTO DE RENDA
    descontoIR = salario * 0.05
    descontoINSS = salario * 0.10
    descontoFGTS = salario * 0.11
    #O FGTS NÃO É DESCONTADO É A EMPRESA QUE DEPOSITA!
    totalDeDescontos = descontoIR + descontoINSS
    salarioLiquido = salario - totalDeDescontos
    print(f"Salário(%d*%d):R$%.2f\n" % (x ,y,salario))
    print(f"(-)IR(5%)" + ":" + f"R$%.2f\n" % descontoIR)
    print(f"(-)INSS(10%)" + ":" + f"R$%.2f\n" % descontoINSS)
    print(f"(-)FGTS(11%)" + ":" + f"R$%.2f\n" % descontoFGTS)
    print(f"Total de descontos:R$%.2f\n" % totalDeDescontos)
    print(f"Salário líquido:R$%.2f\n" % salarioLiquido)
elif(salario > 1500 and salario <= 2500):
    #10% de desconto no imposto de renda!
    descontoIR = salario * 0.10
    descontoINSS = salario * 0.10
    descontoFGTS = salario * 0.11
    #O FGTS NÃO É DESCONTADO É A EMPRESA QUE DEPOSITA!
    totalDeDescontos = descontoIR + descontoINSS
    salarioLiquido = salario - totalDeDescontos
    print(f"Salário(%d*%d):R$%.2f\n" % (x ,y,salario))
    print(f"(-)IR(10%)"   + ":" + f"R$%.2f\n" % descontoIR)
    print(f"(-)INSS(10%)" + ":" + f"R$%.2f\n" % descontoINSS)
    print(f"(-)FGTS(11%)" + ":" + f"R$%.2f\n" % descontoFGTS)
    print(f"Total de descontos:R$%.2f\n" % totalDeDescontos)
    print(f"Salário líquido:R$%.2f\n" % salarioLiquido)
else:
    #20% de desconto no imposto de renda!
    descontoIR = salario * 0.20
    descontoINSS = salario * 0.10
    descontoFGTS = salario * 0.11
    #O FGTS NÃO É DESCONTADO É A EMPRESA QUE DEPOSITA!
    totalDeDescontos = descontoIR + descontoINSS
    salarioLiquido = salario - totalDeDescontos
    print(f"Salário(%d*%d):R$%.2f\n" % (x ,y,salario))
    print(f"(-)IR(20%)"   + ":" + f"R$%.2f\n" % descontoIR)
    print(f"(-)INSS(10%)" + ":" + f"R$%.2f\n" % descontoINSS)
    print(f"(-)FGTS(11%)" + ":" + f"R$%.2f\n" % descontoFGTS)
    print(f"Total de descontos:R$%.2f\n" % totalDeDescontos)
    print(f"Salário líquido:R$%.2f\n" % salarioLiquido)
    
    

