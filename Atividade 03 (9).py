import sys
v1=float(input('Digite um valor ')) 
v2=float(input('Digite outro valor '))
op=int(input('\nEscolha uma opção de calculo:\n\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n\n5-Sair\n')) 
if op==1:
    v1+=v2
elif op==2:
    v1-=v2 
elif op==3:
    v1=v1*v2 
elif op==4:
    v1=v1/v2
elif op==5:
    sys.exit()
else:
    print('Essa opção não existe')
print('Resultado: ',x)
