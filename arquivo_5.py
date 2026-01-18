#TRABALHANDO COM PORCENTAGEM EM PYTHON!

f = float(input("Insira o preço inicial de um produto:\n"))

def ProcessaDados(f):
    desconto = f * 0.2
    precoNovo = f - desconto
    print(f"O preço original do produto: R$ %.2f" % f)
    print(f"O valor do desconto: R$ %.2f " % desconto)
    print(f"O preço novo do produto: R$ %.2f" % precoNovo)


ProcessaDados(f)