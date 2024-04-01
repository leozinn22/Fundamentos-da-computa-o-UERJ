import random
import functools
pares=[]
impares=[]
while True:
    numero =random.randrange(0,1000)
    if numero == 0:
        break;
    if numero %2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)

print(str("Quantidade de pares "+ str(pares.__len__())))
print(str("Quantidade de impares "+ str(impares.__len__())))
print(f"Média de pares  {((functools.reduce(lambda a,b: a+b,pares)/pares.__len__())):.2f}")
