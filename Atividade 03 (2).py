import numpy

tx=int(input("Digite o Angulo: "))
agl=numpy.deg2rad(tx)

sen=math.sin(agl) 
cos=math.cos(agl) 
tg=math.tan(agl) 

print("sen= ", sen,"\ncos= ", cos,"\ntg= ", tg)