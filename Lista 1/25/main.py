r = 0.01
pmt = float(input("Informe o valor das parcelas"))
n = int(input("Informe o numero de parcelas"))
smt = 0
for i in range(0,n+1):
    smt += pmt/((1+r)**i)
print(str(smt))
