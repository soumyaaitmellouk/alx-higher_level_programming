#!/usr/bin/python3
def uniq_add(my_list=[]):
    somme = 0
    temp = list(set(my_list))
    for i in range(len(temp)):
        somme = somme + temp[i]

    return somme
