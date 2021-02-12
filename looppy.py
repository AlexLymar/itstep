#looppy program
x = 101
a = 11, 22, 33, 44, 55, 66, 77, 88, 99
count = 0
while x > 0:
    x -= 1
    if x in a:
        print(x)
    if x <= 9 and x != 0:
        print(x)