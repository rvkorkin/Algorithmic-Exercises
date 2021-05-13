def bellman_ford(V, G, s):
    d = [[float('inf')] * V for _ in range(V)]
    d[0][s] = 0
    for i in range(1, V):
        for u, v, w in G:
            if d[i - 1][u] != float('Inf') and d[i - 1][u] + w < d[i][v]:
                d[i][v] = min(d[i - 1][u] + w, d[i - 1][v], d[i][v])
    return d


with open('input.txt', 'r') as fin:
    V, id1, id2, K = list(map(int, fin.readline().split()))
    z = [[-1] * V for _ in range(V)]
    for u in range(V):
        z[u] = list(map(int, fin.readline().split()))

G = []
for u in range(V):
    for v in range(V):
        if z[u][v] != -1 and u != v:
            G.append([u, v, z[u][v]])
        if u == v:
            G.append([u, v, 0])

d = bellman_ford(V, G, id1)
if K < V:
    result = d[K][id2]
else:
    result = d[-1][id2]
if result == float('Inf'):
    result = -1
with open('output.txt', 'w') as fout:
    fout.write(str(result))
