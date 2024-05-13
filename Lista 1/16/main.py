alturas = []
nome = input("Digite o nome")
primeiroA =0
segundoA=0
while nome != 'MARIA':
    altura = float(input("Digite a altura"))
    alturas.append(altura)
    if(altura > primeiroA and primeiroA > segundoA):
        segundoA = primeiroA
    if(altura > primeiroA):
        primeiroA = altura
    if(altura > segundoA and altura< primeiroA):
        altura = segundoA
print("Primeira altura mais repetida: "+ str(alturas.count(primeiroA)))
print("Segunda altura mais repetida: "+ str(alturas.count(segundoA)))
