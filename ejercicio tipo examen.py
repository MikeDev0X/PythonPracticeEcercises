#Miguel Jiménez Padilla


def depreciacion():
    dolar=28000
    deprecia=4000
    año=1
    deprecia_acumulada=4000
    print('  Año  |  Depreciación  |  Valor al final del año  |  Depreciación acumulada    |')
    print('---------------------------------------------------------------------------------')
    
    for i in range (dolar-deprecia,-1,-4000):
        dolar=dolar-deprecia
        
        print('  ',año,'  |       ',deprecia,'   |            ',dolar,'       |            ',deprecia_acumulada,'          |')
        print('---------------------------------------------------------------------------------')
        año+=1
        deprecia_acumulada =deprecia_acumulada + deprecia
        

def serie_aritmetica(n):
    
    try:
        n=int(n)
        a=1
        d=3
        serie=1
        ran=n
        n=n-2
        count=0
        
        if ran>2:
            for i in range(1,ran+1):
                print(serie)
                count=count+serie
                serie=a+(n-1)*d
                n=n+1
                
            print('serie=',count)
                
        elif ran<=2:
            print('el número debe ser mayor a 2')
    except:
        print('caracter incorrecto')
         
def serie(n):
    rang=n
    if rang>4:
        x=3
        y=1
        
        for i in range(1,rang+1):
           print(x, end='  ')
           
           if x%6!=0 or x==3:
               x=x*6
           elif x%6==0:
               x=x-4
    else:
        print('El número ingresado debe ser mayor  a \n')
            
def main():
    
    
    opcion=1
    while opcion!=0:
        try:
            opcion=int(input('\nIngrese una de las siguientes opciones: \n 0: salir \n 1: problema 1 \n 2: problema 2 \n 3: problema 3 \n'))
        except:
            print('caracter incorrecto')
        else:
            if opcion==1:
                depreciacion()
            elif opcion==2:
                n=input('Ingrese el valor para determinar la serie: \n')
                serie_aritmetica(n)
            elif opcion==3:
                n=int(input('Ingrese la cantidad de dígitos en la serie a mostrarse: \n'))
                serie(n)


main()
