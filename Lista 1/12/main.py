# 12. Crie um  algoritmo  que calcule a soma  dos  primeiros  50  números  pares.  Os 
# primeiros números pares são: 2, 4, 6, ...
# n = int(input("Digite o numero de termos "))
soma = []
cont = 0
while len(soma) <51:
    if(cont%2==0):{
        soma.append(cont)
    }
    cont+=1
print("Soma dos n termos: "+ str(sum(soma))) 