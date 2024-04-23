""" Округление Факториал Фибоначчи"""

def my_round(a):
    new_a = int(a)
    if a-new_a >= 0.5:
        print('округление до целого ', new_a+1)
        return new_a+1

    else:
        print('округление до целого ', new_a)
        return new_a




def my_factorial(num):
    factor = 0
    if (num <= 1):
        return 1
    else:
        factor = (num * my_factorial(num-1))
        return factor






def my_fibonacci(num):
    if num <= 1:
        return num
    else:
        return my_fibonacci(num - 1) + my_fibonacci(num - 2)








