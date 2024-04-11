# 13. Crie um algoritmo para calcular a área de um triângulo qualquer, considerando que 
# são  fornecidos  os  comprimentos  dos  seus  lados.  Esse  programa  não  pode  permitir  a 
# entrada de dados inválidos, ou seja, medidas menores ou iguais a 0
l1 = float(input("Digite o lado do triangulo "))
l2 = float(input("Digite o lado do triangulo "))
l3 = float(input("Digite o lado do triangulo "))
def validar_triangulo(l1,l2,l3):
    valid = False
    if(l1+l2>l3 and l1+l3>l2 and l3+l2>l1):
        valid = True
    return valid
def formula_herao(l1,l2,l3):
    semiPerimetro = (l1+l2+l3)/2
    return ((semiPerimetro*(semiPerimetro-l1)*(semiPerimetro-l2)*(semiPerimetro-l3))**0.5)

if(l1 ==0 or l2 ==0 or l3==0):
    print("Apenas valores válidos, maior que 0, são válidos!") 
    exit()
if(validar_triangulo(l1,l2,l3) == False):
     print("Os comprimentos dos lados não formam um triângulo válido.")
     exit()
print("Área do triângulo "+ str(formula_herao(l1,l2,l3)))