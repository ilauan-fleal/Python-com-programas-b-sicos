
number = float(input("Insira um valor:\n"))

if(number == round((number))):
    print("É um inteiro!\n")
else:
    print("É um decimal!\n")
    print(f"Arredondando o valor para maior: %d\n" % round(number + 0.5))
    print(f"Arredondando o valor para menor: %d\n" % round(number - 0.5))
