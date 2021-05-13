import heapq


def Dijkstra(adj, N, s, h):
    heap = []
    d = [float('inf')] * N
    v = -1
    S = {-1}
    d[s] = 0
    heapq.heappush(heap, (0, s))
    p = [-1] * N
    while heap:
        while v in S and heap:
            v = heapq.heappop(heap)[1]
        if v not in S:
            S.add(v)
            for u, w in adj[v]:
                new_d = d[v] + w
                if new_d < d[u]:
                    heapq.heappush(heap, (new_d, u))
                    d[u] = new_d
                    p[u] = v
    return d[h], p


with open('input.txt', 'r') as fin:
    N, M = list(map(int, fin.readline().split()))
    s, h = list(map(int, fin.readline().split()))
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = list(map(int, fin.readline().split()))
        adj[u].append((v, w))
        adj[v].append((u, w))

d, p = Dijkstra(adj, N, s, h)
path = []
el = h
while el > -1:
    path.append(el)
    el = p[el]

path = path[::-1]

with open('output.txt', 'w') as fout:
    if d < float('inf'):
        fout.write(str(d) + '\n')
        fout.write(str(len(path)) + '\n')
        fout.write(' '.join(map(str, path)))
    else:
        fout.write(str(-1))
