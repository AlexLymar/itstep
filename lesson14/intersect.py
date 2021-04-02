def intersect(tup):
    e = set.intersection(*map(set, tup))
    e = tuple(e)
    print('Rezult: ',e)

tup1 = (4, 2, 6, 7)
tup2 = (1, 2, 7, 2, 9)
tup3 = (2, 2, 2, 7, 1)
tup = tup1, tup2, tup3
intersect(tup)

