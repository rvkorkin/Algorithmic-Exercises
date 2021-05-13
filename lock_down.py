
class Graph:
    def __init__(self, V):
        self.vertices = V
        self.adjacent = [[] for _ in range(V)]

    def DFS(self, s, visited):
        tmp = [s]
        arr = set()
        arr.add(s)
        while tmp:
            v = tmp.pop()
            if not visited[v]:
                visited[v] = True
                for u in self.adjacent[v]:
                    if not visited[u]:
                        tmp.append(u)
                        arr.add(u)
        return arr

    def addEdge(self, x, y):
        self.adjacent[x].append(y)
        self.adjacent[y].append(x)

    def connected(self):
        visited = [False] * self.vertices
        comps = []
        for v in range(self.vertices):
            if not visited[v]:
                comps.append(self.DFS(v, visited))
        return comps


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

N, M, s = list(map(int, fin.readline().split()))
G = Graph(N)

for i in range(M):
    v1, v2 = list(map(int, fin.readline().split()))
    if v1 < N and v2 < N:
        G.addEdge(v1, v2)
if N == 0:
    counter = 0
else:
    counter = 1
for sub_graph in G.connected():
    if s in sub_graph:
        counter = len(sub_graph)
fout.write(str(counter))
fin.close()
fout.close()
