"""возвести в квадрат возвести в любую степень """


def my_square(a):
    '''возводит число в квадрат'''
    if a == 0:
        print('квадрат числа ', 1)
        return 1
    else:
        print('квадрат числа', a * a)
        return a*a



def my_degree(x, y):
    '''возводит число Х в степень У'''
    if x == 0 or y == 0:
        print('степерь числа ', 1)
        return 1
    r = 1
    while (y > 0):
        r *= x
        y -= 1
    print('степерь числа ', r)
    return r






