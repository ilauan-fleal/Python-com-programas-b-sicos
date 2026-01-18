#TRABALHANDO COM NÚMEROS BINÁRIOS, OCTAIS E HEXADECIMAIS


resultado = 0b101 + 0b101010

#RESULTADO OBTIDO EM BINÁRIO

print(f'resultado: %s' % bin(resultado))


NovaOperacao = 0xABC12 + 0xCF1

#RESULTADO EM HEXADECIMAL

print(f'resultado: %s' % hex(NovaOperacao))


OutraOperacao = 0o267 + 0o277

#RESULTADO EM OCTAL

print(f'resultado: %s' % oct(OutraOperacao))

x = int(input("Insira a sua idade em decimal:\n"))

print(f'Sua idade em binário é: %s ' % bin(x))

print(f'Sua idade em octal é: %s' % oct(x))

print(f'Sua idade em hexadecimal é : %s' % hex(x))

