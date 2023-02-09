def score_sort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if ary[cur - 1][1] > ary[cur][1]:
                ary[cur - 1], ary[cur] = ary[cur], ary[cur - 1]
    return ary


scoreAry = [['A', 88], ['B', 99], ['C', 71], ['D', 78], ['E', 67], ['F', 92]]

print('before sort -->', scoreAry)
scoreAry = score_sort(scoreAry)
print('after sort -->', scoreAry)

print('## Score ##')
for i in range(len(scoreAry) // 2):
    print(scoreAry[i][0], ':', scoreAry[len(scoreAry) - 1 - i][0])
