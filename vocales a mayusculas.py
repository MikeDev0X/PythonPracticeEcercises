#Miguel Jiménez Padilla
#Vocales a mayúsculas

def voc():
    cad=input()
    lengt=int(len(cad))
    rec=0
    var=''
    count=''
    
    for i in range(0,lengt):
        if cad[rec]=='a' or cad[rec]=='e' or cad[rec]=='i' or cad[rec]=='o' or cad[rec]=='u':
            var=cad[rec].upper()
        
        else:
            var=cad[rec]
        count=count+var
        rec=rec+1
       
    print(count)
    
voc()