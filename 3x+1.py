import matplotlib.pyplot as plt

valor_apl=input("Qual o número que será aplicado?\n")
valor_apl=int(valor_apl)
valor_ger=0

valor=[]
valorb=[]

while valor_apl !=1:

  if valor_ger==0:
    valor.append(valor_apl)
    valor_ger+=1
    print("valores: ")



  if valor_apl%2==0:
    print (str(valor_apl))
    valor_apl=(valor_apl/2)
    valor.append(valor_apl)

  else:
    print (str(valor_apl))
    valor_apl=valor_apl*3+1
    valor.append(valor_apl)

  valor_ger+=1

print("1.0")
print ("Chegou em 1 após "+str(valor_ger)+" gerações")

for x in range(valor_ger):
  valorb.append(x)

plt.scatter(valorb,valor)
