import random
import time


def bubble_sort(ary):
    n = len(ary)
    for end in range(n - 1, 0, -1):
        change_YN = False
        for cur in range(0, end):
            if ary[cur] > ary[cur + 1]:
                ary[cur], ary[cur + 1] = ary[cur + 1], ary[cur]
                change_YN = True
        if not change_YN:
            break
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


def quickSort(ary):
    qsort(ary, 0, len(ary) - 1)


tempAry = [random.randint(10000, 99999) for _ in range(1000000)]
tempAry.sort()

rndPos = random.randint(0, len(tempAry) - 1)
print(f'data number : {len(tempAry)}')
print(f'place : {rndPos}')
tempAry.insert(rndPos, tempAry[-1])

bubbleAry = tempAry[:]
quickAry = tempAry[:]

start = time.time()
bubble_sort(bubbleAry)
end = time.time()
print(f' bubble sort : {end - start}')

start = time.time()
quickSort(quickAry)
end = time.time()
print(f' quick sort : {end - start}')
