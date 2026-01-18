print("M=matutino; V=vespertino; N=noturno!\n")
turno = input("Escolha seu turno de estudo:\n")


if(turno.upper() == 'M'):
    print("Bom dia!\n")
elif(turno.upper() == 'V'):
    print("Boa tarde!\n")
elif(turno.upper() == 'N'):
    print("Boa noite!\n")

else:
    print("Valor inválido!\n")
    print("Atenção às opções!\n")
    exit(1)