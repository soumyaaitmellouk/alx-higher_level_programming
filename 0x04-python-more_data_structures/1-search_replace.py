#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            temp.append(replace)
        else:
            temp.append(my_list[i])
    return temp
