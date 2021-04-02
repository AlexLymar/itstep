def same_pos(tup1, tup2, tup3):
    if len(tup1) <= len(tup2) and len(tup1) <= len(tup3):
        min_tup = tup1
    elif len(tup2) <= len(tup1) and len(tup2) <= len(tup3):
        min_tup = tup2
    else:
        min_tup = tup3
    rezult = {}
    for idx, num in enumerate(min_tup):
        if num == tup1[idx] and num == tup2[idx] and num == tup3[idx]:
            rezult[num] = idx
    return rezult

print(same_pos((4, 2, 6, 7), (1, 2, 7, 7), (2, 2, 2, 7, 1)))
