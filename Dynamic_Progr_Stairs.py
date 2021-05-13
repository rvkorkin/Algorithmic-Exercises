
def stairs(diff):
    if len(diff) == 1:
        return diff[0]
    min_val = diff.pop(0)
    N = len(diff)
    d = [0] * N
    d[:2] = diff[:2]
    for i in range(2, N):
        d[i] = min(d[i - 1], d[i - 2]) + diff[i]
    return d[N - 1] + min_val


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

N = int(fin.readline())
x = sorted(list(map(int, fin.readline().split())))
diff = [x[i] - x[i - 1] for i in range(1, len(x))]

length = stairs(diff)
fout.write(str(length))

fin.close()
fout.close()
