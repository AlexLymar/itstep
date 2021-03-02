biggers_cities = ['Tokyo', 'Delphi', 'Shanhai', 'Mexico City', 'San Paulo', 'Mumbai', 'Kinki major metropolitan area',
                  'Cairo', 'Pairs']

x = range(1, 10)
print(list(zip(biggers_cities, x)))

print('-------інший варіант------------')

for index, value in enumerate(biggers_cities):
    print(value, index + 1)