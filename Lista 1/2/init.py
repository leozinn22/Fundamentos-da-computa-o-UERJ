def calcularPa(primeiroTermo:int,razao:int,n:int):
    termos=[primeiroTermo + (i * razao) for i in range(n)]
    return termos
primeiroTermo = int(input("Qual o primeiro termo da pa? "))
razao = int(input("Qual a razao da pa? "))
numeroDeTermos = int(input("Qual a quantidade de termos da pa? "))

print(calcularPa(primeiroTermo,razao,numeroDeTermos)) 