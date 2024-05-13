import random
respostas = []
sexos = []
homensNao=0
while len(respostas)< 2000:
    escolha = random.choice(["SIM","NAO"])
    sexo = random.choice(["H","M"])
    respostas.append(escolha)
    sexos.append(sexo)
    if(sexo=="H" and escolha=="NAO"):
        homensNao+=1

print("Número de pessoas que responderam sim:"+ str(respostas.count("SIM")))
print("Número de pessoas que responderam não:"+ str(respostas.count("NAO")))
print(homensNao)
print("porcentagem de homens que responderam não:"+ str(homensNao/respostas.count("NAO")))

