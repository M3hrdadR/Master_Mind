import math
import random

def generate(n, lst, base):
    index = 0
    a = []
    for i in range(n):
        a.append(0)
    k = n-1
    while k >= 0:
        b = a[:]
        lst[index] = b
        index += 1
        a[n-1] = a[n-1] + 1
        k = n-1
        while k >= 0 and a[k] == base:
            a[k] = 0
            k -= 1
            if k >= 0:
                a[k] = a[k] + 1
    return lst


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


def delete(lst, element, m):
    if m == 4:
        m = 0
    for tmp in lst:
        if number_of_in_common(element, tmp) > m:
            print(tmp)
            del lst[lst.index(tmp)]
    return lst


def master_mind(lst):
    c = 0
    while len(lst) > 1:
        rand = random.randint(0, len(lst))
        print(lst[rand])
        i = int(input("how many numbers are in their correct position : "))
        j = int(input("how many number are there in your answer but not in correct position : "))
        lst = delete(lst, lst[rand], i+j)
        for a in lst:
            c += 1
            print(a)
        print(c)
    print(lst)


lst = []
n = 4
base = 3
for i in range(int(math.pow(base, 4))):
    lst.append(0)
lst = generate(n, lst, base)
master_mind(lst)