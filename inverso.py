#Miguel Jiménez Padilla
#Inverso

def inverso():
    n=int(input())
    esp=n
    cont=0
    menos=1
    
    if n<0: #momentaneamente quitarle el negativo 
        menos=-1
        n=n*-1
        esp=esp*-1
        
    while esp>=1:
        esp=esp//10
        cont+=1
    
    if cont>0 and cont<7:
        c=10
        d=0
        x=0
        
        while n>0 or n<0:
            d=n%c
            x=(x*c)+d
            n=n//c
                
        print(x*menos)#en caso de que el número fuera negativo, vuelve a ser negativo
            
    elif cont>=7:
        print('numero demasiado largo')
            
inverso()
