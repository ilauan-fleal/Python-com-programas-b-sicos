#PERGUNTAS INVESTIGATIVAS!

print("ATENÇÃO ÀS PERGUNTAS ABAIXO!\n")

print("1--> SIM\n")
print("0--> NÃO\n")



x = int(input("Telefonou para a vítima?\n"))
if(x != 1 and x != 0):
    print("Valor inválido!\n")
    exit(1)
y = int(input("Esteve no local do crime?\n"))
if(y != 1 and y != 0):
    print("Valor inválido!\n")
    exit(1)
z  = int(input("Mora perto da vítima?\n"))
if(z != 1 and z != 0):
    print("Valor inválido!\n")
    exit(1)
w = int(input("Devia para a vítima?\n"))
if(w != 1 and w != 0):
    print("Valor inválido!\n")
    exit(1)
k = int(input("Já trabalhou para a vítima?\n"))
if(k != 1 and k != 0):
    print("Valor inválido!\n")
    exit(1)

if(x == 1 and y == 1 and z == 1 and w == 1 and k == 1):

    print("Assassino!\n")

elif(x == 1 and y == 1 and z == 1):
    print("Cúmplice!\n")

elif(x == 1 and w == 1 and k == 1):
    print("Cúmplice!\n")

elif(y == 1 and z == 1 and w == 1):
    print("Cúmplice!\n")

elif(y == 1 and k == 1 and x == 1):
    print("Cúmplice!\n")
elif(z == 1 and w == 1 and k == 1):
    print("Cúmplice!\n")
elif(y == 1 and z == 1 and k == 1):
    print("Cúmplice!\n")
elif(w == 1 and y == 1 and x == 1):
    print("Cúmplice!\n")
elif(y == 1 and w == 1 and k == 1):
    print("Cúmplice!\n")
elif(z == 1 and k == 1 and y == 1):
    print("Cúmplice!\n")
elif(x == 1 and z == 1 and w == 1):
    print("Cúmplice!\n")

elif(x == 1 and y == 1):
    print("Suspeito!\n")

elif(x == 1 and z == 1):
    print("Suspeito!\n")

elif(x == 1 and w == 1):
    print("Suspeito!\n")

elif(x == 1 and k == 1):
    print("Suspeito!\n")    

elif(x == 1):
    print("Inocente!\n")
elif(y == 1):
    print("Inocente!\n")

elif(z == 1):
    print("Inocente!\n")

elif(w == 1):
    print("Inocente!\n")

elif(k == 1):
    print("Inocente!\n")
else:
    print("Cúmplice!\n")


