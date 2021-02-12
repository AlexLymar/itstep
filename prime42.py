# prime 42 program
end = 1
num = 2
kor = 0
lst = []
while end > 0:
    num += 1
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                kor += 1
        if kor == 0:
           if i not in lst:
            lst.append(i)
        else:
            kor = 0
        if len(lst) == 42:
            print(lst)
            exit()