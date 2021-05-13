from math import log2, floor, ceil


class Decomposer:
    def __init__(self, element):
        self.N = 2 ** int(ceil(log2(len(x))))
        self.neutral_value = 0
        self.element = element
        self.data = [None] * (self.N - 1)
        self.data += [int(el == self.element) for el in x]
        self.data += [self.neutral_value] * (self.N - len(x))
        for i in range(self.N - 2, (self.N - 1) // 2, -1):
            c1 = x[2 * i - self.N + 2] == self.element
            c2 = x[2 * i - self.N + 3] == self.element
            self.data[i] = c1 + c2
        for i in range((self.N - 1) // 2, -1, -1):
            c1 = self.data[2 * i + 1]
            c2 = self.data[2 * i + 2]
            self.data[i] = c1 + c2

    def req(self, left, right):
        left = max(0, left)
        right = min(len(x), right)
        left += self.N - 1
        right += self.N - 1
        z = self.neutral_value
        while right > left:
            if not left & 1:
                z += self.data[left]
                left += 1
            if not right & 1:
                right -= 1
                z += self.data[right]
            left = (left - 1) // 2
            right = (right - 1) // 2
        return z

    def update(self, k, d):
        i = k + self.N - 1
        self.data[i] = x[k] == self.element
        while i > (self.N - 1) // 2:
            i = (i - 1) // 2
            c1 = x[2 * i - self.N + 2] == self.element
            c2 = x[2 * i - self.N + 3] == self.element
            self.data[i] = c1 + c2
        while i > 0:
            c1 = self.data[2 * i + 1]
            c2 = self.data[2 * i + 2]
            self.data[i] = c1 + c2
            i = (i - 1) // 2


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N, M, K = list(map(int, fin.readline().split()))
x = list(map(int, fin.readline().split()))
x += [-1] * (2 ** int(ceil(log2(len(x)))) - len(x))
y = [Decomposer(k) for k in range(K + 1)]
for i in range(M):
    request = fin.readline().rstrip('\n').split()
    if request[0] == '?':
        l, r, k = request[1:]
        response = y[int(k)].req(int(l), int(r))
        fout.write(str(response) + '\n')
    elif request[0] == '+':
        i, d = request[1:]
        old_value = x[int(i)]
        x[int(i)] += int(d)
        new_value = x[int(i)]
        y[old_value].update(int(i), int(d))
        y[new_value].update(int(i), int(d))
fin.close()
fout.close()
