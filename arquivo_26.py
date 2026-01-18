#OS ANOS BISSEXTOS SÃO AQUELES MÚLTIPLOS DE 4 MAS QUE NÃO SÃO MÚLTIPLOS DE 100

ano = int(input("Insira um ano válido!\n"))

if(ano % 4 == 0 and ano % 100 != 0):
    print(f"O ano %d inserido é bissexto!\n" % ano)
else:
    print(f"O ano %d inserido não é bissexto!\n" % ano)

