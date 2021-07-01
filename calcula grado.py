#Miguel Jiménez

numero=float(input())
def calcula_grado(numero):
    
    if numero>0.9 and numero<1:
        print('A')
    elif numero>0.8 and numero<0.9:
        print('B')
    elif numero>0.7 and numero<0.8:
        print('C')
    elif numero>0.6 and numero<0.7 :
        print('D')
    elif numero<=0.6 and numero>0:
        print('F')
    elif numero<=0 or numero>=1:
        print('score incorrecto')
        
calcula_grado(numero)

















