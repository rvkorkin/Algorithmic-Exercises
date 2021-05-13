

def heap_push(heap, x):
    heap.append(x)
    sift_up(heap, len(heap) - 1)


def heap_pop(heap, i=0):
    heap[i], heap[-1] = heap[-1], heap[i]
    res = heap.pop()
    sift_up(heap, i)
    sift_down(heap, i)
    return res[1]


def sift_up(heap, i):
    if i == 0:
        return
    parent = (i - 1) // 2
    if heap[parent] > heap[i]:
        heap[i], heap[parent] = heap[parent], heap[i]
        sift_up(heap, parent)


def sift_down(heap, x):
    i1, i2 = 2 * x + 1, 2 * x + 2
    if i1 >= len(heap):
        return
    if i2 >= len(heap):
        i_min = i1
    else:
        if heap[i1] < heap[i2]:
            i_min = i1
        else:
            i_min = i2
    if heap[i_min] < heap[x]:
        heap[x], heap[i_min] = heap[i_min], heap[x]
    sift_down(heap, i_min)


def heapify(heap):
    for i in range(len(heap) - 1, -1, -1):
        sift_down(heap, i)


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

heap = []
N = int(fin.readline())
user = 0
for i in range(N):
    line = fin.readline().split()
    if line[0] == '+':
        heap_push(heap, [-int(line[2]), user])
        user += 1
    else:
        if len(heap):
            var = heap_pop(heap)
            fout.write(str(var) + '\n')
fin.close()
fout.close()
