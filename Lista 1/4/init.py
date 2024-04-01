# guardar nome, preço, 
# atribuir um id (opcional)
comandoDeParada = "xxx"
mensagemParada = "Para parar de inserir produtos, assuma xxx como nome do produto!"
#array de dicts(objetos)
armazenamentoProdutos = {}
maiorPreco= 0
while True:
    print(mensagemParada)
    nome = str(input("Digite o nome do produto "))
    if(nome == comandoDeParada.casefold()):
        break;
    preco = float(input("Digite o preço do produto "))
   
    armazenamentoProdutos[nome]= preco
#encontrando o maior preço
maiorPreco = max(armazenamentoProdutos,key=armazenamentoProdutos.get)
print("O produto com maior preço é o produto " + maiorPreco)