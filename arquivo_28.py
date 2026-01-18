
x = int(input("Digite um valor:\n"))

def DeterminaParOuImpar(x):
    if(x % 2 == 0):
        print(f"O valor %d é par.\n" % x)
    else:
        print(f"O valor %d é ímpar.\n" % x)

DeterminaParOuImpar(x)

