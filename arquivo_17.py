

#ESSE PROGRAMA DEVERÁ TROCAR O VALOR DE VARIÁVEIS!

x = int(input("Digite um valor para x:\n"))

y = int(input("Digite outro valor, para y:\n"))

def TrocaValor(x,y):
    
    z = x
    x = y
    y = z

    print(f"O novo valor de y é %d\n" % y)
    print(f"O novo valor de x é %d\n" % x)

TrocaValor(x,y)
