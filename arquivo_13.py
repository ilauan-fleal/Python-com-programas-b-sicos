#NOVO MODELO DE CARRO

#20 km === 1l de combustível


#1l de combustível ==== R$ 5,00

x = float(input("Olá, informe a quantidade de dinheiro disponível para pagar:\n"))


n = x/5

km = n * 20

print(f'Você pode comprar %.2f litros de combustível' % n)

print(f'O veículo poderá rodar %.2f km.\n' % km)

