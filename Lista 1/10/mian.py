# 10. Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber 
# se  os  consumidores  estavam  satisfeitos,  para  isso  eles  deveriam  responder  sim  ‘S’  ou 
# não  ‘N’.  Crie  um  algoritmo  que  leia  a  resposta  de  todas  as  pessoas  e  escreva  a 
# porcentagem dos que disseram sim e dos que disseram não. Obs: O final da leitura de dados é marcado pela resposta ‘F’.
import random
votos = {"S":0,"N":0}
total = 0
def porcentagem(total,valor):
    if total != 0:
        return (valor/total)*100
    else:
        return 0 
for i in range(10):
    # resposta = str(input("Escreva a resposta do usuário: "))
    # if(resposta.upper() == 'F'):
    #     break;
    resposta = random.choice(["S","N"])
    votos[resposta]+=1
total = sum(votos.values())
for chave,valor in votos.items():
    print("O total dos votos: "+ str(chave) + " " + str(porcentagem(total,valor)))