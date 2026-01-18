#CALCULANDO MÉDIA DAS NOTAS:

m = float(input("Digite a nota de matemática:\n"))

p = float(input("Digite a nota de português:\n"))

i = float(input("Digite a nota de inglês:\n"))

def CalculaMedia(m,  p , i):
    media = (m + p + i)/3
    print(f"A média das três notas é de: %.2f\n" % media)

CalculaMedia(m, p , i)