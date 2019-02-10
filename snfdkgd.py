def number_of_in_common(a, b):
    number = 0
    c = []
    d = []
    for k in range(len(a)):
        c.append(0)
        d.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and c[i] == 0 and d[j] == 0:
                number += 1
                c[i] = 1
                d[j] = 1
    return number


a = [6, 8, 7, 2]
b = [7, 3, 8, 7]
print(number_of_in_common(a,b))
