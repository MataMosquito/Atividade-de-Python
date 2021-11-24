lista=['Diana','Merlin','Bianca','Fernando','Elisabete','Cristofer','Ronaldo',
'Meliodas','Casemiro','FelipeNeto','Escanor','Bianca',
'Fernando','Elisabete','Cristofer','Diana','Merlin','Bianca','Cristofer','Ronaldo','Meliodas','Casemiro','FelipeNeto','Escanor',
'Bianca','Fernando','Elisabete','Cristofer','Diana','Merlin','Bianca','Fernando','Cristofer','Ronaldo','Meliodas','Casemiro','FelipeNeto',
'Elisabete','Cristofer','Ronaldo','Meliodas','Casemiro','FelipeNeto','Escanor','Diana','Merlin','Ronaldo','Meliodas','Casemiro','FelipeNeto','Escanor']
a=lista.count('Diana') 
b=lista.count('Merlin') 
c=lista.count('Bianca')
d=lista.count('Fernando') 
e=lista.count('Elisabete') 
f=lista.count('Cristofer') 
g=lista.count('Ronaldo') 
h=lista.count('Meliodas') 
i=lista.count('Casemiro') 
j=lista.count('FelipeNeto') 
k=lista.count('Escanor') 
listar={'Diana':a,'Merlin':b,'Bianca':c,'Fernando':d,'Elisabete':e,'Cristofer':f,'Ronaldo':g,'Meliodas':h,'Casemiro':i,'FelipeNeto':j,'Escanor':k} 
for nome,vezes in listar.items():
    print(nome, '     \t:', vezes, 'vezes') 