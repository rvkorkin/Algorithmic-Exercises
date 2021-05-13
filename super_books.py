import heapq


def dist(x):
    dst = {}
    for i, el in enumerate(x):
        if el in dst:
            dst[el].append(i)
        else:
            dst[el] = [i]
    return dst


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N, K, M = map(int, fin.readline().split())
x = list(map(int, fin.readline().split()))

book_pos = dict()
tab = set()
heap = []
counter = 0

all_coord = dist(x)
request = [0 for _ in range(N + 1)]

for pos, book_id in enumerate(x):
    request[book_id] += 1
    next_pos = float('inf')
    if request[book_id] < len(all_coord[book_id]):
        next_pos = all_coord[book_id][request[book_id]]
    if book_id in tab:
        heapq.heappush(heap, (-next_pos, book_id))
    else:
        if len(tab) == K:
            exp_pos = 0
            while exp_pos < pos:
                exp_pos, remove_id = heapq.heappop(heap)
                exp_pos = -exp_pos
            tab.remove(remove_id)

        tab.add(book_id)
        heapq.heappush(heap, (-next_pos, book_id))
        counter += 1

fout.write(str(counter))
fin.close()
fout.close()
