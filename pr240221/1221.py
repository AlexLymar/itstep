#def calculate_big_number(num):
#    res = []
#    for i in range(1, 10000):
#        res.append((num*i*10 + 250))
#    return res
#
#print(calculate_big_number(2000000))

words = ['Word', 'Apple', 'sky', 'Map']
#print(list(filter(lambda  word: len(word) < 6, words)))
print(list(filter(str.istitle, words)))
