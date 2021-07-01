#Miguel Jiménez Padilla
#separar un string con guiones


def separa():
    string=input()
    string=string.strip()
    num=int(input())
    lengt=int(len(string))
    x=1
    y=0
    count=''
    rec=0
    varF=''
    
    
    if num>0:
        
        if num!=lengt:
        
            for i in range(0,lengt):
                if num/x==1:
                    if rec!=lengt-1:
                        x=1
                        varF=string[rec]
                        varF=varF+'-'
                    elif rec==lengt-1:
                        varF=string[rec]
                        
                else:
                    x=x+1
                    varF=string[rec]
                rec=rec+1
                count=count+varF
        
            print(count)
        else:
            print(string)
        
    else:
        print("Error")

separa()