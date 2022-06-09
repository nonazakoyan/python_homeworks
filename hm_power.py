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
        if exp < 0 and base !=0:
            exp *= -1
            res = 1 / loop(base, exp)
        elif exp >= 0:
            res = loop(base, exp)
        else:
            return "ERROR"
        return res
    else:
        return "some algorithm ..."

