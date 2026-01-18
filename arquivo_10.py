import math


x = math.pi

r = float(input("Informe o raio do círculo:\n"))

def ProcessaDados(x,r):
    p = 2*x*r
    a = x*r**2
    print(f'O perímetro do círculo é de %.2f\n' % p)
    print(f'A área do círculo é de %.2f\n' % a)



ProcessaDados(x,r)
