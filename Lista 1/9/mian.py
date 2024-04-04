import random
# Crie um algoritmo que apure os votos de uma eleição  municipal, numa cidade com 
# 20.000 eleitores, onde concorreram quatro candidatos. Um servidor da Justiça 
# Eleitoral digitará cada voto individualmente.  Cada voto equivale a um número inteiro. 
# Os votos válidos podem ser 1, 2, 3 e 4, e estão relacionados aos seguintes candidatos:  1 – João da Silva  2 – José Ramalho  3 – Maria Mattos  4 – Pedro Américo
avalibleChoices = ["1", "2", "3" , "4","0"]
voteCount = []
for i in range(2000):
    # voto = int(input("Digite o valor do voto"))
    voto = random.randint(0,4)
    if((str(voto) not in avalibleChoices)):
        print("Valor de voto inserido não é válido, digite novamente")
        continue;
    voteCount.append(voto)

print("Quantidade de votos 1 - João da silva " +str(voteCount.count(1)))
print("Quantidade de votos 2 – José Ramalho "+str(voteCount.count(2)))
print("Quantidade de votos 3 – Maria Mattos "+str(voteCount.count(3)))
print("Quantidade de votos 4 – Pedro Américo "+str(voteCount.count(4)))
print("Quantidade de votos 0 - NULO " +str(voteCount.count(0)))