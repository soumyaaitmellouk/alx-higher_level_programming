#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = my_list.copy()
    for i in range(len(my_list) - 1):
        if my_list[i] % 2 == 0:
            temp[i] = True
        else:
            temp[i] = False
    return temp
