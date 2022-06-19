def ft_map(func, *arg):

    i = 0
    new_lst = [None] *  len(arg[0])
    while i < len(arg[0]):
        j = 0
        lst = [None] * len(arg)
        while j < len(arg):
            lst[j] = arg[j][i]
            j += 1
        new_lst[i] = func(*lst)
        i += 1
    return new_lst

def ft_map3(func, data1, data2, data3):
    return ft_map(func, data1, data2, data3)




def trip_func(n):
    return n ** 3

def ft_triple(data):
    return ft_map(trip_func, data)




def ft_pow(a, b):
    return a ** b

def ft_map2(ft_pow, data1, data2):
    return ft_map(ft_pow, data1, data2)



def ft_filter_utils(func, data):
    count = 0
    i = 0
    while i < len(data):
        if func(data[i]):
            count += 1
        i += 1
    return count

def ft_filter(func, data):
    n = ft_filter_utils(func, data)
    lst = [None] * n
    i = 0
    j = 0
    while i < len(data):
        if func(data[i]):
            lst[j] = data[i]
            j += 1
        i += 1
    return lst

