#CALCULADORA DE EQUAÇÕES DO SEGUNDO GRAU!
from math import sqrt


a = int(input("Digite o valor do coeficiente A(diferente de zero):\n"))

if(a == 0):
    print("Coeficiente A não pode ser igual a zero!\n")
    exit(1)

b = int(input("Digite o valor do coeficiente B:\n"))


c = int(input("Digite o valor do coeficiente C:\n"))


delta = b**2 - 4*a*c

if(delta == 0):
    print("A equação possui duas raízes reais idênticas:\n")
    x1 = x2 = (-b + sqrt(delta))/2*a
    print(f"As raízes x1 e x2 são iguais a: %d\n" % x1)
elif(delta > 0):
    print("A equação possui duas raízes reais distintas:\n")
    x1 = (-b + sqrt(delta))/2*a
    x2 = (-b - sqrt(delta))/2*a
    print(f"O valor da primeira raíz x1 é igual a : %d\n" % x1)
    print(f"O valor da segunda raíz é x2 é igual a : %d\n" % x2)
else:
    print("O valor de delta é negativo, logo a equação não possui raízes reais!\n")
    exit(1)



