numbers = [-1, 5, -7, 3, -10, 5]

def filter_num(nums):
    if nums < 0:
        return True
    else:
        return False

out_lst = filter(filter_num, numbers)
print('Початковий список: \n', numbers)
print('Відфільтрований список: \n', list(out_lst))