

combustivel = input("Escolha o tipo de combustível:\n")

if(combustivel.upper() ==  "GASOLINA"):
    print("Preço por litro: R$2,50.\n")
    g = float(input("Insira o quanto de gasolina irá utilizar(em litros)?\n"))
    preco = g * 2.50
    if(g > 20):
        desconto = preco * 0.06
        NovoPreco = preco - desconto
        print("Como a quantia solicitada é maior que 20 litros, há um desconto de 6% para a gasolina.\n")
        print(f"O valor total a pagar, no caso , será de R$%.2f\n" % NovoPreco)
    else:
        desconto = preco * 0.04
        NovoPreco = preco - desconto
        print("Como a quantia solicitada é menor ou igual a 20 litros, há um desconto de 4% para a gasolina.\n")
        print(f"O valor total a pagar, no caso , será de R$%.2f\n" % NovoPreco)
    
    
elif(combustivel.upper() == "ÁLCOOL" or combustivel.upper() == "ALCOOL"):
    print("Preço por litro: R$1,90.\n")
    al = float(input("Insira quantos litros de álcool irá utilizar(em litros)?\n"))
    preco = al * 1.90
    if(al > 20):
        desconto = preco * 0.05
        NovoPreco = preco - desconto
        print("Como a quantia solicitada é maior que 20 litros, há um desconto de 5% para o álcool.\n")
        print(f"O valor total a pagar, no caso , será de R$%.2f\n" % NovoPreco)
    else:
        desconto = preco * 0.03
        NovoPreco = preco - desconto
        print("Como a quantia solicitada é menor ou igual a  20 litros, há um desconto de 3% para o álcool.\n")
        print(f"O valor total a pagar, no caso , será de R$%.2f\n" % NovoPreco)
        
else:
    print("Dado inválido, tente novamente!\n")
    exit(1)



