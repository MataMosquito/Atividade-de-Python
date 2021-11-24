n=int(input('Numeros da sequencia de Fibonacci: ')) 
x=0
y=1
print('\nFibonacci: {} --> {}'.format(x,y),end='')
if n>2:
    while n-2 > 0:
        t=x+y
        x=y
        y=t
        print(' --> {}'.format(t), end='')
        n-=1
print(' --> FIM') 