

def is_path(a, N, M):
    N, M = len(a), len(a[0])
    d = [[True] * M for _ in range(N)]
    d[0][0] = a[0][0]
    for j in range(1, M):
        d[0][j] = d[0][j - 1] & a[0][j]
    for i in range(1, N):
        d[i][0] = d[i - 1][0] & a[i][0]
    for i in range(1, N):
        for j in range(1, M):
            d[i][j] = (d[i - 1][j] & a[i][j]) or (d[i][j - 1] & a[i][j])
    return d[-1][-1]


def compute_K(c, N, M):
    l = 0
    r = len(c)
    while r - l > 1:
        m = (l + r) // 2
        a = matr(c[:m + 1], N, M)
        if is_path(a, N, M):
            l = m
        else:
            r = m
    return r


def matr(c1, N, M):
    a = [[True] * N for _ in range(M)]
    for c_curr in c1:
        a[c_curr[1]][c_curr[0]] = False
    return a


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N, M, K = list(map(int, fin.readline().split()))
c = [0] * K
for k in range(K):
    c[k] = list(map(int, fin.readline().split()))

if K == 1:
    a = matr(c, N, M)
    if is_path(a, N, M):
        fout.write(str(-1))
    else:
        fout.write(str(0))
elif K == 2:
    a0 = matr(c[:1], N, M)
    a1 = matr(c[:2], N, M)
    if is_path(a0, N, M):
        if is_path(a1, N, M):
            idx = -1
        else:
            idx = 1
    else:
        idx = 0
    fout.write(str(idx))
else:
    if is_path(matr(c, N, M), N, M):
        idx = -1
        fout.write(str(idx))
    else:
        idx = compute_K(c, N, M)
        fout.write(str(idx))
fin.close()
fout.close()
