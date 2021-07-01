#Miguel Jiménez Padilla
#Extremos de un string

def ext():
    cad=input()
    lengt=int(len(cad))    

    if lengt>=2:
        beginning=cad[0:2]
        ending=cad[lengt-2:lengt]
    print(beginning+ending)
ext()



