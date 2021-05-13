
def knapSack(W, N, weight, cost):
    d = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if weight[i - 1] > w:
                d[i][w] = d[i - 1][w]
            else:
                if d[i - 1][w] > d[i - 1][w - weight[i - 1]] + cost[i - 1]:
                    d[i][w] = d[i - 1][w]
                else:
                    d[i][w] = d[i - 1][w - weight[i - 1]] + cost[i - 1]
    if d[N][W] == 0:
        return d[N][W], 0
    i = N
    items = []
    w1 = W
    while i > 0:
        c1 = (w1 - weight[i - 1] >= 0)
        if w1 - weight[i - 1] >= 0:
            c2 = (d[i][w1] - d[i - 1][w1 - weight[i - 1]] == cost[i - 1])
            if c1 and c2:
                items.append(i)
                w1 -= weight[i - 1]
        i -= 1
    return d[N][W], sorted(items)


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

W, N = list(map(int, fin.readline().split()))
if N == 0:
    fout.write('0')
else:
    weight = list(map(int, fin.readline().split()))
    cost = list(map(int, fin.readline().split()))

    Value, items = knapSack(W, N, weight, cost)
    fout.write(str(Value) + '\n')

    if items:
        fout.write(str(len(items)) + '\n')
        fout.write(' '.join(map(str, sorted(items))))
    else:
        fout.write('0')
fin.close()
fout.close()
