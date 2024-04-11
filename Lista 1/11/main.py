# 11. Crie um algoritmo que calcule a soma dos N primeiros números inteiros ímpares e 
# positivos. O valor de N deve ser lido do usuário. 
n = int(input("Digite o numero de termos "))
soma = []
for i in range(n+1):
    if(i%2!=0):{
        soma.append(i)
    }
print("Soma dos n termos: "+ str(sum(soma))) 