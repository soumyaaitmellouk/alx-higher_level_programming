#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            temp.append(True)
        else:
            temp.append(False)
    return temp
