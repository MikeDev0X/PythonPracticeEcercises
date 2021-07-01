def isYearLeap(year):
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
def daysInMonth(year, month):
    
    yearr=isYearLeap(year)
    treeone=[1,3,5,7,8,10,12]
    tree=[4,6,9,11]
    
    if month>0 and month<13:
        if yearr==True and month==2:
            return 29
        elif yearr==False and month==2:
            return 28
        elif month in tree:
            return 30
        elif month in treeone:
            return 31
    else:
        return None



def dayOfYear(year, month, day):
    x=isYearLeap(year)
    actual=0
    tot=0
    for t in range(0,month-1):
        tot=tot + daysInMonth(year,t+1)

    tot=tot+day
    return tot



print(dayOfYear(2020, 12, 31))