import random
sumPBox = 0
countBox = 0
mensagemParada = "Para parar de inserir produtos, assuma xxx peso da caixa"
comandoDeParada = "xxx"
while countBox < 25:
    print(mensagemParada)
    # preco = float(input("Digite o peso do produto em KG "))
    preco = random.randint(0,1000)
    if(preco == comandoDeParada.casefold()):
        break;
    countBox+=1
    sumPBox+= preco
print("O peso total que o caminhão vai carregar é " + str(sumPBox) + " KG")
