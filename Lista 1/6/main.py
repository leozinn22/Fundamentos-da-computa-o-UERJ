#  Crie  um  algoritmo  que  leia  a  quantidade  e  o  preço  de  50  produtos  comprados  por 
# uma empresa. Ao final deve ser escrito o total gasto pela empresa.
import random 
produtos = {}
totalGasto = 0
for i in range(50):
    nome = i
    preco = random.uniform(1,1000)
    produtos[nome] = preco
#gasto total
totalGasto = sum(produtos.values())
print(str("O total gasto foi " + str(totalGasto)))