def guess_enough(value, target):
    if abs(value ** 3 - target) < 0.0001:
        return True
    return False


def improve(root, target):
	return ((target / (root ** 2)) + (2 * root)) / 3


def ft_cbrt(n):
    root = 1
    if n < 0:
        return ("Wrong input!")
    elif n == 0:
        return 0

    while not guess_enough(root, n):
        root = improve(root, n)
    return root

print(ft_cbrt(-0.5))