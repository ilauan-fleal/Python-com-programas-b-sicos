
salario = float(input("Informe sua remuneração mensal:\n"))


if(salario <= 280):
    
    aumento = salario * 0.20
    NovoSalario = salario * 1.20
    print(f"O salário antigo era de R$%.2f\n" % (salario))
    print(f"O percentual de aumento concedido é de 20%.\n")
    print(f"O valor do aumento concedido é de R$%.2f\n" % (aumento))
    print(f"O novo salário é de R$%.2f\n" % (NovoSalario))


elif(salario > 280 and salario <= 700):

    aumento = salario * 0.15
    NovoSalario = salario * 1.15
    print(f"O salário antigo era de R$%.2f\n" % (salario))
    print(f"O percentual de aumento concedido é de 15%.\n")
    print(f"O valor do aumento concedido é de R$%.2f\n" % (aumento))
    print(f"O novo salário é de R$%.2f\n" % (NovoSalario))   


elif(salario > 700 and salario <= 1500):
    aumento = salario * 0.10
    NovoSalario = salario * 1.10
    print(f"O salário antigo era de R$%.2f\n" % (salario))
    print(f"O percentual de aumento concedido é de 10%.\n")
    print(f"O valor do aumento concedido é de R$%.2f\n" % (aumento))
    print(f"O novo salário é de R$%.2f\n" % (NovoSalario))   

else:
    
    aumento = salario * 0.05
    NovoSalario = salario * 1.05
    print(f"O salário antigo era de R$%.2f\n" % (salario))
    print(f"O percentual de aumento concedido é de 5%.\n")
    print(f"O valor do aumento concedido é de R$%.2f\n" % (aumento))
    print(f"O novo salário é de R$%.2f\n" % (NovoSalario))   
