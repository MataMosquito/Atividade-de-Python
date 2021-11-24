n=int(input("Valor em reais: "))
a100=0 
a50=0 
a10=0 
a1=0 
while n >= 1:
 if n-100 >= 0 : 
    a100+=1
    n-=100 
 elif n-50 >= 0: 
    a50+=1 
    n-=50 
 elif n-10 >=0: 
    a10+=1
    n-=10 
 elif n-1 >=0:
    a1+=1
    n-=1 
if a100>=1:
    print("Notas de R$100,00: ", a100)
if a50>=1 :
    print("Notas de R$50,00: ", a50)
if a10>=1 :
    print("Notas de R$10,00: ", a10)
if a1>=1 :
    print("Notas de R$1,00: ", a1)
