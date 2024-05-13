numero = int(input("Digite o numero "))
while numero !=0:
    q1 = numero//50
    r1 = numero%50
    q2 = r1//20
    r2 = r1%20
    q3 = r2//10
    r3 = r2%10
    q4 = r3//5
    r4 = r3//5
    q5 = r3//1
    r6 = r2//1
    print("Notas de 50: "+str(q1))
    print("Notas de 20: "+str(q2))
    print("Notas de 10: "+str(q3))
    print("Notas de 5: "+str(q4))
    print("Notas de 1: "+str(q5))
    numero=int(input("Digite o numero "))


