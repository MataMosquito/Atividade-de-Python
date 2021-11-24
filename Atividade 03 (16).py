dg=int(input('Digite a quantidade de valores: ')) 
lista=[]
i=0
sm=0
while i < dg: 
    t=int(input('Valor:'))
    lista.append(t)  
    i+=1 
    sm+=t
lista.sort() 
maior=lista[dg-1]
menor=lista[0] 
print('Soma dos Número:\t|', sm) 
print('Média dos Números:\t|', sm/dg) 
print('Maior Número:   \t|', maior) 
print('Menor Número:   \t|', menor)