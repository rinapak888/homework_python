<<<<<<< HEAD
def sortirovka_1(spisok):
    a = spisok
    a.sort()
    return
def sortirovka_2(spisok):
    a = spisok
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
print(sortirovka_1([1500, 123, 493, 82319, 38290193]))
=======
def sortirovka_1(spisok):
    a = spisok
    a.sort()
    return
def sortirovka_2(spisok):
    a = spisok
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
print(sortirovka_1([1500, 123, 493, 82319, 38290193]))
>>>>>>> 4884fe8a9a4c3ab1696cf586480f2b62e2299855
print(sortirovka_2([15, 343, 493, 19, 39343324]))