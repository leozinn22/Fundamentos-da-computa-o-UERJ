numero = int(input("Digite o numero"))
somaNumeros = 0
for i in range(1,numero):
        if(numero%i==0):
            somaNumeros+=i 
if(somaNumeros ==numero):
    print("é um numero perfeito")
else:
    print("não é um numero perfeito")
     
