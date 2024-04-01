import random
#adicionando 10 dados ao array
somaSalarioH = 0
somaSalarioF = 0
quantidadeH = 0
quantidadeM=0
maiorSalarioMenor30 = 0
for i in range(10):
    idade = int(random.randint(18,65))
    sexo = str(random.choice(["H","M"]))
    salario = float(random.uniform(1400,1000))

    if sexo == "H":
        somaSalarioH += salario
        quantidadeH += 1
    elif sexo == "M":
        somaSalarioH += salario
        quantidadeM += 1
    if idade < 30 and salario > maiorSalarioMenor30: maiorSalarioMenor30 = salario 
if quantidadeH <= 0:
    print(str("A quantidade de homens é 0, não é possível calcular a média com esse valor!"))
else:
    mediaSalarioH = somaSalarioH/quantidadeH
    print(f"Média salarial dos homens {mediaSalarioH:.2f}") 

if quantidadeM <= 0:
    print("A quantidade de mulheres é 0, não é possível calcular a média com esse valor!")
else:
    mediaSalarioM = somaSalarioH/quantidadeM
    print(f"Média salarial das mulheres {mediaSalarioM:.2f} ")
print(f"maior salario encontrado entre as pessoas abaxio de 30 anos {maiorSalarioMenor30:.2f}" )