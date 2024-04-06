# 7. Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma 
# de  todos  os  números  compreendidos  entre  eles.  Os  valores  A  e  B  não  devem  ser 
# considerados  no  somatório.  Caso  A seja maior do  que  B  deve  ser  enviada  uma 
# mensagem para o usuário informando que a soma não será realizada.
numeroA = int(input("Valor número A "))
numeroB = int(input("Valor número B "))
if(numeroA<numeroB):
    print("A conta não será realizada")
    exit()
intervaloNumero = range(numeroA,numeroB)
print(intervaloNumero)
somaDosValores = sum(intervaloNumero)
print("Soma dos valores entre A e B " + str(somaDosValores))