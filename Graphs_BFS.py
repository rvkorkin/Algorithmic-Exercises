from collections import deque


class Graph:
    def __init__(self, V):
        self.vertices = V
        self.adjacent = [[] for _ in range(V)]

    def addEdge(self, x, y):
        self.adjacent[x].append(y)
        self.adjacent[y].append(x)

    def bfs(self, s, key):
        d = [0] * self.vertices
        visited = [0] * self.vertices
        vertex_queue = deque([s])
        while vertex_queue:
            v = vertex_queue.popleft()
            visited[v] = 2
            for u in self.adjacent[v]:
                if not visited[u]:
                    visited[u] = 1
                    vertex_queue.append(u)
                    d[u] = d[v] + 1
                    if u == key:
                        return d[u]
        return -1


with open('input.txt', 'r') as fin:
    N, M = list(map(int, fin.readline().split()))
    park = [list(fin.readline().split())[0] for _ in range(N)]

G = Graph(N * M)
for i in range(N):
    for j in range(M):
        if i < N - 1 and park[i + 1][j] != '#' and park[i][j] != '#':
            G.addEdge(M + i * M + j, i * M + j)
        if i * M + j - M >= 0:
            if park[i - 1][j] != '#' and park[i][j] != '#':
                G.addEdge(i * M + j - M, i * M + j)
        if j < M - 1 and j + 1 < (N - i) * M:
            if park[i][j + 1] != '#' and park[i][j] != '#':
                G.addEdge(i * M + j, i * M + j + 1)
        if j > 0 and park[i][j - 1] != '#' and park[i][j] != '#':
            G.addEdge(i * M + j, i * M + j - 1)
        if park[i][j] == 'E':
            x0 = i * M + j
        elif park[i][j] == 'X':
            x = i * M + j
with open('output.txt', 'w') as fout:
    if N == 0:
        fout.write(str(0))
    else:
        start = min(x0, x)
        stop = max(x0, x)
        fout.write(str(G.bfs(start, stop)))
