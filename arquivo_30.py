#SIMULADOR DE UM SIMPLES CAIXA ELETRÔNICO!

valor = float(input("Digite um valor, para sacar(mín.: R$10,00 máx.: R$600,00):\n"))

if(valor < 200 or valor > 600):
    print("Valor fora do intervalo!\n")
    exit(1)
else:
    NotasDe100 = int(valor/100)
    valor = valor - (NotasDe100 * 100)
    NotasDe50 = int(valor/50)
    valor = valor - (NotasDe50 * 50)
    NotasDe10 = int(valor/10)
    valor = valor - (NotasDe10 * 10)
    NotasDe5 = int(valor/5)
    valor = valor - (NotasDe5 * 5)
    NotasDe1 = valor
    
    
    print(f"Total de notas de R$1,00 = %d\n"  % NotasDe1)
    print(f"Total de notas de R$5,00 = %d\n"  % NotasDe5)
    print(f"Total de notas de R$10,00 = %d\n" % NotasDe10)
    print(f"Total de notas de R$50,00 = %d\n" % NotasDe50)
    print(f"Total de notas de R$100,00 = %d\n" % NotasDe100)


