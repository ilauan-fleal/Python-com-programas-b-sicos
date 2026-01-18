f = float(input("Digite a temperatura em grau Fahrenheit:\n"))

def ConversorDeTemperatura(c):
    c = 5*(f - 32)/9
    print(f'O valor da temperatura em Celcius é de %.2f' % c)

ConversorDeTemperatura(f)