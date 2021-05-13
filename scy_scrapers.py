def matr_recovery(matr, x, i, j, k):
    if i == 0 and j == 0 or k == 0:
        return [], []
    if matr[i][j][k - 1]:
        return matr_recovery(matr, x, i, j, k - 1)
    elif i >= x[k - 1][1] and matr[i - x[k - 1][1]][j][k - 1]:
        a, b = matr_recovery(matr, x, i - x[k - 1][1], j, k - 1)
        return [x[k - 1][0]] + a, b
    else:
        a, b = matr_recovery(matr, x, i, j - x[k - 1][1], k - 1)
        return a, [x[k - 1][0]] + b


def findPartition(x):
    tot_sum = sum([el[1] for el in x])
    hs = tot_sum // 2
    n = len(x)
    v = False
    matr = [[[v] * (n + 1) for _ in range(hs + 1)] for _ in range(hs + 1)]
    for k in range(n + 1):
        matr[0][0][k] = True
    for i in range(0, hs + 1):
        for j in range(0, hs + 1):
            for k in range(1, n + 1):
                matr[i][j][k] = matr[i][j][k - 1]
                if i - x[k - 1][1] >= 0:
                    v = matr[i - x[k - 1][1]][j][k - 1]
                    matr[i][j][k] = matr[i][j][k] or v
                if j - x[k - 1][1] >= 0:
                    v = matr[i][j - x[k - 1][1]][k - 1]
                    matr[i][j][k] = matr[i][j][k] or v
    parts = []
    for i in range(1, hs + 1):
        if matr[i][i][n]:
            parts.append(matr_recovery(matr, x, i, i, n))
    max_height = 0
    idx = 0
    for i, el in enumerate(parts):
        if sum([x[k][1] for k in el[0]]) > max_height:
            max_height = sum([x[k][1] for k in el[0]])
            idx = i
    return parts[idx], max_height


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N = int(fin.readline())
h = list(map(int, fin.readline().split()))
x = list(enumerate(h))
my_sets, height = findPartition(x)
fout.write(str(height) + '\n')
fout.write(str(len(my_sets[0])) + '\n')
fout.write(' '.join(map(str, my_sets[0])) + '\n')
fout.write(str(len(my_sets[1])) + '\n')
fout.write(' '.join(map(str, my_sets[1])) + '\n')
fin.close()
fout.close()
