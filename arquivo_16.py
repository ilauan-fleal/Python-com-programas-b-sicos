

x = int(input("Digite um valor:\n"))

y = int(input("Digite outro valor:\n"))

if(x == y):
    print("Valores repetidos, não serão aceitos!\n")
    exit(1)

z = int(input("Agora digite um terceiro e último valor:\n"))

if(x == z or y == z):
    print("Valores repetidos não serão aceitos!\n")
    exit(1)



def DefineMaior(x, y, z):
    if(x > y and x > z):
        maior = x
    elif(y > x and y > z):
        maior = y
    elif(z > x and z > y):
        maior = z
    return maior


def DefineMenor(x, y, z):
    if(x < y and x < z):
        menor = x
    elif(y < x and y < z):
        menor = y
    elif(z < x and z < y):
        menor = z
    return menor


print(f"O maior valor é igual a: %d\n" % DefineMaior(x,y,z))

print(f"O menor valor é igual a: %d\n" % DefineMenor(x,y,z))

