from random import *
#  Num  frigorífico  existem  90  bois.  Cada  boi  traz  preso  em  seu  pescoço  um  cartão 
# contendo  seu  número  de  identificação  e  seu  peso.  Crie  um  algoritmo  que  escreva  o 
# número e peso do boi mais gordo e do boi mais magro. Além  disso,  responda:  se  houver  dois  ou  mais  bois  com  o  mesmo  peso,  maior  que 
# todos os demais, este algoritmo escreverá o número de qual deles?

bois = {}
#adicionando os namorados de gabi (gados) no dict
auxId = 0
auxPeso = 0

auxMenorId = 0
auxMenorPeso = 9999999999
for i in range(90):
    identifer = randint(0,1000)
    #em kg
    peso = uniform(30,1000) 
    while identifer in bois:
        identifer = randint(0,1000)    
    bois[identifer]= peso

for i in bois.keys():
    if(bois[i] > auxPeso):
        auxId = i
        auxPeso = bois[i]

for i in bois.keys():
    if(bois[i] < auxMenorPeso):
        auxMenorId = i
        auxMenorPeso = bois[i]


# Dicionário para armazenar a contagem de ocorrências de cada valor
contagem_valores = {}

# Primeiro, conte a ocorrência de cada valor
for chave, valor in bois.items():
    if valor in contagem_valores:
        contagem_valores[valor].append(chave)
    else:
        contagem_valores[valor] = [chave]

# Agora, encontre os valores que têm mais de uma ocorrência
valores_duplicados = {}
for valor, chaves in contagem_valores.items():
    if len(chaves) > 1:
        valores_duplicados[valor] = chaves

# Exiba os valores duplicados e as chaves correspondentes
if valores_duplicados:
    print("Valores duplicados e suas chaves correspondentes:")
    for valor, chaves in valores_duplicados.items():
        print(f"Valor {valor} ocorre nas chaves: {chaves}")
else:
    print("Não há valores duplicados no dicionário.")
print("Maior peso " + "ID:"+str(auxId)+" "+str(auxPeso))
print("menor peso " + "ID:"+str(auxMenorId)+" "+str(auxMenorPeso))
