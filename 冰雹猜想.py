n = int(input('int='))
for i in range(1, n+1):
    while i != 0:
        if i% 2 ==0:
            i/=2
        else:
            i=i*3+1
    print('True')