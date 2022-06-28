filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])


def gt_100(el):
    return el > 100

my_l = [1, 111, 2, 222, 3, 333]

my_l_gt100 = filter(gt_100, my_l)


filter_gt100 = lambda iter: list(filter(lambda x: x > 100, iter))




filter_gt100(my_l)


from functools import reduce
points = (("Wanda", 1), ("Ant", 11), ("Jojo", 2), ("Mr. Jagger", 8))
impares = filter(lambda x: x % 2 != 0, (map(lambda t: t[1], points)))
reduce(lambda x, y: x + y, impares)



























from functools import reduce

points = (("Wanda", 1), ("Ant", 11), ("Jojo", 2), ("Mr. Jagger", 8))

reduce(lambda x, y: x + y, (map(lambda x: x[1], filter(lambda x: x[1] % 2 != 0, points))))
