numero = int(input("Digite o numero "))
primo = True
for i in range(2,numero):
    if(numero%i==0):
        primo = False
        break
    else:
        primo= True
if(primo):
    print("É primo")
else:
    print("Não é primo")
