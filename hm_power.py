def loop(base, exp):
    i = 0
    res = 1

    while i < exp:
        res *=base 
        i += 1
    return res


def ft_power(base, exp):
    i = 0
    res = 1
    if int(exp) == exp:
        if exp < 0:
            exp *= -1
            res = 1 / loop(base, exp)
        else:
            res = loop(base, exp)
        return res
    else:
        return "some algorithm ..."

