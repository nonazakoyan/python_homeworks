def ft_contain(data, val):
    if val in data:
        return True
    return False


def ft_pop(data, i = None):
    
    if i == None:
        tmp = data[len(data) - 1]
        data.remove(data[len(data) - 1])
        return tmp
    tmp = data[i - 1]
    data.remove(data[i - 1])
    return tmp


def ft_remave_all(data, value):
    i = 0
    while i < len(data):
        if data[i] == value:
            data.remove(data[i])
        i += 1


def ft_reverse(data):
    i = 0
    while i < (len(data) // 2):
        tmp = data[i]
        data[i] = data[len(data) - i - 1]
        data[len(data) - i - 1] = tmp
        i += 1


def ft_min(data):
    i = 1
    min = data[0]
    while i < len(data):
        if data[i] < min:
            min = data[i]
        i += 1
    return min


def ft_max(data):
    i = 1
    max = data[0]
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i += 1
    return max
