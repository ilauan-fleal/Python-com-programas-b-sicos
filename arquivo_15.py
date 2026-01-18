

x = float(input("Insira uma nota:\n"))

if(x < 0 or x > 10):
    print("Insira uma nota no intervalo de 1 até 10\n")
    exit(1)

y = float(input("Insira sua outra nota:\n"))

if(y < 0 or y > 10):
    print("Insira uma nota no intervalo de 1 até 10!\n")
    exit(1)
media = (x + y)/2

if(media == 10):
    print("Você foi aprovado com distinção.\n")
    print(f"Sua média foi igual a: %.2f" % media)

elif(media > 6):
    print(f"Você foi aprovado!\n")
    print(f"Sua média foi igual a: %.2f" % media)
else:
    print(f"Sua média foi de %.2f" % media)
    print("Você foi reprovado!\n")    


