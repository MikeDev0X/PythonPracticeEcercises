#Miguel Jiménez Padilla
#Sumar las columnas de una matriz

def generate_matrix (row, column):
    matrix = []
    listx=[]
    for i in range(row):
        listx=[]
        for i in range (column):
            listx.append(int(input()))
        matrix.append(listx)    
    
    print ('Original matrix: ',matrix)
    return matrix
    

def add_columns (matrix,row,column):
    
    
    listx_sums= []
    count=[]
    countx=[]
    
    for h in range(column):
        count=[]
        for j in range (row):
            for k in range (column):
                if h==k:
                    count.append(matrix[j][k])
        count=sum(count)
        listx_sums.append(count)
    
    return listx_sums


def main():
    row = int(input('Enter row length: '))
    column = int(input('Enter column length: '))
    print('')
    if row<1 or column<1:
        print('Error')
    else:
        
        x=generate_matrix(row,column)
        
        print('column sum: ',add_columns(x,row,column))

main()