#Miguel Jiménez Padilla
#Diagonal Principal

def matrix():
    renglones=int(input())
    columnas=int(input())
    if renglones!=columnas:
        print('la matriz no es cuadrada')
    else:
        lista=[]
        matrix=[]
        for i in range(renglones):
            lista=[]
            for j in range (columnas):
                lista.append(int(input()))
            matrix.append(lista)
        
        lista=[]
        
        for i in range(renglones):
            
            for j in range(columnas):
                if i==j:
                    lista.append(matrix[i][j])
            
        print(lista)
matrix()


