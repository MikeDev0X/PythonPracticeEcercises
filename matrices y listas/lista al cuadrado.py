#Miguel Jiménez Padilla
#Lista al cuadrado


def lista_al_cuadrado():
    reng=int(input())
    colum=int(input())
    matrix=[]
    lista=[]
    new=[]
    count=0
    
    for i in range(reng):
        lista=[]
        for i in range(colum):
            lista.append(int(input()))
        matrix.append(lista)
            
    for i in range (reng):
        for j in range (colum):
            if matrix[i][j]%2==0:
                count+=1
        
        new.append(count)
        count=0
        
    print(new)
    
lista_al_cuadrado()