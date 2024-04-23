def my_logorifm(x):
    ''' логорифм по основанию 2'''

    i=0
    n = 2
    if x == 2:
        return ('логарифм по основанию 2 равен', 1)
    if 2**i == x:
        print('логарифм по основанию 2 равен', i)
    else :
        i += 1



print(my_logorifm(8))

