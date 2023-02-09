import random
import time


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


def qsort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    mid = low

    qsort(arr, start, mid - 1)
    qsort(arr, mid, end)


def quick_sort(ary):
    qsort(ary, 0, len(ary) - 1)


countAry = [1000, 10000, 12000, 15000]

for count in countAry:
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f'data number {count}')
    start = time.time()
    selection_sort(selectAry)
    end = time.time()
    print(f' selection number {end - start}')
    start = time.time()
    quick_sort(selectAry)
    end = time.time()
    print(f' quick number {end - start}')
    print()

    count *= 5
