#Miguel Jiménez Padilla, Gabdiel Adame
#Serie de Leibniz (converge en n/4)

def serie_leibniz(numero):
    t=0
    total=0
    while numero!=0:
        numero=numero-1
        arriba=(-1)**t
        abajo=2*t+1
        if (arriba/abajo)==1:
            print("1 ", end= "")
        elif (arriba/abajo)>0:
            print( "+ ",arriba, " / ", abajo , end=" ", sep="")      
        else:
            print("- ",abs(arriba), " / ", abajo , end=" ", sep="")
        t=t +1
        total=total + (arriba/abajo)
    print( "=", " ", "{0:.2f}".format(total), sep = "", end= "")
    

def main():
    numero = int(input())
    serie_leibniz(numero)
    
    
    
main()