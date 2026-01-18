#CRIANDO CALCULADORA

x = int(input("Digite um valor inteiro:\n"))
y = int(input("Agora, digite outro valor inteiro:\n"))

def Calculator(x, y):
    print(f'A soma de ambos é: %d\n' % (x + y))
    print(f'A subtração de ambos é: %d\n' % (x - y))
    print(f'O produto de ambos é: %d\n' % (x * y))
    if(x > y):
        print(f'A divisão de ambos é: %d\n' % (x / y))
    else:
        print(f'A divisão de ambos é: %d\n' % (y / x))
    print(f'A potência de um elevado ao outro é: %d\n' % (x ** y))
    print(f'O resto da divisão entre um é outro é: %d\n' % (x % y))


Calculator(x, y)

