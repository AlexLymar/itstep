my_list = ['32', 'abc', '12', 'list']
func_list = list(map(int, filter(lambda x: x.isdigit(), my_list)))
print(func_list)