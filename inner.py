
def is_sum(x, k):
    l = 0
    r = len(x) - 1
    while l < r:
        if (x[l] + x[r] == k):
            return True
        elif (x[l] + x[r] < k):
            l += 1
        else:
            r -= 1
    return False


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N = int(fin.readline())
if N == 0:
    fout.write(str(0))
else:
    x = list(map(int, fin.readline().split()))
    x = sorted(x)
    tot_pairs = 0
    for i in range(N):
        if is_sum(x, x[i]):
            tot_pairs += 1
    fout.write(str(tot_pairs))
fin.close()
fout.close()
