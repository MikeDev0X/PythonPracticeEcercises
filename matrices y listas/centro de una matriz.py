#Miguel Jiménez Padilla
#Centro Matriz

def matrix():
    renglones=int(input())
    columnas=int(input())
    
    lista=[]
    matrix=[]
    for i in range(renglones):
        lista=[]
        for j in range (columnas):
            lista.append(int(input()))
        matrix.append(lista)
    
    xmatrix=[]
    newmatrix=[]
    for i in range(renglones):
        xmatrix=[]
        if i!=0 and i!=renglones-1:
            for k in range(columnas):
                if k!=0 and k!=columnas-1:
                    xmatrix.append(matrix[i][k])
            newmatrix.append(xmatrix)   
                    
                    
    matrix=newmatrix             
    print(matrix)
    

matrix()








