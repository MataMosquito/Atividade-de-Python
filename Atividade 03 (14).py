dg=str(input('Digite uma frase: '))
frase=dg.split()
imp=dg
for i in frase:
    carac=len(i)
    t=i.islower()
    if t == False:
        imp=imp.replace(i, '*'*carac) 
print('Antes: ',dg,'\nDepois: ', imp)
