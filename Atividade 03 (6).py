n=int(input('Numeros da sequencia de Fibonacci: ')) 
x=0
y=1
print('\nFibonacci: {} --> {}'.format(x,y),end='')
if n>2:
    for i in range (n-2):
        t=x+y
        x=y
        y=t
        print(' --> {}'.format(t), end='')
print(' --> FIM') 