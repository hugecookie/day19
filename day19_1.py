def selection_sort(ary):
    n = len(ary)
    for i in range(0, n - 1):
        min_idx = i
        for k in range(i + 1, n):
            if ary[min_idx] > ary[k]:
                min_idx = k
        tmp = ary[i]
        ary[i] = ary[min_idx]
        ary[min_idx] = tmp

    return ary


ary2 = [[55, 33, 250, 44],
        [88, 1, 67, 23],
        [199, 222, 38, 47],
        [155, 145, 20, 99]]
ary1 = []

for i in range(len(ary2)):
    for k in range(len(ary2[i])):
        ary1.append(ary2[i][k])

print('before sort -->', ary1)
ary1 = selection_sort(ary1)
print('after sort -->', ary1)
print('median --> ', ary1[len(ary1) // 2])
