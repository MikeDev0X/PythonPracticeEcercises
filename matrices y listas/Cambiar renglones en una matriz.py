#Miguel Jiménez Padilla
#Cambia renglones


def change():
    renglones=int(input())
    columnas=int(input())
    
    lista=[]
    matrix=[]
    for i in range(renglones):
        lista=[]
        for j in range (columnas):
            lista.append(int(input()))
        matrix.append(lista)

    
    x=int(input())#1
    y=int(input())#2
    
    x=x-1
    y=y-1
    newmatrix=[]
    
    for e in range(renglones):
        if e==y:
            newmatrix.append(matrix[x])
        elif e==x:
            newmatrix.append(matrix[y])
        else:
            newmatrix.append(matrix[e])
            
    print(newmatrix)
    
    
change()