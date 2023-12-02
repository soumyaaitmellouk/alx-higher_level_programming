def element_at(my_list, idx):
    if idx < 0:
        return None
    else:
        for i in my_list:
            if idx > len(my_list) - 1:
                return None
            else:
                return(my_list[idx])
