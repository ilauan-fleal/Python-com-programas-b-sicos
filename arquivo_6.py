#TRABALHANDO COM NOVOS PROGRAMAS EM PYTHON PARA DESCONTO PERCENTUAL

f = float(input("Insira o preço do produto:\n"))

desconto = float(input("Insira o desconto percentual:\n"))



NewDescount = desconto/100

def ProcessaDados(f, NewDescount):
    NovoPreco = f - f*NewDescount
    print(f'O preço original do produto era de R$%.2f\n' % f)
    print(f'O novo preço do produto é de R$%.2f' % NovoPreco)

ProcessaDados(f, NewDescount)

