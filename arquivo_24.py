
a = int(input("Insira o valor do primeiro lado do triângulo:\n"))

b = int(input("Insira o valor do segundo lado do triângulo:\n"))

c = int(input("Insira o valor do terceiro lado do triângulo:\n"))

if(a > b + c or b > a + c or c > a + b):
    print("Não pode ser um triângulo:\n")
    print("Um lado não pode ser maior do que a soma dos outros dois.\n")
    exit(1)

elif(a == b == c):
    print("É um triângulo equilátero de três lados iguais!\n")
    print(f"Lado A(primeiro lado):%d" % a)
    print(f"Lado B(segundo lado): %d" % b)
    print(f"Lado C(terceiro lado): %d" % c)

elif(a == b or b == c or c == a):
    print("É um triângulo isósceles com dois lados iguais!\n")
    print(f"Lado A(primeiro lado):%d" % a)
    print(f"Lado B(segundo lado): %d" % b)
    print(f"Lado C(terceiro lado): %d" % c)

else:
    print("É um triângulo escaleno com três lados diferentes!\n")
    print(f"Lado A(primeiro lado):%d" % a)
    print(f"Lado B(segundo lado): %d" % b)
    print(f"Lado C(terceiro lado): %d" % c)
