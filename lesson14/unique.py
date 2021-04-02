
def unique(tup1, tup2, tup3):
    tup = ((set(tup1) | set(tup2) | set(tup3)) - ((set(tup1) & set(tup2)) | (set(tup1) & set(tup3)) | (set(tup2) & set(tup3))))
    print(tuple(tup))

tup1 = (4, 2, 6, 7)
tup2 = (1, 2, 7, 2, 9)
tup3 = (2, 2, 2, 7, 1)
tup = set()
unique(tup1, tup2, tup3)