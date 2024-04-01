homem = 'M'
mulher = 'F'
mediaF = 0 
mediaM = 0
somaF = 0
somaM = 0
MS = 0
nF = 0 
nM = 0 
continua = 'S'
while continua == 'S': 
    sexo = input('Informe o sexo(M/F): ')
    a = sexo.upper()

    while ((a != homem) and (a != mulher)):
        a = input('Informação inválida! Insira M ou F: ')
        a = a.upper()

    idade = int(input('Insira a respectiva idade: '))
    while idade < 18 or idade > 65:
        idade = int(input('Idade inválida! Digite novamente: '))
    salario = float(input('Insira o salário recebido: R$'))
    while salario <= 0: 
        salario = int(input('Salário inválido! Insira um salário válido: R$'))
   
    if a == mulher:
        nF += 1
        somaF += salario
    elif a == homem: 
        nM += 1
        somaM += salario
    if(idade <= 30 and salario >MS):
        MS=salario
    b = input('Deseja inserir mais informações? Digite "S" para sim e "N" para não. Caso deseje parar, a média salarial será calculada e faremos uma análise salarial entre as pessoas abaixo de 30 anos: ')
    continua = b.upper()
if nF > 0:
    mediaF = (mediaF+somaF)/nF
if nM > 0:
    mediaM = (somaM+mediaM)/nM
if nF == 0: 
    mediaF = 0 
if nM == 0:
    mediaM = 0
print('A média salarial dos homens e das mulheres é, respectivamente, R${:.2f} e R${:.2f}.'.format(mediaM, mediaF))
print('O maior salário encontrado entre as pessoas abaixo de 30 anos foi R${:.2f}.'.format(MS))