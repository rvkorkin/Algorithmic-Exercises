

def findPartition(x):
    if sum(x) % 2 == 1:
        return False
    half_sum = sum(x) // 2
    matr = [[0] * (len(x) + 1) for _ in range(half_sum + 1)]
    for j in range(len(x) + 1):
        matr[0][j] = True
    for i in range(1, half_sum + 1):
        matr[i][0] = False
    for i in range(1, half_sum + 1):
        for j in range(1, len(x) + 1):
            if i - x[j - 1] >= 0:
                matr[i][j] = matr[i][j - 1] or matr[i - x[j - 1]][j - 1]
            else:
                matr[i][j] = matr[i][j - 1]
    return matr[-1][-1]


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

N = int(fin.readline())

cost = list(map(int, fin.readline().split()))
if findPartition(cost):
    fout.write('YES')
else:
    fout.write('NO')

fin.close()
fout.close()
