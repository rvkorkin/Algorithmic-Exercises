import heapq


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N, K = list(map(int, fin.readline().split()))
if K >= N:
    fout.write(str(max(list(map(int, fin.readline().split())))))
else:
    x = list(map(int, fin.readline().split()))
    w = x[:K]
    heapq.heapify(w)
    for i in range(K, N):
        heapq.heapreplace(w, x[i] + w[0])
    fout.write(str(max(w)))
fin.close()
fout.close()
