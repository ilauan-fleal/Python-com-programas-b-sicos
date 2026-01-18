x = int(input("Insira um valor inteiro, menor do que 1000.\n"))


if(x >= 100 and x < 1000):
    
    u = x % 10
    x = (x - u)/10
    d = x % 10
    x = (x - d)/10
    c = x
    d = int(d)
    c = int(c)


else:
    print("Valor fora do intervalo!\n")
    exit(1)
    
print(f"O valor da centena do número inserido é de: %d\n" % c)
print(f"O valor da dezena do número inserido é de: %d\n" % d)
print(f"O valor da unidade do número inserido é de: %d\n" % u)








