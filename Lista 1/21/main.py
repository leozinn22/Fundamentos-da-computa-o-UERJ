perfeitos = []
index = 0
while len(perfeitos) < 4:
    index +=1
    somaNumero = 0
    for i in range(1,index):
        if(index%i==0):
            somaNumero+=i
    if(somaNumero==index):
        perfeitos.append(index)    
print(str(perfeitos))