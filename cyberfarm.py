def update(arr, l, r):
    arr[l] += 1
    if r != len(arr):
        arr[r] -= 1
    return arr


def restore(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N, M, K = map(int, fin.readline().split())
if N > 0:
    bag = []
    x = [0] * N
    for i in range(M):
        l, r = list(map(int, fin.readline().split()))
        x = update(x, l, r)
    x = restore(x)
    y = [0]
    for i in range(N):
        y.append(y[-1] + x[i])
    for i in range(K):
        ql, qr = list(map(int, fin.readline().split()))
        counter = y[qr] - y[ql]
        fout.write(str(counter) + '\n')
fin.close()
fout.close()
