numero = int(input("Digite a quantidade de numeros"))
primos = []
index = 1
while len(primos)< numero:
    primo = True
    index+=1
    for i in range(2,index):
        if(index%i==0):
            primo = False
            break 
        else:
            primo= True
    if(primo):
        primos.append(index)
print(primos)