

dia = int(input("Diga qual dia da semana(de 1 até 7), está querendo procurar:\n"))


if(dia == 1):
    print("Segunda-feira!\n")
elif(dia == 2):
    print("Terça-feira!\n")
elif(dia == 3):
    print("Quarta-feira!\n")
elif(dia == 4):
    print("Quinta-feira!\n")
elif(dia == 5):
    print("Sexta-feira!\n")
elif(dia == 6):
    print("Sábado!\n")
elif(dia == 7):
    print("Domingo!\n")
else:
    print("A semana tem de 1 até 7, dias, valor inválido!\n")
    exit(1)