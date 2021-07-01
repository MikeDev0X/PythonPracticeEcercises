n = int(input())
a = 0
b = 1
while  a < n and n != 1:
    if n%b == 0:
        a = a + b
    b = b + 1

if a == n:
    print('PERFECTO')
else:
    print('NO PERFECTO')