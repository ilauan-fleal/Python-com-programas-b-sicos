

x = int(input("Digite um primeiro valor:\n"))

y = int(input("Digite um segundo valor:\n"))


if(x == y):
    print("Valores repetidos, não serão aceitos!\n")
    exit(1)

z = int(input("Digite um terceiro valor:\n"))

if(x == z or y == z):
    print("Valores repetidos não serão aceitos!\n")
    exit(1)

def ComparaDados(x, y, z):
    if(x > y and x > z):
        primeiroMaior = x
        if(y > z):
            segundoMaior = y
            terceiroMaior = z
        elif(z > y):
            segundoMaior = z
            terceiroMaior = y

    elif(y > x and y > z):
        primeiroMaior = y
        if(x > z):
            segundoMaior = x
            terceiroMaior = z
        elif(z > x):
            segundoMaior = z
            terceiroMaior = x

    elif(z > x and z > y):
        primeiroMaior = z
        if(x > y):
            segundoMaior = x
            terceiroMaior = y
        elif(y > x):
            segundoMaior = y
            terceiroMaior = x
    print(f"Os números exibidos em ordem decrescente são: %d-%d-%d\n" % (terceiroMaior, segundoMaior, primeiroMaior))

    


ComparaDados(x, y ,z)
