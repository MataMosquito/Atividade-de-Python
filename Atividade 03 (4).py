n=int(input("Valor em segundos: "))
a3600=0 
a60=0 
a1=0 
while n >= 1:
 if n-3600 >= 0 : 
    a3600+=1
    n-=3600
 elif n-60 >= 0: 
    a60+=1 
    n-=60 
 elif n-1 >=0:
     a1+=1
     n-=1 
print("Hora - ",a3600,":",a60,":",a1)
print(hora, ':', min, ':', seg) 