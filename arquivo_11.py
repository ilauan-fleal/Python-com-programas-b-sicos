
c = float(input("Digite a temperatura em grau Celsius:\n"))

def ConversorDeTemperatura(c):
    f = 9/5*c + 32
    print(f'O valor da temperatura em Fahrenheit é de %.2f' % f)

ConversorDeTemperatura(c)