# 8. Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma 
# de  todos  os  números  múltiplos  de  4  compreendidos  entre  eles.  Os  valores  A  e  B  não 
# devem  ser  considerados  no  somatório.  Caso  A  seja  maior  do  que  B  deve  ser  enviada 
# uma mensagem para o usuário informando que a soma não será realizada. 

numeroA = int(input("Valor número A "))
numeroB = int(input("Valor número B "))
if(numeroA>numeroB):
    print("A conta não será realizada")
    exit()
somaDosProdutos =0
for n in range(numeroA,numeroB):
    if(n%4==0):
        somaDosProdutos+=n
# totalSomaProdutos = sum(somaDosProdutos)
print("produto dos valores entre A e B " + str(somaDosProdutos))
