from math import log2, floor, ceil


class ZeroCounter:
    def __init__(self):
        self.N = 2 ** int(ceil(log2(len(x))))
        self.neutral_value = 0
        self.data = [None] * (self.N - 1) + [int(el == 0) for el in x]
        self.data += [self.neutral_value] * (self.N - len(x))
        for i in range(self.N - 2, -1, -1):
            j1, j2 = 2 * i + 1, 2 * i + 2
            if j1 > self.N:
                c1 = int(x[j1 - self.N + 1] == 0)
            else:
                c1 = self.data[j1]
            if j2 > self.N:
                c2 = int(x[j2 - self.N + 1] == 0)
            else:
                c2 = self.data[j2]
            self.data[i] = c1 + c2

    def rzq(self, left, right):
        left = max(0, left)
        right = min(len(x), right)
        left += self.N - 1
        right += self.N - 1
        z = self.neutral_value
        while left < right:
            if not left & 1:
                z += self.data[left]
                left += 1
            if not right & 1:
                right -= 1
                z += self.data[right]
            if left == right - 1:
                return z
            left = (left - 1) // 2
            right = (right - 1) // 2
        return z

    def update(self, k, d):
        x[k] += d
        i = k + self.N - 1
        self.data[i] = int(x[k] == 0)
        while i > 0:
            i = (i - 1) // 2
            j1, j2 = 2 * i + 1, 2 * i + 2
            if j1 > self.N:
                c1 = int(x[j1 - self.N + 1] == 0)
            else:
                c1 = self.data[j1]
            if j2 > self.N:
                c2 = int(x[j2 - self.N + 1] == 0)
            else:
                c2 = self.data[j2]
            self.data[i] = c1 + c2


with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    N, M = map(int, fin.readline().split())
    if N > 0:
        x = list(map(int, fin.readline().split()))
        x += [-1] * (2 ** int(ceil(log2(len(x)))) - len(x))
        counter = ZeroCounter()

        for _ in range(M):
            s, var1, var2 = fin.readline().split()
            if s == '+':
                counter.update(int(var1), int(var2))
            elif s == '?':
                c_zero = counter.rzq(int(var1), int(var2))
                print(c_zero)
                fout.write(str(c_zero) + '\n')
