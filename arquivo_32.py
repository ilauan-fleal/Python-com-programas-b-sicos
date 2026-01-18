
x = float(input("Insira um valor:\n"))

y = float(input("Insira outro valor:\n"))

print("Operações aritméticas disponíveis:\n")
print("1 --> Soma.\n")
print("2 --> Subtração.\n")
print("3 --> Multiplicação.\n")
print("4 --> Divisão.\n")
print("5 --> Exponenciação.\n")
print("ESCOLHA UMA DAS OPÇÕES:\n")
op = int(input())
if(op == 1):
    result = x + y
    print(f'O resultado da soma é igual a %.2f\n' % result)
    if(result % 2 == 0):
    
        print("O resultado é par!\n")
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n")  
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
    else:

        print("O resultado é ímpar!\n")
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n") 
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
elif(op == 2):
    result = x - y
    if(result % 2 == 0):
        print(f'O resultado da subtração é igual a %.2f\n' % result)
        print("O resultado é par!\n")
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")

    else:
        print(f'O resultado da subtração é igual a %.2f\n' % result)
        print("O resultado é ímpar!\n")   
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
elif(op == 3):
    result = x * y
    if(result % 2 == 0):
        print(f'O resultado da multiplicação é igual a %.2f\n' % result)
        print("O resultado é par!\n")
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
    else:
        print(f'O resultado da multiplicação é igual a %.2f\n' % result)
        print("O resultado é ímpar!\n") 
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n")  
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
elif(op == 4):
    result = x/y
    if(result % 2 == 0):
        print(f'O resultado da divisão é igual a %.2f\n' % result)
        print("O resultado é par!\n")
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n") 
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
    else:
        print(f'O resultado da divisão é igual a %.2f\n' % result)
        print("O resultado é ímpar!\n")
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n") 
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")  

elif(op == 5):
    result = x ** y
    if(result % 2 == 0):
        print(f'O resultado da exponenciação do primeiro elevado ao segundo é igual a %.2f\n' % result)
        print("O resultado é par!\n")
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n") 
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
    else:
        print(f'O resultado da exponenciação é igual a %.2f\n' % result)
        print("O resultado é ímpar!\n")  
        if(result >= 0):
            print("O resultado é positivo!\n")
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")
        else:
            print("O resultado é negativo!\n") 
            if(result == round(result)):
                print("O resultado é um inteiro!\n")
            else:
                print("O resultado é um decimal!\n")

else:
    print("Opção inválida!\n")
    exit(1)

