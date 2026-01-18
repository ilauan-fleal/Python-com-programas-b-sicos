

n1 = float(input("Informe a primeira nota:\n"))

n2 = float(input("Informe a segunda nota:\n"))

media = (n1 + n2)/2

if(media >= 9 and media <= 10):
    grau = 'A'
    print(f"Nota 1: %.2f\n" % n1)
    print(f"Nota 2: %.2f\n" % n2)
    print(f"Média: %.2f\n" % media)
    print(f"grau: %s\n" % grau)
    print("Aprovado!\n")
elif(media >= 7.5 and media <= 9):
    grau = 'B'
    print(f"Nota 1: %.2f\n" % n1)
    print(f"Nota 2: %.2f\n" % n2)
    print(f"Média: %.2f\n" % media)
    print(f"grau: %s\n" % grau)
    print("Aprovado!\n")
elif(media >= 6 and media <= 7.5):
    grau = 'C'
    print(f"Nota 1: %.2f\n" % n1)
    print(f"Nota 2: %.2f\n" % n2)
    print(f"Média: %.2f\n" % media)
    print(f"grau: %s\n" % grau)
    print("Aprovado!\n")
elif(media >= 4 and media <= 6):
    grau = 'D'
    print(f"Nota 1: %.2f\n" % n1)
    print(f"Nota 2: %.2f\n" % n2)
    print(f"Média: %.2f\n" % media)
    print(f"grau: %s\n" % grau)
    print(f"Reprovado.\n")
elif(media >= 4 and media <= 0):
    grau = 'E'
    print(f"Nota 1: %.2f\n" % n1)
    print(f"Nota 2: %.2f\n" % n2)
    print(f"Média: %.2f\n" % media)
    print(f"grau: %s\n" % grau)
    print("Reprovado.\n")

