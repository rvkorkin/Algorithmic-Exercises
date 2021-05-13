
def min_path_sum(a):
    if not len(a) or not len(a[0]):
        return 0
    N, M = len(a), len(a[0])
    d = [[0] *M for _ in range(N)]
    d[0][0] = a[0][0]
    for j in range(1, M):
        d[0][j] = d[0][j-1] + a[0][j]
    for i in range(1, N):
        d[i][0] = d[i-1][0] + a[i][0]
    for i in range(1, N):
        for j in range(1, M):
            d[i][j] = min(d[i-1][j], d[i][j-1]) + a[i][j]
    return d[-1][-1]
