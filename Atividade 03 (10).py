ft=int(input('Digite um número para fatorar: '))
x=ft
y=ft-1
for i in range (ft-1):
    x=y*x
    y=y-1 
if x == 0:
    x=1 
print('\nResultado: ',x)